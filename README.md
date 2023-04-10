# build a complete turnkey SD card image:

# customization for z7io

This is a two-pass process

## 1. In the first pass, we create the conventional package:
```
./make.package => release/05-z7io-DATE.tgz
```
   This package is then used in a standard release process

## 2. In the second pass, inputs
```
local-files => deploy2sd => acq400-z7io-base-SD-DATE.tgz
../ACQ400RELEASE/REL/acq400-VER*.tar \ # the ESW release
../../ACQ400RELEASE/OPT/ko/z7io*.img \ # the FPGA
acq400-z7io-base-SD-DATE.tgz \         # base SD image
  => deploy2sd => z7io-acq400-VER-DATE.tgz  # complete SD image, replicate this
```

## FINALLY, update a fresh Z7IO, follow INSTALL.md

