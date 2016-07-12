= Work in Progress =
Porting OpenWrt to the DSL-502T is a work in progress.

This page is to assist those working in that direction.

Thanks Strider for starting the page off for me.

Thank you nbd and all the OpenWRT developers for making this work-Z3r0 (not the z3r0 on IRC)

Thank you Mr Chandler for fixing some of the formatting.

== Specifications ==
ADSL modem with ADSL2/2+ support to 24Mbit/s+, it has port 1 LAN port

Flash chip: 4MBytes - Samsung K8D3216UBC a 32Mbit NOR-type Flash Memory organized as 4M x 8

SDRAM: 16Mbytes - Nanya NT5SV8M16DS-6K

CPU: TNETD7300GDU Texas Instruments AR7 MIPS based

== How to get OpenWRT onto the router: ==
'''Preamble/Disclaimer'''

I do not advise proceeding forward unless you have a JTAG cable, this allows you to recover the firmware in the device in all situations by directly talking to the mips processor and allowing you to upload a new bootloader.

They are around $20 USD from eBay.

Generally the risk of 'bricking' the router (i.e. deleting the bootloader and/or config file thereby requiring a JTAG cable) is low. As long as instructions are followed.

'''Get the source code'''

The sourcecode is held in a subversion repository and is updated daily, install the subversion package (using the synaptic package manager on ubuntu).

To get the code you type this at the command prompt:

svn co https://svn.openwrt.org/openwrt/trunk

To get a specific revision you type this:

svn -r 6250 co https://svn.openwrt.org/openwrt/trunk

If you are updating or rolling back only the changeset is downloaded

'''Download source code for optional extra packages'''

Browse here and see if there's anything you want (you can usually skip this):

https://dev.openwrt.org/browser/packages

For example enter your local trunk/package folder and type:

svn co https://svn.openwrt.org/openwrt/packages/net/miau miau is an IRC bouncer

svn co https://svn.openwrt.org/openwrt/packages/net/ez-ipupdate ez-ipupdate is a dyndns updater

''' Install prerequisites for compiling'''

For Ubuntu grab 'build essentials' 'flex' 'bison' 'autoconf' 'zlib1g-dev' 'libncurses5-dev', 'automake', 
i.e
{{{
apt-get install flex bison autoconf zlib1g-dev libncurses5-dev automake
}}}

'''Select firmware components'''

Enter into the folder and run make menuconfig, select processor as TI AR7 [2.4]

You also need to select your ADSL1 Annex, it's either Annex A or B (Germany only).

If you're using PPPoE you must also compile in br2684ctl and it's dependency linux-atm, if you're using PPPoA you don't use br2684ctl.

Quit and save the config.

Run 'make' to download essential packages (approximately 100MByte) and compile the firmware.

'''Understanding the firmware & memory layout of the DSL-502T'''

This is very important, please try to understand what is going on here.

The Flash memory is divided into blocks, with the D-Link 2.00B07 firmware our memory mappings are:
||||||||<style="text-align: center;">'''Default DLink v2 memory mappings''' ||
||Name ||Start ||End ||Description ||
||mtd0 ||0x90091000 ||0x903f0000 ||Filesystem ||
||mtd1 ||0x90010090 ||0x90091000 ||Kernel ||
||mtd2 ||0x90000000 ||0x90010000 ||Bootloader ||
||mtd3 ||0x9003f0000 ||0x90040000 ||Configuration ||
||mtd4 ||0x90010090 ||0x903f0000 ||fs+kernel ||


The D-Link firmware v2 is flashed to mtd4, this is not a real memory block, it is a virtual block spanning the kernel & filesystem.

The D-Link firmware v2 file is organised like this:
||||<style="text-align: center;">'''Default D-Link V2 firmware memory map (hex)''' ||
||0-90 ||Header used by the web interface to verify firmware compatibility ||
||90-80FFF ||Kernel with padded 0s at the end ||
||81000-20EFFF ||Filesystem with padded 0s at the end ||
||20F000-20F007 ||Checksum made with TICHKSUM (8 bytes=16 hex chars) ||


The new OpenWRT firmware is much better at space saving:
||||<style="text-align: center;">'''OpenWRT firmware mapping''' ||
||0 - x ||Kernel ||
||x - eof ||SquashFS ||


Consequently our filesystem/kernel boundaries will be different to those of the D-Link firmware: For OpenWRT to boot we must find out where the new firmwares kernel and filesystem boundaries are and save these into the routers configuration.

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


'''Adjust the memory mappings on the router'''

