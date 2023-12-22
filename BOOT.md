# Z7IO boot sequence, annotated

## u-boot


```
Xilinx First Stage Boot Loader 
Release 2020.2	Mar 11 2022-11:42:18
DAMC-FMC1Z7IO board support by:
  DESY MicroTCA Technology Lab
Devcfg driver initialized 
Silicon Version 3.1
Boot mode is SD
SD: rc= 0
SD Init Done 
Flash Base Address: 0xE0100000
Reboot status register: 0x60400000
Multiboot Register: 0x0000C000
Image Start Address: 0x00000000
Partition Header Offset:0x00000C80
Partition Count: 2
Partition Number: 1
Header Dump
Image Word Len: 0x0002CDF9
Data Word Len: 0x0002CDF9
Partition Word Len:0x0002CDF9
Load Addr: 0x04000000
Exec Addr: 0x04000000
Partition Start: 0x000065D0
Partition Attr: 0x00000010
Partition Checksum Offset: 0x00000000
Section Count: 0x00000001
Checksum: 0xF7F72DE3
Application
Handoff Address: 0x04000000
In FsblHookBeforeHandoff function 
SUCCESSFUL_HANDOFF
FSBL Status = 0x1


U-Boot 2020.01 (Mar 11 2022 - 11:40:41 +0000)

CPU:   Zynq 7z030
Silicon: v3.1
DRAM:  ECC disabled 1 GiB
Flash: 0 Bytes
NAND:  0 MiB
MMC:   mmc@e0100000: 0, mmc@e0101000: 1
Loading Environment from SPI Flash... SF: Detected s25fl256s0 with page size 256 Bytes, erase size 256 KiB, total 32 MiB
OK
In:    serial@e0001000
Out:   serial@e0001000
Err:   serial@e0001000
Net:   
ZYNQ GEM: e000b000, mdio bus e000b000, phyaddr 0, interface rgmii-id
zynq_board_read_rom_ethaddr: Path to EEPROM /amba/i2c@e0004000/eeprom@57
zynq_board_read_rom_ethaddr: EEPROM with 16-bit addr used
zynq_board_read_rom_ethaddr: I2C EEPROM MAC 80:34:28:8b:34:2f
eth0: ethernet@e000b000
Hit any key to stop autoboot:  0 
Copying Linux from SD to RAM...
Device: mmc@e0100000
Manufacturer ID: 2
OEM: 544d
Name: SA16G 
Bus Speed: 50000000
Mode: SD High Speed (50MHz)
Rd Block Len: 512
SD version 3.0
High Capacity: Yes
Capacity: 14.4 GiB
Bus Width: 4-bit
Erase Group Size: 512 Bytes
ERROR: reserving fdt memory region failed (addr=3c000000 size=4000000)
3511480 bytes read in 216 ms (15.5 MiB/s)
ERROR: reserving fdt memory region failed (addr=3c000000 size=4000000)
17971 bytes read in 38 ms (460.9 KiB/s)
ERROR: reserving fdt memory region failed (addr=3c000000 size=4000000)
2973931 bytes read in 190 ms (14.9 MiB/s)
## Booting kernel from Legacy Image at 03000000 ...
   Image Name:   Linux-4.14.0-acq400-xilinx-g4cd1
   Image Type:   ARM Linux Kernel Image (uncompressed)
   Data Size:    3511416 Bytes = 3.3 MiB
   Load Address: 00008000
   Entry Point:  00008000
   Verifying Checksum ... OK
## Loading init Ramdisk from Legacy Image at 02000000 ...
   Image Name:   D-TACQ ACQ400 INITRD
   Image Type:   ARM Linux RAMDisk Image (gzip compressed)
   Data Size:    2973867 Bytes = 2.8 MiB
   Load Address: 00000000
   Entry Point:  00000000
   Verifying Checksum ... OK
## Flattened Device Tree blob at 02a00000
   Booting using the fdt blob at 0x2a00000
   Loading Kernel Image
   Loading Ramdisk to 1fd29000, end 1ffff0ab ... OK
   Loading Device Tree to 1fd21000, end 1fd28632 ... OK

Starting kernel ...

```

## Kernel Boot

