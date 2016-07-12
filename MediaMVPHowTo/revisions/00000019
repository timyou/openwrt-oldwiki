Hauppauge's '''MediaMVP''' provides music, video and photo display on a standard (PAL or NTSC) television monitor using a small $100 embedded Linux thin-client device.

While it uses IBM's 250MHz PowerPC core with hardware MPEG2 capability (the same processor series used by dream-multimedia-tv.de's boxen) it is a multimedia playback device only. It is not self-contained as it must use DHCP and TFTP to locate and retrieve its firmware from a network connection, much like a diskless workstation.

The stock Hauppauge firmware uses the device solely to display streaming video from a desktop PC. While third-party Linux firmware for this unit does not share a common codebase with projects such as OpenWRT and NSLU2-Linux, it does add key capabilities which allow this device to use an OpenWRT device as network-attached storage. Attached to NAS-capable units such as the Linksys WRTSL54GS, Asus WL-500g series or the Asus WL-700, it could replace a self-contained media player.

=== MediaMVP firmware ===
The MediaMVP device operates by obtaining boot information from a DHCP server, then downloading its firmware from the network using TFTP into 32Mb of onboard RAM. The firmware then retrieves sound and images from the network for display on the TV monitor.

The MediaMVP Media Centre ([http://www.mvpmc.org/index.php?pg=faq mvpmc.org]) is a third-party firmware media player for the Hauppauge MediaMVP. According to its authors, it is a total replacement for the Hauppauge software and can be booted onto the MediaMVP via tftp; mvpmc supports playing audio (mp3, ogg, wav, ac3) and video (mpeg1, mpeg2) from MythTV or ReplayTV digital video recorders. It can also play audio and video via HTTP, NFS, and CIFS and is capable of playing internet radio via !SlimServer or streaming MP3 (such as Shoutcast). It can also display images (jpg, bmp, png) via NFS and CIFS.

The mvpmc package is built on the nanowindows embedded platform from http://microwindows.org and is available under GPL at http://mvpmc.sourceforge.net with documentation [http://www.mvpmc.org/mvpmc-HOWTO-singlehtml.html here] and [http://mvpmc.wikispaces.com/howto_boot_OpenWRT here]. 

Network boot support for this device is provided by OpenWRT Kamikaze [https://dev.openwrt.org/browser/packages/net/mvprelay here].

The functions that the network server must provide to support this device are:
 * DHCP - issue an address to the device and (depending on model version) provide a pointer to the TFTP firmware download
 * TFTP - provide access to a downloadable firmware file (dongle.bin) and possibly device-specific configuration files
 * NFS or CIFS - provide access to the stored multimedia files to be displayed (as network-attached storage)

The MediaMVP device itself then retrieves the media, decompresses MPEG 1/2 in hardware and generates audio/video signals for the TV/monitor.

As nanowindows is intended to provide a subset of X-windows capability, it does follow the X-windows convention of allowing client and server to run on different network nodes. This could raise a possibility of this device becoming a user interface to graphical applications running elsewhere on a LAN. At one point, an attempt to port Mozilla 1.0 to Nano-X (as [http://nxzilla.sourceforge.net NxZilla]) had been made, but this effort appears to be abandoned.

=== Booting MediaMVP hardware from network ===
There are various versions of the MediaMVP for wired and wireless networks; these fall into two general categories:

The first units (no longer manufactured) were considered "non-flash" devices in that they only contained enough flash memory to boot from TFTP. Any application firmware, including the stock Hauppauge application itself, had to be retrieved from the network every time the unit was powered-up.

The current versions (revision H1 and subsequent, H2, H3, H4...) are "flash" devices that contain just enough flash memory to store the standard version of the application firmware. These may also be booted with third-party firmware from a network TFTP server, but there are differences in the boot procedure.

It is assumed that OpenWRT and network-attached storage (see UsbStorageHowto) are already configured before beginning MediaMVP installation.

A DHCP server (dnsmasq) is part of the standard OpenWRT configuration, and a TFTP server (atftpd or tftpd-hpa, latter is shown here) is installed using ipkg:
{{{
 ipkg install libwrap
 ipkg install tftpd-hpa
}}}

In all cases, a TFTP [http://mvpmc.wikispaces.com/bootsever boot server] must be available to serve the firmware (which should be renamed to dongle.bin) and any local [http://mvpmc.wikispaces.com/mvpmc.config configuration] files. Some MediaMVP versions also require a .ver file, which is extracted from the dongle.bin firmware using dd.

Note that the web interface and telnet to the device (username root, no password) is unavailable until the TFTP boot process has successfully completed.

==== Original ("non-flash") MediaMVP boot ====
This applies only to MediaMVP hardware revisions *before* H1. These devices have very little flash memory and must always boot from TFTP.

OpenWRT's default DHCP server is [http://www.nabble.com/Router-Setup-t4145166.html DNSmasq], which is documented more fully [http://www.thekelleys.org.uk/dnsmasq/docs/dnsmasq-man.html here].

In /etc/dnsmasq.conf, the location of the firmware (dongle.bin) and the address of an (optional) network time server need to be [http://forum.openwrt.org/viewtopic.php?pid=11988 specified]:
{{{
 # configure MediaMVP
 # time server (NTP):
  dhcp-option=42,192.43.244.18
 # TFTP/boot-from-LAN info:
  dhcp-boot=dongle.bin,OpenWrt,192.168.1.1
}}}

A static IP address may be assigned to the MediaMVP unit by adding its MAC address (printed on the underside of the unit) to /etc/ethers

The mvpmc firmware must be downloaded and placed in the TFTP server's root directory. For instance, if the firmware is in /opt/tftpboot/dongle.bin, invoke TFTPd from startup scripts using:
{{{
  tftpd-hpa -l -a 192.168.1.1 -c -s /opt/tftpboot
}}}

If the device cannot obtain the download from the default location, it will attempt (additionally) to use an alternate port (16869) for TFTP:
{{{
  tftpd-hpa -l -a 192.168.1.1:16869 -c -s /opt/tftpboot
}}}

==== Current ("flash") MediaMVP device boot ====
This applies to revisions H1 and subsequent. These have slightly more flash memory and the [http://mvpmc.wikispaces.com/H2+Linux+Boot+-+NEW boot sequence] differs from the original.

Instead of obtaining the location of the boot file through DHCP, these devices use DHCP for address assignment only. They expect an MVPrelay server to be present on port 16881 as a pointer to indicate where to look for the TFTP server. TFTP itself is then required to be available on port 16869 at the specified address.

On startup, add:
{{{
 tftpd-hpa -l -a 192.168.1.1:16869 -c -s /opt/tftpboot &
 mvprelay 16881 5906 6337 192.168.1.1 &
}}}

A .ver file needs to be created once, based on the dongle.bin file, using:
{{{
 dd if=/opt/tftpboot/dongle.bin of=/opt/tftpboot/dongle.bin.ver bs=1 count=40 skip=52
}}}

The [https://dev.openwrt.org/ticket/1262 MVPrelay] server is part of OpenWRT ([https://dev.openwrt.org/browser/packages/net/mvprelay Kamikaze] distributions only) and must be active in order to boot the newer MediaMVP's. The first parameter is the port on which [http://mvpmc.wikispaces.com/mvprelay mvprelay] is to listen; the last parameter is the network address of the TFTP server.

=== MediaMVP Configuration ===
The MediaMVP obtains its configuration from a file on the TFTP server; this file is named with the name of the firmware followed by ".config", so for dongle.bin  this would be dongle.bin.config. This configuration can be used to mount individual NFS or CIFS shares, set preferences or select skins/themes for display by the device.

On startup, tftpboot/dongle.bin.config is copied to /etc/dongle.config on the MediaMVP and executed as a startup/configuration script.

Example dongle.config files are [http://mvpmc.wikispaces.com/dongle.config here].

For instance, to mount an NFS share and launch the mvmpc application, create dongle.bin.config as:

{{{
# Setup time, date, hostname
TZ='EST+5EDT,M3.2.0/2,M11.1.0/2' ; export TZ
echo "TZ='EST+5EDT,M3.2.0/2,M11.1.0/2'; export TZ" > /etc/shell.config;
rdate -s 192.168.1.1
HNAME=`mvp` ; export HNAME

# Mount an NFS share from OpenWRT as network-attached media storage
mkdir /var/media;mount -t nfs -o nolock,tcp,rsize=4096,wsize=4096 192.168.1.1:/opt/ /var/media/

# Mount some Win2000 CIFS drives from a desktop PC
mkdir /var/c;mount.cifs //192.168.1.142/sea /var/c -o user=myself,pass=verysupersecret
mkdir /var/d;mount.cifs //192.168.1.142/dee /var/d -o user=myself,pass=verysupersecret

# Add additional options here to change user interface or configure streaming from Linux PC's/MythTV/ReplayTV and the like...

# Invoke mvpmc
mvpmc -f /etc/helvB18.pcf -o composite -S 0 -s 192.168.1.1 -b /data/livetv -p mythtv -u mythtv -y 192.168.1.1 -T mythconverg -r /var/myth -F /var/myth/cfgs/$HNAME.cfg &
}}}

----
CategoryHowTo
