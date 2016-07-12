## Please edit system and help pages ONLY in the moinmaster wiki! For more
## information, please see MoinMaster:MoinPagesEditorGroup.
##acl MoinPagesEditorGroup:read,write,delete,revert All:read
##master-page:HelpTemplate
##master-date:Unknown-Date
#format wiki
#language en
== WRT54GL v1.0 and v1.1 RAM upgrade ==
Originaly WRT54GL come with the Hynix HY5DU281622ET-J which are 16MB. These chips are pin-to-pin compatible with the Micron's [http://download.micron.com/pdf/datasheets/dram/ddr/512MBDDRx4x8x16.pdf MT46V32M16] chip which is 64MB.

If you do not have a professional grade soldering station with a hot air gun you may follow these [http://www.megajournal.ru/journal/users_data/11049/msg_files/24469/video2_tsop48.wmv video] instructions (a ~7MB wmv clip).

The replaced chip should give you a 32MB of RAM on the first power-up.

To obtain the full 64MB capacity now do

before to do this please confirmed that with the exactly the cpu and sdram init
please ref to http://wl500g.dyndns.org/sdram.html

{{{
nvram set sdram_init = 0x0113
nvram set sdram_ncdl = 0x000000
nvram commit
}}}
and power-cycle your WRT54GL.

=== Compatibility ===
These instructions should be valid for WRT54G v2~v4 devices. (Not tested yet, if you do - post your results)
Also valid for WRT54G v8 -upgrade to 32 mb

=== Comment about the WRT54G V2 ===
Comment added 07.08.2007 by Markus Rudolf:  WRT54G V2 contains SDRAM (mine contains 2 pieces of [http://web.icsi.com.tw/domino/packinfo.nsf/eb92bdb85417334b482569ec00225dc2/727fa1dcc13a325948256f320003c65a/$FILE/42s16400(RevE).pdf ISSI IC42S16400-6T] (1M x 16Bit x 4 Banks SDRAM) instead of above mentioned DDR-RAM. So at least with these chips you can't upgrade to 32MByte or more. I'm still trying to find some suitable SDRAMs to upgrade my WRT54G V2 to 32MB+.

WRT54G V2.2 is new PCB layout and at least upgrade to 32MB is possible without any further action but simply changing the RAM chip. 64MB not tested due to lack of sufficient RAM chip.

=== Where to get a RAM chip from? ===
The easyest way to obtain a 66-pin TSOP memory chip is to unsolder it from a SoDIMM DDR module.

Look for a four-chip single-sided 256MB or for an eight-chip double-sided 512MB one. For example, the Kingston's [http://www.valueram.com/datasheets/KVR400X64SC3A_256.pdf KVR400X64SC3A/256] is one of them and [http://www.valueram.com/datasheets/KVR400X64SC3A_512.pdf KVR400X64SC3A/512] is the other.

=== Chips to avoid ===
The WRT54GL needs a 16-bit-wide databus device, here is the list of an 8-bit devices seen on some SoDIMM modules:

Stay away from an ELPIDA's [http://www.elpida.com/pdfs/E0699E50.pdf D5108AFTA-5B-E] available on an eight-chip double-sided 512MB module.

Stay away from an Infineon's [http://www.infineon.com/upload/Document/Memory%20Products/DS/HYB25D256xxxCx_rev212_www.pdf HYB25D256800] available on some Kingston's modules!
