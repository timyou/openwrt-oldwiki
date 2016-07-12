= D-Link G604T flashing =

So let's start. I'll describe the easiest OpenWRT installing method.
You're have a D-Link DSL-G604T device.

First of all you what you need: 

1) Linux machine or shell account;

2) Windows machine for flashing;

3) Yeah, a modem;

4) Simple hex editor like XVI, or shareware WinHex for example.

== Linux part ==

'''Compiling OpenWRT firmware'''

Check that you should have ~ 3Gb free space and you should install all dependencies. Best variant is a Gentoo-based machine, if your have Ubuntu, look at DSL-502T page (link is at the end of page).

Goto Linux console and type:

''svn co https://svn.openwrt.org/openwrt/trunk''

My revision was Kamikaze 7632. If your want to specify revision number type:

''svn -r REVISIONNUMBER co https://svn.openwrt.org/openwrt/trunk''

Now go to ''trunk'' directory and type ''make menuconfig''.

In configuration mode we need select those options:

{{{Target System (TI AR7 [2.6])

Target Profile (Texas Instruments WiFi (default)) - usually set's by default.

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

''mtd0,'' '''(Summ 0x90010000 + YOUROFFSET (You remember, in my case it was 0x000CA00F), and don't forget reject 0xNUMBEROFNULLS, i kept them for do not forget at final result)''',''0x903f0000"
mtd1,0x90010000,'' '''--||--'''" ''

mtd4,0x90010000,0x903f0000"''

= Other =

'''Materials'''

List of installing procedure for other devices:

http://wiki.openwrt.org/CategoryAR7Device

Power guide of DSL-502T flashing:

http://wiki.openwrt.org/OpenWrtDocs/Hardware/D-Link/DSL-502T
