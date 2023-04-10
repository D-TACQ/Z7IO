# build a complete turnkey SD card image:

# customization for z7io

This is a two-pass process

1. In the first pass, we create the conventional package:
```
./make.package => release/05-z7io-DATE.tgz
```
   This package is then used in a standard release process

2. In the second pass, inputs
```
local-files => deploy2sd => acq400-z7io-base-SD-DATE.tgz
../ACQ400RELEASE/REL/acq400-VER*.tar \ # the ESW release
../../ACQ400RELEASE/OPT/ko/z7io*.img \ # the FPGA
acq400-z7io-base-SD-DATE.tgz \         # base SD image
  => deploy2sd => z7io-acq400-VER-DATE.tgz  # complete SD image, replicate this
```

## Inputs
 - local files for Base SD
 - 
Base SD card acq400-z7io-base-SD-DATE.tgz is

 - boot .bin: copy from DESY release (not used, as it's already in QSPI FLASH)
 - sysconfig: copied from GOLD Z7IO
 - custom uboot env uEnv.txt, and binary image created as follows:
```
mkenvimage -s 131072 -o uboot.env uEnv.txt
```


# FPIO

z7io_007> ./fpio_init.py --disable
SPI_BUS 3 SPI_DEV 0
Disabling buffers ...
All buffers disabled, exiting...
z7io_007> ./fpio_init.py --mode app --dir in --buf 0
SPI_BUS 3 SPI_DEV 0


# replaces DTACQfpio.py


