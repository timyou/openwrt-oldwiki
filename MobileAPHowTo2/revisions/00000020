Vincent Fox, Feb 26 2006

= Objective =
Mobile WiFi!

Soon after receiving the new WRTSL54GS and getting OpenWRT running on it (thanks Kaloz)
my thoughts turned to the many uses for the USB port. One obvious one was using a cellular
phone to attach to the internet, for mobile WiFi! Not a new idea, but much easier to implement now.

= Items used =

   1. WRTSL54GS with OpenWRT

   2. Nokia 6230 cellphone with Cingular EDGE/GPRS data service

   3. USB data cable that connects to POP-port on phone

= Basic connectivity to phone =

== Need to get USB-serial module installed ==
{{{
root@OpenWrt:~# ipkg install kmod-usb-serial
root@OpenWrt:~# insmod usbserial
}}}

== See if cellphone recognized ==

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

== PPP device setup ===
First attempt to use our setup will give an error, unless we fix it.
{{{
root@OpenWrt:~# pppd call cingular
pppd: pppd is unable to open the /dev/ppp device.
You need to create the /dev/ppp device node by
executing the following command as root:
        mknod /dev/ppp c 108 0
root@OpenWrt:~# ipkg install 
root@OpenWrt:~# mknod /dev/ppp c 108 0
}}}

== Time for test drive! ==
{{{
root@OpenWrt:~# pppd call cingular

----
CategoryHowTo
