= D-Link DSL-G604T main information =

== Work in Progress ==

Porting OpenWRT to the D-Link DSL-604T is a work in progress. That's means, that you may compile and run only from Kamikaze SVN. Still there isn't support neither in White Russian nor Kamikaze releases, so installation procedure is not so hacking as on ZyXEL's, but more hard than uploading throught web-interface. All run's ok with 2.6.x kernel maybe except wireless, it need some tests.

== Troubles ==

There seems that Wi-Fi isn't work at this date (17/06/2007):

{{{acx: this driver is still EXPERIMENTAL
acx: reading README file and/or Craig's HOWTO is recommended, visit http://acx100.sf.net in case of further questions/discussion
acx: compiled to use 32bit I/O access. I/O timing issues might occur, such as non-working firmware upload. Report them
acx: running on a little-endian CPU
acx: PCI module v0.3.36 initialized, waiting for cards to probe...
PCI: Enabling device 0000:00:00.0 (0000 -> 0002)
PCI: Setting latency timer of device 0000:00:00.0 to 64
acx: found ACX111-based wireless network card at 0000:00:00.0, irq:0, phymem1:0x4000000, phymem2:0x4022000, mem1:0xa4000000, mem1_size:8192, mem2:0xa4022000, mem2_size:131072
initial debug setting is 0x000A
acx: can't use IRQ 0
pci_set_power_state(): 0000:00:00.0: state=3, current state=5
acx_pci: probe of 0000:00:00.0 failed with error -5}}}

See https://dev.openwrt.org/ticket/1865 and http://wiki.openwrt.org/AR7Port situation.

== Specifications ==

Wireless 4-Port ADSL Router (ADSL 2/2+ Compliant).

CPU: Texas Instruments AR7 MIPS-based @ 150MHz.

Flash chip: 4Mbytes.

SDRAM: 16Mbytes.

Switch: IP175A.

Wireless NIC: TI ACX111.

Boot loader: ADAM2.

Here is a picture:

http://www.continent.com.au/images/products/MODSLG604T.gif

= D-Link G604T flashing =

So let's start. I'll describe the easiest OpenWRT installing method.
You're have a D-Link DSL-G604T device.

First of all you what you need: 

1) Linux machine or shell account;

2) Windows machine for flashing;

3) Simple hex editor like XVI, or shareware WinHex for example;

4) For Windows machines of course and PuTTY ssh-client.

== Linux part ==

'''Compiling OpenWRT firmware'''

Check that you should have ~ 3Gb free space and you should install all dependencies. Best variant is a Gentoo-based machine, if your have Ubuntu, look at DSL-502T page (link is at the end of page).

Goto Linux console and type:

''svn co https://svn.openwrt.org/openwrt/trunk''

My revision was Kamikaze 7659 (bleeding edge, r7631). If your want to specify revision number type:

''svn -r REVISIONNUMBER co https://svn.openwrt.org/openwrt/trunk''

Now go to ''trunk'' directory and type ''make menuconfig''.

In configuration mode we need select those options:

{{{Target System (TI AR7 [2.6])

Target Profile (Texas Instruments WiFi (default)) - usually set's by default. (Still at date 15/06/2007 it isn't work). 

Base system ---> br2684ctl

Libraries ----> linux-atm

Kernel modules ---> Network Devices ---> kmod-sangam-atm-annex-a}}}

Exit from configure menu and save settings.

Then input ''make'' and wait long time (it's depends of your machine's capatibles).

== Windows part ==

'''Adding checksum'''

Now we'll add checksum to firmware. Go to ''trunk/bin'' (or where you have firmware binaries) and type these commands:

{{{wget ftp://ftp.dlink.co.uk/dsl_routers_modems/dsl-g604t/gpl_source_code/DSL-G604T.B01T16_GPL_release.tgz

tar xvzf DSL-G604T.B01T16_GPL_release.tgz

cd LINUX_GPL_SOURCE

tar xvzf TI_chksum-0.1.orig.tar.gz

cd TI-chksum-0.1

make

mv tichksum ../..

cd ../..

rm -rf LINUX_GPL_SOURCE && rm DSL-G604T.B01T16_GPL_release.tgz

./tichksum openwrt-ar7-2.6-squashfs.bin}}}

