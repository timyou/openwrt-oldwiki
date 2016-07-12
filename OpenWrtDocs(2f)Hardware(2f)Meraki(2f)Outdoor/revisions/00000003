== Intro ==
'nicknamed': Sparky

The Meraki Outdoor (FCCID:UDX-MERAKI-OTDR) is a variant of the Meraki Mini with a weather sealed enclosure, two ethernet ports and a more powerful 200 mW radio.  The system is built on a Atheros AR2317. This device is very similar to the older Meraki Mini units and has similar software layout. 99% of the entries on the Mini apply to the sparky unit.

== Watchdog guards this device... ==
The stock firmware both a software watchdog that writes to the ar2315 hardware watchdog.  90 seconds after power up, unless the software watchdog starts, the system reboots.
Care must be taken in flashing device as Redboot will reboot the device after 5 minutes. 
I believe this does it by activating the hardware watchdog with a 5 minute heartbeat.
Meraki has released the source code to its RedBoot [http://dl.meraki.net/linux/redboot-ap61.tar.gz here]. This compiles (there is a syntax error with tail +2), and the existing Reboot will execute the new Redboot. It can be tested on the device by naming it art_ap51.elf and putting it on 192.168.84.9:tft.

== Restore, with watchdog ==
I sucked the existing flash partitions of a virgin Meraki Outdoor unit:
{{{
ssh meraki@192.168.84.1 'dd if=/dev/mtd1 bs=64k' >stage2.bak
ssh meraki@192.168.84.1 'dd if=/dev/mtd2 bs=64k' >storage.bak
ssh meraki@192.168.84.1 'dd if=/dev/mtd3 bs=64k' >part1.bak
ssh meraki@192.168.84.1 'dd if=/dev/mtd4 bs=64k' >part2.bak
ssh meraki@192.168.84.1 'dd if=/dev/mtd5 bs=64k' >redboot-config.bak
}}}
The most important is the Storage Partition. The part1 and part2 are scrambled (?) and copied to ram by the stage2 bootloader.
If you make changes to the storage partition that leave the device in an un-ssh'able state, you will need to restore the storage partition.

I was able to restore the stock Meraki flash from a bad flash by flashing in parts. Each flash takes <5 minutes:
This was done by:
telnet 192.168.84.1 9000 in the first 10 seconds after power-on
{{{
load -r -b 0x80150000 part1.bak
fis write -b 0x80150000 -l 0x1a0000 -f 0xa8150000
*reboot*
load -r -b 0x80150000 part1.bak
fis write -b 0x802f0000 -l 0x1a0000 -f 0xa82f0000
*reboot*
load -r -b 0x80150000 part2.bak
fis write -b 0x80150000 -l 0x1a0000 -f 0xa8490000
*reboot*
load -r -b 0x80150000 part2.bak
fis write -b 0x802f0000 -l 0x1a0000 -f 0xa8630000
*reboot*
load -r -b 0x80150000 stage2.bak
fis create 
stage2            0xA8030000  0x80100000  0x00020000  0x80100000
}}}
=== Restore Storage Parition ===
{{{
load -r -b 0x80050000 storage.bak
fis write -b 0x80050000 -l 0x100000 -f 0xa8050000
}}}

* I think this will take longer than 5 mins. You may need to be quick, or do it in parts
like part1.bak or part2.bak.

== The watchdog: meraki_watchdog and the ar2315_wdt (Hardware watchdog) ==
To run a vanilla OpenWrt without periodic reboots, it would seem that either the reset needs to be disabled, or an alternate watchdog needs to poke the right thing.
Use of the busybox 'watchdog' module may work, if the hardware watchdog is supported in the kernel. I believe the source to this device was released by Meraki and merged into the openwrt linux kernel source.
In the stock Meraki firmware, a process called 'meraki_watchdog' connects to /dev/watchdog and checks:

* device has enough memory (7*1024 in kB)
* /click filesystem is mounted 
* 'brain' process is running
* ping to 18.26.4.9 (or another IP) is successful
* if the device is upgrading

The brain process sends the wireless interfaces up and down and configured.
It starts the udhcpc client and hostapd daemons.

If the meraki_watchdog process is terminated, the hardware watchdog is not updated and the device hard reboots after 90 seconds.
If the brain or click is terminated, the watchdog software reboots it after 5 minutes.

The meraki_watchdog process can be terminated if "watchdog -t 30 /dev/watchdog" is called afterward.
This busybox module will update the hardware watchdog to prevent reboots.

After the meraki_watchdog process has been terminated the 'brain' terminated and click filesystem can be dismounted.

== Breaking in... ==
The stock firmware gives 2 entry points into the boot process. It looks for /storage/early-init.sh and /storage/late-init.sh
The early-init.sh is called just after the meraki_watchdog executes and before the brain/meraki specific processes are run.

I made a new file /storage/S80meraki:
{{{
ip route flush table main dev wired0
/sbin/udhcpc -i wired0 -f -p /var/run/wired0.pid -R >> /var/log/udhcpc.wired0.lo
ip route flush table main dev wired1
/sbin/udhcpc -i wired1 -f -p /var/run/wired1.pid -R >> /var/log/udhcpc.wired1.lo

if [ -f /storage/late-init.sh ]; then
    . /storage/late-init.sh
fi

if [ -d /storage/late-startup ]; then
    for i in /storage/late-startup/*; do
        [ -x $i ] && $i
    done
fi
}}}
I put this in /storage/early-init.sh:
{{{
#!/bin/sh
rm /etc/init.d/S80meraki
cp /storage/S80meraki /etc/init.d/S80meraki
}}}
I put this in /storage/late-init.sh
{{{
#!/bin/sh
killall meraki_watchdog
watchdog -t 30 /dev/watchdog
}}}

These files are on the storage partition and will be called as part of the usual startup. This will prevent the brain and click from being started, and terminate the meraki_watchdog. The busybox watchdog will keep the device alive (Tested for 8 hours+).

The device is now yours and will not dial home!
Am working on getting radio to work correctly now.
