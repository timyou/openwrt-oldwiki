With a ConfigurableFirewall package OpenWRTs configuration of the firewall could be be very flexible yet easy. A good option seem to be the FireHOL firewall builder scripts. (http://firehol.sourceforge.net)

The scripts take a configuration like the following:

 * /etc/firehol/FireholConf

To ease automatic configuration when installing packages it was proposed to split zone policy into separate files:

 * /etc/firehol/RedZone
 * /etc/firehol/OrangeZone
 * /etc/firehol/BlueZone
 * /etc/firehol/GreenZone

The firewall rules are then build and activated during startup:

 * /etc/init.d/S45Firewall