```
Starting kernel ...

[    0.000000] Booting Linux on physical CPU 0x0
[    0.000000] Linux version 4.14.0-acq400-xilinx-g4cd1b648c487 (pgm@staffa3) (gcc version 7.3.1 20180314 (Linaro GCC 7.3-2018.04-rc3)) #1 SMP PREEMPT Sun Apr 16 17:18:14 BST 2023
[    0.000000] CPU: ARMv7 Processor [413fc090] revision 0 (ARMv7), cr=18c5387d
[    0.000000] CPU: PIPT / VIPT nonaliasing data cache, VIPT aliasing instruction cache
[    0.000000] OF: fdt: Machine model: Xilinx Zynq
[    0.000000] Memory policy: Data cache writealloc
[    0.000000] cma: Reserved 16 MiB at 0x3f000000
[    0.000000] percpu: Embedded 16 pages/cpu @ef7ca000 s34700 r8192 d22644 u65536
[    0.000000] Built 1 zonelists, mobility grouping on.  Total pages: 260608
[    0.000000] Kernel command line: earlyprintk console=ttyPS0,115200 root=/dev/ram rw rootwait
[    0.000000] PID hash table entries: 4096 (order: 2, 16384 bytes)
[    0.000000] Dentry cache hash table entries: 131072 (order: 7, 524288 bytes)
[    0.000000] Inode-cache hash table entries: 65536 (order: 6, 262144 bytes)
[    0.000000] Memory: 1011000K/1048576K available (5120K kernel code, 218K rwdata, 1344K rodata, 1024K init, 151K bss, 21192K reserved, 16384K cma-reserved, 245760K highmem)
[    0.000000] Virtual kernel memory layout:
[    0.000000]     vector  : 0xffff0000 - 0xffff1000   (   4 kB)
[    0.000000]     fixmap  : 0xffc00000 - 0xfff00000   (3072 kB)
[    0.000000]     vmalloc : 0xf0800000 - 0xff800000   ( 240 MB)
[    0.000000]     lowmem  : 0xc0000000 - 0xf0000000   ( 768 MB)
[    0.000000]     pkmap   : 0xbfe00000 - 0xc0000000   (   2 MB)
[    0.000000]     modules : 0xbf000000 - 0xbfe00000   (  14 MB)
[    0.000000]       .text : 0xc0008000 - 0xc0600000   (6112 kB)
[    0.000000]       .init : 0xc0800000 - 0xc0900000   (1024 kB)
[    0.000000]       .data : 0xc0900000 - 0xc0936988   ( 219 kB)
[    0.000000]        .bss : 0xc0936988 - 0xc095c624   ( 152 kB)
[    0.000000] Preemptible hierarchical RCU implementation.
[    0.000000] 	RCU restricting CPUs from NR_CPUS=4 to nr_cpu_ids=2.
[    0.000000] 	Tasks RCU enabled.
[    0.000000] RCU: Adjusting geometry for rcu_fanout_leaf=16, nr_cpu_ids=2
[    0.000000] NR_IRQS: 16, nr_irqs: 16, preallocated irqs: 16
[    0.000000] efuse mapped to f0800000
[    0.000000] slcr mapped to f0802000
[    0.000000] L2C: platform modifies aux control register: 0x72360000 -> 0x72760000
[    0.000000] L2C: DT/platform modifies aux control register: 0x72360000 -> 0x72760000
[    0.000000] L2C-310 erratum 769419 enabled
[    0.000000] L2C-310 enabling early BRESP for Cortex-A9
[    0.000000] L2C-310 full line of zeros enabled for Cortex-A9
[    0.000000] L2C-310 ID prefetch enabled, offset 1 lines
[    0.000000] L2C-310 dynamic clock gating enabled, standby mode enabled
[    0.000000] L2C-310 cache controller enabled, 8 ways, 512 kB
[    0.000000] L2C-310: CACHE_ID 0x410000c8, AUX_CTRL 0x76760001
[    0.000000] zynq_clock_init: clkc starts at f0802100
[    0.000000] Zynq clock init
[    0.000011] sched_clock: 64 bits at 333MHz, resolution 3ns, wraps every 4398046511103ns
[    0.000034] clocksource: arm_global_timer: mask: 0xffffffffffffffff max_cycles: 0x4ce07af025, max_idle_ns: 440795209040 ns
[    0.000062] Switching to timer-based delay loop, resolution 3ns
[    0.000163] clocksource: ttc_clocksource: mask: 0xffff max_cycles: 0xffff, max_idle_ns: 537538477 ns
[    0.000198] timer #0 at f080a000, irq=17
[    0.000686] Console: colour dummy device 80x30
[    0.000714] Calibrating delay loop (skipped), value calculated using timer frequency.. 666.66 BogoMIPS (lpj=3333333)
[    0.000732] pid_max: default: 32768 minimum: 301
[    0.000878] Mount-cache hash table entries: 2048 (order: 1, 8192 bytes)
[    0.000895] Mountpoint-cache hash table entries: 2048 (order: 1, 8192 bytes)
[    0.001491] CPU: Testing write buffer coherency: ok
[    0.001686] CPU0: thread -1, cpu 0, socket 0, mpidr 80000000
[    0.040353] Setting up static identity map for 0x100000 - 0x100060
[    0.060313] Hierarchical SRCU implementation.
[    0.100314] smp: Bringing up secondary CPUs ...
[    0.170655] CPU1: thread -1, cpu 1, socket 0, mpidr 80000001
[    0.170767] smp: Brought up 1 node, 2 CPUs
[    0.170785] SMP: Total of 2 processors activated (1333.33 BogoMIPS).
[    0.170794] CPU: All CPU(s) started in SVC mode.
[    0.171756] devtmpfs: initialized
[    0.175482] random: get_random_u32 called from bucket_table_alloc+0x1c4/0x204 with crng_init=0
[    0.175683] VFP support v0.3: implementor 41 architecture 3 part 30 variant 9 rev 4
[    0.176004] clocksource: jiffies: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 19112604462750000 ns
[    0.176026] futex hash table entries: 512 (order: 3, 32768 bytes)
[    0.177069] pinctrl core: initialized pinctrl subsystem
[    0.178149] NET: Registered protocol family 16
[    0.180488] random: fast init done
[    0.182402] DMA: preallocated 256 KiB pool for atomic coherent allocations
[    0.191069] hw-breakpoint: found 5 (+1 reserved) breakpoint and 1 watchpoint registers.
[    0.191085] hw-breakpoint: maximum watchpoint size is 4 bytes.
[    0.191213] zynq-ocm f800c000.ocmc: ZYNQ OCM pool: 256 KiB @ 0xf0880000
[    0.191633] zynq-pinctrl 700.pinctrl: zynq pinctrl initialized
[    0.191999] e0001000.serial: ttyPS0 at MMIO 0xe0001000 (irq = 26, base_baud = 6249999) is a xuartps
[    0.662511] console [ttyPS0] enabled
[    0.683162] SCSI subsystem initialized
[    0.687310] usbcore: registered new interface driver usbfs
[    0.692882] usbcore: registered new interface driver hub
[    0.698279] usbcore: registered new device driver usb
[    0.703750] pps_core: LinuxPPS API ver. 1 registered
[    0.708712] pps_core: Software ver. 5.3.6 - Copyright 2005-2007 Rodolfo Giometti <giometti@linux.it>
[    0.719103] PTP clock support registered
[    0.723108] EDAC MC: Ver: 3.0.0
[    0.731856] clocksource: Switched to clocksource arm_global_timer
[    0.747936] NET: Registered protocol family 2
[    0.753207] TCP established hash table entries: 8192 (order: 3, 32768 bytes)
[    0.760347] TCP bind hash table entries: 8192 (order: 4, 65536 bytes)
[    0.766958] TCP: Hash tables configured (established 8192 bind 8192)
[    0.773432] UDP hash table entries: 512 (order: 2, 16384 bytes)
[    0.779400] UDP-Lite hash table entries: 512 (order: 2, 16384 bytes)
[    0.785973] NET: Registered protocol family 1
[    0.790694] RPC: Registered named UNIX socket transport module.
[    0.796632] RPC: Registered udp transport module.
[    0.801326] RPC: Registered tcp transport module.
[    0.806078] RPC: Registered tcp NFSv4.1 backchannel transport module.
[    0.812709] Trying to unpack rootfs image as initramfs...
[    0.818610] rootfs image is not initramfs (no cpio magic); looks like an initrd
[    0.843912] Freeing initrd memory: 2908K
[    0.848165] hw perfevents: no interrupt-affinity property for /pmu@f8891000, guessing.
[    0.856367] hw perfevents: enabled with armv7_cortex_a9 PMU driver, 7 counters available
[    0.866128] workingset: timestamp_bits=30 max_order=18 bucket_order=0
[    0.873031] squashfs: version 4.0 (2009/01/31) Phillip Lougher
[    0.879109] jffs2: version 2.2. (NAND) (SUMMARY)  © 2001-2006 Red Hat, Inc.
[    0.886949] bounce: pool size: 64 pages
[    0.890794] io scheduler noop registered
[    0.894730] io scheduler deadline registered
[    0.899053] io scheduler cfq registered (default)
[    0.903855] io scheduler mq-deadline registered
[    0.908378] io scheduler kyber registered
[    0.921801] brd: module loaded
[    0.932016] loop: module loaded
[    0.938063] m25p80 spi0.0: found s25fl256s0, expected n25q128a11
[    1.051274] m25p80 spi0.0: s25fl256s0 (65536 Kbytes)
[    1.056296] 5 ofpart partitions found on MTD device spi0.0
[    1.061771] Creating 5 MTD partitions on "spi0.0":
[    1.066583] 0x000000000000-0x000000100000 : "qspi-fsbl-uboot"
[    1.073287] 0x000000100000-0x000000600000 : "qspi-linux"
[    1.079449] 0x000000600000-0x000000620000 : "qspi-device-tree"
[    1.085303] mtd: partition "qspi-device-tree" doesn't end on an erase/write block -- force read-only
[    1.095299] 0x000000620000-0x000000c00000 : "qspi-rootfs"
[    1.100693] mtd: partition "qspi-rootfs" doesn't start on an erase/write block boundary -- force read-only
[    1.111222] 0x000000c00000-0x000001000000 : "qspi-bitstream"
[    1.118137] libphy: Fixed MDIO Bus: probed
[    1.125413] libphy: MACB_mii_bus: probed
[    1.232065] macb e000b000.ethernet eth0: Cadence GEM/MAC: TechLab: patch for FIBRE (88E1512)
[    1.240510] macb e000b000.ethernet eth0: Cadence GEM rev 0x00020118 at 0xe000b000 irq 29 (80:34:28:8b:34:2f)
[    1.250356] Marvell 88E1510 e000b000.ethernet-ffffffff:00: attached PHY driver [Marvell 88E1510] (mii_bus:phy_addr=e000b000.ethernet-ffffffff:00, irq=POLL)
[    1.265512] ehci_hcd: USB 2.0 'Enhanced' Host Controller (EHCI) Driver
[    1.272164] usbcore: registered new interface driver usb-storage
[    1.279703] i2c /dev entries driver
[    1.289390] pca953x 0-0020: interrupt support not compiled in
[    1.296088] at24 0-0057: 32768 byte 24c256 EEPROM, writable, 64 bytes/write
[    1.303131] cdns-i2c e0004000.i2c: 100 kHz mmio e0004000 irq 23
[    1.310197] cdns-wdt f8005000.watchdog: Xilinx Watchdog Timer at f0988000 with timeout 20s
[    1.318812] EDAC MC: ECC not enabled
[    1.322759] sdhci: Secure Digital Host Controller Interface driver
[    1.328931] sdhci: Copyright(c) Pierre Ossman
[    1.333302] sdhci-pltfm: SDHCI platform and OF driver helper
[    1.391908] mmc0: SDHCI controller on e0100000.mmc [e0100000.mmc] using ADMA
[    1.399387] ledtrig-cpu: registered to indicate activity on CPUs
[    1.407714] usbcore: registered new interface driver usbhid
[    1.413302] usbhid: USB HID core driver
[    1.420550] NET: Registered protocol family 10
[    1.428157] Segment Routing with IPv6
[    1.431928] sit: IPv6, IPv4 and MPLS over IPv4 tunneling driver
[    1.438542] NET: Registered protocol family 17
[    1.443283] Registering SWP/SWPB emulation handler
[    1.452837] hctosys: unable to open rtc device (rtc0)
[    1.457921] of_cfs_init
[    1.460428] of_cfs_init: OK
[    1.463919] RAMDISK: gzip image found at block 0
[    1.488208] mmc0: new high speed SDHC card at address 1234
[    1.501966] mmcblk0: mmc0:1234 SA16G 14.4 GiB 
[    1.507916]  mmcblk0: p1
[    1.864614] EXT4-fs (ram0): couldn't mount as ext3 due to feature incompatibilities
[    1.873326] EXT4-fs (ram0): mounted filesystem without journal. Opts: (null)
[    1.880400] VFS: Mounted root (ext4 filesystem) on device 1:0.
[    1.886398] devtmpfs: mounted
[    1.892181] Freeing unused kernel memory: 1024K
[    1.951279] FAT-fs (mmcblk0p1): Volume was not properly unmounted. Some data 
```

