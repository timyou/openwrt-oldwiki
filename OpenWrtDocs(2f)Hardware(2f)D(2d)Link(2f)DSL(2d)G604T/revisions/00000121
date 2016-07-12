= D-Link DSL-G604T main information =
== Work in Progress ==
Porting OpenWRT to the D-Link DSL-604T is a work in progress. That's means, that you may compile and run only from Kamikaze SVN. Still there isn't support neither in White Russian nor Kamikaze releases, so installation procedure is not so hacking as on ZyXEL's, but more hard than uploading throught web-interface. All run's ok with 2.6.x kernel maybe except wireless, it need some tests.

== Troubles ==
Since .21 kernel, to have Port Forwarding i.e. DNAT you need libipt_DNAT.so for MIPS and put it into /lib/ at router. It may be found here:

{{{
build_mipsel/linux-2.6-ar7/iptables-1.3.7/extensions/libipt_DNAT.so
or
build_mipsel/linux-2.6-ar7/iptables-1.3.7/ipkg-install/usr/lib/iptables/libipt_DNAT.so
}}}
Look https://dev.openwrt.org/ticket/1772 for more information.

There seems that Wi-Fi isn't work at this date (17/06/2007):

{{{
acx: this driver is still EXPERIMENTAL
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

http://www.dlink.ru/base/picz/DSL-G604T_.jpg

= D-Link G604T flashing =
So let's start. I'll describe the easiest OpenWRT installing method. You're have a D-Link DSL-G604T device.

First of all you what you need:

1) Linux machine or shell account;

2) Windows machine for flashing;

3) Simple hex editor like XVI, or shareware WinHex for example;

4) For Windows machines of course and PuTTY ssh-client.

== Linux part ==
'''Compiling OpenWRT firmware'''

Check that you should have ~ 3Gb free space and you should install all dependencies. Best variant is a Gentoo-based machine, if your have Ubuntu, look at [:OpenWrtDocs/Hardware/D-Link/DSL-502T:DSL-502T page].

Goto Linux console and type:

''svn co https://svn.openwrt.org/openwrt/trunk''

My revision was Kamikaze 7671 (bleeding edge, r7631). If your want to specify revision number type:

''svn -r REVISIONNUMBER co https://svn.openwrt.org/openwrt/trunk''

Now go to ''trunk'' directory and type ''make menuconfig''.

In configuration mode we need select those options:

{{{
Target System (TI AR7 [2.6])
Target Profile (Texas Instruments WiFi (default)) - usually set's by default. (Still at date 15/06/2007 it isn't work).
Base system ---> br2684ctl
Libraries ----> linux-atm
Kernel modules ---> Network Devices ---> kmod-sangam-atm-annex-a (Select kmod-sangam-atm-annex-a for DSL-G664T)
                  > Cryptographic API modules ---> kmod-crypto-core (includes kmod-crypto-aes and kmod-crypto-arc4)
                        this is needed until bug #2589 https://dev.openwrt.org/ticket/2589 gets fixed.
Base system ---> busybox Configuration ---> Networking Utilities ---> [ ] httpd (Turn off).}}}
Optional:

{{{
Base system ---> busybox Configuration ---> Archival Utilities ---> unzip - Zip archivator.
Base system ---> busybox Configuration ---> Networking Utilities ---> hostname - Show hostname.}}}
Exit from configure menu and save settings.

Then input ''make'' and wait long time (it's depends on your machine's capabilities).

'''Adding checksum'''Now we'll add a checksum to the firmware. Go to ''trunk/bin'' (or where you have firmware binaries) and type these commands:

