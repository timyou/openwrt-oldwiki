== create dir ==
{{{
 mkdir -p /mnt/IDE1/flash/dump
 cd /mnt/IDE1/flash/dump
}}}
== dump flash ==
{{{
 dd </dev/mtd0 >redboot.bin (bootloader?)
 dd </dev/mtd1 >zImage (kernel)
 dd </dev/mtd2 >rd.gz (ramdisk ext2)
 dd </dev/mtd3 >hddapp.tgz (samba and so on)
 dd </dev/mtd4 >VCTL.bin (??)
 dd </dev/mtd5 >curconf.tgz (config)
 dd </dev/mtd6 >fid.dat (??)
}}}
== copy ImageInfo ==
{{{
 cp /system/ImageInfo ./
}}}
== create firmware ==
{{{
 tar czf ../firm.tar.gz *
}}}
now you have your Firmware on /mnt/IDE1/flash/dump/firm.tar.gz<br/>
'''save this file on your pc!'''
