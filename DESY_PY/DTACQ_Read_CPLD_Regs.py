#! /usr/bin/env python3

# Demo Software: Configure DAMC-FMC1Z7IO front panel IO 0-7
# as direct input to BSP application section

#   ADDR_CPLD_FW_ID_REG = 0x00
#   ADDR_CPLD_FW_VER_REG = 0x01
#   ADDR_CPLD_SCRATCH_REG =	0x02
#   ADDR_CPLD_BUF_SEL_REG =	0x03
#   ADDR_CPLD_BUF_DIR_REG =	0x04
#   ADDR_CPLD_BUF_EN_REG = 0x05
#   ADDR_CPLD_BUF_LEV_CTL_REG =	0x06
#   ADDR_CPLD_MLVDS_BUF_DE_REG = 0x07

import logging
import time 

from cpld_interface_lib.MuxDataCtrl import MuxDataCtrl
from cpld_interface_lib.FPIOCtrl import FPIOCtrl
from cpld_interface_lib.CPLDSpiDriver import CPLDSpiDriver
from cpld_interface_lib.HwAccessAarch32 import HwAccessAarch32

if __name__ == '__main__':

#  logging.basicConfig(level=logging.DEBUG)
  logging.basicConfig(level=0)
  logger = logging.getLogger(__name__)

  mux_ctrl = MuxDataCtrl()
  fpio_ctrl = FPIOCtrl()
  cpld_driver  = CPLDSpiDriver()  
  
   # CPLD: read registers 
  addr = 0x00
  data = fpio_ctrl.cpld.rd(CPLDSpiDriver.ADDR_CPLD_FW_ID_REG)
  data = fpio_ctrl.cpld.rd(CPLDSpiDriver.ADDR_CPLD_FW_VER_REG)
  data = fpio_ctrl.cpld.rd(CPLDSpiDriver.ADDR_CPLD_SCRATCH_REG)
  data = fpio_ctrl.cpld.rd(CPLDSpiDriver.ADDR_CPLD_BUF_SEL_REG)
  data = fpio_ctrl.cpld.rd(CPLDSpiDriver.ADDR_CPLD_BUF_DIR_REG)
  data = fpio_ctrl.cpld.rd(CPLDSpiDriver.ADDR_CPLD_BUF_EN_REG)
  data = fpio_ctrl.cpld.rd(CPLDSpiDriver.ADDR_CPLD_BUF_LEV_CTL_REG)
  data = fpio_ctrl.cpld.rd(CPLDSpiDriver.ADDR_CPLD_MLVDS_BUF_DE_REG)
 # CPLD: Write Pattern to Scratch
  fpio_ctrl.cpld.wr(fpio_ctrl.cpld.ADDR_CPLD_SCRATCH_REG, 0xAA)
  data = fpio_ctrl.cpld.rd(CPLDSpiDriver.ADDR_CPLD_SCRATCH_REG)
  fpio_ctrl.cpld.wr(fpio_ctrl.cpld.ADDR_CPLD_SCRATCH_REG, 0x55)
  data = fpio_ctrl.cpld.rd(CPLDSpiDriver.ADDR_CPLD_SCRATCH_REG)