'''Calculating new memory mappings'''

Now, it's time to move your ''openwrt-ar7-2.6-squashfs.bin'' to Windows machine.

Now open this firmware file with hex editor. And find ascii string ''hsqs''. Now looks at it's offset. For example my was ''CA00F'', but in your binary it's be different value. So we give it to right look ''0x000CA00F''.

Next, i'm not an arifmethic geek, and i don't understand work with memory good. If you're interesting - look at DSL-502T page, it's have not to bad calculation how-to in it. So i made simple alghoritm for DSL-G604T, and you don't need worry, only carefully do what i wrote below. Now we need Windows Calculator or your great brain. Start the calculator, and set it to 4 byte hex mode.

Now how-to calculate:

''mtd0,'' '''(Summ 0x90010000 + YOUROFFSET (You remember, in my case it was 0x000CA00F), and don't forget reject 0xNUMBEROFNULLS, i kept them for do not forget at final result)''',''0x903f0000

mtd1,0x90010000,'' '''--||--''' ''

mtd4,0x90010000,0x903f0000''

That's all, and my final result see like that (''DON'T FORGET TO CALCULATE, DON'T SILLY COPY&PAST THIS''):

{{{mtd0,0x900DA00F,0x903f0000
mtd1,0x90010000,0x900DA00F
mtd4,0x90010000,0x903f0000}}}

'''Flashing'''

Now do Start -> Run -> cmd and goto directory with ''openwrt-ar7-2.6-squashfs.bin'', and type ''ftp 192.168.1.1'', but DON'T PRESS ENTER KEY. Set settings of your modem connection with IP ''192.168.1.5'', DNS mask with ''255.255.255.0'', remove previous gateway and DNS settings. Then turn off your modem and wait about 10 seconds, then power on it, and look at connection icon at tray, it will look as disconnected, and as soon as it's look as connected computer, immideantly press enter key, maybe you will need some practise with it, so try turn off and ftp to modem before you're don't see ADAM2 FTP welcome.

Now it's time to enter results of your calculation, but in little other format, so it's mine (''OF COURSE USE YOUR OWN VALUES, AND NEVER SET ANY OTHERS BUT mtd0, mtd1 and mtd4''):

{{{quote "SETENV mtd0,0x900DA00F,0x903f0000"
quote "SETENV mtd1,0x90010000,0x900DA00F"
quote "SETENV mtd4,0x90010000,0x903f0000"}}}

That's set new memory mappings. Next you need finally flash the device, look that not FLASH at first string, but FLSH, it's quite normally, and DON'T WRITE ANYTHING OTHER BUT mtd4:

{{{quote "MEDIA FLSH"
binary
debug
hash
put "openwrt-ar7-2.6-squashfs.bin" "openwrt-ar7-2.6-squashfs.bin mtd4"
quote REBOOT
quit}}}

Now router will reboot. It's be a first boot. Stay it for 1-2 minutes, then power off and power on it. Now it's second boot: wait about minute, look when the Status led will light, then wait when it's light off, and you'll can set router's connection settings to DHCP. Remember that you can retrieve address at any new boot only after led light&off, so don't panic, if all ok you retrieve an address such as 192.168.1.XX.

My congratulations, you finally flashed it :-)

= Configuring OpenWRT =

'''Where is web-interface?'''

There isn't such :-) There is webif^2 admin interface, but still there isn't it's support in Kamikaze, only in White Russian, so wait. While you can see http://www.bitsum.com/xwrt/ screenshots, and think how it's power. I think so, but now there isn't better solution, so only good solution is use console and your hands, i'll help you, you can see some information below.

But there is http daemon, so you may store any content in ''/www'' folder, or turn off daemon start, look at section "Turning off non-using daemons".

'''Setting up ADSL'''

Go Start -> Run -> cmd and input ''telnet 192.168.1.1'', you'll see OpenWRT logo and shell welcome, input ''passwd'' and set root's password, after this and one reboot telnet will not avaliable anymore. After this connect with PuTTY to 192.168.1.1 and you'll be in the system.

