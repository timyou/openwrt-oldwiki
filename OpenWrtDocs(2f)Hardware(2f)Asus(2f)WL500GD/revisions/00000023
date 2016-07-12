'''Asus WL-500g Deluxe'''

The router is supported in OpenWrt 1.0 (White Russian) and later. 
You need to install the openwrt-brcm-2.4-<type>.trx firmware images.

{{{
System-On-Chip:  Broadcom 5365
CPU Speed: 200 Mhz
Flash size: 4 MB
RAM: 32 MB (some older units have only 16 MB enabled)
Wireless: integrated Broadcom BCM4306 802.11b/g Wireless LAN Controller
Ethernet: Robo switch BCM5325e
two external USB 2.0 ports   
serial port accessable
no jtag
}}}

The {{{boot_wait}}} NVRAM variable is on by default.

The router is sometimes called Asus WL-500GX or Asus WL-500g Deluxe V.

'''TFTP Installation notes'''

Enable '''Failure Mode''' - remove the power, press and hold the reset button while returning power. Within a few seconds the PWR LED starts flashing slowly (once second on, one second off). Release the reset button and continue.

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

For some reason though, the device doesn't reboot after flashing. Just wait 5 minutes, unplug the power and reconnect. After a while (1-2 minutes), the WLAN LED should light and OpenWRT is up and running.

'''Send image with Firmware Restoration technique'''
You can use the ASUS Firmware Restoration tool to send am image from a Windows PC to the router (including OpenWrt). The tool is on the supplied CD or available from the ASUS web site.

/!\ Before you start the Firmware Restoration tool, disable all interfaces on the PC except for the one connected to the Router. The software seems to pick an interface at random.

Put the Router in '''Failure Mode''' (see above) and start the '''Firmware Restoration''' program. Select the desired firmware and click on Upload. The software will search for the router - the status is ''Connect to the wireless device'', it will do this for about 32 seconds.

/!\ The software will only find the router if it is in recovery mode.

The tool provides status as it works:

 * Uploading (LAN interface LED blinks during transfer)
 * Recovery is in progress
 * Success

After this you should be able to connect to the Router.

'''Serial console'''

See [http://wl500g.info/showthread.php?t=1993].


'''USB storage'''

For information about how to use a USB storage device (such as a memory stick or a hard
drive) and even boot from it, see [:UsbStorageHowto].

----
CategoryModel
