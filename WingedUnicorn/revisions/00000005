= Here is the set of patches i use to run linux on my Di624-d2 : =
This page is add-on to [http://forum.openwrt.org/viewtopic.php?pid=59259#p59259 my post] in the forum.

== madwifi-0.9.3.3 ==
attachment:madwifi-ar2316.patch

This is just a quick hack - Di624 lacks boardconfig on flash, so this code is
used to assemble one on the fly. It uses dummy mac address 00:00:11:11:11:11, so is more like a reference,
not a proposed patch.

I build it with the following shell script:
{{{
export CROSS_COMPILE=mips-linux-
d=/pub
k=/root/di/di624/kernels/ar231x
make -j 3 TARGET=ap51 KERNELPATH=$k DESTDIR=$d BUS=AHB all
make TARGET=ap51 KERNELPATH=$k DESTDIR=$d BUS=AHB install
}}}

== ecos-2.0 (for redboot) ==
attachment:ecos-patch-ar2316.patch

I need to be able to upload original firmware at any time. Thus, i left untouched original loader and backup firmware. I use original loader to load redboot code as if it was just a primary firmware. 
Thus i have quite an odd memory layout for redboot: it's neither ROM, RAM or ROMRAM.
It's like RAM, but requires some initialization from ROM, but not like ROMRAM, because no need to copy to
RAM (original loader already did that). So, i just go ahead and hack startup code and ld scripts for ROM
model. Here is the [attachment:mkimg.pl perl script] to build firmware images compatible with original loader.

== kernel patches ==
Kernel patches are created against kernel sources taken from 
[ftp://ftp.dlink.se/Products/di-products/di-624/drivers_firmware/di624.source.tgz here].

=== mvPhy port trailer support for ae531x driver ===
attachment:eth-mvphy-vlan-traler-ar2316.patch

When mvPhy is built with CONFIG_VENETDEV option, packets that go out throug port5 (MAC) are appended with
4-byte trailer which identity the originating port. Same for packets that came from port5 - mvPhy strips
last 4 bytes and depending on the value may override default frame routing. This patch adds support for
"hw accelerated" vlan feature to ae531x driver: it tags packets that came from port0..port3 as vlan1 and 
port4 as vlan2. Similar for outgoing packets. This is very limited and non-flexible functionality, but 
thats enough to build 4lan/1wan port router.

This patch fixes a bug with load avg always >= 1:
original code creates a daemon thread during eth device open (ifconfig up).
It does not reparentize or daemonize new thread, thus 'ifconfig eth0 up' process remains in status "D"
(non interruptible sleep) in ps forever. In linux, non-interruptible wait is accounted as 100% cpu usage
during load avg calculations, so this is all kind of weird. I've changed the logic, so the same daemon 
thread appeared as normal kernel daemon process sleeping in interruptable sleep but ingnoring all signals. 
Yet, again, it is not stopped during device close and could be started again during next ifconfig up. So, it's not the best fix ever :)

=== ar2316 arch support ===
attachment:arch-ar2316.patch

adds MIPS32 4KecR2 processor id support. without this code kernel lacks wait instruction,
thus wasting power on heating the air.

=== mtd patch for my flash layout ===
attachment:mtd-ar2316.patch

this is my personal flash layout. you may hack this file to use your own. I've tried to use redboot 
fis partition parser code, but it seems to be broken and i was not in mood to fix it.


'''
Disclaimer: none of this patches are ready to be adopted. They are just a braindump/research results.
It can only be used as a reference by someone who have enough time and will to add support for this
platform to according projects.
'''
