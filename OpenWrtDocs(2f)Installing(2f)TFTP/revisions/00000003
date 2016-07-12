= Installing OpenWrt via TFTP =

Although you can install the firmware through more traditional means (via webpage), there are reasons to install via TFTP. This is '''NOT''' a requirement, simply a damned good idea if you use self compiled firmware images; if anything goes wrong you can just TFTP the old firmware back.

When the device boots it runs a bootloader. It's the responsibility of this bootloader to perform basic system initialization along with validating and loading the actual firmware; think of it as the BIOS of the device before control is passed over to the operating system. Should the firmware fail to pass a CRC check, the bootloader will presume the firmware is corrupt and wait for a new firmware to be uploaded over the network. The type of the preinstalled bootloader depends on your router model. Broadcom based routers use CFE - Common Firmware Environment (older system boards use PMON), Texas Instruments based routers use ["ADAM2"].

The basic procedure of using a tftp client to upload a new firmware to your router:

 * unplug the power to your router
 * start your tftp client
  * give it the router's address (usually 192.168.1.1)
  * set mode to octet/binary
  * tell the client to resend the file, until it succeeds.
  * put the file
 * plug your router, while having the tftp client running and constantly probing for a connection
 * the tftp client will receive an ack from the bootloader and starts sending the firmware

/!\ '''Please be patient, the reflashing occurs AFTER the firmware has been transferred. DO NOT unplug the router, it will automatically reboot into the new firmware.'''

On routers with a DMZ LED, !OpenWrt will light the DMZ LED while booting, after the bootup scripts are finished it will turn off the DMZ LED. Sometimes automatic rebooting does not work, so you can safely reboot (power cycle) after waiting 6 minutes.

The TFTP commands vary across different implementations. Here are some examples:

== Linux/BSD ==
 
netkit's tftp commands:

{{{
tftp 192.168.1.1
binary
rexmt 1
timeout 60
trace
Packet tracing on.
tftp> put openwrt-xxx-x.x-xxx.bin
}}}

Setting "rexmt 1" will cause the tftp client to constantly retry to send the file to the given address. As advised above, plug in your box after typing the commands, and as soon as the bootloader starts to listen, your client will successfully connect and send the firmware. You can try to run "ping -f 192.168.1.1" (as root) in a separate window and enter the line "put openwrt-xxx-x.x-xxx.bin" as the colons stop running over your terminal when you power-recycle your router.

Note: for some versions of the CFE bootloader, the last line may need to be "put openwrt-xxx-x.x-xxx.bin code.bin".

Advanced TFTP commands:
(atftp source code: http://downloads.openwrt.org/sources/atftp-0.7.tar.gz)

{{{
atftp
connect 192.168.1.1
mode octet
trace
timeout 1
put openwrt-xxx-x.x-xxx.bin

Or use the command-line:
atftp --trace --option "timeout 1" --option "mode octet" --put --local-file openwrt-xxx-x.x-xxx.bin 192.168.1.1
}}}

== MacOS X ==

On Mac OS X, you should be able to flash the router with the command line tftp client, which behaves identically to netkit's tftp above.

Some people have had problems with the command line tftp client, however, and recommend using [http://www.mactechnologies.com/pages/downld.html MacTFTP] instead:

 * Download, install, and open MacTFTP
 * Choose Send
 * Address: 192.168.1.1
 * Choose the openwrt-xxx-x.x-xxx.bin file
 * Click on start while applying power to the WRT54G

Many Macs will disable the Ethernet card when the router is powered off and will take too long to re-enable the card, causing the TFTP transfer to fail with an "Invalid Password" error. Many people have had success if they manually configure their network card (in the "Ethernet" tab of "Built-in Ethernet" in System Preferences' Network panel) to:

 * Configure: Manual (Advanced)
 * Speed: 10 BaseT/UTP
 * Duplex: full-duplex

Alternatively, you can connect the router to the Mac via a hub or switch; see below for more information.

== Windows 2000/XP ==

Windows 2000 and Windows XP have a built-in TFTP client and it [http://martybugs.net/wireless/openwrt/flash.cgi can be used] to flash with !OpenWrt firmware.

'''Important:''' If you have a personal firewall, make sure it is disabled for this part. Some personal firewalls will not give any indication that they have blocked the tftp client. Please bear in mind that you should only be connected to the router when your personal firewall is disabled to avoid any nastiness, and remember to re-enable it when you are done.

Windows 2000/XP TFTP Client short Instructions

 * Open two command windows (Start-Run-Enter "cmd")
 * In one window, type "ping -t 192.168.1.1" and press enter. 192.168.1.1 is the router IP.
 * Ping will continuously try to contact the wrt. Keep this running
 * In the other window, prepare the tftp command "tftp -i 192.168.1.1 PUT OpenWrt-gs-code.bin". Do not press enter yet!
 * Now you may plug in the router (unplug it first if it was plugged).
 * In the ping window it will start saying "Hardware Error"
 * Return to the tftp window. As soon as the ping window starts to answer again, press enter in the tftp window.
 * The image should now be flashed without multiple tries.
 * If ping starts with "Hardware Error", then starts to answer, and then returns to  "Hardware Error" again for a short moment, you waited too long.

== Troubleshooting ==

Don't forget about your firewall settings, if you use one. It is best to run the "put" command and then immediately apply power to the router, since the upload window is extremely short and very early in boot.

||'''TFTP Error''' ||'''Reason''' ||
||Code pattern is incorrect ||The firmware image you're uploading was intended for a different model. ||
||Invalid Password ||The firmware has booted and you're connected to a password protected tftp server contained in the firmware, not the bootloader's tftp server. ||
||Timeout ||Ping to verify the router is online[[BR]]Try a different tftp client (some are known not to work properly) ||

Some machines will disable the ethernet when the router is powered off and not enable it until after the router has been powered on for a few seconds. If you're consistantly getting "Invalid Password" failures try connecting your computer and the router to a hub or switch. Doing so will keep the link up and prevent the computer from disabling its interface while the router is off.

Before you go searching for a hub to keep your link live, try setting your TCP/IP setting to a static IP (192.168.1.10; 255.255.255.0; 192.168.1.1 [gateway]) method instead of DHCP.
