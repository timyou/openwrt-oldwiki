'''Flashing Asus products'''

The {{{boot_wait}}} NVRAM variable is '''on''' by default for Asus products compatible with !OpenWrt.

'''Enabling Failsafe Mode'''

This is done by removing the power, and pressing and holding the reset button while returning power. Within a few seconds the PWR LED starts flashing slowly (one second on, one second off). Once the LED is flashing the reset button can be released.

'''TFTP Installation notes'''

After enabling Failsafe Mode you should be able to ping the unit. Asus products do not revert to a default IP address when in Failsafe Mode, but will instead use the address stored in NVRAM.

{{{
ping -t <ip-address>
}}}

Factory IP adresses for Asus products:

 * WL-500gx: 192.168.1.1
 * WL-HDD: 192.168.1.220

(!) Even if the LED is blinking the device sometimes does not respond. If you can’t ping the unit try reenabling "'Failsafe Mode'".

Send image with TFTP:

{{{
tftp 192.168.1.1
tftp> binary
tftp> trace
tftp> put openwrt-xxx-x.x-xxx.trx
}}}

After this, wait for the PWR LED to stop flashing and for the device to reboot and you should be set. There's also a nice shell script to do this work for you at http://openwrt.org/downloads/utils/flash.sh. This script is also included in the source under scripts/flash.sh.

For some reason, though, the device doesn't reboot after flashing. Just wait 5 minutes, unplug the power and reconnect. After a while (1-2 minutes) the WLAN LED should light and OpenWRT is up and running.

'''Send image with Firmware Restoration technique'''

You can use the ASUS Firmware Restoration tool to send an image from a Windows PC to the router (including OpenWrt). The tool is on the supplied CD or available from the ASUS web site ''('''For the WL-HDD:''' Go to '''www.asus.com''', click on '''Download''', search for '''WL-HDD''', click on '''Utilities''' and download the program in the language of your choice. Part of the program is the Firmware Restoration tool)''

/!\ Before you start the Firmware Restoration tool, disable all interfaces on the PC except for the one connected to the Router. The software seems to pick an interface at random.

Put the Router in '''Failsafe Mode''' (see above) and start the '''Firmware Restoration''' program. Select the desired firmware and click on Upload. The software will search for the router - the status is ''Connect to the wireless device'', it will do this for about 32 seconds.

/!\ The software will only find the router if it is in recovery mode.

The tool provides status as it works:

 * Uploading (LAN interface LED blinks during transfer)
 * Recovery is in progress
 * Success

After this, you should be able to connect to the Router.

'''If the Firmware Recovery utility doesn't work'''

Several Asus products are not able to be flashed directly using tftp due to them requiring special commands to enable them to accept a new firmware. Others refuse to accept a firmware using the accompanying Firmware Recovery utility as well, ironically.

Units known to require a special command:

 * WL-300g
 * WL-500g
 * WL-HDD 

There are two possible workarounds to this problem.

''TFTP with control commands''

After putting the device in Failsafe Mode, issue the following commands:

TFTP commands:

{{{
tftp 192.168.1.1
tftp> binary
tftp> trace
tftp> get ASUSSPACELINK\x01\x01\xa8\xc0 /dev/null
tftp> put openwrt-xxx-x.x-xxx.trx ASUSSPACELINK
}}}

After this, wait until the PWR LED stops flashing and for the device to reboot and you should be set.

There's also a nice shell script doing this work for you at http://openwrt.org/downloads/utils/flash.sh.

''Using Firmware Recovery utility to prepare unit for new firmware''

First enter Failsafe Mode. Start the Firmware Recovery utility, select a firmware and click the Upload button. The unit will, of course, not be able to flash the firmware, but you should notice that the LED is no longer blinking. Wait until the utility times out after 31 seconds, then issue the following command:

{{{
tftp -i <ip-address> PUT openwrt-xxx-x.x-xxx.trx
}}}

/!\ If you selected the same firmware in the Firmware Recovery utility that you are trying to upload, you will need to close the utility so the file is available to be uploaded with tftp.

Replace <ip-address> with the units IP address ('<' and '>' should not be part of the command) and make sure you are either in the same directory as the firmware, or you designate the correct path to the firmware. After a second or two a message stating the transfer was successful should appear.

The unit should restart on its own. If you are unable to contact the unit after a few minutes, restart it.
