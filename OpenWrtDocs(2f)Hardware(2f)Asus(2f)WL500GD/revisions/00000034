= Asus WL-500g Deluxe =

The device is supported in OpenWrt 1.0 (White Russian) and later. 
You need to install the openwrt-brcm-2.4-<type>.trx firmware images.

{{{
Bootloader: CFE 
System-On-Chip:  Broadcom 5365
CPU Speed: 200 Mhz
Flash size: 4 MB
RAM: 32 MB (some older units have only 16 MB enabled)
Wireless: integrated Broadcom BCM4306 802.11b/g Wireless LAN Controller
Ethernet: Robo switch BCM5325e
USB: 2x USB 2.0   
Serial: yes
JTAG: no
}}}

The {{{boot_wait}}} NVRAM variable is on by default. Resetting to factory defaults via reset button or {{{mtd erase nvram}}} is '''safe''' on this unit. 

The router is sometimes called Asus WL-500GX or Asus WL-500g Deluxe V.

== TFTP Installation notes ==

Enable '''Failure Mode''' - remove the power, press and hold the reset button while returning power. Within a few seconds the PWR LED starts flashing slowly (once second on, one second off). Release the reset button and continue.

[note by frr] Alternative approach: the WL-500GD's got a group of four LEDs on the right: LAN1 through LAN4. If you press and hold the reset button, so that it's pressed during power-up, these four LEDs become alight right from the power-up. Now pay attention: some two/three seconds after power-up, these four LEDs turn dark. Release the reset button immediately when you observe this. The WL-500GD should revert to the "Failure mode". (If you keep the button pressed, the Failure mode doesn't activate.)
Can't say whether or not the behaviour depends on the firmware installed - may be different with the original ASUS firmware. This is the way it seems to behave with RC4 installed.

You should be able to ping the unit:

{{{
ping 192.168.1.1
}}}

/!\ Note, the ASUS WL-500GD doesn't revert to the 192.168.1.1 address when starting the bootloader, but uses the LAN IP address set in NVRAM. Try this address if you have difficulties.

(!) If you can’t ping the unit retry enabling "'Failure Mode'", even if the LED is blinking it sometimes does not respond. Turn it off and then on first. You can even do a factory reset.

Send image with TFTP:
{{{
tftp 192.168.1.1
tftp> binary
tftp> trace
tftp> put openwrt-xxx-x.x-xxx.trx
}}}

After this, wait for the PWR LED to stop flashing and the device to reboot and you should be set. There's also nice shell script to do this work for you at http://openwrt.org/downloads/utils/flash.sh. This script is also included in the source under scripts/flash.sh.

[note by frr] It seems that on my WL-500GD with RC4 already installed, you don't need the whole script. At least the first line (the one with GET ASUSSPACELINK) seems defunct.
All you need is the line saying
 
echo -en "binary\nput $YOUR_FIRMWARE_TRX ASUSSPACELINK\nquit\n" | tftp 192.168.1.1

For some reason though, the device doesn't reboot after flashing. Just wait 5 minutes, unplug the power and reconnect. After a while (1-2 minutes), the WLAN LED should light and OpenWRT is up and running.


=== Send image with Firmware Restoration technique ===

You can use the ASUS Firmware Restoration tool to send an image from a Windows PC to the router (including OpenWrt). The tool is on the supplied CD or available from the ASUS web site.

[note by frr] It seems that the restoration tool only works if you have an original ASUS firmware (re)installed. It doesn't detect the WL-500GD if it's already got OpenWRT installed (observed with an unresponsive RC4 on my box). If this is the case, perhaps your only chance is TFTP.

/!\ Before you start the Firmware Restoration tool, disable all interfaces on the PC except for the one connected to the Router. The software seems to pick an interface at random.

Put the Router in '''Failure Mode''' (see above) and start the '''Firmware Restoration''' program. Select the desired firmware and click on Upload. The software will search for the router - the status is ''Connect to the wireless device'', it will do this for about 32 seconds.

/!\ The software will only find the router if it is in recovery mode.

The tool provides status as it works:

 * Uploading (LAN interface LED blinks during transfer)
 * Recovery is in progress
 * Success

After this you should be able to connect to the Router.

== wrong nvram settings ==

/!\ By providing wrong nvram settings, the router CPU might loose it´s connection to the switch.
(wrong vlan configuration)
If this is the case, it´s impossible to connect to the router via lan. Even in '''Failure Mode''' there
is no way to restore the fw via tftp because the packages never reaches the routers cpu.
Thats because the router reads nvram configuration during cfe sequence.
The only way out of this Situation is to fix the wrong nvram settings
This can only be done via serial console (see below) during the lack of lan support.

Fortunately the router carries default nvram parameter.
They can be restored by deleting the entire nvram. (All settings will be lost!)


== Serial console ==

See [http://wl500g.info/showthread.php?t=1993].


== USB storage ==

For information about how to use a USB storage device (such as a memory stick or a hard
drive) and even boot from it, see [:UsbStorageHowto].

== Sonics Silicon Backplane ==

The silicon backplane is an internal processor bus that connects several on-chip devices much like the PCI bus. Most of these internal devices are sort of emulated as PCI devices. At least the bcm43xx 44xx 47xx and BCM53XX broadcom chipsets contain this internal bus. In the BCM63xx series it seems they switched to a different bus type, or have made it hidden. 

The files sbchipc.h and sbconfig.h (Google) contain a lot of information on this topic for the interested reader.

{{{
Devices that pop up on the Silicon backplane, these are emulated as PCI devices on bus 0:

Physical    Vendor  Core    CoreRev sbbidlow        Description
18000000    4243    800     5       100422dd        Common core: chip 5365 rev 1
18001000    4243    806     6       110422c5        enet mac core
18002000    4243    80b     1       110422c5        ipsec core
18003000    4243    808     2       110422c5        usb 1.1 host/device core
18004000    4243    804     8       101422d5        pci core
18005000    4243    816     1       100522c5        mips3302 core
18006000    4243    80f     0       1000225d        memc sdram core

Is this the same as on 0x18005000?
40001000    4243    816     1       100522c5        mips 3302 core

The external SB cells for the BCM4306:
40004000    4243    812     5       110422c5        802.11 MAC core
40005000    4243    804     9       101522d5        pci core


Devices that pop up on the "real" PCI bus:

Bus.dev.func  registers          vend:prod     Description
1.0.0         iomem 0x40000000   14e4:5365     BCM5365P Sentry5 Host Bridge
                  - 0x40001fff
1.2.0         io 0x100-0x11f     1106:3038     VT82xxxxx UHCI USB 1.1 Controller
1.2.1         io 0x120-0x13f     1106:3038     VT82xxxxx UHCI USB 1.1 Controller
1.2.2         iomem 0x40002000   1106:3104     VIA USB 2.0
                  - 0x400020ff
1.3.0         iomem 0x40004000   14e4:4320     BCM4306 802.11b/g Wireless LAN Controller
                  - 0x40005fff

Devices that pop up on the MII bus, accesible via the mac core:

bcm5325e or compatible, MII (MDC/MDIO)  5 ports switch

}}}
==Enabling all RAM==
If you have only 16MB of RAM enable you can enable all of the 32 MB with these command
{{{
nvram set sdram_init=0x2008
nvram set sdram_ncdl=0
nvram commit
reboot
}}}
== 64MB RAM upgrade ==
The following schematics from page 183 FCC report shows current RAM section:
[[ImageLink(wl500gx-ram-schematics.png,width=100%)]]

Upgrading RAM to 64 MB is possible with 256Mbit chips from PC 133 SDRAM modules.

Skilled amateur can follow [[http://begunje.dyndns.org/articles/wl500gx-ram-upgrade/index.html Oleo's instructions]] for 
upgrading RAM. There is also [[http://begunje.dyndns.org/gallery/ram-upgrade/index.html photo gallery]] for upgrade 
procedure.
----
CategoryModel
