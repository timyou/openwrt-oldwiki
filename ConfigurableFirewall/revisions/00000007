With a ConfigurableFirewall package OpenWRTs configuration of the firewall could be be very flexible yet easy. A nice solution seems to be the FireHOL firewall builder scripts. (available at http://firehol.sourceforge.net and in debian)

The script takes a configuration like the following:

 * /etc/firehol/FireholConf

To ease automatic configuration when installing packages it was proposed to split zone policy into separate files:

 * /etc/firehol/RedZone
 * /etc/firehol/OrangeZone
 * /etc/firehol/BlueZone
 * /etc/firehol/GreenZone

The firewall rules are then build and activated during startup:

 * /etc/init.d/S45Firewall

The boot script executes the /sbin/firehol shell script which in turn sources /lib/firehol/firehol and the configuration files.

= Shorewall HowTo =

== Introduction ==

=== What is it? ===

[http://www.shorewall.net/ Shorewall] is a popular set of shell scripts used to ease configuration of an iptables based firewall, and also allow a more complex set of firewall rules to be managed easily.

=== Why? ===

The default firewall for openwrt is very basic and not as robust as some would like. Shorewall also configures some advanced functionalities (not all supported by openwrt) that are harder to do by hand. Another possible advantage is that automating shorewall configuration through a web interface is not very hard.

== Requirements ==

First we need to download shorewall. I downloaded the latest stable [http://www.shorewall.net/pub/shorewall/2.0/shorewall-2.0.9/shorwall-2.0.9.lrp (2.09) LRP package]. The LRP package is made for the [http://leaf.sourceforge.net/ Linux Embedded Appliance Firewall] project, and thus is particularly suited to the needs of OpenWRT. The LRP Package is in fact just a tar.gz tarball, and you can rename it as such.

== Installation ==
