= Work in Progress =
Porting OpenWrt to the DSL-502T is a work in progress. This page is to assist those working in that direction.

Thanks Strider for starting the page off & thank you nbd + all the openwrt guys for making this work - Z3r0 (not the guy called z3r0 on IRC don't pester him!) + Thanks Mr. Chandler for the formatting.

Kamikaze builds 5174, 5495, 5636, 6193, 6250 work on the DSL-502T AU & AT

6193 & 6250 have a slight bug with passwd not being saved, please read for a fix: [http://forum.openwrt.org/viewtopic.php?pid=41501This http://forum.openwrt.org/viewtopic.php?pid=41501]

This is a bit of a mess maybe someone can edit this properly and give it some nice formatting thanks! :)

== Specifications ==
*ADSL modem with ADSL2/2+ support to 24Mbit/s+, it has port 1 LAN port

Flash chip: 4MBytes - Samsung K8D3216UBC a 32Mbit NOR-type Flash Memory organized as 4M x 8

SDRAM: 16Mbytes - Nanya NT5SV8M16DS-6K

CPU: TNETD7300GDU Texas Instruments AR7 MIPS based

*see Enabling ADSL section for more info''' '''

== How to get OpenWRT onto the router: ==
'''Preamble '''

I do not advise proceeding forward unless you have a JTAG cable, this allows you to recover the firmware in the device in all situations by directly talking to the mips processor and allowing you to upload a new bootloader. They are around $20 USD from Ebay

Generally the risk of 'bricking' the router (i.e. deleting the bootloader and/or config file) is low. As long as instructions are followed.

'''Getting and compiling the firmware'''

You will need to compile your own firmware, it's simple enough, this can be done using Ubuntu Linux 6.10 (Fedora Core 6 also works great) For Ubuntu grab 'build essentials' 'flex' 'bison' 'autoconf' 'zlib1g-dev' 'libncurses5-dev' and 'subversion' Now we can download a copy of the source code from the subversion repository svn co https://svn.openwrt.org/openwrt/trunk

or get the same revision as myself and use

svn -r 6250 co https://svn.openwrt.org/openwrt/trunk

Enter into the folder and run make menuconfig, select processor as TI AR7 [2.4], quit and save the config.

Run make to download essential packages (approx 100MB) and compile the firmware

'''Setting up the memory layout'''

To flash OpenWRT onto your DSL-502T modem you must first understand how the Flash memory is divided into blocks, with the default D-Link  firmware our memory mappings are:
||||||||<style="text-align: center;">'''Default DLink V2 memory mappings''' ||
||Name ||Start ||End ||Description ||
||mtd0 ||0x90091000 ||0x903f0000 ||Filesystem ||
||mtd1 ||0x90010090 ||0x90090000 ||Kernel ||
||mtd2 ||0x90000000 ||0x90010000 ||Bootloader ||
||mtd3 ||0x9003f0000 ||0x90040000 ||Configuration ||
||mtd4 ||0x90010090 ||0x903f0000 ||fs+kernel ||


The default D-Link firmware is flashed to mtd4, this is not a real memory block, it spans kernel/filesystem.

The default D-Link firmware file is organised like this:
||||<style="text-align: center;">'''Default D-Link V2 firmware memory map (hex)''' ||
||0-90 ||Header used by the web interface to verify firmware compatibility ||
||90-80FFF ||Kernel with padded 0s at the end ||
||81000-20EFFF ||Filesystem with padded 0s at the end ||
||20F000-20F007 ||Checksum made with TICHKSUM (8 bytes=16 hex chars) ||


The new OpenWRT firmware is organised like this:
||||<style="text-align: center;">'''OpenWRT firmware mapping''' ||
||0 - x ||Kernel ||
||x - eof ||SquashFS ||


As you can see, the OpenWRT firmware does not have a header or checksum and has no space wasted by having fixed/padded partition lengths.

For OpenWRT to boot we must find out where the kernel and filesystem boundaries are and save these into the routers configuration.

Just grab a hex editor such as ghex2 (linux) or xvi (windows), open up the firmware and search for the hsq or hsqs this represents the start of the squashFS. (i.e. sqsh for big endian or hsqs for little endian processors)

In my case this position was 0x000750E0

So for the modem to boot up into OpenWRT I need to change my mtd0,1 and 4 boundaries:
||||||||<style="text-align: center;">'''Custom memory map for OpenWRT''' ||
||Name ||Start ||End ||Description ||
||mtd0 ||0x900850E0 ||0x903f0000 ||Filesystem ||
||mtd1 ||0x90010000 ||0x900850E0 ||Kernel ||
||mtd2 ||0x90000000 ||0x90010000 ||bootloader ||
||mtd3 ||0x903f0000 ||0x90400000 ||config ||
||mtd4 ||0x90010000 ||0x903f00000 ||Kernel + FS ||


DO NOT CHANGE mtd2 or mtd3, this will brick your router and you will need a JTAG cable to recover it.

Now we adjust our mtd variables by setting our IP to 10.8.8.1 and telnetting to 10.8.8.8 but on port 21 (FTP) not port 23 (Telnet)

We now type the following:

{{{
user adam2
pass adam2
quote "SETENV mtd0,0x900850E0,0x9003f0000" (fs)
quote "SETENV mtd1,0x90010000,0x900850E0" (kernel)
quote "SETENV mtd4,0x90010000,0x9003f0000" (fs+kernel)
}}}
You must use the comma as a separator.

DO NOT CHANGE mtd2 or mtd3 as this will brick your router and you will require JTAG cable to fix it.

'''Adding a checksum'''

I haven't needed to use a checksum myself but some routers may have a version of adam2 that requires each file to have one, otherwise it just rejects the file.

TICHKSUM can be found in the GPL source code for the original firmware available on D-Links website, it may already be compiled as a mipsel binary or may be available as seperate source code.

'''Flashing the new firmware'''

Now you are ready to flash OpenWRT onto your router, ftp into the adam2 bootloader as above:

{{{
quote "MEDIA FLSH" #write to flash memory
binary #binary transfer mode
debug #turn debugging output on
hash #print ##### when transfering
put "openwrt-ar7-2.4-squashfs.bin" "c mtd4"  (c can be anything)
quote REBOOT #tell the router to reboot
quit
}}}
'''Getting the LAN connection to work'''

Generally the router won't work until the second bootup. Leave it for a minute or two on the first bootup as it runs some scripts to set itself up.

If you reboot several times and your modem doesn't work (on some firmware versions a green light comes on when the modem boots up), you may need to enable the correct setting for the ethernet device

In adam2 you may need to do quote "SETENV MAC_PORT,0" or "SETENV MAC_PORT,1" (note uppercase and it's not MAC_PORTS).

This option selects between internal and external PHY.

'''Congratulations you are successful :)'''

Now try to get an IP assigned by DHCP from the router by using dhclient eth0 from xterm in Linux or just unsetting IP variables in XP

You should be given an IP like 192.168.1.111 (NOT 169.x.x.x this means something is broken see above), telnet into 192.168.1.1 and you're should see the OpenWRT logo :)

== Enabling ADSL... ==
Please refer to this forum post for more info after reading this:http://forum.openwrt.org/viewtopic.php?pid=35563

'''Set up modulation'''

Currently as of build 6250 only ADSL1 is supported, ADSL2/2+ with Annex M support may appear soon as the drivers have become available.

If you use this on an adsl2+ connection it *should* fall back to adsl1 and work fine.

Change the modulation via the adam2 prompt: quote "SETENV modulation,GDMT" or T1413/GLITE/MMODEG.DMT is used for up to 8mbit/s ADSL.

T.1413 is an older version of G.DMT.

G.Lite is a lighter version of G.DMT that supports up to 1.5Mbit/s.

MMODE is Multi-Mode and it just chooses the best one to use.

'''Compile modules'''

You need to compile in the firmware for the correct annex for your modem, choose either A or B, do not compile both. If you are unsure of your region, it is usually Annex A (except in Germany), you can open the modem up and look on the PCB if you need to.

If you're using PPPoE you must also compile in br2684ctl and it's dependency linux-atm, if you're using PPPoA you don't use br2684ctl.

'''Check your line is in sync'''

Type dmesg, it should say "DSL Line in Sync" after about 1 minute.

You can also do cat /proc/tiatm/avsar_modem_stats and if it says "IDLE" that means you've probably set the wrong annex, if it says "INIT" that is good as the modem is negotiating a speed with the exchange, then it should say "SHOWTIME" when it is ready to work.

You can also do cat /proc/tiatm/avsar_modem_stats this is the best way of working out if you connection is initialised as it will show US/DS connection rates.

'''Load the modules (PPPoE + PPPoA)'''

You need to load the modules for ppp, most of these are already loaded.

{{{
cd /lib/modules/2.4.32
insmod br2684.o
insmod slhc.o
insmod ppp_generic.o
insmod ppp_async.o
insmod pppox.o #PPPoE only
insmod pppoe.o #PPPoE only
insmod pppoatm.o #PPPoA only
}}}
'''Start the bridging interface (PPPoE only)'''

Now we run br2684ctl -b -c 0 -a 8.35 to create the nas0 interface (please type br2684ctl --help to see what the options are, you need to know your ADSL VCI/VPI and which encapsulation type you want to use, i.e. VCMUX or LLC)

You should get:

{{{
RFC1483/2684 bridge: Interface "nas0" (mtu=1500, payload=bridged) created sucessfully
RFC1483/2684 bridge: Communicating over ATM 0.8.35, encapsulation: LLC
RFC1483/2684 bridge: Interface configured
}}}
'''Choosing between VC-Mux and LLC ''''''(PPPoE + PPPoA)'''

To choose between VC-Mux and LLC when using PPPoE you simply add another command on to the end of your br2684ctl line, like this: br2684ctl -b -c 0 -a 8.35 -e 0 (0 for LLC and 1 for VC-MUX).

For PPPoA, it's a bit more complex, the pppoatm plugin supports both vc-encaps and llc-encaps as a command.  You need to edit the /lib/network/pppoa.sh script as follows:

{{{
plugin pppoatm.so ${vpi:-8}.${vci:-35}
}}}
becomes

{{{
plugin pppoatm.so ${vpi:-8}.${vci:-35} vc-encaps (this is the default, for LLC use llc-encaps)
}}}
This works as of pppd 2.4.3

Generally with PPPoE use LLC and with PPPoA use VC-MUX

PPPoA VC-MUX will be marginally more efficient and depending on your local exchange should be the best choice. But I would experiment with ping times to your first hop.

Use an MTU of 1500 with PPPoA and 1492 with PPPoE, it has been suggested also that using 1462 for PPPoA and 1454 for PPPoE may be even more efficient due to the fact that the packets have to be divided into ATM cells of 53 bytes.

'''Set up your wan configuration (PPPoE + PPPoA)'''

Go to /etc/config and type vi network to edit network configuration and add:

{{{
config interface wan
option ifname nas0
option device ppp
option proto pppoa #or pppoe
option mtu 1500 #1492 for PPPoE
}}}
'''Brief Instructions for using VI'''''' '''

Press insert to start editing

Press escape and then type :w to save and exit

If the files are read only just rename the original and then copy it to make it writable.

'''Bring up the bridging interface (PPPoE only)'''

ifconfig nas0 up # brings up the nas0 interface

'''Create the ppp device ''''''(PPPoE + PPPoA)'''

mknod /dev/ppp c 99 0 #creates the ppp device

'''Edit the ppp options (PPPoE + PPPoA)'''

now we need to edit the /etc/ppp/options file, add these options

{{{
lock
defaultroute
noipdefault
noauth
passive
asyncmap 0
usepeerdns
user " me@isp.com "
lcp-echo-interval 4
lcp-echo-failure 20
}}}
lock - lock the serial device to ensure exclusive access

defaultroute - accept peers idea of it's own (remote) IP address

noipdefault - don't attempt to determine local ip address from hostname, i.e. peer must supply local IP address during IPCP negotiation

asyncmap 0 - no idea really

noauth - does not require other side to authenticate with us (we authenticate with the other side still)

passive - wait for a lcp packet and don't disconnect

usepeerdns - get the dns servers from the isp

user - you need to put the same details as in chap-secrets / pap-secrets

You can set the MTU / MRU here if you wish, it has no affect, also trying to change it in /lib/network/pppoa.sh or pppoe.sh will not work, you can only change it in /etc/config/network

'''Set up chap/pap authentication ''''''(PPPoE + PPPoA)'''

edit /etc/ppp/chap-secrets and create a pap-secrets which contains:

{{{
" me@isp.com " "*" "passwd" "*"
}}}
'''Bring up the ADSL connection ''''''(PPPoE + PPPoA)'''

Just type "ifup wan" and the adsl interface should come up

You should do ifconfig and get something like this:

{{{
ppp0      Link encap:Point-to-Point Protocol
          inet addr:202.164.193.121  P-t-P:203.24.101.23  Mask:255.255.255.255
          UP POINTOPOINT RUNNING NOARP MULTICAST  MTU:1500  Metric:1
          RX packets:783 errors:0 dropped:0 overruns:0 frame:0
          TX packets:1131 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:3
          RX bytes:438223 (427.9 KiB)  TX bytes:163835 (159.9 KiB)
}}}
If it doesn't come up do ps -ax and if you see loads of pppds have spawned then just use kill with their process number to kill them:  i.e. kill 516

you may also need to kill the br2684ctl and start again from that step. (This has since been fixed in a later version of OpenWRT kamikaze).

If you type logread you can see some debug messages and also your ISPs gateway IP/DNS IPs.

Logread for PPPoA VC-MUX:

{{{
Jan  1 01:39:29 (none) daemon.info pppd[2516]: Plugin pppoatm.so loaded.
Jan  1 01:39:29 (none) daemon.notice pppd[2517]: pppd 2.4.3 started by root, uid 0
Jan  1 01:39:29 (none) daemon.debug pppd[2517]: using channel 9
Jan  1 01:39:29 (none) daemon.info pppd[2517]: Using interface ppp0
Jan  1 01:39:29 (none) daemon.notice pppd[2517]: Connect: ppp0 <--> 8.35
Jan  1 01:39:29 (none) daemon.warn pppd[2517]: Warning - secret file /etc/ppp/pap-secrets has world and/or group access
Jan  1 01:39:29 (none) daemon.debug pppd[2517]: sent [LCP ConfReq id=0x1 <magic 0xa0574e2e>]
Jan  1 01:39:30 (none) daemon.debug pppd[2517]: rcvd [LCP ConfReq id=0x99 <auth chap MD5> <magic 0x567ba313>]
Jan  1 01:39:30 (none) daemon.debug pppd[2517]: sent [LCP ConfAck id=0x99 <auth chap MD5> <magic 0x567ba313>]
Jan  1 01:39:32 (none) daemon.debug pppd[2517]: sent [LCP ConfReq id=0x1 <magic 0xa0574e2e>]
Jan  1 01:39:32 (none) daemon.debug pppd[2517]: rcvd [LCP ConfAck id=0x1 <magic 0xa0574e2e>]
Jan  1 01:39:32 (none) daemon.debug pppd[2517]: sent [LCP EchoReq id=0x0 magic=0xa0574e2e]
Jan  1 01:39:32 (none) daemon.debug pppd[2517]: rcvd [CHAP Challenge id=0xa8 <8a57023b6e5901a9a770eb8a58886bd9>, name = "vezf-exhibition"]
Jan  1 01:39:32 (none) daemon.warn pppd[2517]: Warning - secret file /etc/ppp/chap-secrets has world and/or group access
Jan  1 01:39:32 (none) daemon.debug pppd[2517]: sent [CHAP Response id=0xa8 <f3ec9abe98d208064f6dac1fb73e85bc>, name = "removed"]
Jan  1 01:39:32 (none) daemon.debug pppd[2517]: rcvd [LCP EchoRep id=0x0 magic=0x567ba313]
Jan  1 01:39:32 (none) daemon.debug pppd[2517]: rcvd [CHAP Success id=0xa8 ""]
Jan  1 01:39:32 (none) daemon.info pppd[2517]: CHAP authentication succeeded
Jan  1 01:39:32 (none) daemon.notice pppd[2517]: CHAP authentication succeeded
Jan  1 01:39:32 (none) daemon.warn pppd[2517]: kernel does not support PPP filtering
Jan  1 01:39:32 (none) daemon.debug pppd[2517]: sent [IPCP ConfReq id=0x1 <compress VJ 0f 01> <addr 0.0.0.0> <ms-dns1 0.0.0.0> <ms-dns3 0.0.0.0>]
Jan  1 01:39:32 (none) daemon.debug pppd[2517]: rcvd [IPCP ConfReq id=0x1 <addr removed>]
Jan  1 01:39:32 (none) daemon.debug pppd[2517]: sent [IPCP ConfAck id=0x1 <addr removed>]
Jan  1 01:39:32 (none) daemon.debug pppd[2517]: rcvd [IPCP ConfRej id=0x1 <compress VJ 0f 01>]
Jan  1 01:39:32 (none) daemon.debug pppd[2517]: sent [IPCP ConfReq id=0x2 <addr 0.0.0.0> <ms-dns1 0.0.0.0> <ms-dns3 0.0.0.0>]
Jan  1 01:39:32 (none) daemon.debug pppd[2517]: rcvd [IPCP ConfNak id=0x2 <addr removed> <ms-dns1 removed> <ms-dns3 removed>]
Jan  1 01:39:32 (none) daemon.debug pppd[2517]: sent [IPCP ConfReq id=0x3 <addr removed> <ms-dns1 removed> <ms-dns3 removed>]
Jan  1 01:39:32 (none) daemon.debug pppd[2517]: rcvd [IPCP ConfAck id=0x3 <addr removed> <ms-dns1 removed> <ms-dns3 removed>]
Jan  1 01:39:32 (none) daemon.info dnsmasq[346]: reading /tmp/resolv.conf.auto
Jan  1 01:39:32 (none) daemon.info dnsmasq[346]: using nameserver removed
Jan  1 01:39:32 (none) daemon.info dnsmasq[346]: using nameserver removed
Jan  1 01:39:32 (none) daemon.info dnsmasq[346]: using local addresses only for domain lan
Jan  1 01:39:32 (none) daemon.notice pppd[2517]: local  IP address removed
Jan  1 01:39:32 (none) daemon.notice pppd[2517]: remote IP address removed
Jan  1 01:39:32 (none) daemon.notice pppd[2517]: primary   DNS address removed
Jan  1 01:39:32 (none) daemon.notice pppd[2517]: secondary DNS address removed
Jan  1 01:39:32 (none) daemon.debug pppd[2517]: Script /etc/ppp/ip-up started (pid 2573)
Jan  1 01:39:32 (none) daemon.debug pppd[2517]: Script /etc/ppp/ip-up finished (pid 2573), status = 0x1
}}}
Logread for PPPoE LLC:

{{{
Jan  3 21:07:31 (none) daemon.info pppd[5938]: Plugin rp-pppoe.so loaded.
Jan  3 21:07:31 (none) daemon.notice pppd[5939]: pppd 2.4.3 started by root, uid 0
Jan  3 21:07:36 (none) daemon.debug pppd[5939]: PADS: Service-Name: ''
Jan  3 21:07:36 (none) daemon.info pppd[5939]: PPP session is 6715
Jan  3 21:07:36 (none) daemon.debug pppd[5939]: using channel 6
Jan  3 21:07:36 (none) daemon.info pppd[5939]: Using interface ppp0
Jan  3 21:07:36 (none) daemon.notice pppd[5939]: Connect: ppp0 <--> nas0
Jan  3 21:07:36 (none) daemon.warn pppd[5939]: Couldn't increase MTU to 1500
Jan  3 21:07:36 (none) daemon.warn pppd[5939]: Couldn't increase MRU to 1500
Jan  3 21:07:36 (none) daemon.warn pppd[5939]: Warning - secret file /etc/ppp/pap-secrets has world and/or group access
Jan  3 21:07:36 (none) daemon.debug pppd[5939]: sent [LCP ConfReq id=0x1 <mru 1480> <magic 0x978b0f00>]
Jan  3 21:07:36 (none) daemon.debug pppd[5939]: rcvd [LCP ConfReq id=0x3 <mru 1492> <auth chap MD5> <magic 0x2c956ea7>] 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
Jan  3 21:07:36 (none) daemon.debug pppd[5939]: sent [LCP ConfNak id=0x3 <auth pap>]
Jan  3 21:07:36 (none) daemon.debug pppd[5939]: rcvd [LCP ConfAck id=0x1 <mru 1480> <magic 0x978b0f00>] 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
Jan  3 21:07:37 (none) daemon.debug pppd[5939]: rcvd [LCP ConfReq id=0x4 <mru 1492> <auth pap> <magic 0x2c956ea7>] 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
Jan  3 21:07:37 (none) daemon.debug pppd[5939]: sent [LCP ConfAck id=0x4 <mru 1492> <auth pap> <magic 0x2c956ea7>]
Jan  3 21:07:37 (none) daemon.debug pppd[5939]: sent [LCP EchoReq id=0x0 magic=0x978b0f00]
Jan  3 21:07:37 (none) daemon.warn pppd[5939]: Warning - secret file /etc/ppp/pap-secrets has world and/or group access
Jan  3 21:07:37 (none) daemon.debug pppd[5939]: sent [PAP AuthReq id=0x1 user="removed" password=<hidden>]
Jan  3 21:07:37 (none) daemon.debug pppd[5939]: rcvd [LCP EchoRep id=0x0 magic=0x2c956ea7] 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
Jan  3 21:07:37 (none) daemon.debug pppd[5939]: rcvd [LCP ConfReq id=0x1 <auth chap MD5> <magic 0x67575ed0>] 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
Jan  3 21:07:37 (none) daemon.warn pppd[5939]: Couldn't increase MTU to 1500
Jan  3 21:07:37 (none) daemon.warn pppd[5939]: Couldn't increase MRU to 1500
Jan  3 21:07:37 (none) daemon.debug pppd[5939]: sent [LCP ConfReq id=0x2 <mru 1480> <magic 0x91a57f28>]
Jan  3 21:07:37 (none) daemon.debug pppd[5939]: sent [LCP ConfAck id=0x1 <auth chap MD5> <magic 0x67575ed0>]
Jan  3 21:07:37 (none) daemon.debug pppd[5939]: rcvd [LCP ConfNak id=0x2 <mru 1500>] 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
Jan  3 21:07:37 (none) daemon.debug pppd[5939]: sent [LCP ConfReq id=0x3 <magic 0x91a57f28>]
Jan  3 21:07:37 (none) daemon.debug pppd[5939]: rcvd [LCP ConfAck id=0x3 <magic 0x91a57f28>] 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
Jan  3 21:07:37 (none) daemon.warn pppd[5939]: Couldn't increase MRU to 1500
Jan  3 21:07:37 (none) daemon.debug pppd[5939]: sent [LCP EchoReq id=0x0 magic=0x91a57f28]
Jan  3 21:07:37 (none) daemon.debug pppd[5939]: rcvd [CHAP Challenge id=0x1 <6d4b4bee02e6657647f3c9b34a1ba47d>, name ="removed"] 00 00 00 00
Jan  3 21:07:37 (none) daemon.debug pppd[5939]: sent [CHAP Response id=0x1 <d4a403d7272abbc83a45d2c3d3350e02>, name ="removed"]
Jan  3 21:07:37 (none) daemon.debug pppd[5939]: rcvd [LCP EchoRep id=0x0 magic=0x67575ed0] 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
Jan  3 21:07:37 (none) daemon.debug pppd[5939]: rcvd [CHAP Success id=0x1 ""] 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 ...
Jan  3 21:07:37 (none) daemon.info pppd[5939]: CHAP authentication succeeded
Jan  3 21:07:37 (none) daemon.notice pppd[5939]: CHAP authentication succeeded
Jan  3 21:07:37 (none) daemon.notice pppd[5939]: peer from calling number removed authorized
Jan  3 21:07:37 (none) daemon.warn pppd[5939]: kernel does not support PPP filtering
Jan  3 21:07:37 (none) daemon.debug pppd[5939]: sent [IPCP ConfReq id=0x1 <addr 0.0.0.0> <ms-dns1 0.0.0.0> <ms-dns3 0.0.0.0>]
Jan  3 21:07:37 (none) daemon.debug pppd[5939]: rcvd [IPCP ConfReq id=0x1 <addr removed>] 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
Jan  3 21:07:37 (none) daemon.debug pppd[5939]: sent [IPCP ConfAck id=0x1 <addr removed>]
Jan  3 21:07:37 (none) daemon.debug pppd[5939]: rcvd [IPCP ConfNak id=0x1 <addr removed> <ms-dns1 removed> <ms-dns3 removed
>] 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
Jan  3 21:07:37 (none) daemon.debug pppd[5939]: sent [IPCP ConfReq id=0x2 <addr removed> <ms-dns1 removed> <ms-dns3 removed>]
Jan  3 21:07:37 (none) daemon.debug pppd[5939]: rcvd [IPCP ConfAck id=0x2 <addr removed> <ms-dns1 removed> <ms-dns3 removed>] 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
Jan  3 21:07:37 (none) daemon.notice pppd[5939]: local  IP address removed
Jan  3 21:07:37 (none) daemon.notice pppd[5939]: remote IP address removed
Jan  3 21:07:37 (none) daemon.notice pppd[5939]: primary   DNS address removed
Jan  3 21:07:37 (none) daemon.notice pppd[5939]: secondary DNS address removed
Jan  3 21:07:37 (none) daemon.info dnsmasq[326]: reading /tmp/resolv.conf.auto
Jan  3 21:07:37 (none) daemon.info dnsmasq[326]: using nameserver removed
Jan  3 21:07:37 (none) daemon.info dnsmasq[326]: using nameserver removed
Jan  3 21:07:37 (none) daemon.info dnsmasq[326]: using local addresses only for domain lan
Jan  3 21:07:37 (none) daemon.debug pppd[5939]: Script /etc/ppp/ip-up started (pid 5984)
Jan  3 21:07:37 (none) daemon.debug pppd[5939]: Script /etc/ppp/ip-up finished (pid 5984), status = 0x1}}}
You should now be able to ping your ISPs gateway IP from telnet.

'''Set up DNS lookup'''

Normally with the usepeerdns command the DNS is saved in resolv.conf automatically, but you may need to edit /etc/resolv.conf and add the lines: "search wan" and you may want to add a nameserver (DNS server) before you bring the interface up

'''Set up forwarding'''

For general port forwarding just change /etc/firewall.user this executes at each bootup.

This is fixed in later Kamikaze Subversions.

If your PC is directly connected via ethernet to the modem you may find that you can't browse any sites yet or ping them you need to enable IPv4 forwarding and NAT in your firewall (i.e. ip masquerading in iptables): taken from here:http://www.yolinux.com/TUTORIALS/LinuxTutorialIptablesNetworkGateway.html

As a quick test you can try this:

{{{
iptables -P INPUT ACCEPT
iptables -P OUTPUT ACCEPT
iptables -P FORWARD ACCEPT
iptables --flush                           # Flush all the rules in filter and nat tables
iptables --table nat --flush
iptables --delete-chain                    # Delete all chains that are not in default filter and nat table
iptables --table nat --delete-chain        # Set up IP FORWARDing and Masquerading
iptables --table nat --append POSTROUTING --out-interface ppp0 -j MASQUERADE
iptables --append FORWARD --in-interface eth0 -j ACCEPT         # Assuming one NIC to local LAN
echo "1" > /proc/sys/net/ipv4/ip_forward                        # Enables packet forwarding by kernel
}}}
please note that this may not be complete and you may require additional rules to protect your router on the wan interface - Note: don't connect to irc.freenode.net from an unfirewalled box on your lan as you might get banned for open proxies.

Actually the best thing to do is to use OpenWRTs existing firewall rules and add the masquerading commands to the end of /etc/firewall.user

{{{
iptables -t nat -A postrouting_rule -o ppp0 -j MASQUERADE
iptables -A forwarding_rule -i eth0 -j ACCEPT
}}}
This means they will execute at bootup

If you get any errors you may need to compile in additional NAT kernel modules.

See www.netfilter.org for full iptables documentation, it should be noted that in recent builds of openwrt do all the setting up and enabling nat/masquerading for you if you use the "ifup wan" command with a correctly configured /etc/config/network file

'''How to give interfaces fixed IP addresses'''

For port forwarding you need to have fixed IP addresses, just find out the MAC address of the ethernet card via the XP command prompt ipconfig /all or via linux ifconfig.

Then just add the following line to /etc/ethers

xx:xx:xx:xx:xx:xx ip.ip.ip.ip

or

xx:xx:xx:xx:xx:xx hostname

and edit /etc/ethers to:

ip.ip.ip.ip hostname The hostname of your PC can be found the same way as the MAC address.'''
'''

'''Script to bring the ADSL interface up on bootup and also check the interface is up '''

Please see http://forum.openwrt.org/viewtopic.php?id=8342 for more info

Make a file called /etc/crontab/root and put */1 * * * * sh /etc/adsl

This calls a file called /etc/adsl every minute for infinity

Now make a file called /etc/adsl and put

{{{
#!/bin/sh
MODEMSTATUS=$(cat /proc/tiatm/avsar_modem_training &> /dev/null)
ADSLSTATUS=$(ps | grep pppd)
ADSLSTATUSLEN=$(expr "$ADSLSTATUS" : '.*')
if [ "$MODEMSTATUS" = "SHOWTIME" ]; then
if [[ "$ADSLSTATUSLEN" -lt "48" ]]; then #integer comparison specified
ifup wan
fi
fi
}}}
== Troubleshooting ==
Poor performance of the ADSL connection exists between the Netgear WPNT834 Rangemax 240 and D-Link DSL-502T, characterised by poor transfer speeds which may be asynchronous in nature, many retransmits and general packet loss in TCPdump and poor telnet access/webpage access to the DSL-502T, this is caused by poor ethernet performance between the two devices. This is possibly caused by a duplex mismatch or buggy 100FD/HD code on one of the devices.

The only way to solve this at present is to force the DSL-502T ethernet connection to Autonegotiate 10Mbit/s by changing one line of source code: see the last two posts here:

 . http://forum.openwrt.org/viewtopic.php?id=8117
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

{{{
1 (TRST) - 14
2 - 13
3 - 12
4 - 11
5 - 10
6 - 9
7 - 8 (VIO/VCCC/VREF)
}}}
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

{{{
root@ZPC:~# ftp 10.8.8.8 21
ftp: connect: No route to host
ftp> o
(to) 10.8.8.8 21
Connected to 10.8.8.8.
220 ADAM2 FTP Server ready.
Name (10.8.8.8:z): adam2
331 Password required for adam2.
Password: adam2
230 logged in.
ftp> quote MEDIA FLSH
200 media set to FLASH
ftp> binary
200 Type set to I.
ftp> hash
Hash mark printing on (1024 bytes/hash mark).
ftp> debug
Debugging on (debug=1).
ftp> put "fw" "fs mtd4"
local: fw remote: fs mtd4
---> PORT 10,8,8,7,170,251 200 Port command successful.
---> STOR fs mtd4 150 Opening BINARY mode
226 Transfer complete. 1996699 bytes sent in 27.36 secs (71.3 kB/s)
ftp> quote REBOOT
---> REBOOT 221 Goodbye.
}}}
But let me guess... you didn't get the firmware to upload? Did you get 550 can not erase or 550 flash erase failed I think I know why!! This is because the configuration file we just uploaded had the old firmware version 1 memory map (or you used a different map for OpenWRT) and we are trying to upload a firmware version 2 which has a different memory mapping. You can solve this by issuing SETENV commands with the correct memory mappings before uploading the firmware

{{{
quote "SETENV mtd0,0x90091000,0x903f0000" - filesystem
quote "SETENV mtd1,0x90010090,0x90090000" - kernel
quote "SETENV mtd2,0x90000000,0x90010000" - bootloader (adam2 mostly)
quote "SETENV mtd3,0x903f0000,0x90400000" - configuration
quote "SETENV mtd4,0x90010090,0x903f0000" - this just covers filesystem/kernel
}}}
(p.s. the extra , is no mistake, I think it's needed)

'''Congratulations your router is alive:)'''

Ok so, power cycle the router and it should now work... lights should come on after 30 secs or so.

----
 . ["CategoryAR7Device"]
