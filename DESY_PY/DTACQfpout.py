#! /usr/bin/env python3

# Demo Software: Configure DAMC-FMC1Z7IO front panel IO 0-7
# as direct input to BSP application section

import logging
import time 

from cpld_interface_lib.MuxDataCtrl import MuxDataCtrl
from cpld_interface_lib.FPIOCtrl import FPIOCtrl

if __name__ == '__main__':

#  logging.basicConfig(level=logging.DEBUG)
#  logging.basicConfig(level=0)
  logger = logging.getLogger(__name__)

  mux_ctrl = MuxDataCtrl()
  fpio_ctrl = FPIOCtrl()

  # CPLD: ensure that buffer 1 is disabled
  fpio_ctrl.fpio_buf_set_en(1, False)
  # CPLD: ensure that muliplexer is disabled
  fpio_ctrl.cpld.wr(fpio_ctrl.cpld.ADDR_CPLD_BUF_SEL_REG, 0xFF)

  logger.debug(" Buffer_1: Initialize to OUTPUT at 3.3V")
  # CPLD: set buffer 1 level to 3v3
  fpio_ctrl.fpio_buf_set_lev(1, "3v3")
  # CPLD: set buffer 0 direction to output
  fpio_ctrl.fpio_buf_set_dir(1, "output")
  # CPLD: enable buffer 1
  fpio_ctrl.fpio_buf_set_en(1, True)

  # CPLD: set multiplexer to buffer 1
  fpio_ctrl.cpld.wr(fpio_ctrl.cpld.ADDR_CPLD_BUF_SEL_REG, 0x01)

  # ZYNQ: set cpld_data_in_mux to direct input (to BSP application part)
#  mux_ctrl.set_in_mux_direct()

  logger.setLevel(logging.DEBUG)
  for x in range(0,100000):
 #     time.sleep(4)
      fpio_ctrl.fpio_buf_set_output(0xAA,1)
 #     time.sleep(4);
      fpio_ctrl.fpio_buf_set_output(0x55,1)    
 #     print("{} reading fpio_buf_get_input() {}".format(x, fpio_ctrl.fpio_buf_get_input()))