## Userland

### rcS initial

```
Starting rcS...
++ Mounting filesystem
++ Mounting main fs
skip local
++ Setting up mdev
++ Setting hostname
+++ setting hn z7io_101 from macaddr 80:34:28:8b:34:2f
++ Start Lo
++ Setting EPOCH 2000 in case there is no NTP later
Sat Jan  1 00:00:00 UTC 2000
++ Networking .. assigning serial console, use CTRL-C to break
[    2.655435] IPv6: ADDRCONF(NETDEV_UP): eth0: link is not ready
eth0 Waiting for link up ... 6
eth0 Waiting for link up ... 5
[    3.822112] macb e000b000.ethernet eth0: link up (1000/Full)
[    3.827786] IPv6: ADDRCONF(NETDEV_CHANGE): eth0: link becomes ready
eth0 ethernet link up
+++ Starting dhcp daemon [default]
udhcpc: started, v1.34.1
udhcpc: broadcasting discover
udhcpc: broadcasting select for 10.12.196.190, server 10.12.196.15
udhcpc: lease of 10.12.196.190 obtained from 10.12.196.15, lease time 86400
deleting routers
route: SIOCDELRT: No such process
adding dns 10.12.196.15
+++ dhcp good, remove failsafe 737
udhcpc: started, v1.34.1
udhcpc: broadcasting discover
udhcpc: broadcasting select for 10.12.196.190, server 10.12.196.15
udhcpc: lease of 10.12.196.190 obtained from 10.12.196.15, lease time 86400
deleting routers
route: SIOCDELRT: No such process
adding dns 10.12.196.15
++ locate kernel modules
PACKAGE KO /mnt/ko/packageko-4.14.0-acq400-xilinx-g4cd1b648c487-230627170729.img exists, mount it
+++ bind legacy modules dir /usr/local/lib/modules
++ Starting http daemon
/etc/init.d/rcS: line 150: httpd: not found
++ Starting ssh daemon
++ Loading packages from /mnt/packages

```
### acq400common

