= How to flash the firmware =

This page about how to flash the firmware of the ASUS WL700gE.
It tells what you need and what you can expect.

Needed:
 * The (new) firmware, in the examples it is named `newfirmware.img`, yours will have another name
 * computer with ethernet card, IP-address set in the range `192.168.1.2-192.168.1.254` and not in use by another computer. Netmask set to `255.255.255.0`. ( WL700gE is `ip 192.168.1.1 nm 255.255.255.0` )
 * networkcable, those with RJ45 connectors

== web gui ASUS ==

 * Go with a webbrowser to `http://192.168.1.1`
 * login
 * click `advanced setting` from the top menu
 * click `system` from the left side menu
 * click `upgrade firmware` from the left side menu
 * click button `browse`
 * select `newfirmware.img`
 * click button `upload`
 * there will be an infobox that says something like {{{
Upgrade will take about 2 minutes. Do NOT interrupt it
}}}  Acknowledge it with `OK`.
 * you can expect some progressbars, even with no progressbars you still could have a succesfull firmware upgrade ( an extra poweroff - poweron might be needed )

== web gui foo ==

this is just a placeholder for using 'foo' firmware


== From within OpenWrt ==

Once OpenWrt is running with / mounted from the disk (rather than from the squashfs and/or jffs2 partition), the flash device is not used any more, so it is possible to install a newer image while running: it will be used at the next boot.  To do that, you first want to make sure that the flash is not used, e.g. with `umount /rom`.  Then you can simply run `mtd -e linux -r write <foo.trx> linux` where `<foo.trx>` is the firmware file you want to install.


== forced TFTP ==

You will need `tftp` client software on your computer.

To get the ASUS WL700 in `tftp server mode` you need to do

 * unplug the power cord
 * press the orange 'ezsetup' button and keep it pressed
 * plug in the power cord
 * wait for a few blinks on the 'ready' led
 * release 'ezsetup', 'ready' stops blinking (stops flashing), it might be on, it might be off, both states are fine. (note: no LED for `link detect` in the 'LAN' is on.)

Verify that you have connecting with the ASUS by `ping 192.168.1.1`, it should be succesfull.

=== TFTP with Microsoft Windows XP ===

 * open command line interface with 'cmd'
 * `tftp -i newfirmware.img 192.168.1.1`
 * FIXME please help to keep this wiki in good shape

=== TFTP with Microsoft Windows Vista ===

 * open command line interface with 'powershell'
 * `tftp  FIXME`

=== TFTP with Linux and other Unix alikes ===

 * you allready have a command line interface
 * `tftp 192.168.1.1`
 * tftp> `binary`
 * tftp> `trace`
 * tftp> `put newfirmware.img`
 * (download progress scrolls over screen ( due the `trace` ))
 * tftp> `quit`

## 
## == serial line ==
## 
## It is not known if this works FIXME
## 

## == JTAG ==
