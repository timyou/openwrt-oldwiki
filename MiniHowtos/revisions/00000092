[[TableOfContents]]


= Hardware =

== Dual-port serial modification ==

If you want to [:OpenWrtDocs/Customizing: add two serial ports] to your Gv2 or
GS, please see [http://www.rwhitby.net/wrt54gs/serial.html Rod Whitby's Dual Serial Port Mod]
for thorough details.  This will enable you to have a serial port intended as a
hardware serial console, as well as a serial port for a modem or other device.

(Note that Rod's instructions are for the version 3 PCB in the AD233BK kit. The version
3 PCB mislabelled Cts and Rts, putting them around the wrong way. The version 4 labelling
for the PCB is correct. Rod's instructions are correct for the version 3 PCB, but if you
have a version 4 PCB, you will have to reverse Cts and Rts for your second serial port to
work)

To get decent, usable performance out of the second serial port, you need to install the
setserial package and rebuild busybox to add the stty program. The following will get you
a second port at maximum speed:

{{{
setserial /dev/tts/1 port 0xB8000400 irq 3
stty -F /dev/tts/1 speed 115200
}}}

Note that both UART ports share one interrupt.

German People could also take a look at the page from
[http://hamburg.freifunk.net/twiki/bin/view/Technisches/WRT54gSerielleSchnittstelle freifunk hamburg].


== Single-port serial modification ==

If you're only interested in having serial console working on your G v2 or GS, check out
[http://jdc.parodius.com/wrt54g/serial.html koitsu's Single-Port Serial Modification] page.
This page includes links to online sites that sell the necessary hardware for both his and
Rod's modifications, as well as a (soon-to-be-written) walk-through of how to do the mod.
Pictures are also provided.


= Software =

This section should describe commonly-used packages, built-in !BusyBox tweaks, and things
of that nature.


== Setting up logging ==

syslogd is started on startup. You can read it with 'logread'

Syslog logging can be very useful when trying to find out why things don't work.  There are
two options for where to send the logging output: (1) to a local file stored in RAM, (2) to
a remote system.  The local file option is very easy but because it is stored in RAM it will
go away whenever the router reboots.  Using a remote system allows the output to be saved
for ever.

To run syslogd and klogd you should edit `/etc/inittab` and add the following two lines:{{{
::respawn:/sbin/syslogd -n
::respawn:/sbin/klogd -n
}}}

This tells `syslogd` to write the log file to `/var/log/messages`.  However, note that `/var`
is linked to `/tmp` but we need to create `/var/log` at boot time.  Do that by adding:
{{{
mkdir /var/log
}}}
to `/etc/init.d/rcS`.

If you want to log to a remote system, add `-R <hostname>` to the `syslogd` line in
`/etc/inittab`.  In this case you don't need to add the `mkdir /var/log` command to the
startup.  However, you will need to tell the remote system to listen for the log messages.
On my (Red Hat) Linux system that requires adding the `-r` flag to the syslogd startup
(which I did by editing `/etc/sysconfig/syslog`).  You may need to check the `man` page
for your host `syslogd` program.

If you want both local and remote logging, add `-L -R <hostname>` to the `syslogd` line
in `/etc/inittab`.
Update: the existing rcS file in whiterussian rc3 reads the nvram variable "log_ipaddr",
so remote logging gets activated by doing
{{{
nvram set log_ipaddr=<your syslogd ip>
nvram commit
}}}


= Networking =

== Alternative statistics solution ==

If you want statistics for multiple routers, with simple PHP interface, you can also try [http://pjf.dotgeek.org/downloads/openwrt/statswrt-0.1.tar.gz].
Another project with pretty much the same focus is OpenWRT-stats [http://sf.net/projects/openwrt-stats].
And RRDCollect [http://openwrt.brainabuse.de/rrdcollect/readme.html] will even produce
the status graphs on the WRT itself, without the need for a collecting host.


== OpenWrt + Chillispot solution ==

I put the links in here because many people asking for such a solution based on !OpenWrt.

''Share your internet access! This firmware turns any WLAN router with openwrt: Linksys
WRT54g/gs into a hotspot for free or fee. Easy web interface. No PC needed. Welcome page,
RADIUS/!NoCatsplash, can use server for reports,online voucher sales,monitoring.''

For details please see, [http://sourceforge.net/projects/hotspot-zone HOTSPOT-ZONE] and
[http://www.hot-spot-zone.de/hsz/ipkg/].

'''NOTE:''' On questions to this firmware project please contact the autor at
maurice.schoenmakers@hot-spot-zone.de, thanks.

Thanks to M (nick on IRC).


= Useful details =

[:EditingRomFiles] Howto edit the original files that are read-only in the ROM image

[:HowtoEnableCron] Enable cron to run scheduled tasks

[:PublishYourWANIp] Howto publish your WAN IP address to a webserver instead of using DynDNS


== boot_wait - What it is, and how it works ==

Information here was verified with a WRT54G 1.0.  There are minor changes with each
variable hardware revision (1.0 vs. 1.1 vs. 2.0 vs. GS), but the general principles
remain the same, as well as the final result.  To really understand `boot_wait`, you
need to understand the boot process on the WRT, and how ARP tables work.

When the boot loader begins (PMON on v1.x and CFE on v2.x), it starts by validating
the nvram data (configuration data that is stored at the end of flash).  If this data
is valid, it checks for the existence of the variable `boot_wait`.  If `boot_wait` is
set to `on` (`nvram set boot_wait=on`), the loader will go into a "boot_wait state".

The WRT will remain in this state for 3 seconds before proceeding with loading the kernel.
The next step of the bootstrap is to do a CRC check on the trx file stored in flash (trx
contains kernel and root file-system; bin file is trx with some extra headers).  If the
CRC check fails, the router falls back to the boot loader and stays there, waiting for a
new firmware.  If the CRC check passes, the router loads the kernel from flash and executes
it.

During the 3 second `boot_wait` state, or if the CRC fails, the loader will be accepting
Ethernet packets.  '''It does not contain a fully-working IP stack''', and is only looking
for 2 types of packets: ARP broadcasts and incoming TFTP attempts.

An ARP is an "Address Resolution Protocol" which converts an IP address into a mac address
(machine address / hardware address), used for basic ethernet communication. An ARP request
for 192.168.1.1 will return the mac address of the router. While in boot_wait, the router
will accept any packet with the correct mac address, regardless of IP address. In particular
in some situations on various networks, this is a bit problematic, because the ARP tables
are not updated correctly or there are old stale ARP entries laying around (on another switch,
or on the client PC; most layer-2 equipment does some form of ARP caching).  In this case,
you can bypass the ARP stage altogether and set a static ARP entry for an otherwise unused IP
on your LAN with the MAC address of the router.

If you TFTP put a valid firmware image during the 3-5 second window, the unit will accept
the file, and flash the file and proceed to boot -- which will then check the CRC. The
easiest way to send a file during boot is to just start the TFTP tranfer (binary mode)
to 192.168.1.1 during the 3-5 second window of opportunity.

The most common problem we hear about is folks under the mistaken impression that the TFTP
server requires a username and password to send a file during boot_wait state.  '''This
is FALSE.'''  There is a TFTP server enabled within the stock Linksys firmware; '''this is
not the same thing as `PMON` or `CFE`'''.  If you attempt to TFTP a firmware image to the
unit while the Linksys TFTP server is running, you'll receive an error message claiming
"incorrect password" or something of that nature.  If you see that error message, then you
missed the `boot_wait` window of opportunity or you didn't set `boot_wait` to on.  In this
case, you can still update the firmware via the Web-based "Firmware Upgrade" page.  Note
that without boot_wait set, recovery is tricker, so once you've upgraded it's highly
recommended that you do enable `boot_wait`.

If you have a v2 or GS unit, during the `CFE` phase, '''you will always be able to reach
the unit at IP 192.168.1.1'''.  If this doesn't work for you, you likely forgot to enable
`boot_wait`.

If you do end up with a 'dead' WRT unit due to not enabling `boot_wait`, there's still hope.
Please see [http://voidmain.is-a-geek.net:81/redhat/wrt54g_revival.html VoidMain's WRT54G Revival Page].


== CFE/PMON TFTP maximum image size limitation ==

There is a physical limit of approximately 3,141,632 bytes that `CFE/PMON` will accept
during the `boot_wait` stage.  Only 3,141,632 bytes will be flashed to the firmware. If
your firmware image is larger than this, the result will be undefined; the kernel may
load then either panic, or possibly the unit will reboot itself then proceed to spit
out `Boot program checksum is invalid` during `PMON`, and drop you to the `CFE>` prompt
(requiring serial console).

''If this hasn't been done already, this can be solved with an intermediate-stage rom
image that accepts a full-size image. This is like how LILO works'' -- Micksa


== Backing up the JFFS2 partition ==

{{{
mount /dev/mtdblock/4 /jffs
cd /jffs
tar jcvf /tmp/backup.tar.bz2 .
}}}

Then using nfs or dropbear's scp to copy /tmp/backup.tar.gz to a safe place.
