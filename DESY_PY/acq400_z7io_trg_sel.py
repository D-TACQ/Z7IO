#! /usr/bin/env python3

# Trigger source select 

import logging
import time 

from cpld_interface_lib.FPIOCtrl import FPIOCtrl, FPIODir, FPIOLevel, FPIORouting

BUF = 0

def fpio_disable(fpio_ctrl):
    fpio.buf_init([FPIODir.IN] * 6, [False] * 6, [FPIOLevel.LEVEL_3V3] * 6)
                                                  
def fpio_enable(fpio_ctrl):
    fpio.buf_init_single(BUF, FPIODir.IN, FPIOLevel.LEVEL_3V3, FPIORouting.APP)

def mlvds_disable(mlvds):
    mlvds.port_init(MLVDSDir.IN, MLVDSRouting.REG)
    
    
STATUS = "/dev/shm/acq400_z7io_trg_status"

def show_report():
    try:
        with open(STATS, 'r') as f:
            print(f.read())
    except:
        print("ERROR: acq400_z7io_trg_status not set")

def make_report(source):
    with open(STATS, 'w') as f:
        f.print(source)
    
def select_trg(fpio_ctrl, mlvds, source):
    if source == "OFF":
        fpio_disable(fpio_ctrl)
        mlvds_disable(mlvds)
    if source == "FP":
        mlvds_disable(mlvds)
        fpio_enable(fpio_ctrl)
    elif source == "RP":
        fpio_disable(fpio_ctrl)
        mlvds.port_init(MLVDSDir.IN, MLVDSRouting.APP)
    elif source == "FPM":
        fpio_enable(fpio_ctrl)
        for _ in range(10):
            if mlvds.port_input_get() != 0:
                raise RuntimeError(
                    "Traffic on the MLVDS lines detected, unable to activate output"
                )
        mlvds.port_init(MLVDSDir.OUT, MLVDSRouting.APP)
    else:
        show_report()
        return 
    
    make_report(source)
    
             
    

def run_main():
    parser = argparse.ArgumentParser(description='select trigger source for z7io')
    parser.add_argument(
        "--debug", action="store_true", help="Enable verbose output (debug level)"
    )
    parser.add_argument(
        "--trace",
        action="store_true",
        help="Enable even more verbose output (trace level)",
    )        
    parser.add_argument('source', nargs=1, help="OFF,FP,RP,FPM")
    args = parser.parse_args()
    
    if args.trace or args.debug:
        logging.basicConfig(level=(LEVEL_TRACE if args.trace else LEVEL_DEBUG))
    logger = logging.getLogger(__name__)
    select_trg(FPIOCtrl(), MLVDSCtrl(), args.source)
    
if __name__ == '__main__':
    run_main()