Soon after receiving the new WRTSL54GS and getting OpenWRT running on it (thanks Kaloz)
my thoughts turned to the many uses for the USB port. One obvious one was using a cellular
phone to attach to the internet, for mobile WiFi! Not a new idea, but much easier to implement now.

Items that I had:
1. WRTSL54GS with OpenWRT

2. Nokia 6230 cellphone with data server

3. USB data cable that connects to POP-port on phone

''Steps:''

1) Need to get USB-serial module installed

ipkg install kmod-usb-serial
insmod usbserial

2) Get cellphone recognized

logread shows recognized, but not fully:
{{{
Jan  1 00:33:01 (none) kern.info kernel: hub.c: new USB device 01:02.0-1, assigned address 2
Jan  1 00:33:01 (none) kern.warn kernel: usb.c: USB device 2 (vend/prod 0x421/0x40f) is not claimed by any active driver.
Jan  1 00:39:01 (none) kern.info kernel: usb.c: registered new driver serial
Jan  1 00:39:01 (none) kern.info kernel: usbserial.c: USB Serial support registered for Generic
Jan  1 00:39:01 (none) kern.info kernel: usbserial.c: USB Serial Driver core v1.4
}}}

Those vendor and product numbers, we must do something with them.....

3) Modify usb-serial options
Edit /etc/modules.d/70-usb-serial for the device:
usbserial vendor=0x421 product=0x40f

4) Install microcrom so we can check things out
ipkg install microcom
reboot

5) Login again, check
{{{
microcom -D/dev/usb/tts/0
AT

OK
}}}
:)

----
CategoryHowTo
