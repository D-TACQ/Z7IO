To create an SD card for Z7IO

1. The mac address is stored in an EEPROM on the Z7IO, this is the ONLY unique information.

2. Unpack the base SD card to SD root shown here as 'SD'

```
tar xvzf acq400-z7io-base-SD-YYMMDD.tgz
```

3. Unpack the main release to SD root:
eg release 485:

```
tar xvf acq400-485-??????????????.tar 
```

3.3 copy the kernel

```
cp uImage uImage.acq400
```

3.5 Unpack the rootfs

```
(cd SD; gunzip rootfs.tar.gz)
```

3.6 Install Payload customization

```
(cd SD; mv packages.opt/04-custom_z7io_payload_acq424-??????????.tgz packages
```

4. Copy FPGA images to set to the SD

```
cp fpga-485-??????????????.img SD/ko
```

5. Insert the SD card, connect to the z7io CONSOLE at 115200baud

6. Boot the z7io, break into u-boot by pressing <SPACE>

7. Modify and install a u-boot environment to z7io QSPI FLASH

```
fatload mmc 0 0x4000000 uboot.env
env import -b 0x4000000
saveenv
```

8. Boot the z7io

9. The z7io will boot as a standard ACQ400 SYSTEM with RTM2 and 2xACQ424

By default z7io will try to get a network address using dhcp.
You should use the table SD/local/sysconfig/machosts to configure your dhcp server.



