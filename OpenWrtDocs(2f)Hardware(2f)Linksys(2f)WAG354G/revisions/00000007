= Linksys WAG354G =

== Running OpenWRT ==

'''WARNING''' This page is a work in progress.  So far I (IanJackson) am just collecting information found in various other places (eg, IRC logs) together.

Bootloader: ["PSPBoot"] Firmware image: *-WA31.bin for annex a (ADSL over POTS) devices

Known problems:

* `Crashes occasionally' for some people or with some devices.  Currently not known whether this is a hardware problem.

* Using the tftp procedure to upload an openwrt image seems for some people to disable the tftp facility in PSPBoot, so that future upgrades have to be done from within openwrt.  However this didn't happen to me -IanJackson.

=== Enable ADSL ===

If you flash openwrt to wag354g you may want to use adsl. All the info can be found on the [http://wiki.openwrt.org/OpenWrtDocs/Hardware/D-Link/DSL-502T D-Link 502T page], in the section 1.3 "Enabling ADSL".

----

== Hardware Infos ==

=== Serial console ===

[http://wiki.openwrt.org/OpenWrtDocs/Hardware/Linksys/WAG354G?action=AttachFile&do=get&target=serial-wag354G.png Schematics Serial Console]

Configure teminal with 38400 bauds, 8 bits, no parity, 1 stop bit (38400 8N1)


=== Flash layout ===
{{{
      
0x2f0000   fs                           3008K       (mtd0)                   0x900e0000,0x903d0000
0x0C0000  kernel             ---> 768K   +     "        = (mtd1)  0x90020000,0x903d0000
0x020000  BL                    ---> 128K  (mtd2)                        0x90000000,0x90020000
0x020000  lang partition ---> 128K  (mtd4)                        0x903d0000,0x903f0000
0x010000  nvram               --->  64K  (mtd3)                        0x903f0000,0x90400000
________________                     _______
0x400000  TOT                       4096K

}}}

----
 . ["CategoryAR7Device"]    