```
++ Loading Package 03-acq400_common-231221174353.tgz
acq400_common.init
[    8.932068] xdevcfg f8007000.devcfg: ioremap 0xf8007000 to f09bb000

```

### z7io package

1. Load "BARE", a minimal FPGA to enable RTM i2c
```
+++ model z7io load support
++ Loading Package 05-z7io-231221192745.tgz
xiloader r1.01 (c) D-TACQ Solutions
eoh_location set 0
Xilinx Bitstream header.
built with tool version   : 2b
generated from filename   : Z7IO_BARE
part                      : 7z030ffg676
date                      : 2023/12/20
time                      : 12:46:36
bitstream data starts at  : 105
bitstream data size       : 5979916
```
2. Enumerate i2c
/usr/local/CARE/Z7IO/load.rtmi2c_overlay

```
[   10.096299] pca953x 2-0021: interrupt support not compiled in
[   10.111799] ad7418 2-0028: ad7417 chip found
[   10.123233] ad7418 2-0028: configuring for mode 1
[   10.140636] ad7418 2-0029: ad7417 chip found
[   10.158973] ad7418 2-0029: configuring for mode 1
[   10.165081] i2c i2c-1: Added multiplexed i2c bus 2
[   10.175731] at24 3-0051: 8192 byte 24c64 EEPROM, writable, 1 bytes/write
[   10.188768] ad7418 3-0029: ad7417 chip found
[   10.198178] ad7418 3-0029: configuring for mode 1
[   10.207242] i2c i2c-1: Added multiplexed i2c bus 3
[   10.218065] at24 4-0052: 8192 byte 24c64 EEPROM, writable, 1 bytes/write
[   10.233438] ad7418 4-002a: ad7417 chip found
[   10.248839] ad7418 4-002a: configuring for mode 1
[   10.256338] i2c i2c-1: Added multiplexed i2c bus 4
[   10.262451] i2c i2c-1: Added multiplexed i2c bus 5
[   10.268975] i2c i2c-1: Added multiplexed i2c bus 6
[   10.278822] i2c i2c-1: Added multiplexed i2c bus 7
[   10.291832] i2c i2c-1: Added multiplexed i2c bus 8
[   10.312992] i2c i2c-1: Added multiplexed i2c bus 9
[   10.323210] pca954x 1-0073: registered 8 multiplexed busses for I2C switch pca9548
[   10.331658] cdns-i2c e0005000.i2c: 100 kHz mmio e0005000 irq 50

```
3. gpio init
/usr/local/CARE/Z7IO/z7io_init_gpio

