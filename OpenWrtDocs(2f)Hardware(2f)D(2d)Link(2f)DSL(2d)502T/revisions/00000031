= Work in Progress =
Porting OpenWrt to the DSL-502T is a work in progress. This page is to assist those working in that direction.

Thanks Strider for starting the page off & thank you nbd + all the openwrt guys for making this work - Z3r0 (not the guy called z3r0 on IRC don't pester him!)

Kamikaze builds 5174 and 5495 work on the DSL-502T AU & AT

This is a bit of a mess maybe someone can edit this properly and give it some nice formatting thanks! :)

== Specifications ==
ADSL modem with ADSL2 support to 8Mbit/s+, it has port 1 LAN port

Flash chip: 4MBytes - Samsung K8D3216UBC a 32Mbit NOR-type Flash Memory organized as 4M x 8

SDRAM: 16Mbytes - Nanya NT5SV8M16DS-6K

CPU: TNETD7300GDU Texas Instruments AR7 MIPS based ''' '''

== How to get OpenWRT onto the router: ==
'''Getting and compiling the firmware'''

I do not advise proceeding forward unless you have a JTAG cable or are willing to pay for one (around 20 USD from ebay).

Although the risk of 'bricking' the router is low (as long as you follow the instructions to the letter and do not overwrite the bootloader or modem configuration file), as long as the bootloader and config file are intact the modem can always be recovered.

You will need to compile your own firmware, it's simple enough, if you have ubuntu grab build essentials using synaptic and also grab flex, bison and subversion Download the latest trunk using

svn co https://svn.openwrt.org/openwrt/trunk

or get the same revision as myself and use

svn -r 5495 co https://svn.openwrt.org/openwrt/trunk

Enter into the folder and run make menuconfig, select processor as TI AR7 [2.4], quit and save the config.

Run make to download and compile the firmware

'''Setting up the memory layout'''

To flash your new firmware you must first understand how the memory is divided into blocks, with the default DLink firmware it is this:
||||||||<style="text-align: center;">'''Default DLink Firmware V2 map''' ||
||Name ||Start ||End ||Description ||
||mtd0 ||0x90091000 ||0x903f0000 ||Filesystem ||
||mtd1 ||0x90010090 ||0x90090000 ||Kernel ||
||mtd2 ||0x90000000 ||0x90010000 ||Bootloader ||
||mtd3 ||0x9003f0000 ||0x90040000 ||Configuration ||
||mtd4 ||0x90010090 ||0x903f0000 ||fs+kernel ||


The default firmware flashes to mtd4 It is divided like so (hex):
||||<style="text-align: center;">'''Default firmware map (hex)''' ||
||0-90 ||Header used by the web interface to verify firmware compatibility ||
||90-80FFF ||Kernel with padded 0s at the end ||
||81000-20EFFF ||Filesystem with padded 0s at the end ||
||20F000-20F007 ||Checksum made with TICHKSUM (8 bytes=16 hex chars) ||


But we are flashing OpenWRT to our router and the Openwrt-ar7-2.4-squashfs.bin is set up like this:
||||<style="text-align: center;">'''OpenWRT firmware mapping''' ||
||0 - x ||Kernel ||
||x - eof ||SquashFS ||


Basically OpenWRT doesn't waste space and where the kernel ends the filesystem starts.This means you need to change your mtd3 configuration variables so that the mappings are correct and the filesystem can be found by OpenWRT.

Just grab ghex2 (linux) or xvi (windows), open up the firmware and search for the hsq or hsqs this is the start of the squashfs.

In my case this position was 0x000750E0

so my memory should be mapped like this:
||||||||<style="text-align: center;">'''Custom memory map for OpenWRT''' ||
||Name ||Start ||End ||Description ||
||mtd0 ||0x900850E0 ||0x903f0000 ||Filesystem ||
||mtd1 ||0x90010000 ||0x900850E0 ||Kernel ||
||mtd2 ||0x90000000 ||0x90010000 ||bootloader ||
||mtd3 ||0x903f0000 ||0x90400000 ||config ||
||mtd4 ||0x90010000 ||0x903f00000 ||Kernel + FS ||


Now we adjust our mtd variables by setting our IP to 10.8.8.1 and telnetting to 10.8.8.8 21 we do

user adam2

pass adam2

quote "SETENV mtd0,0x900850E0,0x9003f0000" (fs)

quote "SETENV mtd1,0x90010000,0x900850E0" (kernel)

