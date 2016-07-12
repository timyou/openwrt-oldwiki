= Freecom FSG-3 =
Freecom FSG-3 is Intel XScale based consumer NAS device. '''OpenWrt does NOT currently support this device.''' However, there's an XScale port in progress by Kaloz; it's not targeted to FSG-3, but when it's ready it should be fairly easy to add FSG-3 specific features to it. Freecom has shown a friendly attitude towards the opensource community and they're willing to help us with few restrictions (no additional warranty replacements due to hacked devices, no extra tech support questions due to customizations and no unfair advantage provided to competitors).

== Hardware ==
 * Intel XScale IXP422 at 266MHz with hardware encryption
 * 64MB RAM and 4MB flash
 * Four port Realtek RTL8305SB switch configured as one WAN port and three LAN ports. Uses two XScale NPEs (eg. not VLANs like most WLAN APs)
 * NEC USB 2.0 on PCI-bus. Four external (two front, two back) and one internal (empty pads on PCB)
 * VIA VT6421A IDE controller on PCI-bus. One external eSATA, one internal PATA. Empty pads on PCB for secondary SATA bus
 * Internal HDD. Various sizes available (80G, 160G, 250G, 400G, 500G)
 * Empty Mini-PCI socket on PCB for WLAN option. Stock firmware supports only Marvell based cards.
 * Power button, Unplug button and Reset button. On PCB there's SYNC button pads
 * Six user controllable leds (HDD, power, USB, USB unplug, WAN, WLAN)
 * Small approx. 3cm * 3cm fan
 * JTAG connector (pin-out unknown)
 * TTL serial connector (another empty pads next to it, maybe second serial port)
 * Winbond W83782D environment monitoring chip with three temperature sensors and fan RPM monitoring+control
 * Onboard RTC with removable battery on I2C bus

== Software ==
 * FSG-3 uses RedBoot bootloader and runs bigendian SnapGear Linux 3.1.6 based on 2.4.27 kernel. Freecom told they're going to upgrade to 2.6 kernel during 2006.
 * There's various add-ons and GPL download on [http://www.openfsg.com/ http://www.openfsg.com]

== Status ==
 * 2.6.16 patched and running (based on SlugOS 3.10-beta)
 * Network interfaces and switch work (0,1,2=LAN, 3=LAN/NPE, 4=WAN)
 * MAC addresses for network interfaces correctly read from flash
 * SATA and PATA disks work (with slightly modified Fedora Core 4 patch from VIA)
 * USB ports work with stock USB drivers
 * WIFI card on Mini-PCI slot detected by kernel (Tested with Atheros and Intel, haven't tried loading drivers yet)
 * Freecom registered proper ARM Linux machine ID for FSG-3 (1091)
 * I2C, RTC, sensors and FAN rpm control working with stock drivers

== ToDo ==
 * Enable buttons (GPIO's known, need to adapt NSLU2 code)
 * Leds (Connected to expansion bus, needs some new code to support)
 * Hardware crypto (Driver downloadable from Intel but does it work in Little-Endian mode?)
 * Passing arguments from RedBoot to 2.6 kernel causes crash. Works with stock Freecom 2.4 kernel.
 * OpenWrt support (Waiting for buildroot-ng XScale support) 

== Notes ==
 * Holding reset button while powering on enables recovery mode. FSG requests IP using bootp and tries to load zImage-recovery with tftp from bootp server.
 * RedBoot incorrectly reports Coyote machine ID to Linux kernel
 * Fan is noisy. It can be slowed down using software but it causes higher internal temperatures.
 * At least 250GB model came with internal Samsung 7200rpm 8MB PATA HDD. I don't know if other models are PATA or SATA.

== Links ==
 * http://www.nslu2-linux.org/ Linux on the ARM-based NASes
 * Official Freecom support site: http://www.openfsg.com
 * Sales page: http://www.freecom.com/ecProduct_detail.asp?ID=2347
 * Resellers: [http://www.mobileplanet.com/product.asp?code=129619 US] and [http://www.mobileplanet.com/product.asp?code=129619 Europe(UK)]
 * Internal photos: http://80.81.183.101/fsg3/
 * Thread on OpenWrt forum: http://forum.openwrt.org/viewtopic.php?id=5828
