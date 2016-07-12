= Hardware performance of devices running under OpenWRT =
This page is dedicated to performance of small devices running OpenWRT (or similar distro, unslung for example)

== Devices performance table ==
'''Performance of CPU / Memory'''

||'''Date''' ||'''Tester''' ||'''Time for mem''' ||'''Time for pi''' ||'''Time for e''' ||'''Version of bench''' ||'''Device''' ||'''CPU''' ||'''CPU Freq''' ||'''Link to HW page''' ||
|| 2006-05-01 || jecuendet || 7s || 1.6s || 15.9s || v0.3 || ASUS WL-500GD || BCM3302 V0.7 || 200MHz || http://wiki.openwrt.org/OpenWrtDocs/Hardware/Asus/WL500GD ||
|| 2006-05-01 || arteqw || 7.2s || 1.6s || 16.1s || v0.3 || ''Motorola WR850G v2'' || ''BCM3302 V0.7'' || ''200MHz'' || ''http://wiki.openwrt.org/OpenWrtDocs/Hardware/Motorola/WR850G'' ||


'''Performance of IO (IDE, USB, Disk)'''

TODO, which bench to use?

||'''Date''' ||'''Tester''' ||'''Time to run''' ||'''Version of bench''' ||'''Device''' ||'''CPU''' ||'''Freq''' ||'''Link to HW page''' ||


== How to compile and run the benchmark ==
 1. you need to download it: attachment:openwrt_cpu_bench_v03.c
 1. Compile it

{{{
    cd <...>/OpenWrt-SDK-Linux-i686-1
    staging_dir_mipsel/bin/mipsel-linux-gcc -o openwrt_cpu_bench openwrt_cpu_bench.c
       => This will produce a binary openwrt_cpu_bench
}}}
 3. Or download it precompiled for mipsel here: attachment:openwrt_cpu_bench_v03.bin
 3. Copy it to your device
 3. Run it: '''./openwrt_cpu_bench'''
 3. Report in the table above the time it took to run
