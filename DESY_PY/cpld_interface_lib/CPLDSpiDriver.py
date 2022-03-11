#! /usr/bin/env python3

import argparse
import logging

import spidev

LEVEL_TRACE = logging.DEBUG-5
logging.addLevelName(LEVEL_TRACE, 'TRACE')

class CPLDSpiDriver:

    Z7IO_SPI_BUS = 3
    Z7IO_CPLD_SPI_DEV = 0

    ADDR_CPLD_FW_ID_REG = 0x00
    ADDR_CPLD_FW_VER_REG = 0x01
    ADDR_CPLD_SCRATCH_REG =	0x02
    ADDR_CPLD_BUF_SEL_REG =	0x03
    ADDR_CPLD_BUF_DIR_REG =	0x04
    ADDR_CPLD_BUF_EN_REG = 0x05
    ADDR_CPLD_BUF_LEV_CTL_REG =	0x06
    ADDR_CPLD_MLVDS_BUF_DE_REG = 0x07

    EXPECTED_CPLD_FW_ID = [0xC9]

    def __init__(self):

        self.dev = spidev.SpiDev()
        print("pgm: open {}.{}".format(self.Z7IO_SPI_BUS, self.Z7IO_CPLD_SPI_DEV))
        self.dev.open(self.Z7IO_SPI_BUS, self.Z7IO_CPLD_SPI_DEV)
        self.dev.max_speed_hz = 25000000

        self.logger = logging.getLogger(__name__)

        self._check_device()

    def _check_device(self):
        """ Check for CPLD firmware info """

        self.logger.debug("_check_device called")

        cpld_fw_id = self.rd(self.ADDR_CPLD_FW_ID_REG)
        assert cpld_fw_id in self.EXPECTED_CPLD_FW_ID, \
            "Unrecognized CPLD Number, expected %04x, got %04x" % \
            (self.EXPECTED_CPLD_FW_ID, cpld_fw_id)

        cpld_fw_ver = self.rd(self.ADDR_CPLD_FW_VER_REG)

        self.logger.info("CPLD firmware information:")
        self.logger.info("  firmware id:  0x%02x", cpld_fw_id)
        self.logger.info("  firmware ver: 0x%02x", cpld_fw_ver)

    def rd(self, addr: int):
        to_send = [0x80 + addr, 0x00]
        """ Read a single byte """
        b = self.dev.xfer(to_send)
        data = b[1]
        self.logger.log(LEVEL_TRACE, "read: addr = %02x, data = %02x", addr, data)
        return data

    def wr(self, addr: int, val: int):
        to_send = [0x00 + addr, val]
        """ Write a single byte """
        self.dev.xfer(to_send)
        self.logger.log(LEVEL_TRACE, "write: addr = %02x, data = %02x", addr, val)


def main():
    """ Example usage, reads info from CPLD firmware """

    logging.basicConfig(level=logging.DEBUG)

    cpld = CPLDSpiDriver()

if __name__ == "__main__":
    main()