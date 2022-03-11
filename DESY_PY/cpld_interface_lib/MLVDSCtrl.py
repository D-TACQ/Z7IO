#! /usr/bin/env python3

import argparse
import logging

from cpld_interface_lib.MuxDataCtrl import MuxDataCtrl
from cpld_interface_lib.CPLDSpiDriver import CPLDSpiDriver

class MLVDSCtrl:

    def __init__(self):

        self.logger = logging.getLogger(__name__)

        self.cpld = CPLDSpiDriver()
        self.mux_ctrl = MuxDataCtrl()

    # enable MLVDS output (directly from application)
    def mlvds_enable_output(self):

        # reset buffer select in CPLD
        self.cpld.wr(CPLDSpiDriver.ADDR_CPLD_BUF_SEL_REG, 0xff)
        # set cpld_data_out_mux to direct output
        self.mux_ctrl.set_out_mux_direct()
        # set MLVDS buffer on Z7IO to output
        self.cpld.wr(CPLDSpiDriver.ADDR_CPLD_MLVDS_BUF_DE_REG, 0xff)
        # set buffer select in CPLD
        self.cpld.wr(CPLDSpiDriver.ADDR_CPLD_BUF_SEL_REG, 0x10)

        self.logger.debug("Enable MLVDS buffer output, driven by fw. app")

    # enable MLVDS input (directly to application)
    def mlvds_enable_input(self):

        # reset buffer select in CPLD
        self.cpld.wr(CPLDSpiDriver.ADDR_CPLD_BUF_SEL_REG, 0xff)
        # set cpld_data_in_mux to direct input
        self.mux_ctrl.set_in_mux_direct()
        # set MLVDS buffer on Z7IO to input
        self.cpld.wr(CPLDSpiDriver.ADDR_CPLD_MLVDS_BUF_DE_REG, 0x00)
        # set buffer select in CPLD
        self.cpld.wr(CPLDSpiDriver.ADDR_CPLD_BUF_SEL_REG, 0x10)

        self.logger.debug("Enable MLVDS buffer input, driven to fw. app")


def main():
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger(__name__)

    mlvds = MLVDSCtrl()

    # set buffer 0 to output
    mlvds.mlvds_enable_output()

if __name__ == "__main__":
    main()