```
++ acq400_init_gpio_common end 01
++ lamp test 01
++ lamp test 99
++ leds all clear now 
++ acq400_init_gpio_common end 99
++ enable RTM power
++ z7io_init_gpio done
```
4. Load the main FPGA
FMC_SCAN_FPGA=Z7IO FMC_SCAN_SITES="1 2" SITE2BUS=2 /usr/local/bin/fmc-scan

```
+++ mounted fpga stock /mnt/ko/z7io_fpga-610-20230627171003.img at /mnt/fpga.d
++ decode FRU EEPROM site 1 OK
++ decode FRU EEPROM site 2 OK
is_identical myspec Z7IO_TOP_04_04 filespec Z7IO_TOP_04_04_40_9300_32B
WARNING:Z7IO 04 04: Z7IO 04 04 40 9300 32B is compatible but has extra stuff, so not identical
is_compatible myspec Z7IO_TOP_04_04 filespec Z7IO_TOP_04_04_40_9300_32B
+++ compatible bitfile Z7IO_TOP_04_04_40_9300_32B
+++ Internal name consistency check
is_compatible myspec Z7IO_TOP_04_04 filespec Z7IO_TOP_04_04_40_9300_32B
+++ compatible bitfile Z7IO_TOP_04_04_40_9300_32B
load FPGA /mnt/Z7IO_TOP_04_04_40_9300_32B.bit.gz
++ Sites populated: 2 ALL GOOD
ls: /mnt/fpga.d/Z7IO_TOP_04_04_40_9300_32B.bit.gz: No such file or directory

```