You need to convict of ADSL work. Simply input ''dmesg | grep DSL'' or try ''dmesg'' and look at end of print. If it's work, you'll see ''DSL in Sync'' phrase.

We need setup nas0 interface, for this type:

{{{
br2684ctl -b -c 0 -a VPI.VCI
}}}, where VPI and VCI are real numeric values from your ISP.

Now type ''vi /etc/config/network'' and add these lines to this config:

{{{
config interface wan
option ifname nas0
option proto pppoe
option username "YOUR LOGIN, FOR EXAMPLE ppp******@isp"
option password "YOUR PASSWORD"
}}}

Finally type ''ifup wan'' and connection should establish. You may sucnessnes of this through ''logread''. Now you may ping your ISP or other names at the Internet. Don't forget to manually set ISP DNS'es at computer's connection.

'''Turning off the DHCP'''

DHCP have usually critics from different people, so i don't like it too. Turn off the DHCP is very simple procedure, just input ''vi /etc/config/dhcp'' and comment all strings. Then of course go to computer's connection settings and manually set adress like 192.168.1.2 (for example), mask 255.255.255.0 and gateway 192.168.1.1. And finally reboot the router.

'''Setting time'''

To set current time and date you need firstly set timezone. As for it, look here for a table with timezones. http://wiki.openwrt.org/OpenWrtDocs/Configuration

The command will:

{{{
echo "YOURZONE" > /etc/TZ
}}}

For example:

{{{
echo "MSK-3MSD,M3.5.0/2,M10.5.0/3" > /etc/TZ
}}}

The D-Link DSL-G604T haven't real-time clock hardware onboard, and must get the date and time at boot or use the default of 2000-01-01. So only way is use NTP-client such as ''rdate''.

Edit the crontab file by typing:

{{{
crontab -e
}}}

Then add this lines to the file:

{{{
@reboot /usr/sbin/rdate -s HOST
30 6 * * * /usr/sbin/rdate -s HOST
}}}

insted of HOST you may use any public NTP host, for example ''pool.ntp.org''.

'''Turning off non-using daemons'''

Goto ''/etc/init.d/'', and create backup directory with name you wish, for example ''hlam'', then move non-using scripts in here, for example i moved, ''br2684ctl'', ''telnet'', ''usb''.

'''Configuring firewall'''

OpenWRT uses iptables firewall, so it's very simple, play with rules - it's simplest then in default D-Link DSL-G604T web-interface, and firewall more more stable. All that you need it's to do ''vi /etc/firewall.user'' and look at commented examples. But for best understanding here are mine:

1) Closing all ports for internet except these, for those we'll create rules:

{{{iptables -t nat -A prerouting_wan -p tcp -j DROP
iptables        -A input_wan      -p tcp -j DROP}}}

2) SSH on port 22000 and open from outside. Let's start:

Goto ''vi /etc/config/dropbear'' and change line ''option Port         '22' '' to ''option Port         '22000' '', then save and restart router. Then go ''vi /etc/firewall.user'' and add such lines:

{{{iptables -t nat -A prerouting_wan -p tcp --dport 22000 -j ACCEPT
iptables        -A input_wan      -p tcp --dport 22000 -j ACCEPT
}}}

Type ''/etc/init.d/firewall restart''. That's all, now you can connect through ssh from outside.

3) Web server at port 8000 (it's for example, because my ISP blocks 80 port):

Goto ''vi /etc/init.d/httpd'' and change ''[ -d /www ] && httpd -p 80 -h /www -r ${hostname:-OpenWRT}'' to ''[ -d /www ] && httpd -p 8000 -h /www -r ${hostname:-OpenWRT}'', then ''/etc/init.d/httpd restart''.

Do firewall config with analogue of previous example, but with new port value, 8000, and save. Again do ''/etc/init.d/firewall restart''. That's all.

= Other =

'''Materials'''

List of installing procedure for other devices:

http://wiki.openwrt.org/CategoryAR7Device

Power guide of DSL-502T flashing:

http://wiki.openwrt.org/OpenWrtDocs/Hardware/D-Link/DSL-502T

Fail of flashing the DSL-624T :-(

http://wiki.openwrt.org/OpenWrtDocs/Hardware/D-Link/DSL-G624T
