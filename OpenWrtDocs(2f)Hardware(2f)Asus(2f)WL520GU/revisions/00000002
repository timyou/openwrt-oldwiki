I've tried micro-openwrt-brcm-2.4-squashfs.trx, default-openwrt-brcm-2.4-squashfs.trx and openwrt-brcm-2.4-squashfs.trx, and no luck :( Router became unavailable. I was able to install asus firmware back using tftp.

Verified, it is true that you can swap back to stock ASUS firmware after flashing with this and that.

- - - - -

Tomato 1.17 ND.trx works for this model. But there's no USB, and that's the cool part about this unit.
Ok, so here's how to scrutinize this unit, should you be curious, and don't have the source code.

One very nice feature of the ASUS wl-520GU is the USB storage drive and vfat support already built into the kernel. the first partition on a USB stick with vfat is automounted at /tmp/harddisk/part0/

So, to improve the webif ;D download nc (mipsel) by itself from

http://packages.debian.org/sarge/mipsel/netcat/download

copy the nc binary to the root of your USB stick.

slap your USB stick into the USB port on the wl520gu, power cycle the router.

head on over to:

 http://192.168.1.1/Main_AdmStatus_Content.asp

enter this: /tmp/harddisk/part0/nc -l -p 31337 -e /bin/sh

you'll notice that the webif just sits there waiting... good!

back to your favorite command line,

# nc 192.168.1.1 31337

you're in!

Really, the only advantage of this /bin/sh is that you are not going to be limited by the webif... /bin/busybox is very crippled anyway and it's mostly a read-only file system. (no cp, rm, tar, wget, etc) i tried some silly stuff already, i can run other mipsel executables! all i have to do is fill my USB stick full of useful mipsel commands :)
