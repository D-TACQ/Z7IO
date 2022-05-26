# build a complete turnkey SD card image:

We needs a local FAT file system, the easiest thing is to plug in a local
SD card. Do this and find the mount point.

eg
/run/media/pgm/417B-5B97

build an image:
./deploy2sd /run/media/pgm/417B-5B97
z7io-acq400-511-20220525111647.tgz


# customization for z7io

mkenvimage -s 131072 -o uboot.env uEnv.txt

# FPIO

z7io_007> ./fpio_init.py --disable
SPI_BUS 3 SPI_DEV 0
Disabling buffers ...
All buffers disabled, exiting...
z7io_007> ./fpio_init.py --mode app --dir in --buf 0
SPI_BUS 3 SPI_DEV 0


# replaces DTACQfpio.py