{{{
wget ftp://ftp.dlink.co.uk/dsl_routers_modems/dsl-g604t/gpl_source_code/DSL-G604T.B01T16_GPL_release.tgz
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

== Windows part ==
(Will also work on linux with for example ''hexer'' and plain ''ftp!)''

Now open this firmware file with a hex editor. And find the ascii string ''hsqs''. Now looks at it's offset. For example mine was ''CA00F'', but in your binary it'll be a different value. So we give it to right look ''0x000CA00F''.

Next, I'm not an arithmetic geek, and I don't understand how to work well with memory. If you're interested - look at the [:OpenWrtDocs/Hardware/D-Link/DSL-502T:DSL-502T page], it's having a good calculation how-to on it. So, I made simple alghoritm for DSL-G604T, and you don't need worry, only carefully do what i wrote below. Now we need Windows Calculator or your great brain. Start the calculator, and set it to 4 byte hex mode.

Now how-to calculate:

''mtd0,'' '''(Sum 0x90010000 + YOUROFFSET (You remember, in my case it was 0x000CA00F), and don't forget reject 0xNUMBEROFNULLS, i kept them for do not forget at final result)''',''0x903f0000 ''

''mtd1,0x90010000,'' '''(Sum ''''''0x90010000 + YOUROFFSET again)''' '' ''

''mtd4,0x90010000,0x903f0000''

That's all, and my final result looks like this (''DON'T FORGET TO CALCULATE, DON'T  BE SILLY AND JUST COPY&PASTE THIS''):

{{{
mtd0,0x900DA00F,0x903f0000
mtd1,0x90010000,0x900DA00F
mtd4,0x90010000,0x903f0000}}}
'''Flashing'''For the next bit you need to know the IP address of the ADAM2 bootloader. Have a look in  ["OpenWrtDocs/TroubleshootingAR7"] for more info. The address is assumed to be ''192.168.1.1 ''for the next paragraph. '' ''

Now do Start -> Run -> cmd and goto the directory where ''openwrt-ar7-2.6-squashfs.bin is located'', and type ''ftp 192.168.1.1'' (192.168.1.199 for DSL-G664T), but DON'T PRESS ENTER KEY YET. Change the settings of your computers Wired connection to: IP: ''192.168.1.5'' Subnet: ''255.255.255.0'' Empty Gateway & DNS Turn off your modem and wait 10 seconds, then power on it, and look at the connection icon in the tray. As soon as it changes from disconnected to connected '''''IMMEDIATELY''''' press enter, maybe you will need some practice with it! If it doesn't work, see on ["OpenWrtDocs/TroubleshootingAR7"] for more info

Now it's time to enter the results of your calculation, but in little other format. It should look like this (''OF COURSE USE YOUR OWN VALUES, AND NEVER SET ANY OTHERS BUT mtd0, mtd1 and mtd4''):

{{{
quote "SETENV mtd0,0x900DA00F,0x903f0000"
quote "SETENV mtd1,0x90010000,0x900DA00F"
quote "SETENV mtd4,0x90010000,0x903f0000"}}}
That sets new memory mappings. Now you will finally flash the device: (Dont´t mistake FLSH for FLASH)

{{{
quote "MEDIA FLSH"
binary
debug
hash
put "openwrt-ar7-2.6-squashfs.bin" "openwrt-ar7-2.6-squashfs.bin mtd4"
quote REBOOT
quit}}}
Now your router will reboot. Wait 1-2 minutes, then reboot the router. After about a minute, look when the Status led will light, then wait when it's light off, and you can set router's connection settings to DHCP. Remember that you can retrieve address at any new boot only after led light&off, so don't panic, if all ok you retrieve an address such as 192.168.1.XX.

My congratulations, you finally flashed it :)

= Configuring OpenWRT =
'''Where is web-interface?'''

There isn't  one :) There is the [http://x-wrt.org/ webif] admin interface, but that isn't supported in Kamikaze yet.There isn't a better solution yet, so just use the console and your hands. Don´t worry, I'll help you, as you can see below.

'''Setting up ADSL'''

Go Start -> Run -> cmd and input ''telnet 192.168.1.1'', you'll see OpenWRT logo and shell welcome, input ''passwd'' to set the root password, after this and one reboot telnet will not avaliable anymore. After this connect via SSH (with PuTTY) to 192.168.1.1 and you'll be in the system.

You need to convict of ADSL work. Simply input ''dmesg | grep DSL'' or try ''dmesg'' and look at end of print. If it's work, you'll see ''DSL in Sync'' phrase.

We need setup nas0 interface, for this type:

{{{
br2684ctl -b -c 0 -a VPI.VCI
}}}
, where VPI and VCI are real numeric values from your ISP.

Now type ''vi /etc/config/network'' and add these lines to this config:

{{{
config interface wan
option ifname nas0
option proto pppoe
option username "YOUR LOGIN, FOR EXAMPLE ppp******@isp"
option password "YOUR PASSWORD"
}}}
Finally type ''ifup wan'' and connection should establish. You may sucnessnes of this through ''logread''. Now you may ping your ISP or other names at the Internet from router doing ''ping HOST''. Than reboot router, and start br2684ctl and ''ifup wan'' again, because ADSL works from computer after second running. Don't forget to manually set ISP DNS'es at computer's connection.

'''Turning off the DHCP'''

DHCP have usually critics from different people, so i don't like it too. Turn off the DHCP is very simple procedure, just do ''rm /etc/config/dhcp''. Then of course go to your computer's connection settings and manually set your IP-adress like 192.168.1.2, subnet 255.255.255.0, gateway 192.168.1.1 and reboot the router.

'''Changing hostname'''

Input ''vi /etc/config/system'' and change the ''option hostname OpenWRT'' to ''option hostname YOURHOSTNAME''.

'''Setting time'''

To set current date and time you to set your timezone first. Look here for a table with timezones. http://wiki.openwrt.org/OpenWrtDocs/Configuration

The command is:

{{{
echo "YOURZONE" > /etc/TZ
}}}
For example:

{{{
echo "MSK-3MSD,M3.5.0/2,M10.5.0/3" > /etc/TZ
}}}
The D-Link DSL-G604T does´nt have a real-time clock onboard, and has to get the date and time at boot or use the default of 2000-01-01. So the only way is to use an NTP-client like ''rdate''.

type:

{{{
rdate -s HOST
}}}
Instead of HOST you may use any public NTP host, for example ''pool.ntp.org''.

Than add rule to crontab, doing ''crontab -e'':

{{{
0 0 * * * /usr/sbin/rdate -s 128.138.140.44 >/dev/null 2>&1
}}}
You may use any other NTP-server instead of 128.138.140.44. That's will correct time every day at 00:00.

'''Turning off unused daemons'''

Goto ''/etc/init.d/'', and create backup directory with name you wish, for example ''hlam'', then move non-using scripts in here, for example i moved, ''br2684ctl'', ''telnet'', ''usb''.

'''Configuring firewall'''

OpenWRT uses iptables firewall, so it's very simple, play with rules - it's simpler than the original D-Link DSL-G604T web-interface, and the firewall is way more stable. All that you need to do is ''vi /etc/firewall.user'' and look at commented examples. But for better understanding here are mine:

1) Closing all ports for internet except these, for those we'll create rules:

{{{
iptables -t nat -A prerouting_wan -p tcp -j DROP
iptables        -A input_wan      -p tcp -j DROP}}}
WARNING! IT ALWAYS MUST BE AFTER ALL OTHER RULES, I.E. EVERY TIME IT MUST BE AT THE END OF FILE.

2) SSH on port 22000 and open from outside. Let's start:

