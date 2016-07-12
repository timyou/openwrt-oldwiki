Describe OpenWrtDocs/Hardware/Buffalo/WBR-B11 here.

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
 . We just add the part before HDR0 to the OpenWRT Firmware. Take into account that the filelen value will be different.  

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

Cheers,
