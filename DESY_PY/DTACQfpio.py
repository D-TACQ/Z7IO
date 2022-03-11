#! /usr/bin/env python3

# Demo Software: Configure DAMC-FMC1Z7IO front panel IO 0-7
# as direct input to BSP application section

import logging
import time 

from cpld_interface_lib.MuxDataCtrl import MuxDataCtrl
from cpld_interface_lib.FPIOCtrl import FPIOCtrl

if __name__ == '__main__':

#  logging.basicConfig(level=logging.DEBUG)
  logging.basicConfig(level=0)
  logger = logging.getLogger(__name__)

  mux_ctrl = MuxDataCtrl()
  fpio_ctrl = FPIOCtrl()

  # CPLD: ensure that buffer 0 is disabled
  fpio_ctrl.fpio_buf_set_en(0, False)
  # CPLD: ensure that muliplexer is disabled
  fpio_ctrl.cpld.wr(fpio_ctrl.cpld.ADDR_CPLD_BUF_SEL_REG, 0xFF)

  logger.debug(" Buffer_0: Initialize to INPUT at 3.3V")
  # CPLD: set buffer 0 level to 3v3
  fpio_ctrl.fpio_buf_set_lev(0, "3v3")
  # CPLD: set buffer 0 direction to input
  fpio_ctrl.fpio_buf_set_dir(0, "input")
  # CPLD: enable buffer 0
  fpio_ctrl.fpio_buf_set_en(0, True)

  # CPLD: set multiplexer to buffer 0
  fpio_ctrl.cpld.wr(fpio_ctrl.cpld.ADDR_CPLD_BUF_SEL_REG, 0x00)

  # ZYNQ: set cpld_data_in_mux to direct input (to BSP application part)
  mux_ctrl.set_in_mux_direct()

# logger.setLevel(logging.DEBUG)
# for x in range(0,10):
#      time.sleep(2)
#      print("{} reading fpio_buf_get_input() {}".format(x, fpio_ctrl.fpio_buf_get_input()))