quote "SETENV mtd4,0x90010000,0x9003f0000" (fs+kernel)

DO NOT CHANGE mtd2 or mtd3 as this will brick your router and you will required JTAG cable to fix it.

I haven't needed to use a checksum myself but some routers may have a version of adam2 that requires each file to have one, otherwise it just rejects the file.

'''Adding a checksum'''

TICHKSUM can be found in the GPL source code for the original firmware available on D-Links website, it may already be compiled as a mipsel binary or may be available as seperate source code.

'''Flashing the new firmware'''

Now you are ready to flash ftp into adam2

quote "MEDIA FLSH"

binary

debug

hash

put "openwrt-ar7-2.4-squashfs.bin" "c mtd4"  (c can be anything)

quote REBOOT

quit

'''Getting the LAN connection to work'''

In adam2 you may need to do quote "SETENV MAC_PORT,0" or "SETENV MAC_PORT,1" (note uppercase and it's not MAC_PORTS), This option selects between internal and external PHY.

'''Congratulations you are successful :)'''

now try to get an IP from the router by using dhclient eth0 or just unsetting IP variables in XP

You should be given an IP like 192.168.1.111 (NOT 169.x.x.x this means something is broken)telnet into 192.168.1.1 and you're done :)

== Enabling ADSL... ==
Please refer to this forum post for more info after reading this:http://forum.openwrt.org/viewtopic.php?pid=35563

This is quite lengthy at present, we really need an init script to do this for us...

'''Set up modulation'''

First of all, you need to set the modulation nvram variable, you can find the modulation from your existing modem logs, MMODE usually suffices. using adam2 ftp... quote "SETENV modulation,GDMT" or GLITE or MMODE or T1413

'''Compile modules'''

You need to compile in the firmware for the correct annex for your modem, either A or B. (it should be ticked on the PCB if you have no idea).

If you're using PPPoE you must also compile in br2684ctl and it's dependency linux-atm, if you're using PPPoA you don't use br2684ctl and you don't use the nas0 device either.

'''Check your line is in sync'''

dmesg should tell you "DSL Line in Sync"You can also do cat /proc/tiatm/avsar_modem_stats and if it says "IDLE" that means you've probably set the wrong annex, if it says "INIT" that is good, then it should say "SHOWTIME" when it is ready to work.

You can also do cat /proc/tiatm/avsar_modem_stats this is the best way of working out if you connection is initialised (see the US/DS connection rate values) and if it is up also check ifconfig regularly to see if you have the nas0 and ppp0 device we set up later on.  The rest of this guide assumes you're using PPPoE.  If you're using PPPoA then search on the openwrt wiki for ARM8100 as this AR7 device is known to work with ADSL PPPoA with VC-MUX encapsulation.

'''Load the modules'''

You need to load the modules for ppp, most of these are already loaded.

cd /lib/modules/2.4.32

insmod br2684.o

insmod slhc.o

insmod ppp_generic.o

insmod ppp_async.o

insmod pppox.o #PPPoE

insmod pppoe.o #PPPoE

insmod pppoatm.o #PPPoA

'''Start the bridging interface''' #PPPoE only

Now we run br2684ctl -b -c 0 -a 8.35 to create the nas0 interface (please type br2684ctl --help to see what the options are, you need to know your ADSL VCI/VPI and if you want to do VCMUX or LLC)

You should get: RFC1483/2684 bridge: Interface "nas0" (mtu=1500, payload=bridged) created sucessfully

RFC1483/2684 bridge: Communicating over ATM 0.8.35, encapsulation: LLC

RFC1483/2684 bridge: Interface configured

'''Set up your wan configuration'''

Go to /etc/config and type vi network to edit network configuration and add: (press insert to start editing... press escape and then type :w to save and exit) (if the files are read only just rename the original and copy)

config interface wan

option ifname nas0

option device ppp

option proto pppoe #change to pppoa for PPPoA (PPP over ATM)

#option user " me@isp.com "

#option name " me@isp.com "

#option atm 1

'''Bring up the bridging interface''' #PPPoE only

ifconfig nas0 up # brings up the nas0 interface

'''Create the ppp device'''

mknod /dev/ppp c 99 0 #creates the ppp device

'''Edit the ppp options'''

now we need to edit the /etc/ppp/options file, add these options

lock

defaultroute

noipdefault

noauth

passive

asyncmap 0

usepeerdns #important gets DNS servers from ISP and adds to resolv.conf

#name " me@isp.com "

user " me@isp.com " #REQUIRED FOR PAP/CHAP AUTH TO BE SUCCESSFUL

lcp-echo-interval 4

lcp-echo-failure 20

#plugin rp-pppoe.so #use pppoatm.so for PPPoA  #No longer needed as we have a pppoe/pppoa script called from "ifup wan" instead

mtu 1492 #pppoa should be 1500

mru 1492 #should equal MTU

'''Set up chap/pap authentication '''

edit /etc/ppp/chap-secrets and create a pap-secrets which contains:

" me@isp.com " "*" "passwd" "*"

'''Bring up the ADSL connection'''

just do "ifup wan" and it should come up, edit /lib/network/pppoe.sh or pppoa.sh to change mtu/mru (typing pppd used to bring the connection up, this doesn't work properly anymore)

ppp0      Link encap:Point-to-Point Protocol inet addr:61.69.250.153  P-t-P:210.8.1.19  Mask:255.255.255.255 UP

POINTOPOINT RUNNING NOARP MULTICAST  MTU:1480  Metric:1

RX packets:3 errors:0 dropped:0 overruns:0 frame:0

TX packets:3 errors:0 dropped:0 overruns:0 carrier:0 collisions:0 txqueuelen:3 RX bytes:114 (114.0 B-)  TX bytes:54 (54.0 B-)

if it doesn't come up do ps -ax and if you see loads of pppd then just use kill 512 etc to kill them all... also kill the br2684ctl and start again...

you should now be able to ping your ISPs gateway IP from telnet, but you won't be able to lookup domain names (i.e. ping www.google.com)

'''Set up DNS lookup'''

you need to edit /etc/resolv.conf and add the lines: search wan and add a nameserver (DNS server) before you bring the interface up

'''Set up forwarding'''

if your PC is directly connected via ethernet to the modem you may find that you can't browse any sites yet or ping them you need to enable IPv4 forwarding in your firewall (i.e. ip masquerading in iptables): taken from here:http://www.yolinux.com/TUTORIALS/LinuxTutorialIptablesNetworkGateway.html

If you get any errors you may need to compile in additional NAT kernel modules.

iptables -P INPUT ACCEPT

iptables -P OUTPUT ACCEPT

iptables -P FORWARD ACCEPT

iptables --flush                           - Flush all the rules in filter and nat tables

iptables --table nat --flush

iptables --delete-chain                    - Delete all chains that are not in default filter and nat table

iptables --table nat --delete-chain # Set up IP FORWARDing and Masquerading

iptables --table nat --append POSTROUTING --out-interface ppp0 -j MASQUERADE

iptables --append FORWARD --in-interface eth0 -j ACCEPT         - Assuming one NIC to local LAN

echo 1 > /proc/sys/net/ipv4/ip_forward     - Enables packet forwarding by kernel

please note that this may not be complete and you may require additional rules to protect your router on the wan interface - Note: don't connect to irc.freenode.net from an unfirewalled box on your lan as you might get banned for open proxies.

Actually the best thing to do is to use OpenWRTs existing firewall rules and add the masquerading commands to the end of /etc/firewall.user 

iptables -t nat -A postrouting_rule -o ppp0 -j MASQUERADE 

iptables -A forwarding_rule -i eth0 -j ACCEPT 

This means they will execute at bootup

See www.netfilter.org for full iptables documentation, it should be noted that in recent builds of openwrt do all the setting up and enabling nat/masquerading for you if you use the "ifup wan" command with a correctly configured /etc/config/network file


== How to Debrick and further information: ==
See the forum for how to debrick the DSL-502T[http://forum.openwrt.org/viewtopic.php?id=7742[[BR http://forum.openwrt.org/viewtopic.php?id=7742]

See the forum for instructions on getting the ADSL interface to work: http://forum.openwrt.org/viewtopic.php?pid=35563

You can generally use the methods on DLinks site or just change ur mtd0/1/4 variables back to defaults and upload the dlink firmware.

But if you've accidentally destroyed your mtd2 adam2 bootloader or mtd3 config file you will need a JTAG cable.

'''Instructions for debricking with a JTAG'''

'''How to get hold of a JTAG or make one '''

I grabbed one from ebay but you can make your own with 4/5 resistors, pin schematics are here:

http://wiki.openwrt.org/AR7Port http://wiki.openwrt.org/OpenWrtDocs/Customizing/Hardware/JTAG_Cable

The cable I purchased from Ebay was for the WRT54G, it had a 12 pin header, whereas my router had an already soldered 14 pin header, the WRT54G uses EJTAG 2.0 and the AR7 uses EJTAG 2.6, to make the JTAG cable work I simple connected pin 1 TRST with pin 8 VCC/VIO/VRED via a 100 ohm resistor (I didn't  bother soldering it on) and then placed the 12 pin JTAG on top squashing it into place, bending back the extra 2 pins.

My pins are numbered as so:

1 (TRST) - 14

2 - 13

3 - 12

4 - 11

5 - 10

6 - 9

7 - 8 (VIO/VCCC/VREF)

'''Bios settings'''

My BIOS settings for my printer port were: ECP+EPP, 0x378.

'''Using the Debrick utility to restore the bootloader and config'''

Once you do this you can use HairyDairyMaids debrick utility 4.8 Get it here:http://downloads.openwrt.org/utils/

Under Windows: load giveio.sys by running loaddrv.exe and adding 'giveio.sys' to the end of the line and clicking install+start.

Under Linux (Ubuntu): Get the build essentials package, compile the binary using 'make' from the folder you extracted the files to, then you need to do this to read the parallel port: rmmod lp, modprobe parport, mknod /dev/parport0 c 99 0

You can now do ./wrt54g -probeonly to test if the unit can be detected

Grab Olegs Adam2 bootloader: http://star.oai.pp.ru/jtag/adam2-oleg.zip

rename the adam2 file to CUSTOM.BIN then do:

./wrt54g -flash:custom  /noerase /nobreak /nodma /window:0x90000000 /start:0x90000000 /length:0x10000  /nocwd

Grab mtd3 config http://mcmcc.bat.ru/dlinkt/restore_mtd3_50xT.rar

rename this to CUSTOM.BIN then do:

./wrt54g -flash:custom  /noerase /nobreak /nodma /window:0x903f0000 /start:0x903f0000 /length:0x10000  /nocwd

You may not have to do /noerase /nobreak or /nocwd but /nodma is required

Once this is done, set you lan IP as 10.8.8.1 subnet 255.0.0.0 (on Linux u need to do ifconfig eth0 10.8.8.1 to set your IP) and then reboot the router, ftp into 10.8.8.8 21 using the command prompt FTP (not anything else) and you will see an adam2 prompt (gratz!).

ping 10.8.8.8 to see if adam2 is working

'''Uploading the original firmware'''

To get back to dlinks default firmware grab the singleimage.bin from them, if you want to flash OpenWRT see above!

root@ZPC:~# ftp 10.8.8.8 21

ftp: connect: No route to host

ftp> o

(to) 10.8.8.8 21

Connected to 10.8.8.8.

220 ADAM2 FTP Server ready.

Name (10.8.8.8:z): adam2

331 Password required for adam2.

Password: 230 adam2

logged in.

ftp> quote MEDIA FLSH 200 media set to FLASH

ftp> binary 200 Type set to I.

ftp> hash Hash mark printing on (1024 bytes/hash mark).

ftp> debug Debugging on (debug=1).

ftp> put "fw" "fs mtd4"

local: fw remote: fs mtd4

---> PORT 10,8,8,7,170,251 200 Port command successful.

---> STOR fs mtd4 150 Opening BINARY mode

226 Transfer complete. 1996699 bytes sent in 27.36 secs (71.3 kB/s)

ftp> quote REBOOT

---> REBOOT 221 Goodbye.

But let me guess... you didn't get the firmware to upload? Did you get 550 can not erase or 550 flash erase failed I think I know why!! This is because the configuration file we just uploaded had the old firmware version 1 memory map (or you used a different map for OpenWRT) and we are trying to upload a firmware version 2 which has a different memory mapping. You can solve this by issuing SETENV commands with the correct memory mappings before uploading the firmware

quote "SETENV mtd0,0x90091000,0x903f0000" - filesystem

quote "SETENV mtd1,0x90010090,0x90090000" - kernel

quote "SETENV mtd2,0x90000000,0x90010000" - bootloader (adam2 mostly)

quote "SETENV mtd3,0x903f0000,0x90400000" - configuration

quote "SETENV mtd4,0x90010090,0x903f0000" - this just covers filesystem/kernel

(p.s. the extra , is no mistake, I think it's needed)

'''Congratulations your router is alive:)'''

Ok so, power cycle the router and it should now work... lights should come on after 30 secs or so.