The DSL-502T has an adam2 bootloader that is available between 0 - 5 seconds at bootup. This is where you can change the mtd variables.

Now we adjust our mtd variables by setting our IP to 10.8.8.1 (subnet 255.255.255.0) and telnetting to 10.8.8.8 but on port 21 (FTP)

We now type the following:

{{{
USER adam2
PASS adam2
quote "SETENV mtd0,0x900850E0,0x9003f0000" (fs)
quote "SETENV mtd1,0x90010000,0x900850E0" (kernel)
quote "SETENV mtd4,0x90010000,0x9003f0000" (fs+kernel)
}}}
You must use the comma as a separator.

DO NOT CHANGE mtd2 or mtd3, this will brick your router and you will need a JTAG cable to recover it.

'''Adding a checksum (not necessary)'''

Some DSL-502T routers may have a version of adam2 that requires each file to have a checksum, otherwise the file is rejected.

TICHKSUM can be found in the GPL source code for the original firmware available on D-Links website, it may already be compiled as a mipsel binary or may be available as separate source code.

'''Flashing the new firmware'''

Now you are ready to flash OpenWRT onto your router, FTP into the adam2 bootloader as above:

{{{
quote "MEDIA FLSH"
binary
debug
hash
put "openwrt-ar7-2.4-squashfs.bin" "c mtd4"
quote REBOOT
quit
}}}
Here we switch to flash memory, we enable binary transfer mode, we turn on debugging, we print hashes during file transfer and we upload our file (c can be anything).

'''Booting up for the first time'''

Generally the router won't work until the second bootup. Leave it for a minute or two on the first bootup as it runs some scripts to set itself up.

Remember to unset your ip settings under windows, also under linux type dhclient eth0 to get a dhcp assigned IP address.

'''Enable the internal or external PHY'''

Ignore the LEDs, they don't come on anyway.

If you reboot several times and you can't get an IP it could be that you need to tell the modem which PHY it needs to use:

