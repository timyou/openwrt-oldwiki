'''Microsoft hardware notes'''

The only Microsoft router capable to run OpenWrt is the MN-700, but You have to use JTAG to flash a new bootloader first. More info about this can be found [http://wl500g.info/showthread.php?t=1616 here].
To use RS232 you need to install a 16550 on the pads under the board, the J8 header, a crystal, some resistors and capacitors (SMD). More info at: [http://wl500g.info/showthread.php?t=1616&page=7&pp=15&highlight=mn-700  Microsoft MN700 hack project]

On Whiterussian RC3 and RC4, the broadcom et ethernet driver causes random reboots of the device. Use the b44 driver instead. (See also [https://dev.openwrt.org/ticket/76])

On Whiterussian rc6 this box is quite stable. 

It is possible to run hacked asus firmware on this box, but recent versions of oleg's firmware exhibit the same random reboots as were experienced with the et driver in whiterussian rc3 and rc4. Possibly some older version of oleg's firmware does not have this issue.  

= nvram =

this model will write out the following nvram values if the bootloader detects a corrupted nvram: 

{{{
boardtype=bcm94710ap
boardnum=mn700
clkfreq=125
sdram_init=0x0419
sdram_config=0x0000
sdram_refresh=0x8040
et0macaddr=00:11:22:33:44:55
et0phyaddr=30
et0mdcport=0
et1macaddr=00:11:22:33:44:55
et1phyaddr=5
et1mdcport=1
dl_ram_addr=a0001000
os_ram_addr=80001000
os_flash_addr=bfc40000
lan_ipaddr=192.168.1.1
lan_netmask=255.255.255.0
scratch=a0180000
boot_wait=on
watchdog=3000
hardware_version=WL500-02-02-01-00
regulation_domain=0X30DE
}}}

This was obtained by running 'strings' against /dev/mtd/0ro. macaddr values will obviously vary by whatever value you patched cfe.bin with when you jtagged your mn-700. 

It still may not be safe to erase the nvram on this hardware. But hey, you have jtag. Go nuts. 

= Power LED =

As of Whiterussian RC6 the diag driver detects this router as an Asus WL500g. This is not surprising, since the bootloader is a tweaked Asus bootloader image. Hopefully future versions of diag.o will recognize "boardnum=mn700". 

Since diag doesn't recognize the board correctly, the power LED does not light or blink. Other LEDs work fine. 

The power led is GPIO 6. 

If you wish to fiddle with it manually, the easiest method is to use the gpio utility:  http://downloads.openwrt.org/utils/gpio.tar.gz

{{{
cd /tmp
wget http://downloads.openwrt.org/gpio.tar.gz
gzip -d gpio.tar.gz
tar xvf gpio.tar
mv gpio /usr/sbin
}}}

"gpio enable 6" will turn the power LED green. Disabling it will turn it orange. Polling it will turn it off. 

fwiw, the restore button is GPIO 7. 

= Hardware Issues =

This board has a very good groundplane. The side-effect of this is that the author of this article was unable to desolder any through-holes with a 65-watt Weller WTCPS soldering iron. 

It is far easier to just get an eensy drill bit and, twisting it betwixt thumb and forefinger, drill out the solder. This makes adding headers for jtag and serial MUCH easier. Harbor Freight Tools will sell you a random selection of 'micro carbide rasps' for a few dollars - these are essentially tiny drill bits, the same as are used by pc board manufacturers. 

'''Bad capacitor'''

Every picture of an mn-700 board the author of this section has ever seen shows the capacitor next to the jtag port bulging at the top and leaking electrolyte. 

This capacitor needs to be replaced. It is a low-ESR 1500uf 6.3v electrolytic. 

Any reasonbly new 1500uf cap should work in this position, if you can fit it in the case. You should not skimp on the value. 

Mouser part number 647-UUD0J152MN is recommended. This is a high quality Nichicon UUD capacitor that is actually smaller than the original. It costs 90 cents. Since it is a surface mount capacitor, you will need to gently bend the legs straight and pull off the plastic base, magically converting it to a through-hole capacitor. 

Please remember to observe polarity. 

It is possible that the original capacitor was damaged in part by high-frequency ripple from the switchmode power supply that feeds it. For peace of mind, you may wish to parallel the 1500uf electrolytic with a .1uf or .01uf ceramic. It may or may not help, but it certainly won't hurt. Best case scenario it shunts the noise to ground, saving the cap. Worst case scenario it increases the capacitance at this point in the circuit by an insignificant measure. 

The author of this section also replaced the 470uf 25v capacitor near the power jack with a 1000uf 35v part. This probably isn't necessary, because the original part still read 469uf on an LCR after removal, but didn't hurt. 

Any of these modifications are at your own risk. You broke it, you bought it. Nobody takes any responsibility but you. 

----
CategoryBrand CategoryModel
