Vincent Fox, Feb 26 2006

= Objective =
Mobile WiFi!

Soon after receiving the new Linksys WRTSL54GS (SL for short) and getting OpenWRT running on it
(thanks Kaloz), my first thought was "what an awkward product-name!".  Second thought was the
the many uses for the USB port. One obvious one was using a cellular phone to attach to
the internet, for mobile WiFi! Not a new idea, but much easier to implement now.

I should say up front that all cellular data networks have latency that just blows. 
Pings of 500+ms are the norm and may bounce up to 2000ms. So don't expect it to replace
your landline. But there are certain good uses for it, like setting up quick
connectivity for a few people at an event. Or mounted in a vehicle for a
totally mobile hotspot! Once you do get a response, throughput can be pretty good.
But you definitely want to use dnsmasq, and any other caching mechanism you
can get your hands on, to keep things as local as possible.

= Items used =

   Linksys WRTSL54GS with OpenWRT

   Nokia 6230 cellphone with Cingular EDGE/GPRS "Media Net" package with unlimited data

   USB data cable that connects to POP-port on phone

= Basic connectivity to phone =

== Install USB-serial module ==
{{{
root@OpenWrt:~# ipkg install kmod-usb-serial
root@OpenWrt:~# insmod usbserial
}}}

== Verify that cellular phone is recognized ==

{{{
root@OpenWrt:~# logread | tail
Jan  1 00:33:01 (none) kern.info kernel: hub.c: new USB device 01:02.0-1, assigned address 2
Jan  1 00:33:01 (none) kern.warn kernel: usb.c: USB device 2 (vend/prod 0x421/0x40f) is not claimed by any active driver.
Jan  1 00:39:01 (none) kern.info kernel: usb.c: registered new driver serial
Jan  1 00:39:01 (none) kern.info kernel: usbserial.c: USB Serial support registered for Generic
Jan  1 00:39:01 (none) kern.info kernel: usbserial.c: USB Serial Driver core v1.4
}}}

Those vendor and product numbers, we must do something with them.....

== Modify usb-serial options ==
{{{
root@OpenWrt:~# vi /etc/modules.d/70-usb-serial
usbserial vendor=0x421 product=0x40f
}}}

== Install microcrom so we can check things out ==
{{{
root@OpenWrt:~# ipkg install microcom
root@OpenWrt:~# reboot
}}}

== Login again, check by typing AT to modem, see if it responds OK ==
{{{
root@OpenWrt:~# microcom -D/dev/usb/tts/0
AT

OK

}}}

:)

Hit ~x to get out of microcom


= PPP conectivity =

== Install PPP ==
{{{
root@OpenWrt:~# ipkg install kmod-ppp
root@OpenWrt:~# ipkg install ppp
root@OpenWrt:~# ipkg install chat
root@OpenWrt:~# reboot
}}}

== PPP config file ==

