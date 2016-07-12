I've tried micro-openwrt-brcm-2.4-squashfs.trx, default-openwrt-brcm-2.4-squashfs.trx and openwrt-brcm-2.4-squashfs.trx, and no luck :( Router became unavailable. I was able to install asus firmware back using tftp.


- - - - -

Verified, it is true that you can swap back to stock ASUS firmware after flashing with this and that.

Tomato 1.17 ND.trx works for this model. But there's no USB. 

- - - - - 

using the stock ASUS firmware, you can get a limited shell through the net interface of the router at http://192.168.1.1/Main_AdmStatus_Content.asp by copying the netcat mipsel binary to the root of a USB stick and then entering "/tmp/harddisk/part1/nc -l -p 31337 -e /bin/sh" and then returning to your usual computer already equipped with nc and entering "nc 192.168.1.1 31337" neat, but almost completely useless unless the only reason you are looking at openwrt is to support one or two additional programs that won't automatically run as services :( 


I was informed that the "trunk" release of kamikaze supports the BCM5354, so I tried it. After brute forcing some things that may have been related only to my configuration choices (iptables forwarding was broken for me but easily 'fixed'), it works! 

...unless you are comfortable with compiling a kernel, this is not the USB-enabled OpenWRT router for you. Not quite yet. 

But if you are comfortable compiling a kernel, then it's a very nice 4/16MB router with USB support, if I do say so myself!!

USB ohci as well as ehci-hcd 2.0 drivers --(are working just fine with vfat using openwrt.)-- Crash. the 2.0 drivers that is. When sending or reading data to any filesystem at the faster speed, a reboot can occur. 

on the WL-520U ** DO NOT USE THE USB STICK WITH 2.0 DRIVERS TO LOAD NEW KERELS ** I did, and during the process the router rebooted. I'm very, very lucky to have recovered and re-flashed it. Since that time I have verified that transferring large amounts of data to or from the memory stick reboots the router when using EHCI-HCD USB. 

Even ASUS does not build the 2.0 driver, as proven by their .config. 

So indeed, ohci is all that can be expected to work longer than an hour at the moment. 

Still testing, now with the USB 1.1 Mass storage... 

...still a WIP