Goto ''vi /etc/config/dropbear'' and change line ''option Port         '22' '' to ''option Port         '22000' '', then save and restart router. Then go ''vi /etc/firewall.user'' and add such lines:

{{{
iptables -t nat -A prerouting_wan -p tcp --dport 22000 -j ACCEPT
iptables        -A input_wan      -p tcp --dport 22000 -j ACCEPT
}}}
3) Example Torrent and eMule rules:

{{{
# Torrent
iptables -t nat -A prerouting_wan -p tcp --dport 32021 -j DNAT --to 192.168.1.2:32021
iptables        -A forwarding_wan -p tcp --dport 32021 -d 192.168.1.2 -j ACCEPT
# Mule
iptables -t nat -A prerouting_wan -p tcp --dport 25572 -j DNAT --to 192.168.1.2:25572
iptables        -A forwarding_wan -p tcp --dport 25572 -d 192.168.1.2 -j ACCEPT}}}
Type ''/etc/init.d/firewall restart''. That's all, now it should work.

'''Using ipkg'''

ipkg is one of the hearts of OpenWRT. It's a package installing/removing tool. Therefore there are small numbers of avaliable packages in Kamikaze SVN, it's useful. For example we'll remove dnsmasq and wireless-tools:

{{{
ipkg update
ipkg remove dnsmasq
ipkg remove wireless-tools}}}
and install wi-fi driver:

{{{
ipkg install kmod-acx
}}}
Useful commands are ''ipkg update'' for updating the package lists, ipkg , ''ipkg remove <package>'' for removing, ''ipkg install <package>'' for installing, ''ipkg list'' to show avaliable packages list and ''ipkg list_installed'' to show installed packages.

'''Setting up dyndns'''

There are two tools: ''updatedd'' and ''inadyn''. Both are in unofficial package repository. We'll use second, because it don't need scripting. So go http://www.ipkg.be and search for ''inadyn'' there, or get it directly using ''ipkg install http://www.forgotten-realm.net/openwrt/inadyn_1.86_mipsel.ipk''. Then do ''rm /etc/init.d/S65inadyn''. Then do ''vi /etc/inadyn.conf'' and write your values looking as in example.

'''Script to bring up ADSL if it's down, set time and start dyndns updating service'''

Thanks Z3r0 for skeleton and Vladimir Baboshin for advices:

Create new file ''vi /etc/adsl'' and input:

{{{
#!/bin/sh (-)
MODEMSTATUS=$(head -n 1 /proc/avalanche/avsar_modem_training)
ADSLSTATUS=$(ps | grep pppd)
ADSLSTATUSLEN=$(expr "$ADSLSTATUS" : '.*')
DATE=$(date '+%y')
# Set yor VPI and VCI values
if [ "$MODEMSTATUS" = "SHOWTIME" ]; then
br2684ctl -b -c 0 -a VPI.VCI
if [[ "$ADSLSTATUSLEN" -lt "48" ]]; then
ifup wan; sleep 5; /bin/inadyn
fi
fi
if [ "$DATE" = "00" ]; then
# You may use any other NTP server
rdate -s 128.138.140.44
fi
}}}
Make it executable:

{{{
chmod 755 /etc/adsl
}}}
Than execute ''crontab -e'' and add:

{{{
*/1 * * * * sh /etc/adsl  >/dev/null 2>&1
}}}
That will check ADSL every minute.

= Other =
'''Materials'''

List of installing procedure for other devices:

http://wiki.openwrt.org/CategoryAR7Device

Power guide of DSL-502T flashing:

http://wiki.openwrt.org/OpenWrtDocs/Hardware/D-Link/DSL-502T

Fail of flashing the DSL-624T :(

http://wiki.openwrt.org/OpenWrtDocs/Hardware/D-Link/DSL-G624T

For those who want to configure router with official firmware right

http://www.seattlewireless.net/DlinkDslG604tConfiguration