This part took some Googling. Finally I found a good page that I used as the basis:
[http://www.advantedgecomputing.com/opensource/gc83linux.html]

{{{
root@OpenWrt:~# vi /etc/ppp/peers/cingular
# information about your device
/dev/usb/tts/0 # device file assigned to Nokia 6230
230400 # DTE speed
# Initial authentication
user ISPDA@CINGULARGPRS.COM # username (data acceleration)
password CINGULAR1 # a common GPRS/EDGE password
defaultroute # use cellular network's gateway
noipdefault # force peer to specify local IP (GC83 only)
usepeerdns # use DNS servers from remote host
remotename attws # assume 'attws' as name of remote system
ipparam attws # add 'attws' to ip-up & ip-down script
crtscts # enable hardware flow control
lock # lock the serial port when in use
noauth # don't expect peer to authenticate
persist # re-dial connection if dial fails

# Uncomment next 2 lines for debugging
#debug
#nodetach

ipcp-max-configure 20 # increase the maximum IPCP config requests
maxfail 0 # do not stop retrying connection

# Move on to the chat script after connection
connect '/usr/sbin/chat -v -V -t3 -f /etc/ppp/peers/chat-cingular'
}}}

== PPP Chat script ==
{{{
root@OpenWrt:~# vi /etc/ppp/peers/chat-cingular
#
SAY 'Starting GPRS connect script...\n'
SAY '\n'
# ispauth CHAP # define auth method (optional)

SAY 'Setting the abort string\n'
SAY '\n'

# Abort String ---------------------------------

#ABORT BUSY ABORT 'NO CARRIER' ABORT VOICE ABORT 'NO DIALTONE'
ABORT 'NO DIAL TONE' ABORT 'NO ANSWER' ABORT DELAYED
#TIMEOUT 10
#ABORT 'BUSY' ABORT 'NO ANSWER' ABORT 'NO CARRIER'

# ----------------------------------------------
SAY 'Initializing modem\n'

# Modem Initialization -------------------------
#'' ATZ
# Eo=No echo, V1=English result codes
#OK 'ATE0V1'
'' AT+cfun=1
OK AT+cfun=1
OK AT+cgreg=1
OK AT
#TIMEOUT 40
# ----------------------------------------------

# Additional initialization (optional) ---------
# /begin att
OK AT&F&D2&C1E0V1S0=0
OK AT+IFC=2,2
OK ATS0=0
OK AT
OK AT&F&D2&C1E0V1S0=0
OK AT+IFC=2,2
# /end att
#AT&FE0S0=0
}}}

== PPP device setup ==
First attempt to use our setup will give an error, unless we fix it.
{{{
root@OpenWrt:~# pppd call cingular
pppd: pppd is unable to open the /dev/ppp device.
You need to create the /dev/ppp device node by
executing the following command as root:
        mknod /dev/ppp c 108 0
root@OpenWrt:~# mkdir /var/lock
root@OpenWrt:~# vi /etc/modules.d/70-ppp
ppp_generic
ppp_async
slhc
}}}

== Lock file directory creation ==
If we are going to have the "lock" option in the config file, we need the
/var/lock directory created. By nature OpenWRT recreates /var on each boot.
So add a startup script that ensures it is created on each boot.
{{{
root@OpenWrt:~# vi /etc/init.d/S80ppp
mkdir -p /var/lock
root@OpenWrt:~# chmod +x /etc/init.d/S80ppp
}}}

== WAN interface change ==
Time to cut the umbilical cord. Unplug the WAN port ethernet line used for all this setup work.
{{{
root@OpenWrt:~# nvram set wan_device=ppp0
root@OpenWrt:~# nvram set wan_ifname=ppp0
root@OpenWrt:~# nvram commit
root@OpenWrt:~# reboot
}}}

== Time for test drive! ==
{{{
root@OpenWrt:~# pppd call cingular debug nodetach
(output)
}}}

Hopefully you made WOO-HOO noises at this point as you watched it successfully connect.

== Check connectity ==
{{{
root@OpenWrt:~# ifconfig ppp0
ppp0      Link encap:Point-Point Protocol
          inet addr:166.172.48.113  P-t-P:10.6.6.6  Mask:255.255.255.255
          UP POINTOPOINT RUNNING NOARP MULTICAST  MTU:1500  Metric:1
          RX packets:4 errors:0 dropped:0 overruns:0 frame:0
          TX packets:4 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:3
          RX bytes:64 (64.0 B)  TX bytes:82 (82.0 B)
root@OpenWrt:~# netstat -nr
Kernel IP routing table
Destination     Gateway         Genmask         Flags   MSS Window  irtt Iface
10.6.6.6        0.0.0.0         255.255.255.255 UH        0 0          0 ppp0
192.168.1.0     0.0.0.0         255.255.255.0   U         0 0          0 br0
0.0.0.0         10.6.6.6        0.0.0.0         UG        0 0          0 ppp0
root@OpenWrt:~# ping -c 4 www.gatech.edu
PING www.gatech.edu (130.207.165.120): 56 data bytes
64 bytes from 130.207.165.120: icmp_seq=0 ttl=243 time=836.0 ms
64 bytes from 130.207.165.120: icmp_seq=1 ttl=243 time=676.3 ms
64 bytes from 130.207.165.120: icmp_seq=2 ttl=243 time=738.1 ms
64 bytes from 130.207.165.120: icmp_seq=3 ttl=243 time=680.0 ms

--- www.gatech.edu ping statistics ---
4 packets transmitted, 4 packets received, 0% packet loss
round-trip min/avg/max = 676.3/732.6/836.0 ms
}}}

= Usage =
All you should need to do is ssh in, and execute:
{{{
root@OpenWrt:~# pppd call cingular
}}}

I am adding this last few lines of text, using the Nokia PPP connection :)

= Caveats =

 1. Some packages came from different "people" directories on download site. I didn't keep very good track of which came from where, but what didn't come from the kaloz or stable trees, probably came from nico. At this moment nbd seems to have the most complete selection, so if I were to start over I'd try to install everything from the nbd build directory.
 2. A NoCatSplash page with buttons for Connect/Disconnect would be handy.
 3. Want the "Internet" LED on or blinking when dialed up, as a reminder. Or use SES button/LED for connect/disconnect and indication.
 4. Would be nice to have a local clock source, as the SL has no clock and comes up with wrong time at boot. PPP does note the large time disparity in the logs. You can sync after connecting with rdate or ntpclient, obvious place to append this is in /etc/ppp/ip-up.

----
CategoryHowTo
