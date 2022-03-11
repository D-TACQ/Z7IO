#! /usr/bin/env python3

import argparse
import logging

from cpld_interface_lib.MuxDataCtrl import MuxDataCtrl
from cpld_interface_lib.CPLDSpiDriver import CPLDSpiDriver
from cpld_interface_lib.HwAccessAarch32 import HwAccessAarch32

class FPIOCtrl:

    ADDR_ZYNQ_IO_DATA_OUT_REG = 0x2000
    ADDR_ZYNQ_IO_DATA_IN_REG = 0x2008

    def __init__(self):

        self.logger = logging.getLogger(__name__)

        self.cpld = CPLDSpiDriver()
        self.zynq = HwAccessAarch32()
        self.mux_ctrl = MuxDataCtrl()

    #ToDo: Set to direct input/output (to/from BSP application)

    # set FPIO buffer to static output
    def fpio_buf_set_output(self, data, buf_num=0, level="3v3"):

        # reset buffer select in CPLD (avoid updating wrong buffer with wrong data)
        self.cpld.wr(CPLDSpiDriver.ADDR_CPLD_BUF_SEL_REG, 0xff)

        # set cpld_data_out_mux to static output
        self.mux_ctrl.set_out_mux_static()

        # Check if Buffer is disabled
        if not self.fpio_buf_get_en(buf_num):
            self.logger.debug("buffer %i is disabled", buf_num)
            self.fpio_buf_init(buf_num, "output", level)
        else:
            self.logger.debug("buffer %i is enabled", buf_num)
            if (self.fpio_buf_get_dir(buf_num) != "output") or (self.fpio_buf_get_lev(buf_num) != level):
                self.fpio_buf_set_en(buf_num, False)
                self.fpio_buf_init(buf_num, "output", level)

        # set FPIO output val via AXI GPIO
        self.zynq.wr32(self.ADDR_ZYNQ_IO_DATA_OUT_REG, data)

        # set buffer select in CPLD
        self.cpld.wr(CPLDSpiDriver.ADDR_CPLD_BUF_SEL_REG, buf_num)

        # FPIO Buffer enable
        if not self.fpio_buf_get_en(buf_num):
            self.fpio_buf_set_en(buf_num, True)

        self.logger.debug("set FPIO buffer %i output to %02x", buf_num, data)

    # get static input from FPIO Buffer
    def fpio_buf_get_input(self, buf_num=0, level="3v3"):

        # set cpld_data_in_mux to static input
        self.mux_ctrl.set_in_mux_static()

        # Check if Buffer is disabled
        if not self.fpio_buf_get_en(buf_num):
            self.logger.debug("buffer %i is disabled", buf_num)
            self.fpio_buf_init(buf_num, "input", level)
        else:
            self.logger.debug("buffer %i is enabled", buf_num)
            if (self.fpio_buf_get_dir(buf_num) != "input") or (self.fpio_buf_get_lev(buf_num) != level):
                self.fpio_buf_set_en(buf_num, False)
                self.fpio_buf_init(buf_num, "input", level)

        # FPIO Buffer enable
        if not self.fpio_buf_get_en(buf_num):
            self.fpio_buf_set_en(buf_num, True)

        # set buffer select in CPLD
        self.cpld.wr(CPLDSpiDriver.ADDR_CPLD_BUF_SEL_REG, buf_num)

        # read FPIO input val via AXI GPIO
        data = self.zynq.rd32(self.ADDR_ZYNQ_IO_DATA_IN_REG)
        self.logger.debug("read FPIO buffer %i input: data is %02x", buf_num, data)

        return data

    def fpio_buf_init(self, buf_num, dir, level):
        self.logger.debug("buffer %i, initialize to %s at %s", buf_num, dir, level)
        self.fpio_buf_set_lev(buf_num, level)
        self.fpio_buf_set_dir(buf_num, dir)

    def fpio_buf_set_en(self, buf_num, en):
        # get FPIO buffer enable vector
        buf_en_vec = self.cpld.rd(CPLDSpiDriver.ADDR_CPLD_BUF_EN_REG)
        if en:
            self.cpld.wr(CPLDSpiDriver.ADDR_CPLD_BUF_EN_REG, (buf_en_vec & ~(1 << buf_num)))
            self.logger.debug("set buffer %i to enabled", buf_num)
        else:
            self.cpld.wr(CPLDSpiDriver.ADDR_CPLD_BUF_EN_REG, (buf_en_vec | (1 << buf_num)))
            self.logger.debug("set buffer %i to disabled", buf_num)

    def fpio_buf_get_en(self, buf_num):
        # get FPIO buffer enable vector
        buf_en_vec = self.cpld.rd(CPLDSpiDriver.ADDR_CPLD_BUF_EN_REG)
        if buf_en_vec & (1 << buf_num):
            return False
        else:
            return True

    def fpio_buf_set_dir(self, buf_num, dir):
        # get FPIO buffer direction vector
        buf_dir_vec = self.cpld.rd(CPLDSpiDriver.ADDR_CPLD_BUF_DIR_REG)
        if dir == "output":
            self.cpld.wr(CPLDSpiDriver.ADDR_CPLD_BUF_DIR_REG, (buf_dir_vec | (1 << buf_num)))
        elif dir == "input":
            self.cpld.wr(CPLDSpiDriver.ADDR_CPLD_BUF_DIR_REG, (buf_dir_vec & ~(1 << buf_num)))
        self.logger.debug("set buffer %i to %s", buf_num, dir)

    def fpio_buf_get_dir(self, buf_num):
        # get FPIO buffer direction vector
        buf_dir_vec = self.cpld.rd(CPLDSpiDriver.ADDR_CPLD_BUF_DIR_REG)
        if buf_dir_vec & (1 << buf_num):
            return "output"
        else:
            return "input"

    def fpio_buf_set_lev(self, buf_num, level):
        # get FPIO buffer voltage level vector
        buf_lev_vec = self.cpld.rd(CPLDSpiDriver.ADDR_CPLD_BUF_LEV_CTL_REG)
        if level == "5v":
            self.cpld.wr(CPLDSpiDriver.ADDR_CPLD_BUF_LEV_CTL_REG, (buf_lev_vec & ~(1 << buf_num)))
        elif level == "3v3":
            self.cpld.wr(CPLDSpiDriver.ADDR_CPLD_BUF_LEV_CTL_REG, (buf_lev_vec | (1 << buf_num)))
        self.logger.debug("set buffer %i voltage level to %s", buf_num, level)

    def fpio_buf_get_lev(self, buf_num):
        # get FPIO buffer voltage level vector
        buf_lev_vec = self.cpld.rd(CPLDSpiDriver.ADDR_CPLD_BUF_LEV_CTL_REG)
        if buf_lev_vec & (1 << buf_num):
            return "5v"
        else:
            return "3v3"


def main():
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger(__name__)

    fpio = FPIOCtrl()

    # set buffer 0 to output
    fpio.fpio_buf_set_output(0xab, 0, "3v3")

    # get input from buffer 3
    fpio.fpio_buf_get_input(3, "3v3")

if __name__ == "__main__":
    main()