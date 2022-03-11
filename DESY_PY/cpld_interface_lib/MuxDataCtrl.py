#! /usr/bin/env python3

from cpld_interface_lib.HwAccessAarch32 import HwAccessAarch32

class MuxDataCtrl:

    ADDR_ZYNQ_IN_MUX_SEL_REG = 0x0000
    ADDR_ZYNQ_OUT_MUX_SEL_REG = 0x0008

    def __init__(self):
        self.zynq = HwAccessAarch32()

    # Set MUX_DATA_OUT to static output from GPIO in the BSP logic
    def set_out_mux_static(self):
        self.zynq.wr32(self.ADDR_ZYNQ_OUT_MUX_SEL_REG, 0x0000)

    # Set MUX_DATA_OUT to direct output from the application logic
    def set_out_mux_direct(self):
        self.zynq.wr32(self.ADDR_ZYNQ_OUT_MUX_SEL_REG, 0x0001)

    # Set MUX_DATA_IN to static input to GPIO in the BSP logic
    def set_in_mux_static(self):
        self.zynq.wr32(self.ADDR_ZYNQ_IN_MUX_SEL_REG, 0x0000)

    # Set MUX_DATA_IN to direct input to the application logic
    def set_in_mux_direct(self):
        self.zynq.wr32(self.ADDR_ZYNQ_IN_MUX_SEL_REG, 0x0001)
