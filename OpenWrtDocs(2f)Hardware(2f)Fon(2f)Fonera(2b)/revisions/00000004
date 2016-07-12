[[TableOfContents]]

= Fonera + =

The Fonera+ is very similar to the Fonera, especially to the FON2200. From the
outside the main difference is a bigger case and the additional Ethernet port.

Please also check the page about the Fonera in addition to this page, as most
information there applies to the Fonera+ too.

= RedBoot =

This was the original RedBoot configuration, when I got my Fonera+:
{{{
RedBoot> fconfig -l -n
boot_script: true
boot_script_data:
.. fis load -b 0x80100000 loader
..  go 0x80100000

boot_script_timeout: 2
bootp: false
bootp_my_gateway_ip: 0.0.0.0
bootp_my_ip: 192.168.1.1
bootp_my_ip_mask: 255.255.255.0
bootp_server_ip: 192.168.1.254
console_baud_rate: 9600
gdb_port: 9000
info_console_force: false
net_debug: false
}}}

That is: On boot we have a two seconds time frame to loggin via telnet and send
a Ctrl-C to abort the boot process and get access to RedBoot. So actually we
don't need a serial kable, we only need to configure the IP 192.168.1.254 on
our local network interface, that's nice! OTOH two seconds is somewhat short
and you may need severald tries to hit the time window, so
I change the configuration to give me a 10 second time frame:

{{{
RedBoot> fconfig boot_script_timeout 10
boot_script_timeout: Setting to 10
Update RedBoot non-volatile configuration - continue (y/n)? y
... Erase from 0xa87e0000-0xa87f0000: .
... Program from 0x80ff0000-0x81000000 at 0xa87e0000: .
}}}

Actually to get my telnet to send a proper ^C to the RedBoot I need to
have a .telnetrc file in my home directory, with the following content:

{{{
192.168.1.1
	mode line
}}}

Unfortunately this has one minor side effect: When flashing the device, telnet
doesn't display any progress (it displays all the progress when it is done), so
what you can do to work around this is: After pressing Ctrl-C you close the
telnet session, switch to an other user (or move .telnetrc out of the way)
and then connect again - RedBoot will be waiting anyway.

== Original flash layout ==

{{{
RedBoot> fis list
Name              FLASH addr  Mem addr    Length      Entry point
RedBoot           0xA8000000  0x80040400  0x00030000  0xA8000000
loader            0xA8030000  0x80100000  0x00010000  0x80100000
image             0xA8040000  0x80040400  0x00230004  0x80040400
image2            0xA8660000  0xA8660000  0x00140000  0x80040400
FIS directory     0xA87E0000  0xA87E0000  0x0000F000  0x00000000
RedBoot config    0xA87EF000  0xA87EF000  0x00001000  0x00000000
}}}

= Resources =
 * [https://shop.fon.com/FonShop/shop/US/ShopController?view=product&product=PRD-018 FON Shop Link]
