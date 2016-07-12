## Please edit system and help pages ONLY in the moinmaster wiki! For more
## information, please see MoinMaster:MoinPagesEditorGroup.
##acl MoinPagesEditorGroup:read,write,delete,revert All:read
##master-page:HelpTemplate
##master-date:Unknown-Date
#format wiki
#language en
== WRT54GL v1.0 and v1.1 RAM upgrade ==
Originaly WRT54GL come with the Hynix HY5DU281622ET-J which are 16MB.
This chip is pin-to-pin compatible with the Micron's [http://download.micron.com/pdf/datasheets/dram/ddr/512MBDDRx4x8x16.pdf MT46V32M16] chip which is 64MB.

If you do not have a professional grade soldering station with a hot air gun you may follow these [http://www.megajournal.ru/journal/users_data/11049/msg_files/24469/video2_tsop48.wmv video] instructions (a ~7MB wmf clip).

The replaced chip should give you a 32MB of RAM on the first power-up.

To obtain the full 64MB capacity now do
{{{
nvram set sdram_init = 0x0113
nvram set sdram_ncdl = 0x000000
nvram commit
}}}
and power-cycle your WRT54GL.

=== Compatibility ===
These instructions should be valid for WRT54G v2~v4 devices.
(Not tested yet, if you do - post your results)
