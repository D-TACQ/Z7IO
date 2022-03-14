#! /usr/bin/env python3

# Demo Software: Configure DAMC-FMC1Z7IO front panel IO 0-7
# as direct input to BSP application section

import logging
import time 

from cpld_interface_lib.FPIOCtrl import FPIOCtrl, FPIODir, FPIOLevel, FPIORouting

if __name__ == '__main__':

#  logging.basicConfig(level=logging.DEBUG)
  logging.basicConfig(level=0)
  logger = logging.getLogger(__name__)

  fpio_ctrl = FPIOCtrl()

  logger.debug("NEW API COMMAND TO INIT FPIO")
  fpio_ctrl.buf_init_single(0, FPIODir.IN, FPIOLevel.LEVEL_3V3, FPIORouting.APP)
