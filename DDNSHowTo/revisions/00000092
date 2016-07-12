= DDNS howto =

[[TableOfContents]]

== About Dynamic DNS (DDNS) ==
The DDNS service comes in handy for establishing connections from computers on the Internet to your network at home. This is especially useful if you want to run server software or SSH on your !OpenWrt and only have a dynamic IP.

!OpenWrt uses the package {{{ddns-scripts}}} for providing DDNS service.

== Requirements ==
 * A recent !OpenWrt version. This howto was written for the 'Kamikaze 7.07' and later releases.
 * An account with a compatible DDNS service, currently
   * dyndns.org
    * changeip.com
    * zoneedit.com
    * no-ip.com
    * freedns.afraid.org
    * Any other that can update when some URL is accessed.  The script's quite versatile.

== Installation ==
Install the ddns-scripts package.
{{{
# use ipkg on older Kamikaze builds
opkg update
opkg install ddns-scripts
}}}

== Configuration ==
The configuration is stored in /etc/config/ddns.

In order to enable dynamic dns you need at least one section, and in that section the "enabled" option must be set to one

Each section represents an update to a different service

You specify your domain name, your username and your password with the options "domain", "username" and "password" respectively

Next you need to specify the name of the service you are connecting to "e.g. dyndns.org".  The format of the update URLsfor several different dynamic DNS services is specified in the /usr/lib/ddns/services file.  This list is hardly complete as there are many, many different dynamic DNS services.  If your service is on the list you can merely specify it with the "service_name" option.  Otherwise you will need to determine the format of the url to update with.  You can either add an entry to the /usr/lib/ddns/services file or specify this with the "update_url" option.

Currently the following services are

We also need to specify the source of the ip address to associate with your domain.  The "ip_source" option can be "network", "interface" or "web", with "network" as the default.

If "ip_source" is "network" you specify a network section in your /etc/network config file (e.g. "wan", which is the default) with the "ip_network" option.  If you specify "wan", you will update with whatever the ip for your wan is.

If "ip_source" is "interface" you specify a hardware interface (e.g. "eth1") and whatever the current ip of this interface is will be associated with the domain when an update is performed.

The last possibility is that "ip_source" is "web", which means that in order to obtain our ip address we will connect to a website, and the first valid ip address listed on that page will be assumed to be ours.  If you are behind another firewall this is the best option since none of the local networks or interfaces will have the external ip.  The website to connect to is specified by the "ip_url" option.  You may specify multiple urls in the option, separated by whitespace.

Finally we need to specify how often to check whether we need to check whether the ip address has changed (and if so update it) and how often we need to force an update ( many services will expire your domain if you don't connect and do an update every so often).  Use the "check_interval" to specify how often to check whether an update is necessary, and the "force_interval" option to specify how often to force an update.  Specify the units for these values with the "check_unit" and the "force_unit" options.  Units can be "days", "hours", "minutes" or "seconds".  The default force_unit is hours and the default check_unit is seconds.  The default check_interval is 600 seconds, or ten minutes.  The default force_interval is 72 hours or 3 days.

{{{
config service "myddns"
        option enabled          "0"

        option service_name     "dyndns.org"
        option domain           "mypersonaldomain.dyndns.org"
        option username         "myusername"
        option password         "mypassword"

        option ip_source        "network"
        option ip_network       "wan"


        option force_interval   "72"
        option force_unit       "hours"
        option check_interval   "10"
        option check_unit       "minutes"

        #option ip_source       "interface"
        #option ip_interface    "eth0.1"

        #option ip_source       "web"
        #option ip_url          "http://www.whatismyip.com/automation/n09230945.asp"

        #option update_url      "http://[USERNAME]:[PASSWORD]@members.dyndns.org/nic/update?hostname=[DOMAIN]&myip=[IP]"
}}}

== Trying it out ==
The script runs when hotplug events happen or a monitored IP address changes, so initially, you have to start it manually.  After setting "enabled" to 1, run the following:

{{{
sh
. /usr/lib/ddns/dynamic_dns_functions.sh # note the leading period
start_daemon_for_all_ddns_sections
exit
}}}

= Old methods =
DDNS scripts have been a surprisingly complicated part of OpenWrt.  There have been many other scripts and packages used.

  * ez-ipupdate (no longer maintained?)
  * [OpenWrtDocs/Kamikaze/UpdateDD updatedd] (no longer maintained?) Supports many other services
  * [http://forum.openwrt.org/viewtopic.php?pid=48762 JimWright's White Russian dyndns.org script] (probably based off a script mbm posted in the forum)
  * [http://forum.openwrt.org/viewtopic.php?id=14040 exobyte's Kamikaze dyndns.org script (based of JimWright's)]
    * ddns-scripts's dyndns.org support was [http://www.mail-archive.com/openwrt-devel@lists.openwrt.org/msg00922.html based off] this
