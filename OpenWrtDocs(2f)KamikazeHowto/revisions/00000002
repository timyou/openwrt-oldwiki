[[TableOfContents]]

= Hardware =
== Dual-port serial modification ==
If you want to [:OpenWrtDocs/Customizing:add two serial ports] to your Gv2 or GS, please see [http://www.rwhitby.net/wrt54gs/serial.html Rod Whitby's Dual Serial Port Mod] for thorough details.  This will enable you to have a serial port intended as a hardware serial console, as well as a serial port for a modem or other device.

(Note that Rod's instructions are for the version 3 PCB in the AD233BK kit. The version 3 PCB mislabelled Cts and Rts, putting them around the wrong way. The version 4 labelling for the PCB is correct. Rod's instructions are correct for the version 3 PCB, but if you have a version 4 PCB, you will have to reverse Cts and Rts for your second serial port to work)

To get decent, usable performance out of the second serial port, you need to install the setserial package and rebuild busybox to add the stty program. The following will get you a second port at maximum speed:

{{{
setserial /dev/tts/1 port 0xB8000400 irq 3
stty -F /dev/tts/1 speed 115200
}}}
Note that both UART ports share one interrupt.

German People could also take a look at the page from [https://snr.freifunk.net/trac/freifunk freifunk hamburg].

== Single-port serial modification ==
If you're only interested in having serial console working on your G v2 or GS, check out [http://jdc.parodius.com/wrt54g/serial.html koitsu's Single-Port Serial Modification] page. This page includes links to online sites that sell the necessary hardware for both his and Rod's modifications, as well as a (soon-to-be-written) walk-through of how to do the mod. Pictures are also provided.

If you don't feel confident about your Dremel skills, consider using the [http://www.compsys1.com/workbench/On_top_of_the_Bench/Max233_Adapter/max233_adapter.html STR232] adapter, which only requires drilling a single hole in the case. It brings out the basic RS-232 signals to a 1/8" (3.5mm) stereo jack, and you then use an adapter cord to connect to your favorite connector.

= Software =
This section should describe commonly-used packages, built-in !BusyBox tweaks, and things of that nature.

== Setting up logging ==
syslogd is started on startup. You can read it with 'logread'

Syslog logging can be very useful when trying to find out why things don't work.  There are two options for where to send the logging output: (1) to a local file stored in RAM, (2) to a remote system.  The local file option is very easy but because it is stored in RAM it will go away whenever the router reboots.  Using a remote system allows the output to be saved for ever.

Update: the existing rcS file in whiterussian rc3 (and newer) reads the nvram variable "log_ipaddr", so remote logging gets activated by simply doing

{{{
nvram set log_ipaddr=<your syslogd ip>
nvram commit
}}}
To run syslogd and klogd you should edit {{{/etc/inittab}}} and add the following two lines:

{{{
::respawn:/sbin/syslogd -n
::respawn:/sbin/klogd -n
}}}
This tells {{{syslogd}}} to write the log file to {{{/var/log/messages}}}.  However, note that {{{/var}}} is linked to {{{/tmp}}} but we may need to create {{{/var/log}}} at boot time if it is not already automatically created.  Do that by adding:

{{{
mkdir /var/log
}}}
to {{{/etc/init.d/rcS}}}.

If you want to log to a remote system, add {{{-R <hostname>}}} to the {{{syslogd}}} line in {{{/etc/inittab}}}.  In this case you don't need to add the {{{mkdir /var/log}}} command to the startup.  However, you will need to tell the remote system to listen for the log messages. On my (Red Hat) Linux system that requires adding the {{{-r}}} flag to the syslogd startup (which I did by editing {{{/etc/sysconfig/syslog}}}). Also, on my (Red Hat) Linux system the log messages received from the remote system appear in {{{/var/log/messages}}} interspersed with the local messages.  You may need to check the {{{man}}} page for your host {{{syslogd}}} program.

Expect the log messages to arrive through UDP port 514.

If you want both local and remote logging, add {{{-L -R <hostname>}}} to the {{{syslogd}}} line in {{{/etc/inittab}}}.

== Saving a few kB in flash (ipkg package lists in /tmp) ==
Every byte stored in the flash filesystem is expensive. Migrate ipkg lists to /tmp:

 * add {{{mkdir -p /tmp/ipkg/lists}}} to the {{{start}}} section in {{{/etc/init.d/boot}}}
 * {{{mkdir -p /tmp/ipkg/lists}}}
 * {{{cd /usr/lib/ipkg}}}
 * {{{rm -r lists}}}
 * {{{ln -s /tmp/ipkg/lists}}}
 * {{{ipkg update}}}
 * {{{df}}}
 * have fun, ipkg is now faster and you gained some 100KiB free space in jffs2 (depending on your configured ipkg sources)
= Software =
== Networking ==
=== OpenWrt + Chillispot solution ===
I put the links in here because many people asking for such a solution based on !OpenWrt.

''Share your internet access! This firmware turns any WLAN router with openwrt: Linksys WRT54g/gs into a hotspot for free or fee. Easy web interface. No PC needed. Welcome page, RADIUS/!NoCatsplash, can use server for reports,online voucher sales,monitoring.''

For details please see, [http://sourceforge.net/projects/hotspot-zone HOTSPOT-ZONE] and http://www.hot-spot-zone.de/hsz/ipkg/.

'''NOTE:''' On questions to this firmware project please contact the autor at maurice.schoenmakers@hot-spot-zone.de , thanks.

Thanks to M (nick on IRC).

=== Quick info about your connection ===
Followed are a couple of scripts that are useful when writing other scripts.  They help you determine your ip, gateway and gateway mac.  With a little modification, they can be adapted to do other stuff

Putting this script in /usr/bin/whatismyip will allow you to check your ip just by typing "whatismyip {interface}"

{{{
#!/bin/sh
ifconfig $1 | awk '/inet addr/ {printf "%s\n", substr($2,6)}'
}}}
If you want to lock the thing to only check a certain interface, replace the $1 with the interface name.  I do it this way because I can easily find out my ip in scripts by typing {{{whatismyip vlan1}}} rather than hoping I remembered the sequence right.

If you want to find out what your default gateway is, put this info into a script at /usr/bin/whatismygw

{{{
#!/bin/sh
netstat -rn | awk '/^0\.0\.0\.0/ {print $2}'
}}}
and then you can call the script from another script by typing {{{whatismygw}}}.

finally, if you want the mac address of your wan gateway (your cable modem or the like) put this info into a script at /usr/bin/whatismygwmac

{{{
#!/bin/sh
arping -fq -I vlan1 `whatismygw`
cat /proc/net/arp | grep `whatismygw` | awk '{print $4}'
}}}
you can see where the whatismygw script is called inside this other script.  In the arping line, -f means stop after first response and -q means quiet (so that the only thing returned by the script is the mac address).  -I is the interface you are choosing to ping out on.  You actually don't have to set the interface but if you don't set an interface, it can take a good 30 seconds for this script to work and you have to put a sleep inbetween line 3 and 5.

Hopefully you know to chmod the scripts so they are executable, but if not the command looks like this:

{{{
chmod a+x {thescriptname}
}}}
You don't have to give them the names that I did, nor do you have to put them in /usr/bin/ to work - that is just the way I did it.  Please edit this if you see errors related to my ability to form coherant sentences or if you know a better way to do this.

== =Simplified Firewall === There is a modified version of /etc/firewall.user in SimpleFirewall.

=== Wake-On-LAN (WOL) ===
 . http://wiki.openwrt.org/Wake-On-LAN
=== IPSec pass-through ===
The stock wrt54gl router software has the ability to perform ipsec pass-through.  This is useful if you are running a VPN client behind your NATed wrt54gl router.  By default, the openwrt install does not provide ipsec passthrough.  If you need this feature, add the following rules to the bottom of your /etc/firewall.user file:

{{{
iptables -t nat -A postrouting_rule -p 50 -j ACCEPT
iptables -t nat -A postrouting_rule -p 51 -j ACCEPT
}}}
This will enable ipsec pass-through.  Protocol 50 is ESP and protocol 51 is AH.

NOTE: 2007-03-01: These two postrouting rules actually broke IPSEC-ESP for us. jschnip

=== Monitoring signal strengths of nearby access points in client mode ===
You can use scripts to monitor the nearby access points in a readable ascii format like below:

{{{
Date: Sun Jan 16 08:31:06 UTC 2000
Channel Signal  Noise  SNR      ESSID
------- ------  -----  ---      ------------------
 1      -67     -90     23      Default
 11     -45     -78     33      Linksys
}}}
Note that ''SNR'' is calculated by subtracting ''Signal'' from ''Noise''.

'''Requirements''':

 * {{{microperl}}} needs to be installed
 * WRT should be running in the client-mode
'''Steps''':

 * Create {{{monitor.pl}}} file under {{{/sbin}}}. Contents are as follows:
 {{{
open(INP, '-') or die "Couldn't read from STD input!\n";
my $line = ""; my $essid = ""; my $channel = "";
my $signal = ""; my $noise = ""; my $snr = "";
print "Channel Signal  Noise  SNR\tESSID\n";
print "------- ------  -----  ---\t------------------\n";
while ($line = <INP>) {
   if ($line =~ m/ESSID:"(.*)"/) {
      $essid = $1;
   }
   elsif ($line =~ m/Channel:(\d+)/) {
      $channel = $1;
   }
   elsif ($line =~ m/Quality.*Signal level:-(\d+) .*Noise level:-(\d+)/) {
      $signal = $1;
      $noise = $2;
      $snr = $2 - $1;
      print " $channel\t-$signal\t-$noise\t$snr\t$essid\n";
   }
}
}}}
 * create {{{wstat.sh}}} under {{{/sbin}}}:
 {{{
#!/bin/sh
echo -n "Date: "; date
iwlist eth1 scanning | microperl /sbin/monitor.pl
}}}
 * Make both of them executable, i.e. {{{chmod 755 <filename>}}}
'''Usage''':

 * Run the script by calling {{{wstat.sh}}}
==== Ash alternative ====
You may also run this shell (ash) script which relies on the [http://downloads.openwrt.org/whiterussian/packages/non-free/ non-free wl package]:

{{{
#!/bin/sh (-)
wl scan 2> /dev/null
if [ "watch" = "$1" ]; then
        clear
        date
        echo
else
        sleep 1
fi
wl scanresults | \
sed 's/Ad Hoc/AdHoc/;s/"//g' | \
awk '
/^SSID/ { SSID=$0 };
/^Mode/ { SIG=$4; NOISE=$7; CHAN=$10 };
/WEP/ { SSID=SSID "*" };
/AdHoc/ { SSID=SSID "%" };
/^BSSID/ { printf "%- 22s Sig/Noise: %4d/%- 4d (%3d) Chan: %d\n",
 SSID, SIG, NOISE, -1*(NOISE-SIG), CHAN}' | \
sort
if [ "watch" = "$1" ]; then
        sleep 7
        exec $0 watch
fi}}}
=== Disabling telnet ===
Telnet is enabled by default.  On Kamikaze (at least), ssh is also provided by default, through Dropbear.  You may want to disable Telnet for better security.

To stop the telnet daemon, run {{{/etc/init.d/telnet stop}}}.  To disable it at boot, run {{{/etc/init.d/telnet disable}}}.

=== Using Go6.net for IPv6 ===
This section describe how to setup IPv6 using the [[http://go6.net/ | Go6.net]] service.

 1. Sign up for a free account with Go6.
 1. Setup your router for IPv6.
  1. Install the following packages: kmod-ipv6, kmod-tun, ip, libpthread, radvd.
  1. Install the Gateway6 client v5 from here: http://www.roadrunner.cx/openwrt/gw6c_4.2.2_mipsel.ipk
 1. Configure the Gateway6 Client. The config file is located at /etc/gw6c/
  1. Change userid and passwd to your username and password.
  1. Change server to broker.freenet6.net
  1. Change host_type to one of the following:
   1. router if you want to use IPv6 on your whole network.
   1. host if you want to use IPv6 just on your router.
  1. You should not have to mess with any other settings.
 1. Start the Gateway6 Client.
  1. Start immediately with /etc/init.d/gw6c start
  1. Reboot your router
 1. Check syslog for errors.
Most of this information came from [http://forum.openwrt.org/profile.php?id=524 jake1981] at the OpenWRT forums from this post:

http://forum.openwrt.org/profile.php?id=524

=== Samba ===
[:OpenWrtDocs/SambaHowto:Samba]

== Useful Details ==
=== boot_wait - What it is, and how it works ===
Information here was verified with a WRT54G 1.0.  There are minor changes with each variable hardware revision (1.0 vs. 1.1 vs. 2.0 vs. GS), but the general principles remain the same, as well as the final result.  To really understand {{{boot_wait}}}, you need to understand the boot process on the WRT, and how ARP tables work.

When the boot loader begins (PMON on v1.x and CFE on v2.x), it starts by validating the nvram data (configuration data that is stored at the end of flash).  If this data is valid, it checks for the existence of the variable {{{boot_wait}}}.  If {{{boot_wait}}} is set to {{{on}}} ({{{nvram set boot_wait=on}}}), the loader will go into a "boot_wait state".

The WRT will remain in this state for 3 seconds before proceeding with loading the kernel. The next step of the bootstrap is to do a CRC check on the trx file stored in flash (trx contains kernel and root file-system; bin file is trx with some extra headers).  If the CRC check fails, the router falls back to the boot loader and stays there, waiting for a new firmware.  If the CRC check passes, the router loads the kernel from flash and executes it.

During the 3 second {{{boot_wait}}} state, or if the CRC fails, the loader will be accepting Ethernet packets.  '''It does not contain a fully-working IP stack''', and is only looking for 2 types of packets: ARP broadcasts and incoming TFTP attempts.

An ARP is an "Address Resolution Protocol" which converts an IP address into a mac address (machine address / hardware address), used for basic ethernet communication. An ARP request for 192.168.1.1 will return the mac address of the router. While in boot_wait, the router will accept any packet with the correct mac address, regardless of IP address. In particular in some situations on various networks, this is a bit problematic, because the ARP tables are not updated correctly or there are old stale ARP entries laying around (on another switch, or on the client PC; most layer-2 equipment does some form of ARP caching).  In this case, you can bypass the ARP stage altogether and set a static ARP entry for an otherwise unused IP on your LAN with the MAC address of the router.

If you TFTP put a valid firmware image during the 3-5 second window, the unit will accept the file, and flash the file and proceed to boot -- which will then check the CRC. The easiest way to send a file during boot is to just start the TFTP tranfer (binary mode) to 192.168.1.1 during the 3-5 second window of opportunity.

The most common problem we hear about is folks under the mistaken impression that the TFTP server requires a username and password to send a file during boot_wait state.  '''This is FALSE.'''  There is a TFTP server enabled within the stock Linksys firmware; '''this is not the same thing as {{{PMON}}} or {{{CFE}}}'''.  If you attempt to TFTP a firmware image to the unit while the Linksys TFTP server is running, you'll receive an error message claiming "incorrect password" or something of that nature.  If you see that error message, then you missed the {{{boot_wait}}} window of opportunity or you didn't set {{{boot_wait}}} to on.  In this case, you can still update the firmware via the Web-based "Firmware Upgrade" page.  Note that without boot_wait set, recovery is tricker, so once you've upgraded it's highly recommended that you do enable {{{boot_wait}}}.

If you have a v2 or GS unit, during the {{{CFE}}} phase, '''you will always be able to reach the unit at IP 192.168.1.1'''.  If this doesn't work for you, you likely forgot to enable {{{boot_wait}}}.

If you do end up with a 'dead' WRT unit due to not enabling {{{boot_wait}}}, there's still hope. Please see [http://voidmain.is-a-geek.net:81/redhat/wrt54g_revival.html VoidMain's WRT54G Revival Page].

=== CFE/PMON TFTP maximum image size limitation ===
There is a physical limit of approximately 3,141,632 bytes that {{{CFE/PMON}}} will accept during the {{{boot_wait}}} stage.  Only 3,141,632 bytes will be flashed to the firmware. If your firmware image is larger than this, the result will be undefined; the kernel may load then either panic, or possibly the unit will reboot itself then proceed to spit out {{{Boot program checksum is invalid}}} during {{{PMON}}}, and drop you to the {{{CFE>}}} prompt (requiring serial console).

''If this hasn't been done already, this can be solved with an intermediate-stage rom image that accepts a full-size image. This is like how LILO works'' -- Micksa

=== Backing up the JFFS2 partition ===
{{{
mount /dev/mtdblock/4 /jffs
cd /jffs
tar jcvf /tmp/backup.tar.bz2 .
}}}
Then using nfs or dropbear's scp to copy /tmp/backup.tar.gz to a safe place.

=== Using the buttons to control your router ===
For White Russian RC5 and earlier.

 * Reboot your router with the reset button on the back.
 * Switch your WiFi ON and OFF by pressing the Cisco SES (Secure Easy Setup) button (if your router has one).
 * Orange Cisco LED acknowledges the button-press event.
Put this in /etc/init.d/S70buttons:

{{{
#!/bin/sh
while : ; do
  sleep 1
  # Reset button
  if [ $(cat /proc/sys/reset) = "1" ]; then
    logger "Rebooting (Reset button)"
    LEDSTATUS=$(cat /proc/sys/diag)
    LEDSTATUS=$((LEDSTATUS | 0x10))  # Orange Cisco LED ON
    echo $LEDSTATUS > /proc/sys/diag
    reboot
  fi
  # Cisco button
  if [ "$(cat /proc/sys/button)" = "1" ]; then
    LEDSTATUS=$(cat /proc/sys/diag)
    if [ "$(nvram get wl0_radio)" = "0" ]; then
      logger -t wifi "Activating wi-fi (Cisco button)"
      LEDSTATUS=$((LEDSTATUS | 0x10))  # Orange Cisco LED ON
      echo $LEDSTATUS > /proc/sys/diag
      nvram set wl0_radio=1
      wifi
    else
      logger -t wifi "Deactivating wi-fi (Cisco button)"
      LEDSTATUS=$((LEDSTATUS | 0x10))  # Orange Cisco LED ON
      echo $LEDSTATUS > /proc/sys/diag
      nvram set wl0_radio=0
      wifi
    fi
    sleep 3  # just to be safe
    #LEDSTATUS=$(cat /proc/sys/diag)
    LEDSTATUS=$((LEDSTATUS & ~0x14))  # Power LED Flashing OFF (wl module issues?) & Orange Cisco LED OFF
    echo $LEDSTATUS > /proc/sys/diag
  fi
done &
}}}
Modify the script for your needs and don't forget to '''chmod a+x''' it.

See also: ["wrtLEDCodes"] and http://forum.openwrt.org/viewtopic.php?id=5286

For RC6 the whole shebang is changed; instead you put shell scripts in /etc/hotplug.d/button, and the LEDs are controlled by separate files in /proc/diag/led.  See http://forum.openwrt.org/viewtopic.php?id=8745 for details and http://forum.openwrt.org/viewtopic.php?id=8151 for an updated script (which I haven't tested).
