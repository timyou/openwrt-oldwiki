=== Hardware Description ===

http://southern-beach.dee.cc/wbr-b11/wbr-b11naka.jpg http://southern-beach.dee.cc/wbr-b11/wbr-b11mpci.jpg http://southern-beach.dee.cc/wbr-b11/wbr-b11antena.jpg

 * mini-PCI WLAN card: WLI-MPCI-B11G with BCM4301

 * PCB prepared for USB connection (preferably for self-powered USB devices, since the router has 3.3V external power supply)   


=== Installation of OpenWRT Firmware ===

Where do we start. the TFTP firmware upgrade did not work for me with the openwrt-brcm-2.4-squashfs.trx as it was described to work for the WBR2-G54.

The update through the Webinterface of the WBR-B11 Firmware 1.20 didn't work either.

It was throwing me a red AN  ERROR HAS OCCURED DURING FIRMWARE UPLOAD. DEVICE REBOOTING message. Did the upload for the WRT54g SquashFS bin, renamed the trx to bin and tried that. No change. So ... thanks to [mbm] who pointed me to the header of the the original firmware header vs. the trx one. (Could have been my idea *g*)

So here it goes:''''''

'''Original BUFFALO Firmware (WBR-B11_1.20_7.03)'''

{{{
WBR-B11 1.20 7.03 filelen=3469312 HDR0}}}

''' http://blueflubberball.de/buffalo-WBR-B11/WBR-B11_1.20.png '''

'''OpenWRT Firmware (openwrt-brcm-2.4-squashfs.trx)'''

{{{
HDR0}}}

http://blueflubberball.de/buffalo-WBR-B11/openwrt-brcm-2.4-squashfs.trx.png

----
We just add the part before HDR0 to the OpenWRT Firmware. Take into account that the filelen value will be different.     

The original Firmware is a total of 3469346 long. Difference of 34 charachters which is exactly the part before the HDR0.

The OpenWRT Firmware is a total of 1531904 so that the new header will look like this:

{{{
WBR-B11 rc05 7.03 filelen=1531904 HDR0 }}}

http://blueflubberball.de/buffalo-WBR-B11/openwrt-brcm-2.4-squashfs_changed.trx.png

As you see, I was sneaky enough to change the 1.20 version to, rc05. Gawd, I am so l337 it (mega)herz. ;-)

Anyways, save the changes and upload over the Webinterface of the original firmware.

You will see:

{{{
Upgrading the firmware... 
(It takes one and half minute) 
Don't cut off the power while the LED flashes. 
After complete the upgrading, restart automatically. 

Upgrade is complete. 
Rebooting... 
If you want to continue configuration, please close browser software then execute it again. }}}

The DIAG light will blink, turn off and turn on again. It took roughly a minute (+- some) for the WBR-B11 to completely reboot.

Gave it another minute or so and then opened ["http://192.168.11.1"].

Welcome to OpenWRT RC5.

You are done. :)

----
Haven't opened it yet so no clue about JTAG nor SERIAL. Have fun 

If any questions arise, want pretty pictures or whatnot. Send me an E-Mail. stacato [at] gmail [dOt] com

Cheers, stacato

----
P.S.: This process should be the same for the WBR-G54 since it supposedly is the exact same device just with a different mini-PCI card. 

----
=== Hints that might save you some time ===

 * use Internet Explorer to access the Buffalo admin page (there is a browser check - a firmware update with FireFox won't work)

 * among many redundant NVRAM entries there are settings that will make S50dnsmasq fail. The following commands will fix this:

{{{nvram set dhcp_num=50
nvram set dhcp_start=101
nvram commit}}}

 * the WL package doesn't seem to work with the built in 803.11b WLAN card. It throws the following error message:
{{{root@OpenWrt:~# wl scan
eth2: Operation not supported}}}

 * most commands of iwlist won't work 

 * I should have known right from the start: no WPA either... I won't even try WDS. 

What you get is a OpenWRT WEP only router. Buy a different router, if you need something else.
