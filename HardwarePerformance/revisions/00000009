= Hardware performance of devices running under OpenWRT =
This page is dedicated to performance of small devices running OpenWRT (or similar distro, unslung for example)

== Devices performance table ==
'''Performance of CPU / Memory'''
||<tablewidth="800px" tablealign="">'''Date'''||'''Tester'''||'''Time for mem'''||'''Time for pi'''||'''Time for e'''||'''Version of bench'''||'''Device'''||'''CPU'''||'''CPU Freq'''||'''Link to HW page'''||
|| 2006-05-01 || jecuendet || 7s || 14s || 16s || v0.1 || ASUS WL-500G || BCM3302 V0.7 || 200MHz || http://wiki.openwrt.org/OpenWrtDocs/Hardware/Asus/WL500G ||



'''Performance of IO (IDE, USB, Disk)'''

TODO, which bench to use?

||<tablewidth="800px" tablealign="">'''Date'''||'''Tester'''||'''Time to run'''||'''Version of bench'''||'''Device'''||'''CPU'''||'''Freq'''||'''Link to HW page'''||
|| || || || || || || || ||
|| || || || || || || || ||
|| || || || || || || || ||


== How to compile and run the benchmark ==

 1. you need to download it: attachment:openwrt_cpu_bench.cpp
 2. Compile it
{{{
    cd <...>/OpenWrt-SDK-Linux-i686-1
    staging_dir_mipsel/bin/mipsel-linux-gcc -o openwrt_cpu_bench openwrt_cpu_bench.cpp
       => This will produce a binary openwrt_cpu_bench
}}}
 3. Copy it to your device
 4. Run it: '''./openwrt_cpu_bench'''
 5. Report in the table above the time it took to run
