Here we can put up a couple of MiniHOWTOs for Users.

= Hardware =
== Dual-port serial modification ==
If you want to add two serial ports to your Gv2 or GS, please see [http://www.rwhitby.net/wrt54gs/serial.html Rod Whitby's Dual Serial Port Mod] for thorough details.  This will enable you to have a serial port intended as a hardware serial console, as well as a serial port for a modem or other device.

== Single-port serial modification ==
If you're only interested in having serial console working on your Gv2 or GS, check out [http://jdc.parodius.com/wrt54g/serial.html koitsu's Single-Port Serial Modification] page.  This page includes links to online sites that sell the necessary hardware for both his and Rod's modifications, as well as a (soon-to-be-written) walk-through of how to do the mod.  Pictures are also provided.

= Software =
This section should describe commonly-used packages, built-in Busybox tweaks, and things of that nature.

== Making getty work with serial console ==
You have two (2) options: using `/sbin/getty` (recommended) or using `/bin/ash`.  `getty` is the recommended method (and the reason why is [http://codepoet.org/lists/busybox/2004-May/011705.html listed here], but it does not come included with stock OpenWRT at this time, therefore most people will probably want to use `/bin/ash` instead.

Remember that stock out-of-the-box OpenWRT points `/etc/inittab` to `/rom/etc/inittab`, which means it's on a read-only filesystem.  If you've never set up `/etc/inittab` for use before, do the following:

{{{
@OpenWrt:/# rm /etc/inittab
@OpenWrt:/# cp -p /rom/etc/inittab /etc/inittab
}}}

To use `/bin/ash`, add the following to `/etc/inittab`:

{{{
::askfirst:-/bin/ash --login
}}}

Then send a HUP signal to `init` (`kill -HUP 1`).

You should now have a working shell via serial console.

If you've rebuilt OpenWRT to support `/sbin/getty`, use this in `/etc/inittab` instead:

{{{
::askfirst:/sbin/getty -i -n -L console 115200
}}}

Don't forget the HUP.  :-)

== Setting up logging ==
Syslog logging can be very useful when trying to find out why things don't work.  There are two options for where to send the logging output: (1) to a local file stored in RAM, (2) to a remote system.  The local file option is very easy but because it is stored in RAM it will go away whenever the router reboots.  Using a remote system allows the output to be saved for ever.

To run syslogd and klogd you should edit `/etc/inittab` and add the following two lines:{{{
::respawn:/sbin/syslogd -n
::respawn:/sbin/klogd -n
}}}

This tells `syslogd` to write the log file to `/var/log/messages`.  However, note that `/var` is linked to `/tmp` but we need to create `/var/log` at boot time.  Do that by adding:{{{
mkdir /var/log
}}}
to `/etc/init.d/rcS`.

If you want to log to a remote system, add `-R <hostname>` to the `syslogd` line in `/etc/inittab`.  In this case you don't need to add the `mkdir /var/log` command to the startup.  However, you will need to tell the remote system to listen for the log messages.  On my (Red Hat) Linux system that requires adding the `-r` flag to the syslogd startup (which I did by editing `/etc/sysconfig/syslog`).  You may need to check the `man` page for your host `syslogd` program.

If you want both local and remote logging, add `-L -R <hostname>` to the `syslogd` line in `/etc/inittab`.

= Networking =
== Publishing system infos on a webpage ==
You want to publish system infos of your WRT54G on the web, like it's done at [http://rrust.com/sysinfo/rrdtool-graphs/openwrt-index.php]? 
Here's the howto:

=== Installing the scripts on the WRT54G ===
I did all of this using Nico's firmware here
[http://nthill.free.fr/nicowrt/firmware/]

It had all the openvpn stuff I needed, thnx Nico!
{{{
mkdir /etc/cron.5min
vi /etc/cron.5min/stats.sh
}}}
Paste in the following:
{{{
cat /proc/loadavg | awk '{ print $1":"$2":"$3 }' > /tmp/load
cat /proc/net/dev | grep tun1 | cut -d: -f2 | awk '{ print $1":"$9}' > /tmp/tun1
cat /proc/net/dev | grep vlan1 | cut -d: -f2 | awk '{ print $1":"$9}' > /tmp/eth
cat /proc/meminfo > /tmp/mem
df -k | grep /dev/mtdblock/4 | awk '{ print $3":"$4 }' > /tmp/flashdisk
}}}
Then do a
{{{
chmod 755 /etc/cron.5min/stats.sh
}}}
Go into you `/www` directory and
{{{
ln -s /tmp/flashdisk flashdisk
ln -s /tmp/load load
ln -s /tmp/mem mem
ln -s /tmp/tun1 tun1
}}}
If your rrdtool server is located on the outside, your lan you will need to edit your /etc/init.d/S45firewall to allow outside http access.

Install crond, set it up to exec `/etc/cron.5min/stats.sh` every 5 minutes.

That's it for the openwrt box, now onto the rrdtool server..

=== Installing the server-side stuff ===
Download [http://rrust.com/openwrt-stats.tar.gz]

Edit and copy the `rrdtoolgraphs.conf` to your `/etc`.

Edit `updates.sh` and `graphs.sh` for your paths.

Edit your crontab with
`*/5 * * * * root run-parts /etc/cron.5min > /dev/null 2>&1`

Finallay, get the cronjobs working:
{{{
cp updates.sh /etc/cron.5min
cp graphs.sh to /etc/cron.hourly 
}}}

= Useful details =
[:EditingRomFiles] Howto edit the original files that are read-only in the ROM image

[:HowtoEnableCron] Enable cron to run scheduled tasks

[:PublishYourWANIp] Howto publish your WAN IP address to a webserver instead of using DynDNS

== Build fails with "404 File Not Found" errors ==
Please see the [http://openwrt.ksilebo.net/Bugs OpenWRT Bugs Page] for further details and workarounds.

== boot_wait - What it is, and how it works ==
Information here was verified with a WRT54G 1.0.  There are minor changes with each variable hardware revision (1.0 vs. 1.1 vs. 2.0 vs. GS), but the general principles remain the same, as well as the final result.  To really understand `boot_wait`, you need to understand the boot process on the WRT, and how ARP tables work.

When the boot loader begins, it starts by validating the nvram data (configuration data that is stored in Flash).  If this data is valid, it checks for the existence of the variable `boot_wait`.  If `boot_wait` is set to `on` (`nvram set boot_wait=on`), the loader will go into a state that we call 'the boot wait state' on #wrt54g (IRC).  This state is also occasionally referred to as `PMON`.

The WRT will remain in this state for 3-5 seconds before proceeding with loading the kernel.  The next step of the bootstrap is to do a CRC check of the kernel and root file-system.  If the CRC check fails, the router falls back to `PMON` and stays there.  If the CRC check passes, the router loads the kernel from flash and executes it.

During the `boot_wait` state, the loader will be accepting Ethernet packets on eth0 (which is normally configured to be the 4 port switch).  '''It does not contain a fully-working IP stack''', and is only looking for 2 types of packets: ARP broadcasts and incoming TFTP attempts.

An ARP request addressed to the Ethernet broadcast will be replied to with an address of 192.168.1.1, and it's own Ethernet address in the packet.  A TFTP packet that has an Ethernet address corresponding to the router, will be accepted.  Under normal circumstances, if you TFTP put a valid firmware image during the 3-5 second window, the unit will accept the file, and once finished receiving it, will execute header and CRC checks on it.  If both pass, the firmware is written to Flash, and the unit is restarted.

The easiest way to send a file during boot is to just start the TFTP tranfer (binary mode) to 192.168.1.1 during the 3-5 second window of opportunity.  In particular in some situations on various networks, this is a bit problematic, because the ARP tables are not updated correctly or there are old stale ARP entries laying around (on another switch, or on the client PC; most layer-2 equipment does some form of ARP caching).  In this case, you can bypass the ARP stage altogether and set a static ARP entry for an otherwise unused IP on your LAN with the MAC address of the router.  Once you've added a static ARP entry for that MAC, you should be able to communicate with the WRT54G regardless of what IP it has.

The most common problem we hear about is folks under the mistaken impression that the TFTP server requires a username and password to send a file during boot_wait state.  '''This is FALSE.'''  There is a TFTP server enabled within the stock Linksys firmware; '''this is not the same thing as `PMON`'''.  If you attempt to TFTP a firmware image to the unit while it's TFTP server is running, you'll receive an error message claiming "incorrect password" or something of that nature.  If you see that error message, then you missed the `boot_wait` window of opportunity or you didn't set `boot_wait` to on.  In this case, you can still update the firmware via the Web-based "Firmware Upgrade" page.  Note that once you've upgraded, it's highly recommended that you do enable `boot_wait` anyways.

If you have a v2 or GS unit, during the `PMON` phase, '''you will always be able to reach the unit at IP 192.168.1.1'''.  If this doesn't work for you, you likely forgot to enable `boot_wait`.

If you do end up with a 'dead' WRT unit due to not enabling `boot_wait`, there's still hope.  Please see [http://voidmain.is-a-geek.net:81/redhat/wrt54g_revival.html VoidMain's WRT54G Revival Page].


'''Gentoo users''': The default tftp client doesn't seem to work, use the linksys-tftp ebuild instead

== CFE/PMON TFTP maximum image size limitation ==
There is a physical limit of approximately 3,141,632 bytes that `CFE/PMON` will accept during the `boot_wait` stage.  Only 3,141,632 bytes will be flashed to the firmware.  If your firmware image is larger than this, the result will be undefined; the kernel may load then either panic, or possibly the unit will reboot itself then proceed to spit out `Boot program checksum is invalid` during `PMON`, and drop you to the `CFE>` prompt (requiring serial console).

This was [http://www.sveasoft.com/modules/phpBB2/viewtopic.php?p=22112#22112 briefly touched on] over at the Sveasoft forums.
