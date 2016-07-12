= Hardware performance of devices running under OpenWRT =
This page is dedicated to performance of small devices running OpenWRT (or similar distro, unslung for example)

== Devices performance table ==
'''Performance of CPU / Memory'''

||'''Date''' ||'''Tester''' ||'''Time for mem''' ||'''Time for pi''' || '''Time for e''' || '''Time for float''' || '''Version of bench''' ||'''Device''' ||'''CPU''' ||'''CPU Freq''' ||'''Link to HW page''' ||
|| 2006-05-01 || jecuendet || 7.2s || 14.3s || 16.8s || 12.1s || v0.5 || ASUS WL-500GD || BCM3302 V0.7 || 200MHz || [:OpenWrtDocs/Hardware/Asus/WL500GD] ||
|| 2006-05-01 || arteqw || 7.3s || 14.5s || 16.1s || 11.3s || v0.5 || Motorola WR850G v2 || BCM3302 V0.7 || 200MHz || [:OpenWrtDocs/Hardware/Motorola/WR850G] ||
|| 2006-05-01 || mauritzius || 10.3s || 25.3s || 30.9s || 15.1s || v0.5 || Asus WL-500g || BCM4710 V0.0 || 125MHz || [:OpenWrtDocs/Hardware/Asus/WL500G] ||
|| 2006-05-01 || Ultimo || 7.5s || 1.6s || 15.8s || || v0.3 || WRT54GL v1 || BCM3302 V0.7 || 200MHz || [:OpenWrtDocs/Hardware/Linksys/WRT54GL] ||
|| 2006-05-01 || hoerchen || 12.5s || 30.6s || 38.39s || 19.2s || v0.3 || Microsoft MN-700 || BCM4710 || 125MHz || [:OpenWrtDocs/Hardware/Microsoft] ||
|| 2006-05-01 || pyllyukko || 7.7s || 14.6s || 16.2s || 9.4s || v0.5 || WRT54GS v4 || BCM3302 V0.8 || 200MHz || [:OpenWrtDocs/Hardware/Linksys/WRT54GS] ||
|| 2006-05-01 || charles || 5.9s || 10.9s || 12.2s || 6.9s || v0.5 || WRTSL54GS || BCM4704 || 266MHz || [:OpenWrtDocs/Hardware/Linksys/WRTSL54GS] ||
||2006-05-01 ||yans ||7.2s ||14.4s ||16.1s ||11.4s || v0.5 ||WR850Gv3 ||BCM3302 V0.7 || 200MHz || [:OpenWrtDocs/Hardware/Motorola/WR850G] ||
|| 2006-05-01 || cabo || 6.4s || 13.2s || 14.6s || 10.2s || v0.5 || WRT54GS 1.0 || BCM3302 V0.7 || 216MHZ || [:OpenWrtDocs/Hardware/Linksys/WRT54GS] ||

'''jecuendet''': would be very cool if a NSLU2 owner could bench it and report results!

'''Performance of IO (IDE, USB, Disk)'''

TODO, which bench to use?

||'''Date''' ||'''Tester''' ||'''Time to run''' ||'''Version of bench''' ||'''Device''' ||'''CPU''' ||'''Freq''' ||'''Link to HW page''' ||


== How to compile and run the benchmark ==
 1. you need to download it: attachment:openwrt_cpu_bench_v05.c
 1. Compile it

{{{
    cd <...>/OpenWrt-SDK-Linux-i686-1
    staging_dir_mipsel/bin/mipsel-linux-gcc -O0 -o openwrt_cpu_bench openwrt_cpu_bench_vXX.c
       => This will produce a binary openwrt_cpu_bench
       => Be careful to add -O0, we don't want to check compiler optimization but CPU capabilities
}}}

 3. Or download it precompiled for mipsel here: attachment:openwrt_cpu_bench_v05.bin
 3. Copy it to your device
 3. Run it: '''./openwrt_cpu_bench_vXX.bin'''
 3. Run it 2 more times and report the average of the 3 runs
 3. Report in the table above the time it took to run

== Versions of the benchmark ==
 * v0.1 : Initial revision
 * v0.2 : ???
 * v0.3 : Various bug fixes
 * v0.4 : Added floating point calculation
 * v0.5 : Corrected pi benchamrk
