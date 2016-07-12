= Hardware performance of devices running under OpenWRT =
Although some people believe that these devices are not dependent on their CPU speed due to the commonly low load averages, this is not necessarily true. A processor at any moment is either executing applicable code or not, essentially ON or OFF. Load averages are averages over time. Therefore, increased processor (and memory) clocks can decrease latency, speed execution of scripts and programs, and increase I/O.

Additionally, many processors can be overclocked (though this operation has some risk and should not be attempted lightly). See ["OpenWrtDocs/Customizing/Hardware/Overclocking"] for overclocking information. It includes arguments for and against overclocking. Users on either side of the fence should refrain from forcing their opinions on the majority.

[See further discussion, which has been moved to end of this page...]

== Devices performance table ==
'''Performance of CPU / Memory'''
||'''Date''' ||'''Tester''' ||'''Time for mem''' ||'''Time for pi''' ||'''Time for e''' ||'''Time for float''' ||'''Bench version''' ||'''OS''' ||'''Device''' ||'''CPU''' ||'''CPU Freq''' ||'''Link to HW page''' ||
||2006-04-02 ||evildevil ||6.7s ||13.5s ||15.0s ||8.0s ||v0.5 ||DD-WRT2.3 ||Linksys WRT54G v3.1 ||BCM3302 V0.7 ||216MHz ||["OpenWrtDocs/Hardware/Linksys/WRT54G"] ||
||2006-05-01 ||cabo ||6.4s ||13.2s ||14.6s ||10.2s ||v0.5 ||(unknown) ||Linksys WRT54GS 1.0 ||BCM3302 V0.7 ||216MHZ ||["OpenWrtDocs/Hardware/Linksys/WRT54GS"] ||
||2006-05-01 ||yans ||7.2s ||14.4s ||16.1s ||11.4s ||v0.5 ||OpenWRT RC5 ||Motorola WR850Gv3 ||BCM3302 V0.7 ||200MHz ||["OpenWrtDocs/Hardware/Motorola/WR850G"] ||
||2006-05-01 ||arteqw ||7.3s ||14.5s ||16.1s ||11.3s ||v0.5 ||OpenWRT RC5 ||Motorola WR850G v2 ||BCM3302 V0.7 ||200MHz ||["OpenWrtDocs/Hardware/Motorola/WR850G"] ||
||2006-05-01 ||pyllyukko ||7.7s ||14.6s ||16.2s ||9.4s ||v0.5 ||(unknown) ||Linksys WRT54GS v4 ||BCM3302 V0.8 ||200MHz ||["OpenWrtDocs/Hardware/Linksys/WRT54GS"] ||
||2006-05-01 ||mauritzius ||10.3s ||25.3s ||30.9s ||15.1s ||v0.5 ||OpenWRT pre-RC5 ||Asus WL-500g ||BCM4710 V0.0 ||125MHz ||["OpenWrtDocs/Hardware/Asus/WL500G"] ||
||2006-05-01 ||hoerchen ||12.5s ||30.6s ||38.39s ||19.2s ||v0.3 ||(unknown) ||Microsoft MN-700 ||BCM4710 ||125MHz ||["OpenWrtDocs/Hardware/Microsoft"] ||
||2006-05-02 ||pkirchhofer ||9.3s ||61.4s ||52.4s ||8.0s ||v0.6 ||Debonaras (gcc-3.4) ||Linksys NSLU2 ||XScale-IXP420 ||133MHz ||[http://www.nslu2-linux.org/wiki/Info/HomePage NSLU2-LINUX] ||
||2006-05-02 ||evildevil ||7.7s ||15.2s ||16.9s ||10.3s ||v0.5 ||Kamikaze ||Netgear WGT634U ||BCM3302 V0.7 ||200MHz ||["OpenWrtDocs/Hardware/Netgear/WGT634U"] ||
||2006-05-02 ||Ultimo ||7.5s ||14.2s ||15.8s ||9.1s ||v0.5 ||OpenWRT RC5 ||Linksys WRT54GL v1 ||BCM3302 V0.7 ||200MHz ||["OpenWrtDocs/Hardware/Linksys/WRT54GL"] ||
||2006-05-03 ||''PhilipPemberton'' ||9.1s ||48.4s ||33.8s ||4.1s ||v0.6 ||!OpenDebianSlug Sarge (Debonaras), 2.6.16rc4 kernel ||Linksys NSLU2 ||XScale-IXP420 ||266MHz ||[http://www.nslu2-linux.org/wiki/Info/HomePage NSLU2-LINUX] ||
||2006-05-04 ||''MickeyMouse'' ||7.2s ||14.5s ||16.2s ||11.4s ||v0.6 ||OpenWRT RC5 ||Linksys WRT54G v2.2 ||BCM3302 V0.7 ||200Mhz ||["OpenWrtDocs/Hardware/Linksys/WRT54G"] ||
||2006-08-04 ||''ww'' ||6.7s ||13.4s ||15.1s ||10.3s ||v0.6 ||''DD-WRT 23'' ||''Linksys WRT54G v2.2'' ||''BCM3302 V0.7'' ||''200MHz'' ||["OpenWrtDocs/Hardware/Linksys/WRT54G"] ||
||2006-05-04 ||LinuxInside ||7.6s ||12.6s ||14.5s ||7.6s ||v0.6 ||(unknown) ||Linksys WAG54GX2 ||BCM3302 V0.7 ||240Mhz ||["OpenWrtDocs/Hardware/Linksys/WAG54GX2"] ||
||2006-05-11 ||ArteQ ||10.5s ||24.7s ||30.2s ||13.0s ||v0.6 ||Oleg 1.9.2.7-7c ||ASUS Wl500g ||BCM4710 V0.0 ||125MHz ||["OpenWrtDocs/Hardware/Asus/WL500G"] ||
||2006-05-03 ||evildevil ||5.3s ||29.8s ||27.0s ||4.0s ||v0.6 ||!DebianSlug Sid ||Linksys NSLU2 ||XScale-IXP420 ||266MHz ||[http://www.nslu2-linux.org/wiki/Info/HomePage NSLU2-LINUX] ||
||2006-05-03 ||jecuendet ||7.2s ||14.3s ||16.8s ||12.1s ||v0.6 ||OpenWRT RC5 ||ASUS WL-500GD ||BCM3302 V0.7 ||200MHz ||["OpenWrtDocs/Hardware/Asus/WL500GD"] ||
||2006-05-09 ||CharlesAmos ||5.9s ||11.0s ||12.2s ||6.8s ||v0.6 ||OpenWRT pre-RC5 ||Linksys WRTSL54GS ||BCM4704 ||266MHz ||["OpenWrtDocs/Hardware/Linksys/WRTSL54GS"] ||
||2006-05-16 ||Figurehead ||6.9s ||13.7s ||15.4s ||10.8s ||v0.6 ||OpenWrt RC5 ||Linksys WRT54G v3.1 ||BCM3302 V0.7 ||216MHz ||["OpenWrtDocs/Hardware/Linksys/WRT54G"] ||
||2006-06-09 ||jcollake ||6.4s ||12.4s ||13.3s ||7.7s ||v0.6 ||OpenWrt RC5 ||Linksys WRT54G v4.0 ||BCM3302 v0.8 ||250mhz (OC) ||["OpenWrtDocs/Hardware/Linksys/WRT54G"] ||
||2006-06-09 ||Loloke ||5.7s ||10.6s ||11.8s ||6.6s ||v0.6 ||OpenWRT RC5 ||Linksys WRTSL54GS ||BCM4704 ||266MHz ||["OpenWrtDocs/Hardware/Linksys/WRTSL54GS"] ||
||2000-06-15 ||achim71000 ||5.5s ||10.6s ||11.8s ||6.7s ||v0.6 ||OpenWRT RC5 ||ASUS Wl500gP ||BCM4704 ||266MHZ ||["OpenWrtDocs/Hardware/Asus/WL500GP"] ||
||2006-07-03 ||''Secutor'' ||7.5s ||14.2s ||15.8s ||9.1s ||v0.6 ||''OpenWrt RC5'' ||''WRT54GL 1.1'' ||''BCM3302 V0.8'' ||''200MHz'' ||''OpenWrtDocs/Hardware/Linksys/WRT54GL'' ||
||2006-07-07 ||RafalRzeczkowski ||5.3s ||10.5s ||11.5s ||6.5s ||v0.6 ||OpenWRT RC5 ||Buffalo WZR-RS-G54 ||BCM4704 rev 8 ||264MHz ||["OpenWrtDocs/Hardware/Buffalo/WZR-RS-G54"] ||
||2006-07-19 ||DurvalMenezes ||7.2s ||14.2s ||15.8s ||11.3s ||v0.6 ||OpenWRT RC5 ||ASUS WL-500GD ||BCM3302 V0.7 ||200MHz ||["OpenWrtDocs/Hardware/Asus/WL500GD"] ||
||2006-07-20 ||FrederikKlama ||5.3s ||10.5s ||11.6s ||6.6s ||v0.6 ||OpenWRT RC5 ||ASUS WL-500gP ||BCM4704 ||266MHz ||["OpenWrtDocs/Hardware/Asus/WL500GP"] ||
||2006-09-21 ||jp ||7.7s ||14.5s ||16.1s ||9.3s ||v0.6 ||OpenWRT RC5 ||Linksys WRT 54GL v1.0 ||BCM3302 V0.8 ||200MHz ||["OpenWrtDocs/Hardware/Linksys/WRT54GL"] ||
||2006-09-21 ||jp ||7.0s ||13.2s ||14.7s ||8.5s ||v0.6 ||OpenWRT RC5 ||Linksys WRT 54GL v1.0 ||BCM3302 V0.8 ||216MHz ||["OpenWrtDocs/Hardware/Linksys/WRT54GL"] ||
||2006-12-26 ||malfi ||7.3s ||18.5s ||20.2s ||7.1s ||v0.6 ||OpenWRT trunk 2006-12-25 ||Fonera Fon ||AR5315 4KEc V6.4 ||183MHz ||["OpenWrtDocs/Hardware/Fon/Fonera"] ||
||2007-01-29 ||phlegmer ||7.4s ||14.4s ||16.0s ||9.4s ||v0.6 ||DD-WRT v23 SP3 (01/26/07) std ||Buffalo WHR-G54S ||BCM5352 rev 0 ||200MHz ||["OpenWrtDocs/Hardware/Buffalo/WHR-G54S"] ||
||2007-01-29 ||phlegmer ||7.2s ||14.4s ||16.1s ||9.8s ||v0.6 ||DD-WRT v23 SP2 (09/15/06) std ||Buffalo WBR2-G54 ||BCM4712 rev 1 ||200MHz ||["OpenWrtDocs/Hardware/Buffalo/WBR2-G54"] ||
||2007-02-02 ||kjrozema ||7.5s ||14.2s ||15.8s ||8.3s ||v0.6 ||OpenWRT RC6 ||Linksys WRT54GL v1.1 ||BCM3302 v0.8 ||200MHz ||["OpenWrtDocs/Hardware/Linksys/WRT54GL"] ||
||2007-02-02 ||kjrozema ||6.9s ||13.1s ||14.6s ||7.6s ||v0.6 ||OpenWRT RC6 ||Linksys WRT54GL v1.1 ||BCM3302 v0.8 ||216MHz ||["OpenWrtDocs/Hardware/Linksys/WRT54GL"] ||
||2007-02-02 ||kjrozema ||6.7s ||12.6s ||14.0s ||7.4s ||v0.6 ||OpenWRT RC6 ||Linksys WRT54GL v1.1 ||BCM3302 v0.8 ||225MHz ||["OpenWrtDocs/Hardware/Linksys/WRT54GL"] ||
||2007-02-06 || Hauke || 0.2s || 1.2s || 1.0s || 0.1s || v0.6 || Ubuntu Linux EdgyEft || PC ||  Core 2 Duo || 2X 2,13GHz || ||
||2007-11-07 || ''IordanIordanov'' || 5.0s || 8.9s || 9.6s || 5.7s || v0.6 ||''DD-WRT'' || ''WRT350N'' || ''BCM3302'' || ''300Mhz'' || '''' ''' ||
||<style="vertical-align: top;">2008-04-30 ||<style="vertical-align: top;">DooMMasteR ||<style="vertical-align: top;">5.26s ||<style="vertical-align: top;">10.14s ||<style="vertical-align: top;">11.27s ||<style="vertical-align: top;">6.19s ||<style="vertical-align: top;">v0.6 ||<style="vertical-align: top;">DD-WRT ||<style="vertical-align: top;">WL500GP ||<style="vertical-align: top;">BCM94704 ||<style="vertical-align: top;">280Mhz ||<style="vertical-align: top;">OpenWrtDocs ||
|| 2008-06-30 || ''a9988cd'' || 4.9s || 9.4s || 10.3s || 5.2s || v0.6 || ''Tomato 1.19''|| ''ASUS WL-500gP v1'' || ''BCM4704 rev 8'' || ''O.C.300Mhz'' || ''OpenWrtDocs/Hardware/Asus/WL500GP'' ||
|| 2008-06-30 || ''a9988cd'' || 6.8s || 11.9s || 13.3s || 7.5s || v0.6 || ''Tomato 1.19-ND''|| ''ASUS WL-500gP v2'' || ''BCM5354 rev 2'' || ''240Mhz'' || ''LinkToHwPage'' ||

TODO, which bench to use?
||Date''' ''' ||Tester''' ''' ||Time to run''' ''' ||Version of bench''' ''' ||Device''' ''' ||CPU''' ''' ||Freq''' ''' ||Link to HW page''' ''' ||


== How to compile and run the benchmark ==
 1. you need to download it: attachment:openwrt_cpu_bench_v06.c
 1. Compile it
{{{
    cd <...>/OpenWrt-SDK-Linux-i686-1
    staging_dir_mipsel/bin/mipsel-linux-gcc -O0 -o openwrt_cpu_bench openwrt_cpu_bench_vXX.c
       => This will produce a binary openwrt_cpu_bench
       => Be careful to add -O0, we don't want to check compiler optimization but CPU capabilities
}}}
 1. Or download it precompiled for mipsel here: attachment:openwrt_cpu_bench_v06.bin
 1. Or download it precompiled for OpenDebianSlug here: ["attachment:openwrt cpu bench opendebianslug.bin"]
 1. Copy it to your device
 1. Run it: ./openwrt_cpu_bench_vXX.bin''' '''
 1. Run it 2 more times and report the average of the 3 runs
 1. Report in the table above the time it took to run
== Versions of the benchmark ==
 * v0.1 : Initial revision
 * v0.2 : ???
 * v0.3 : Various bug fixes
 * v0.4 : Added floating point calculation
 * v0.5 : Corrected pi benchamrk
 * v0.6 : Initialization of variables for gcc on NSLU2
= Discussion =
----
 . [...continued from above]
No, this page is still useless; we're not arguing over what a load average is or what a benchmark is for. We're simply pointing out the absurdity of this benchmark.

Almost all the boards in question are the exact same hardware, they're even based off of the same schematics, otherwise known as a reference design. It doesn't matter what the brand name on the box is; you're comparing a board with a 200Mhz Broadcom mips chip to another board with a 200Mhz Broadcom mips chip and expecting to see dramatic differences. Worse is the fact that you're actually seeing differences between two benchmarks being run on identical models -- this alone should tell you that the testing conditions are flawed.

I'm also not a fan of the "many processors can be safely overclocked" mentality. Yes you can easily change the clock frequency by setting an nvram variable, and it may even work on some boards. The problem is what happens when it doesn't work -- that's where the whole "safe" concept fails, because when it doesn't work there's often no easy or safe way to reset it, you actually have to pull apart the device and connect up a JTAG cable to reset the configuration.

- mbm

----
 . Ah, I understand your argument now, and it does have merit.
However, not all entries in this table are comparing the same hardware. It is slightly helpful to compare two different architectures or processors to see which may perform best at CPU or memory intensive tasks (at least, to the best this synthetic benchmark may tell us).

The differences in performance on identical models (with identical clocks) is probably due to their load at the time of the testing, or something else. Although the differences are not great, you are right that this does indicate the benchmark isn't 100%. However, it's close enough for now, until someone develops a better benchmark (or better recommended testing procedures).

The author recommends averaging 3 tests, yet the program encourages pasting the results of a single run. I think the benchmark could be improved by running the tests multiple times and finding an average. This change would probably yield closer results for identical models. I may make this change myself if the author doesn't.

So, the page, while perhaps far from perfect, isn't useless IMHO. I'd love to present your opinions here as well as my own. Please induldge us and let this page live on with your noted, and quite valid, concerns.

-jcollake

--

= See also =
 * ["OpenWrtDocs/Benchmarks/OpenSSL"]
