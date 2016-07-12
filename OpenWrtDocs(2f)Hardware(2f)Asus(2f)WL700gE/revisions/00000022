= Asus WL-700gE =
Kamikaze has support for this device. However, since you need to fit OpenWrt to internal flash (2MB) it's quite limited on features. IDE HDD is supported, but only as new mount point so installing packages to disk requires some manual work. After replacing the /sbin/init script you can use a partiton of the IDE HDD to install packages the normal way. Device is also marketed as Asus WL-700G.

A precompiled version of OpenWRT Kamikaze 7.09 (Broadcom, 2.4 kernel) is [http://wl700g.homelinux.net/portal/content/view/29/30/ here] and step-by-step instructions are provided. Note that some operations (even ones as simple as ''ls /'') will fail or crash while the installation described on that page is partially-complete; they do operate correctly once the install (and pivot_root to the HDD) are completed.

The precompiled image installs a base set of drivers (aec62xx, diag, ehci-hcd, ext3, fat, ide-core, ide-default, ide-detect, ide-disk, ide-dma, ide-geometry, ide-io, ide-iops, ide-lib, ide-probe-mini, ide-probe, ide-proc, ide-taskfile, ide, jbd, ppp_async, ppp_generic, scsi_mod, sd_mod, setup-pci, slhc, switch-adm, switch-core, switch-robo, uhci, usb-ohci, usb-storage, usbcore, vfat) but does not provide hardware RTC support.

== Hardware ==
 * Broadcom 4780 @ 266MHz (BCM4780PKPBG) SoC with hardware encryption (crypto not currently supported)
 * 2MB FLASH (MX 29LV160CT1C-90G) and 64MB DDR-SDRAM (2 * Samsung K4H561638F-UCCC)
 * VIA USB 2.0 controller (VT6212L), 3 external USB connectors, one internal (pads on PCB)
 * Acard/Artop PATA controller (ATP865-B) and Hitachi 160GB 7200rpm PATA disk (HDT722516DLAT80)
 * Empty mini-pci header on PCB (not usable on stock enclosure and missing mini-pci connector itself)
 * Broadcom switch, 4 LAN, 1 WAN (BCM5325EKQMG)
 * Broadcom Single-Chip 802.11g Transceiver (BCM4318EKFBG)
 * RTC on I2C (Ricoh RV5C386A, CR1220 3V battery)
 * TTL serial port hidden under powersupply (4-pin header)
== GPIO ==
 * GPIO 0 = POWER-button (0 = released, 1 = pressed)
 * GPIO 1 = READY-led (0 = on, 1 = off)
 * GPIO 3 = POWER-enable, turns on power to HDD and switch leds (0 = disable, 1 = enable)
 * GPIO 4 = EZSETUP-button (0 = released, 1 = pressed)
 * GPIO 6 = COPY-button (0 = released, 1 = pressed)
 * GPIO 7 = RESET (0 = reset system, 1 = normal state)
There's references in Asus GPL tarball that GPIO 5 might be I2C SCL and GPIO 2 be I2C SDL. Asus sources also contain Broadcom I2C driver and sources for Ricoh RTC.

== Links ==
 * [Howto] Install OpenWrt Kamikaze 7.09 on the ASUS WL-700g Encore on OpenWrt forum http://forum.openwrt.org/viewtopic.php?id=12887
 * Thread on OpenWrt forum http://forum.openwrt.org/viewtopic.php?pid=41106#p41106
 * User forum, includes inside pictures, Q&A, etc: http://wl700g.info/forumdisplay.php?f=87
 * Detailed inside pictures http://sukkamehulinko.romikselle.com/wl700g/
 * Installing a SerialConsole, with detailed pictures http://www.tiedyedfreaks.org/eric/WL-700gE/
 * Customize firmware here! http://home.comcast.net/~kfurge/wl700ge.html
 * Info about [http://wiki.openwrt.org/HardwareAcceleratedCrypto hardware accelerated crypto]
 * Setup OpenWrt on WL700Ge http://wl700g.homelinux.net/
== NVRAM ==
{{{
apps_pool=MYVOLUME1
apps_share=MYSHARE1
boardflags=0x0110
boardnum=44
boardrev=0x10
boot_wait=off
bridge_disable=0
cfe_wait_led_gpio=1
cfe_wait_on_restore=0
clkfreq=264
custom_shutdown_command=stoprcasus
default_boardflags=0x0110
default_http_passwd=
default_http_username=
default_lan_proto=dhcp_server
default_new_disk_action=one_per_disk
default_new_system_disk_name=SYSTEM
default_physical_authentication_enable=disabled
default_primary_pool_name=MYVOLUME
default_primary_share_name=MYSHARE
default_router_disable=0
default_start_page=start_system.asp
default_workgroup=WORKGROUP
dev_mfr_url=http://www.asus.com/
dev_mfr=ASUS
dl_ram_addr=a0001000
early_startup_command=convertasus
et0macaddr=00:17:31:BA:E4:33
et0mdcport=0
et0phyaddr=30
et0phyaddr=30
et1macaddr=40:10:18:00:00:2c
et1mdcport=1
et1phyaddr=31
gpio_0_name=soft_power_switch
gpio_3_name=power_enable
gpio6=robo_reset
hardware_version=WL700g-01-08-01-00
kernel_gpio_init_out_3=1
kernel_gpio_init_out_6=1
lan_ifname=br0
lan_ifnames=vlan0 eth1
lan_ipaddr=192.168.1.1
lan_netmask=255.255.255.0
landevs=vlan0 wl0
misc_io_mode=bcmgpio
model_desc=ASUS Wireless Storage Router
model_name=ASUS WL700g
model_no=WL700g
model_url=http://www.asus.com/
new_disk_action=one_per_disk
new_system_disk_name=SYSTEM
os_flash_addr=bfc40000
os_ram_addr=80001000
pivot_partition_size=65536
pivot_root_1=/dev/ide/host2/bus0/target0/lun0/part1
pivot_root_2=/dev/ide/host2/bus0/target0/lun0/part2
pivot_root_current=1
pivot_wait=0
pmon_ver=CFE 3.91.23.0
primary_ifname=eth0
primary_pool_name=MYVOLUME
primary_share_name=MYSHARE
regulation_domain=0X30DE
rescue_gpio=4
reset_gpio=7
router_disable=0
scratch=a0180000
sdram_config=0x0062
sdram_init=0x0009
sdram_ncdl=0x10607
sdram_refresh=0x0000
ses_enable=0
standard input boardtype=0x042f
startup_command=rcasus
swap_mode=auto
wait_time=1
wan_ifname=eth0
wan_ifname=eth0
wan_ifnames=eth0
wan_vport=0
wandevs=et0
watchdog=5000
web_hook_libraries=corewebhooks netwebhooks diskwebhooks winnet printwebhooks netregistration samplenetregistration samplehooks
wlan_hardware_present=yes
wlan_ifname=eth1
wlan_ipaddr=192.168.21.1
wlan_netmask=255.255.255.0
vlan0hwname=et0
vlan0ports=1 2 3 4 5*
vlan1hwname=et0
vlan1ports=0 5u
}}}
