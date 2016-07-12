## Please edit system and help pages ONLY in the moinmaster wiki! For more
## information, please see MoinMaster:MoinPagesEditorGroup.
##master-page:CategoryTemplate
##master-date:Unknown-Date
#format wiki
#language en


== Overclocking ==
Many routers can be overclocked, though it should not be done if you don't have a JTAG cable to recover in case things go horribly wrong.

=== Why overclock? ===
==== The argument for: ====


Even if your processor average load is low, this doesn't mean you won't benefit from overclocking. A load average is an average use over a period of time. However, at any given time a processor is either actively executing pertinent code or its not. So at any given moment it's all or none. This means that, in theory, operations can be sped up in cases where the CPU is the bottleneck.

One example is that those users who've added SD card mods to their WRT54G/S see gains in I/O speed proportional to the CPU/SB clock speed. Furthermore, webif, scripts, and everything CPU or memory dependent should run proportionally faster to the amount the CPU/SB clock is increased.

Even Linksys overclocked the WRT54GS v2.x to 216mhz to fix a bug with the system memory, so clearly it's not such a risk to overclock these boxes. Since they have a set of frequencies they are allowed to run at, one wonders if Broadcom hasn't designed them to run at these frequencies when proper cooling is applied.

Most importantly though, why not overclock these units if they run perfectly stable when overclocked? With proper cooling mods these processors can run fine even at their maximum frequencies (depending on the CPU).

==== The argument against: ====

Most people aren't doing things with their WRT54G/S that will be substantially affected by increases in CPU/SB clock speed, so why risk the stability of your box by overclocking it?

=== Cooling Modifications ===
Depending on how high you clock your device, you may need to add complimentary cooling to prevent overheating. A heatsink can easily be put on the CPU and a 12mm fan can often be mounted internally. 

'''Cooling Links:'''

 * [http://jcollake.blogspot.com/2006/06/internal-pics-of-my-wrt54gv4.html Images of a modification to the WRT54Gv4 that adds a heatsink and fan]

=== Overclocking for the WRT54G v4 and above ===
The WRT54G v4 and WRT54G v5 are different from the v2 and v3 models in that they have a BCM5352/BCM3302 revision v0.8 (instead of v0.7). This processor defaults to 200mhz with an sbclock setting of 100mhz. The highest valid CPU frequency for this processor is 250mhz, which yields an sbclock frequency of 125mhz.

Although the v4 and v5 will boot up to frequencies greater than 250mhz (for example, 252 mhz), the CPU clock frequency will actually only be set to its default clock frequency. The nvram variables will not have changed, so some firmwares (i.e. DD-WRT) may mis-report the clock frequency.

To determine the actual clock frequency, use 'cat /proc/cpuinfo' or examine the first few lines of the output from 'dmsg'.

Although it is common practice to set the nvram clkfreq variable so that it includes the sbclock setting, the sbclock is actually ignored for this processor revision since it has a locked CPU/SB clock ratio. For example, clkfreq=240,126 actually ends up with an sbclock setting of 120mhz, since 126mhz is not in a valid ratio with a CPU clock frequency of 240mhz. Therefore, it is recommended to not set the sbclock value (the number after the ',').

Users wishing to set their WRT54G v4 or WRT54G v5 to its maximum clock frequency should execute these commands at the terminal

{{{
nvram set clkfreq=250
nvram commit
reboot }}}

==== Valid BCM5352/BCM3302 r0.8 (WRT54G v4 and v5) Frequencies ====
||__'''CPU'''__ ||__'''SB'''__ || __'''Note'''__ ||
||183 ||92 || ||
||187 ||94 || ||
||198 ||98 || ||
||200 ||100 ||default ||
||216 ||108 || ||
||225 ||113 || ||
||233 ||116 || ||
||237 ||119 || ||
||250 ||125 || ||


==== Overclocking Experiences ====
* I've had a WRT54G v4 running at the maximum valid frequency of 250mhz for a couple weeks with no stability problems. I do have a heat-sink (though not a very good one since it only partially covers the CPU) and a fan installed internally. The box ends up running quite cool. 2.) I've had a WRT54G v5 running at 240mhz for a couple weeks with no stability problems. It has a heat-sink but no fan. It does get pretty hot. 250mhz seemed to be less stable after the unit heated up. A fan addition should allow the v5 to run as well as the v4 mentioned above at 250mhz.

==== Recovery From a Bad Overclock ====
The CFE of these units handles overclocking very well and will simply reject values greater than 250mhz and find a closest match to values less than or equal to 250mhz. Therefore, it is unlikely you'll brick your router. However, be careful just in case you have a different CFE or this information is incorrect!

If things do go wrong, the WRT54G v4 and WRT54G v5 do reset the clkfreq variable to the default of 200mhz when the reset button is held down for a few seconds. Other versions with different CFEs may not do this.

If the clock frequency results in an unstable processor, there may be only a few seconds to initiate a JTAG based nvram erase.

=== Overclocking for the WRT54G/GS v2, v2.2, and v3 ===
Other models use the commonly documented clock frequencies, with a max CPU clock of 300mhz. They do not appear to have CFEs that will prevent the clock from being set to invalid frequencies, or that recover to default clkfreq via a nvram reset. Be even more careful with these versions of the WRT54G.

==== Valid BCM5352/BCM3302 r0.7 Frequencies (WRT54G v2 - v3) ====
||__'''CPU'''__ ||__'''SB'''__ || __'''Note'''__ ||
||192 ||96 || ||
||200 ||100 || default ||
||216 ||108 || ||
||228 ||114 || ||
||240 ||120 || ||
||252 ||126 || ||
||264 ||132 || ||
||280 ||120 || ||
||300 ||120 || ||


=== Overclocking for the WRT54G/GS v1, v1.1 ===
This processor runs at 125mhz by default. Overclocking is reported to not be possible, but this has not been confirmed.
