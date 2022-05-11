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


