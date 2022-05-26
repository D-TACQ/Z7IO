To create an SD card for Z7IO



1. The mac address is stored in an EEPROM on the Z7IO, this is the ONLY unique information.

2. Unpack the base SD card to SD root shown here as 'SD'

z7io is supplied with a unique all-in-one SD card image

```
download eg@ https://github.com/D-TACQ/ACQ400RELEASE/releases/download/v511/z7io-acq400-511-20220525111647.tgz

tar xvzf z7io-acq400-VVV-YYYYMMDD*.tgz
```


3. Insert the SD card, connect to the z7io CONSOLE at 115200baud

*Disable flow control (example for kermit)*
```
root@rpi-008:~# cat .kermrc
set flow-control none
set carrier-watch off
```

6. Boot the z7io, break into u-boot by pressing `<SPACE>`

*do this ONCE only in the lifetime of the z7io*

   - Modify and install a u-boot environment to z7io QSPI FLASH

```
fatload mmc 0 0x4000000 uboot.env
env import -b 0x4000000
saveenv
```

7. Boot the z7io

   - The z7io will boot as a standard ACQ400 SYSTEM with RTM2 and 2xACQ424

By default z7io will try to get a network address using dhcp.
You should use the table SD/local/sysconfig/machosts to configure your dhcp server.