### normal boot from here

```
++ Loading Package 10-acq420-230627170729.tgz
acq420.init B1010
changing loglevel to debug
source /mnt/local/sysconfig/acq400.sh
[   14.865640] dma-pl330 f8003000.dmac: pl330 driver hacked by PGM 1203
[   14.872600] dma-pl330 f8003000.dmac: mcode_cpu:0xf1560000 bus:0x3f043000 c:8 sz:512 totsize:4096
[   14.882836] dma-pl330 f8003000.dmac: Loaded driver for PL330 DMAC-2364208
[   14.889638] dma-pl330 f8003000.dmac: 	DBUFF-128x8bytes Num_Chans-8 Num_Peri-4 Num_Events-16
for debug:
echo file acq400_drv.c +p > /sys/kernel/debug/dynamic_debug/control
echo file acq400_sysfs.c +p > /sys/kernel/debug/dynamic_debug/control
# ACQ424 DETECTED set VRANGE HI
VAP=13
VAN=-13
insmod /lib/modules/4.14.0-acq400-xilinx-g4cd1b648c487/acq420fmc.ko bufferlen=1048576 nbuffers=512 good_sites=1,2
[   15.195716] D-TACQ ACQ400 FMC Driver 3.782
[   15.200102] acq420 40000000.acq2006sc: site:0 GOOD
[   15.204992] acq420 40000000.acq2006sc: request_mem_region(40000000 10000 acq400.0)
[   15.212615] acq420 40000000.acq2006sc: acq400: site_no:0 dev_name:acq400.0 mapped 0x40000000 to 0xf15f0000
[   15.222279] acq420 40000000.acq2006sc: About to read MODID from f15f0000
[   15.228979] acq420 40000000.acq2006sc: Device MODID 86120702
[   15.234663] acq420 40000000.acq2006sc: acq400_modprobe id 86 SC
[   15.240576] acq420 40000000.acq2006sc: allocate_hbm() nb:512 bl:0x00100000
[   16.786842] acq420 40000000.acq2006sc: setting nbuffers 512
[   16.792525] acq420 40000000.acq2006sc: setting nbuffers 512
[   16.798102] acq420 40000000.acq2006sc: gpg:ee918cd0 base:f15ff000 buffer:ed8f9000 cursor:0
[   16.806381] acq420 40000000.acq2006sc: acq400_createSysfs()
[   16.812178] acq420 40000000.acq2006sc: IS_Z7IO_SC using kmcx attrs
[   16.818944] acq420 40000000.acq2006sc: dev_rc_finalize site:0 max:128 last:91 map:00000000 00000000 0f0f0f0f 00000000 T
[   16.829766] acq420 40000000.acq2006sc: dev_rc_finalize site:0 max:128 last:8 map:00000106 00000000 00000000 00000000 
[   16.840581] acq420 40010000.acq400fmc: site:1 GOOD
[   16.845457] acq420 40010000.acq400fmc: request_mem_region(40010000 10000 acq400.1)
[   16.853097] acq420 40010000.acq400fmc: acq400: site_no:1 dev_name:acq400.1 mapped 0x40010000 to 0xf1610000
[   16.862775] acq420 40010000.acq400fmc: About to read MODID from f1610000
[   16.869475] acq420 40010000.acq400fmc: Device MODID 0400091c
[   16.875170] acq420 40010000.acq400fmc: acq400_modprobe id 4 MODULE
[   16.881379] acq420 40010000.acq400fmc: acq400_mod_init_irq 47
[   16.887191] acq420 40010000.acq400fmc: ACQ420 device init
[   16.892616] acq420 40010000.acq400fmc: acq400_createSysfs()
[   16.898521] acq420 40010000.acq400fmc: dev_rc_finalize site:1 max:128 last:9 map:00000380 00000000 00000000 00000000 T
[   16.909244] acq420 40010000.acq400fmc: dev_rc_finalize site:1 max:128 last:3 map:0000000e 00000000 00000000 00000000 
[   16.920033] acq420 40020000.acq400fmc: site:2 GOOD
[   16.924882] acq420 40020000.acq400fmc: request_mem_region(40020000 10000 acq400.2)
[   16.932506] acq420 40020000.acq400fmc: acq400: site_no:2 dev_name:acq400.2 mapped 0x40020000 to 0xf1630000
[   16.942169] acq420 40020000.acq400fmc: About to read MODID from f1630000
[   16.948869] acq420 40020000.acq400fmc: Device MODID 0480001c
[   16.954563] acq420 40020000.acq400fmc: acq400_modprobe id 4 MODULE
[   16.960780] acq420 40020000.acq400fmc: acq400_mod_init_irq 48
[   16.966595] acq420 40020000.acq400fmc: ACQ420 device init
[   16.972019] acq420 40020000.acq400fmc: acq400_createSysfs()
[   16.977935] acq420 40020000.acq400fmc: dev_rc_finalize site:2 max:128 last:9 map:00000380 00000000 00000000 00000000 T
[   16.988660] acq420 40020000.acq400fmc: dev_rc_finalize site:2 max:128 last:3 map:0000000e 00000000 00000000 00000000 
[   16.999454] acq420 40030000.acq400fmc: warning: site 3 NOT GOOD
[   17.041772] D-TACQ MGT400 Comms Module Driver 0.147
[   17.047119] mgt400 400b0000.mgt400: mgt400_probe()
[   17.051970] mgt400 400b0000.mgt400: mgt400_device_tree_init() 01 ef7f66ec
[   17.058761] mgt400 400b0000.mgt400: failed to find IRQ values
[   17.064576] mgt400 400b0000.mgt400: mgt400 "mgt400.C" site:11 sn:2 phys:PCIe
[   17.071657] mgt400 400b0000.mgt400: mgt400_createSysfs()
+++ build_site0 model z7io
[   17.568891] spidev spi3.0: buggy DT: spidev listed directly in DT
Calibration default installed site:1 /usr/local/cal/ACQ424ELF-defcal.xml
build_knobs_device site:1 mtype:4
set clkdiv 200 get.sys /dev/acq400.1.knobs/clkdiv 200
Calibration default installed site:2 /usr/local/cal/ACQ424ELF-defcal.xml
build_knobs_device site:2 mtype:4
set clkdiv 200 get.sys /dev/acq400.2.knobs/clkdiv 200
+++ build nodes mgt400.C
+++ build nodes site 2
+++ build nodes site 1
+++ build nodes site 0
[   25.838144] xilinx-acq400-dma 801f0000.axidma: axi-dma-s2mm-channel offset regs _00000030
[   25.846726] xilinx-acq400-dma 801f0000.axidma: Probing xilinx axi dma engine...Successful
[   25.855123] xilinx-acq400-dma 801e0000.axidma: device_id not instantiated, limit 1 already reached
[   25.864168] xilinx-acq400-dma: probe of 801e0000.axidma failed with error -1
[   25.872366] acq420 40000000.acq2006sc: init_axi_dma() 01 AXI64 init now
[   25.878987] acq420 40000000.acq2006sc: init_axi_dma() 10
[   25.884352] acq420 40000000.acq2006sc: .. not enough buffers limit to 510
[   25.891137] acq420 40000000.acq2006sc: filter_axi: dma-pl330
[   25.896869] acq420 40000000.acq2006sc: filter_axi: dma-pl330
[   25.902560] acq420 40000000.acq2006sc: filter_axi: dma-pl330
[   25.908216] acq420 40000000.acq2006sc: filter_axi: dma-pl330
[   25.913896] acq420 40000000.acq2006sc: filter_axi: dma-pl330
[   25.919558] acq420 40000000.acq2006sc: filter_axi: dma-pl330
[   25.925244] acq420 40000000.acq2006sc: filter_axi: dma-pl330
[   25.930896] acq420 40000000.acq2006sc: filter_axi: dma-pl330
[   25.936577] acq420 40000000.acq2006sc: filter_axi: xilinx-acq400-dma
[   25.942964] acq420 40000000.acq2006sc: filter_axi: dma-pl330
[   25.948620] acq420 40000000.acq2006sc: filter_axi: dma-pl330
[   25.954306] acq420 40000000.acq2006sc: filter_axi: dma-pl330
[   25.959957] acq420 40000000.acq2006sc: filter_axi: dma-pl330
[   25.965632] acq420 40000000.acq2006sc: filter_axi: dma-pl330
[   25.971284] acq420 40000000.acq2006sc: filter_axi: dma-pl330
[   25.976959] acq420 40000000.acq2006sc: filter_axi: dma-pl330
[   25.982632] acq420 40000000.acq2006sc: filter_axi: dma-pl330
[   25.988282] acq420 40000000.acq2006sc: axi_dma not using standard driver using channels A x
[   25.996674] acq420 40000000.acq2006sc: __axi64_init_procfs() acw:ed915200
[   26.003494] acq420 40000000.acq2006sc: __axi64_init_procfs() acw:ce105c40
[   26.010288] acq420 40000000.acq2006sc: init_axi_dma() 99
++ Enable counter monitors
++ Enable analog power..
/usr/local/bin/procServ -p /var/run/knobs0.pid --restrict -q 4820 /usr/local/bin/acq400_knobs -s 0
/usr/local/bin/procServ -p /var/run/knobs1.pid --restrict -q 4821 /usr/local/bin/acq400_knobs -s 1
/usr/local/bin/procServ -p /var/run/knobs11.pid --restrict -q 4831 /usr/local/bin/acq400_knobs -s 11
/usr/local/bin/procServ -p /var/run/knobs2.pid --restrict -q 4822 /usr/local/bin/acq400_knobs -s 2
0: waiting for /var/run/acq400_knobs.0.pid

```