In adam2 you may need to do quote "SETENV MAC_PORT,0" or "SETENV MAC_PORT,1" (note uppercase and it's not MAC_PORTS).

This option selects between internal and external PHY.

'''Congratulations you are successful :)'''

If you can get an IP, well done!

You should be given an IP like 192.168.1.111 (NOT 169.x.x.x this means something is broken), telnet into 192.168.1.1 and you're should see the OpenWRT logo :) ''' '''

'''Password protect the router'''

Get a copy of putty from the internet! (Duh with your spare modem!)

type passwd to set a password and this will enable dropbear the SSH server.

You now need to log back in using putty.

== Enabling ADSL ==
'''Set up modulation'''

Currently we only have ADSL1 options: G.DMT, G.lite T.1413 and Multi-Mode.

If you use this on an adsl2+ connection it *should* fall back to adsl1 and work fine.

The modulation can be changed via the adam2 prompt: quote "SETENV modulation,GDMT" or T1413/GLITE/MMODE

G.DMT supports up to 8mbit/s.

T.1413 is an older version of G.DMT.

G.Lite is a lighter version of G.DMT that supports up to 1.5Mbit/s.

MMODE is Multi-Mode and negotiates the best mode that it can.

'''Check your line is in sync'''

Type dmesg, it should say "Initializing DSL interface" and then about 1 minute later "DSL Line in Sync".

You can also do cat /proc/tiatm/avsar_modem_training and if it says "IDLE" that means you've probably set the wrong annex, if it says "INIT" that is good as the modem is negotiating a speed with the exchange, then it should say "SHOWTIME" when it is ready to work.

You can also do cat /proc/tiatm/avsar_modem_stats this is the best way of working out if you connection is initialised as it will show Upstream/Downstream sync speeds.

'''Connect to your ISP directly using DHCP (Most people will be using PPPoE or PPPoA please ignore this)'''

Please read this thread: http://forum.openwrt.org/viewtopic.php?id=8019

'''Load the modules (PPPoE + PPPoA) (Not necessary anymore)'''

{{{
cd /lib/modules/2.4.34
insmod br2684.o
insmod slhc.o
insmod ppp_generic.o
insmod ppp_async.o
insmod pppox.o
insmod pppoe.o
insmod pppoatm.o
}}}
pppox.o and pppoe.o are required for PPPoE.

pppoatm.o is required for PPPoA.''' '''

'''Start the bridging interface (PPPoE only)'''

The bridging interface is needed for PPPoE over ATM.

We run br2684ctl -b -c 0 -a 8.35 to create the nas0 interface.

Please type br2684ctl --help for more information.

You need to know your VPI/VCI settings.

You should get:

{{{
RFC1483/2684 bridge: Interface "nas0" (mtu=1500, payload=bridged) created sucessfully
RFC1483/2684 bridge: Communicating over ATM 0.8.35, encapsulation: LLC
RFC1483/2684 bridge: Interface configured
}}}
'''Choosing between VC-MUX or LLC'''

Generally with PPPoE use LLC and with PPPoA use VC-MUX

PPPoA VC-MUX will be marginally more efficient than PPPoE LLC and depending on your local exchange should be the best choice.

I would experiment with ping times to your first hop.

'''Setting up VC-Mux or LLC ''''''(PPPoE + PPPoA)'''

To choose between VC-Mux and LLC when using PPPoE use -e 0 (0 for LLC and 1 for VC-MUX) in the command line above.

For PPPoA, it's a bit more complex, the pppoatm plugin supports both vc-encaps and llc-encaps as a command.

You need to edit the /lib/network/pppoa.sh script as follows:

{{{
plugin pppoatm.so ${vpi:-8}.${vci:-35}
}}}
becomes

{{{
plugin pppoatm.so ${vpi:-8}.${vci:-35} vc-encaps (this is the default, for LLC use llc-encaps)
}}}
This works as of pppd 2.4.3

'''Set up your wan configuration (PPPoE + PPPoA)'''

Go to /etc/config and type vi network to edit network configuration and add:

{{{
config interface wan
option ifname nas0
option device ppp
option proto pppoa
option mtu 1500
}}}
proto pppoe & mtu 1492 for pppoe''' '''

'''MTU'''

Use an MTU of 1500 with PPPoA and 1492 with PPPoE, it has been suggested also that using 1462 for PPPoA and 1454 for PPPoE may be even more efficient due to the fact that the packets have to be divided into ATM cells of 53 bytes and they fit into these cells better with these values.

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
          inet addr:removed  P-t-P:removed  Mask:255.255.255.255
          UP POINTOPOINT RUNNING NOARP MULTICAST  MTU:1500  Metric:1
          RX packets:783 errors:0 dropped:0 overruns:0 frame:0
          TX packets:1131 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:3
          RX bytes:438223 (427.9 KiB)  TX bytes:163835 (159.9 KiB)
}}}
If you type logread you can see some debug messages and also your ISPs gateway IP/DNS IPs.Logread for PPPoA VC-MUX:

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
Jan  1 04:49:43 (none) daemon.info pppd[3661]: Plugin rp-pppoe.so loaded.
Jan  1 04:49:43 (none) daemon.notice pppd[3662]: pppd 2.4.3 started by root, uid 0
Jan  1 04:49:43 (none) daemon.err pppd[3662]: Interface nas0 has MTU of 1492 -- should be 1500.  You may have serious connection problems.
Jan  1 04:49:48 (none) daemon.debug pppd[3662]: using channel 4
Jan  1 04:49:48 (none) daemon.info pppd[3662]: Using interface ppp0
Jan  1 04:49:48 (none) daemon.notice pppd[3662]: Connect: ppp0 <--> nas0
Jan  1 04:49:48 (none) daemon.warn pppd[3662]: Couldn't increase MTU to 1500
Jan  1 04:49:48 (none) daemon.warn pppd[3662]: Couldn't increase MRU to 1500
Jan  1 04:49:48 (none) daemon.warn pppd[3662]: Warning - secret file /etc/ppp/pap-secrets has world and/or group access
Jan  1 04:49:48 (none) daemon.debug pppd[3662]: sent [LCP ConfReq id=0x1 <mru 1492> <magic 0xa6a20873>]
Jan  1 04:49:48 (none) daemon.debug pppd[3662]: rcvd [LCP ConfReq id=0xd4 <mru 1492> <auth chap MD5> <magic 0x3e5a2aa2>] 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
Jan  1 04:49:48 (none) daemon.debug pppd[3662]: sent [LCP ConfAck id=0xd4 <mru 1492> <auth chap MD5> <magic 0x3e5a2aa2>]
Jan  1 04:49:48 (none) daemon.debug pppd[3662]: rcvd [LCP ConfAck id=0x1 <mru 1492> <magic 0xa6a20873>] 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
Jan  1 04:49:48 (none) daemon.debug pppd[3662]: sent [LCP EchoReq id=0x0 magic=0xa6a20873]
Jan  1 04:49:48 (none) daemon.debug pppd[3662]: rcvd [CHAP Challenge id=0xa7 <a6bb53398127066ca299dafe47965b7b>, name = "vezf-exhibition"] 00 00
Jan  1 04:49:48 (none) daemon.warn pppd[3662]: Warning - secret file /etc/ppp/chap-secrets has world and/or group access
Jan  1 04:49:48 (none) daemon.debug pppd[3662]: sent [CHAP Response id=0xa7 <07f021b9f5ab5bb1922609306fdde48b>, name = "removed"]
Jan  1 04:49:48 (none) daemon.debug pppd[3662]: rcvd [LCP EchoRep id=0x0 magic=0x3e5a2aa2] 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
Jan  1 04:49:49 (none) daemon.debug pppd[3662]: rcvd [LCP ConfReq id=0x1 <auth chap MD5> <magic 0x797b3439>] 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
Jan  1 04:49:49 (none) daemon.warn pppd[3662]: Couldn't increase MTU to 1500
Jan  1 04:49:49 (none) daemon.warn pppd[3662]: Couldn't increase MRU to 1500
Jan  1 04:49:49 (none) daemon.warn pppd[3662]: Warning - secret file /etc/ppp/pap-secrets has world and/or group access
Jan  1 04:49:49 (none) daemon.debug pppd[3662]: sent [LCP ConfReq id=0x2 <mru 1492> <magic 0x528f071f>]
Jan  1 04:49:49 (none) daemon.debug pppd[3662]: sent [LCP ConfAck id=0x1 <auth chap MD5> <magic 0x797b3439>]
Jan  1 04:49:49 (none) daemon.debug pppd[3662]: rcvd [LCP ConfNak id=0x2 <mru 1500>] 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
Jan  1 04:49:49 (none) daemon.debug pppd[3662]: sent [LCP ConfReq id=0x3 <magic 0x528f071f>]
Jan  1 04:49:49 (none) daemon.debug pppd[3662]: rcvd [LCP ConfAck id=0x3 <magic 0x528f071f>] 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
Jan  1 04:49:49 (none) daemon.warn pppd[3662]: Couldn't increase MRU to 1500
Jan  1 04:49:49 (none) daemon.debug pppd[3662]: sent [LCP EchoReq id=0x0 magic=0x528f071f]
Jan  1 04:49:49 (none) daemon.debug pppd[3662]: rcvd [CHAP Challenge id=0xa8 <68a5542e72ea5df247f3c9b33ff98339>, name = "removed"] 00 00 00 00
Jan  1 04:49:49 (none) daemon.warn pppd[3662]: Warning - secret file /etc/ppp/chap-secrets has world and/or group access
Jan  1 04:49:49 (none) daemon.debug pppd[3662]: sent [CHAP Response id=0xa8 <50e192d7c74d4f535b742bf24956df7c>, name = "removed"]
Jan  1 04:49:49 (none) daemon.debug pppd[3662]: rcvd [LCP EchoRep id=0x0 magic=0x797b3439] 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
Jan  1 04:49:49 (none) daemon.debug pppd[3662]: rcvd [CHAP Success id=0xa8 ""] 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 ...
Jan  1 04:49:49 (none) daemon.info pppd[3662]: CHAP authentication succeeded
Jan  1 04:49:49 (none) daemon.notice pppd[3662]: CHAP authentication succeeded
Jan  1 04:49:49 (none) daemon.notice pppd[3662]: peer from calling number 00:00:00:00:00:00 authorized
Jan  1 04:49:49 (none) daemon.warn pppd[3662]: kernel does not support PPP filtering
Jan  1 04:49:49 (none) daemon.debug pppd[3662]: sent [IPCP ConfReq id=0x1 <addr 0.0.0.0> <ms-dns1 0.0.0.0> <ms-dns3 0.0.0.0>]
Jan  1 04:49:49 (none) daemon.debug pppd[3662]: rcvd [IPCP ConfReq id=0x1 <addr removed>] 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
Jan  1 04:49:49 (none) daemon.debug pppd[3662]: sent [IPCP ConfAck id=0x1 <addr removed>]
Jan  1 04:49:49 (none) daemon.debug pppd[3662]: rcvd [IPCP ConfNak id=0x1 <addr removed> <ms-dns1 removed> <ms-dns3 removed>] 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
Jan  1 04:49:49 (none) daemon.debug pppd[3662]: sent [IPCP ConfReq id=0x2 <addr removed> <ms-dns1 removed> <ms-dns3 removed>]
Jan  1 04:49:49 (none) daemon.debug pppd[3662]: rcvd [IPCP ConfAck id=0x2 <addr removed> <ms-dns1 removed> <ms-dns3 removed>] 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
Jan  1 04:49:49 (none) daemon.notice pppd[3662]: local  IP address removed
Jan  1 04:49:49 (none) daemon.notice pppd[3662]: remote IP address removed
Jan  1 04:49:49 (none) daemon.notice pppd[3662]: primary   DNS address removed
Jan  1 04:49:49 (none) daemon.notice pppd[3662]: secondary DNS address removed
Jan  1 04:49:49 (none) daemon.info dnsmasq[350]: reading /tmp/resolv.conf.auto
Jan  1 04:49:49 (none) daemon.info dnsmasq[350]: using nameserver removed
Jan  1 04:49:49 (none) daemon.info dnsmasq[350]: using nameserver removed
Jan  1 04:49:49 (none) daemon.info dnsmasq[350]: using local addresses only for domain lan
Jan  1 04:49:49 (none) daemon.debug pppd[3662]: Script /etc/ppp/ip-up started (pid 3708)
Jan  1 04:49:49 (none) daemon.debug pppd[3662]: Script /etc/ppp/ip-up finished (pid 3708), status = 0x}}}
You should now be able to ping your ISPs gateway IP from telnet.

'''Set up DNS lookup'''

Normally with the usepeerdns command the DNS is saved in resolv.conf automatically

If this hasn't happened you may need to edit /etc/resolv.conf and add the lines: "search wan" and you may want to add a nameserver (DNS server). Then do ifdown wan and ifup wan.

'''Set up port forwarding'''

For general port forwarding just change /etc/firewall.user this executes at each bootup.

'''How to give interfaces fixed IP addresses'''

For port forwarding you need to have fixed IP addresses, just find out the MAC address of the ethernet card via the XP command prompt ipconfig /all or via linux ifconfig.

Then just add the following line to /etc/ethers

xx:xx:xx:xx:xx:xx ip.ip.ip.ip

or

xx:xx:xx:xx:xx:xx hostname

and edit /etc/ethers to:

ip.ip.ip.ip hostname The hostname of your PC can be found the same way as the MAC address.''' '''

'''Script to bring the ADSL interface up on bootup and also check the interface is up '''

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
'''WPNT834 Performance problem'''

Poor performance of the ADSL connection exists between the Netgear WPNT834 Rangemax 240 and D-Link DSL-502T, characterised by poor transfer speeds which may be asynchronous in nature, many retransmits and general packet loss in TCPdump and poor telnet access/webpage access to the DSL-502T, this is caused by poor ethernet performance between the two devices. This is possibly caused by a duplex mismatch or buggy 100FD/HD code on one of the devices.

The only way to solve this at present is to force the DSL-502T ethernet connection to Autonegotiate 10Mbit/s by changing one line of source code: see the last two posts here:

 . http://forum.openwrt.org/viewtopic.php?id=8117
== How to Debrick ==
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
quote "SETENV mtd1,0x90010090,0x90091000" - kernel
quote "SETENV mtd2,0x90000000,0x90010000" - bootloader (adam2 mostly)
quote "SETENV mtd3,0x903f0000,0x90400000" - configuration
quote "SETENV mtd4,0x90010090,0x903f0000" - this just covers filesystem/kernel
}}}
(p.s. the extra , is no mistake, I think it's needed)

'''Congratulations your router is alive:)'''

Ok so, power cycle the router and it should now work... lights should come on after 30 secs or so.

== Further Information ==
Old threads that may be of some use:

How to debrick the DSL-502T: http://forum.openwrt.org/viewtopic.php?id=7742

How to bring up the ADSL interface: http://forum.openwrt.org/viewtopic.php?pid=35563

PPPoE on the DSL-502T: http://forum.openwrt.org/viewtopic.php?pid=35563

Script to bring up the ADSL interface on bootup: http://forum.openwrt.org/viewtopic.php?id=8342

How to change passwd:[http://forum.openwrt.org/viewtopic.php?id=8342 http://forum.openwrt.org/viewtopic.php?id=9093]

VCMUX/LLC howto: http://forum.openwrt.org/viewtopic.php?id=8700

WPNT834 with DSL-502T duplex mismatch bug: http://forum.openwrt.org/viewtopic.php?id=8117

Bridged DSL (not PPP): http://forum.openwrt.org/viewtopic.php?id=8019

Couldn't increase MTU to 1500: http://forum.openwrt.org/viewtopic.php?id=9281

----
 . ["CategoryAR7Device"]
