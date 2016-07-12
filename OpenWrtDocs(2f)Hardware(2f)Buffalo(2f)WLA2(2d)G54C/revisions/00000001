== TFTP Installation ==

Setup is much the same as the other G54 units.
Default ip is 192.168.11.100


The usual tftp commands as below:

{{{
tftp 192.168.11.100
tftp> binary
tftp> trace
tftp> rexmt 1
tftp> timeout 60
tftp> put openwrt-xxx-x.x-xxx.trx
}}}

Reset LED will go orange, after a couple of minutes you may telnet in, use the passwd command, reboot and you're set.

== Flashing via GUI (DD-WRT) ==

Grab a copy of the latest [http://www.dd-wrt.com/dd-wrtv2/downloads.php Generic Broadcom DD-WRT image], at the time of writing 'dd-wrt.v24 beta' confirmed as working.

Patch the image using the app [http://www.dd-wrt.com/phpBB2/viewtopic.php?t=12166 ddadder] to make it ready for flashing via GUI (credit to '''Eko''' the author).

{{{
> ddadder dd-wrt.v24_generic.bin wla2-g54c
}}}

Take the patched image and upgrade firmware as normal via HTTP on the Buffalo device. Once complete navigate to `http://192.168.1.1` and find the DD-WRT status page.

== WDS+WPA problems ==

If you can't get WDS+WPA working, make sure that the wl0_ifname (eth1) is listed in the lan_ifnames! -- JpSugarbroad
