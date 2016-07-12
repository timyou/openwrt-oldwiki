= Hardware performance of devices running under OpenWRT =

Although some people believe that these devices are not dependent on their CPU speed due to the commonly low load averages, this is not necessarily true. A processor at any moment is either executing applicable code or not, essentially ON or OFF. Load averages are averages over time. Therefore, increased processor (and memory) clocks can decrease latency, speed execution of scripts and programs, and increase I/O.

Additionally, many processors can be safely overclocked. See [http://wiki.openwrt.org/OpenWrtDocs/Customizing/Hardware/Overclocking this page] for overclocking information. It includes arguments for and against overclocking. Users on either side of the fence should refrain from forcing their opinions on the majority.

== Devices performance table ==
'''Performance of CPU / Memory'''

||'''Date''' ||'''Tester''' ||'''Time for mem''' ||'''Time for pi''' || '''Time for e''' || '''Time for float''' || '''Bench version''' || '''OS''' ||'''Device''' ||'''CPU''' ||'''CPU Freq''' ||'''Link to HW page''' ||
|| 2006-06-09 || jcollake || 6.4s || 12.4s || 13.3s || 7.7s || v0.6 || OpenWrt RC5 || Linksys WRT54G v4.0 || BCM3302 v0.8 || 250mhz (OC) || ["OpenWrtDocs/Hardware/Linksys/WRT54G"] ||
|| 2006-05-16 || Figurehead || 6.9s || 13.7s || 15.4s || 10.8s || v0.6 || OpenWrt RC5 || Linksys WRT54G v3.1 || BCM3302 V0.7 || 216MHz || ["OpenWrtDocs/Hardware/Linksys/WRT54G"] ||
|| 2006-05-03 || evildevil || 5.3s || 29.8s || 27.0s || 4.0s || v0.6 || !DebianSlug Sid || Linksys NSLU2 || XScale-IXP420 || 266MHz || [http://www.nslu2-linux.org/wiki/Info/HomePage NSLU2-LINUX] ||
|| 2006-05-09 || CharlesAmos || 5.9s || 11.0s || 12.2s || 6.8s || v0.6 || OpenWRT pre-RC5 || Linksys WRTSL54GS || BCM4704 || 266MHz || ["OpenWrtDocs/Hardware/Linksys/WRTSL54GS"] ||
|| 2006-05-01 || cabo || 6.4s || 13.2s || 14.6s || 10.2s || v0.5 || (unknown) || Linksys WRT54GS 1.0 || BCM3302 V0.7 || 216MHZ || ["OpenWrtDocs/Hardware/Linksys/WRT54GS"] ||
|| 2006-04-02 || evildevil || 6.7s || 13.5s || 15.0s || 8.0s || v0.5 || DD-WRT2.3 || Linksys WRT54G v3.1 || BCM3302 V0.7 || 216MHz || ["OpenWrtDocs/Hardware/Linksys/WRT54G"] ||
|| 2006-05-03 || jecuendet || 7.2s || 14.3s || 16.8s || 12.1s || v0.6 || OpenWRT RC5 || ASUS WL-500GD || BCM3302 V0.7 || 200MHz || ["OpenWrtDocs/Hardware/Asus/WL500GD"] ||
|| 2006-05-01 || yans || 7.2s || 14.4s ||16.1s ||11.4s || v0.5 || OpenWRT RC5 || Motorola WR850Gv3 ||BCM3302 V0.7 || 200MHz || ["OpenWrtDocs/Hardware/Motorola/WR850G"] ||
|| 2006-05-04 || ''MickeyMouse'' || 7.2s || 14.5s || 16.2s || 11.4s || v0.6 || OpenWRT RC5 || Linksys WRT54G v2.2 || BCM3302 V0.7 || 200Mhz || ["OpenWrtDocs/Hardware/Linksys/WRT54G"] ||
|| 2006-05-01 || arteqw || 7.3s || 14.5s || 16.1s || 11.3s || v0.5 || OpenWRT RC5 || Motorola WR850G v2 || BCM3302 V0.7 || 200MHz || ["OpenWrtDocs/Hardware/Motorola/WR850G"] ||
|| 2006-05-02 || Ultimo || 7.5s || 14.2s || 15.8s || 9.1s || v0.5 || OpenWRT RC5 || Linksys WRT54GL v1 || BCM3302 V0.7 || 200MHz || ["OpenWrtDocs/Hardware/Linksys/WRT54GL"] ||
|| 2006-05-01 || pyllyukko || 7.7s || 14.6s || 16.2s || 9.4s || v0.5 || (unknown) || Linksys WRT54GS v4 || BCM3302 V0.8 || 200MHz || ["OpenWrtDocs/Hardware/Linksys/WRT54GS"] ||
|| 2006-05-02 || evildevil || 7.7s || 15.2s || 16.9s || 10.3s || v0.5 || Kamikaze || Netgear WGT634U || BCM3302 V0.7 || 200MHz || ["OpenWrtDocs/Hardware/Netgear/WGT634U"] ||
|| 2006-05-03 || ''PhilipPemberton'' || 9.1s || 48.4s || 33.8s || 4.1s || v0.6 || !OpenDebianSlug Sarge (Debonaras), 2.6.16rc4 kernel || Linksys NSLU2 || XScale-IXP420 || 266MHz || [http://www.nslu2-linux.org/wiki/Info/HomePage NSLU2-LINUX] ||
|| 2006-05-01 || mauritzius || 10.3s || 25.3s || 30.9s || 15.1s || v0.5 || OpenWRT pre-RC5 || Asus WL-500g || BCM4710 V0.0 || 125MHz || ["OpenWrtDocs/Hardware/Asus/WL500G"] ||
|| 2006-05-01 || hoerchen || 12.5s || 30.6s || 38.39s || 19.2s || v0.3 || (unknown) || Microsoft MN-700 || BCM4710 || 125MHz || ["OpenWrtDocs/Hardware/Microsoft"] ||
|| 2006-05-02 || pkirchhofer || 9.3s || 61.4s || 52.4s || 8.0s || v0.6 || Debonaras (gcc-3.4) || Linksys NSLU2 || XScale-IXP420 || 133MHz || [http://www.nslu2-linux.org/wiki/Info/HomePage NSLU2-LINUX] ||
|| 2006-05-04 || LinuxInside || 7.6s || 12.6s || 14.5s || 7.6s || v0.6 || (unknown) || Linksys WAG54GX2 || BCM3302 V0.7 || 240Mhz || ["OpenWrtDocs/Hardware/Linksys/WAG54GX2"] ||
|| 2006-05-11 || ArteQ || 10.5s || 24.7s || 30.2s || 13.0s || v0.6 || Oleg 1.9.2.7-7c || ASUS Wl500g || BCM4710 V0.0 || 125MHz || ["OpenWrtDocs/Hardware/Asus/WL500G"] ||


'''Performance of IO (IDE, USB, Disk)'''

TODO, which bench to use?

||'''Date''' ||'''Tester''' ||'''Time to run''' ||'''Version of bench''' ||'''Device''' ||'''CPU''' ||'''Freq''' ||'''Link to HW page''' ||


== How to compile and run the benchmark ==
 1. you need to download it: attachment:openwrt_cpu_bench_v06.c
 1. Compile it

{{{
    cd <...>/OpenWrt-SDK-Linux-i686-1
    staging_dir_mipsel/bin/mipsel-linux-gcc -O0 -o openwrt_cpu_bench openwrt_cpu_bench_vXX.c
       => This will produce a binary openwrt_cpu_bench
       => Be careful to add -O0, we don't want to check compiler optimization but CPU capabilities
}}}

 3. Or download it precompiled for mipsel here: attachment:openwrt_cpu_bench_v06.bin
 3. Or download it precompiled for OpenDebianSlug here: ["attachment:openwrt cpu bench opendebianslug.bin"]
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
 * v0.6 : Initialization of variables for gcc on NSLU2
