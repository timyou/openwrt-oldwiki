Vincent Fox, Feb 26 2006

= Objective =
Mobile WiFi!

== Background ==
Soon after receiving the new WRTSL54GS and getting OpenWRT running on it (thanks Kaloz)
my thoughts turned to the many uses for the USB port. One obvious one was using a cellular
phone to attach to the internet, for mobile WiFi! Not a new idea, but much easier to implement now.

Items that I had:
   1. WRTSL54GS with OpenWRT

   2. Nokia 6230 cellphone with Cingular EDGE/GPRS data service

   3. USB data cable that connects to POP-port on phone

== Steps: ==

1) Need to get USB-serial module installed
{{{
root@OpenWrt:~# ipkg install kmod-usb-serial
root@OpenWrt:~# insmod usbserial
}}}

2) See if cellphone recognized

{{{
root@OpenWrt:~# logread | tail
Jan  1 00:33:01 (none) kern.info kernel: hub.c: new USB device 01:02.0-1, assigned address 2
Jan  1 00:33:01 (none) kern.warn kernel: usb.c: USB device 2 (vend/prod 0x421/0x40f) is not claimed by any active driver.
Jan  1 00:39:01 (none) kern.info kernel: usb.c: registered new driver serial
Jan  1 00:39:01 (none) kern.info kernel: usbserial.c: USB Serial support registered for Generic
Jan  1 00:39:01 (none) kern.info kernel: usbserial.c: USB Serial Driver core v1.4
}}}

Those vendor and product numbers, we must do something with them.....

3) Modify usb-serial options
{{{
root@OpenWrt:~# vi /etc/modules.d/70-usb-serial
usbserial vendor=0x421 product=0x40f
}}}

4) Install microcrom so we can check things out
{{{
root@OpenWrt:~# ipkg install microcom
root@OpenWrt:~# reboot
}}}

5) Login again, check by typing AT to modem, see if it responds OK
{{{
root@OpenWrt:~# microcom -D/dev/usb/tts/0
AT

OK

}}}

:)

Hit ~x to get out of microcom

6) Now we need to install PPP
{{{
root@OpenWrt:~# ipkg install kmod-ppp
root@OpenWrt:~# ipkg install ppp
}}}

7) Need a config file
{{{
root@OpenWrt:~# vi /etc/ppp/peers/cingular
# information about your device
/dev/usb/tts/0 # device file assigned to Nokia 6230
115200 # slower negotiation speed
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

# Leave uncommented, at least until your connection works consistently
debug # provides verbose output to stderr

# ---------------------------------------------------------------
# Uncomment this option if you don't have the screen window manager
# screen is a helpful tool
# it can be obtained from http://www.gnu.org/software/screen

nodetach # do not allow terminal to detach

ipcp-max-configure 20 # increase the maximum IPCP config requests
maxfail 0 # do not stop retrying connection

# Move on to the chat script after connection
connect '/usr/sbin/chat -v -V -t3 -f /etc/ppp/peers/chat-cingular'
}}}

8) Time for a chat script
{{{
root@OpenWrt:~# vi /etc/ppp/peers/chat-cingular

}}}
----
CategoryHowTo
