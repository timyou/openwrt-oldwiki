= Freecom FSG-3 =
Freecom FSG-3 is Intel XScale based consumer NAS device. '''OpenWrt does NOT currently support this device.''' However, there's XScale port in progress by Kaloz. It's not targeted for FSG-3, but when ready it should be fairly easy to add FSG-3 specific features to it.

== Hardware ==
 * Intel XScale IXP422 at 266MHz with hardware encryption
 * 64MB RAM and 4MB flash
 * Four port Realtek RTL8305SB switch configured as one WAN port and three LAN ports. Uses two XScale NPEs (eg. not VLANs like most WLAN APs)
 * NEC USB 2.0 on PCI-bus. Four external (two front, two back) and one internal (empty pads on PCB)
 * VIA VT6421A IDE controller on PCI-bus. One external eSATA, one internal PATA. Empty pads on PCB likely for another SATA bus
 * Internal HDD. Various sizes available (80G, 160G, 250G, 400G, 500G)
 * Empty Mini-PCI socket on PCB for WLAN option. Stock firmware supports only Marvell based cards.
 * Power button, Unplug button and Reset button. On PCB there's SYNC button pads
 * Six user controllable leds (HDD, power, USB, USB unplug, WAN, WLAN)
 * Small approx. 3cm * 3cm fan
 * JTAG connector
 * TTL serial connector (another empty pads next to it, maybe second serial port)
 * Winbond environment monitoring chip with three temperature sensors and fan RPM monitoring+control
 * Onboard RTC with removable battery on I2C bus

== Software ==
FSG-3 uses RedBoot bootloader and runs bigendian SnapGear Linux 3.1.6 based on 2.4.27 kernel. Freecom told they're going to upgrade to 2.6 kernel during 2006.

There's various add-ons and GPL download on [http://www.openfsg.com/ http://www.openfsg.com]

== Notes ==
 * Holding reset button while powering on enables recovery mode. FSG requests IP using bootp and tries to load zImage-recovery with tftp from bootp server.
 * RedBoot incorrectly reports Coyote machine ID to Linux kernel
 * Fan is noisy but can be slowed down using software but it causes higher internal temperatures.
 * At least 250GB model I bought came with internal PATA HDD. I don't know if others are PATA too or maybe SATA.

== Links ==
 * Official Freecom support site: http://www.openfsg.com
 * Sales page: http://www.freecom.com/ecProduct_detail.asp?ID=2347
 * Internal photos: http://80.81.183.101/fsg3/
 * Thread on OpenWrt forum: http://forum.openwrt.org/viewtopic.php?id=5828
