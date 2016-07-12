Yes, I publish my WAN IP to my Webserver so I don't need DynDNS support in order to connect to my Router.

This HOWTO uses a PHP script on the webserver so you will have to have PHP support on your webserver in order to use this. Maybe somebody else can add how to do it on other servers.

Create the following shell script on your router:

{{{
# File: /usr/bin/checkmyip

#!/bin/sh
 
past_ip="first"
[ -f /tmp/myip ] && {
past_ip=`cat /tmp/myip`
}
current_ip=`ip -f inet addr | grep ppp0 | grep inet | grep -v grep | awk '{print $2;}'`
 
if [ ${past_ip} != ${current_ip} ] ; then
        exec wget -q -O /tmp/myip.html http://YOUR.SERVER.HERE/wrtg-ip.php?ip=${current_ip} 2>&1 &
        echo ${current_ip} > /tmp/myip
        rm /tmp/myip.html
fi
}}}

Replace YOUR.SERVER.HERE with with the domain name or ip of your webserver. And if you are not using pppoe you will have to change the "grep ppp0" to match the interface name you want the IP from.

You must make this file executable. (e.g. 'chmod 755 /usr/bin/checkmyip')

Now create the following php file (wrtg-ip.php) and place it on your webserver. Make sure the URL in the script above matches where you place this php file. You will also have to create a file called "current_ip" where the IP address can be written to by the user your webserver is running as. (Place it in the same directory as the php script and make it writable.)

{{{
# File: wrtg-ip.php

<?php
$current_ip = escapeshellcmd("$ip");
system("echo $current_ip > current_ip");
system("echo Changed on: `date` >> current_ip");
?>
}}}

Now you can run /usr/bin/checkmyip and see if it works. Now surf over to your webserver and open "current_ip" on it.
If it shows an IP address and a creation date then check out HowtoEnableCron to find out how you can automate this with cron.

Another way would be running the script within an ip-up script that gets called every time the WAN interface is brought up.


Here's a trivial script to update dyndns.org accounts. If you are using PPPoE, you may install this on your router and call from /etc/ppp/ip-up. You can also have it update on boot if your router is configured by DHCP, by running it from a script in /etc/init.d sometime after the network is configured. Finally, you might want to consider having it run from cron periodically since DynDNS.org kills free accounts if not updated frequently enough.

{{{
#!/bin/sh

LOGGING_TAG="dyndns-updater"
ACCOUNT=$(nvram get ddns_username)
PASS=$(nvram get ddns_passwd)
DOMAIN=$(nvram get ddns_hostname)
IFACE=ppp0
#EXAMPLES:
#DOMAIN="mysubdomain.is-a-geek.net"
#DOMAIN="mysubdomain.dyndns.org"

if [ "$ACCOUNT" = "" -o "$PASS" = "" -o "$DOMAIN" = "" ]; then
  logger -t ${LOGGING_TAG} -- "DynDNS Updatescript $0 is not properly configured!"
  echo "The DynDNS Updatescript $0 is not properly configured!"
  echo "To configure, set the following nvram variables:"
  echo "ddns_username:  DynDNS Username"
  echo "ddns_passwd:    DynDNS Password"
  echo "ddns_hostname:  DynDNS Hostname"
  echo ""
  echo "Example:"
  echo "nvram set ddns_username JoeSchmuh"
  echo "nvram set ddns_passwd SomethingSecret"
  echo "nvram set ddns_hostname JoeSchmuh.is-a-geek.net"
  echo "nvram commit"
  exit 4
fi

rm -f /tmp/dyndns.org-answer

#update the ip address ...
#first get current address
IP=$(ifconfig ${IFACE} | grep "inet addr" | awk '{print $2}' | awk -F ':' '{print $2}')

if [ "${IP}" = "" ]; then
  logger -t ${LOGGING_TAG} -- "Couldn't get ip address for ppp0."
fi

#now set address with wget (no ssl supported in busybox, so no https ...)
wget -q -O /tmp/dyndns.org-answer "http://$ACCOUNT:$PASS@members.dyndns.org/nic/update?system=dyndns&hostname=$DOMAIN&myip=${IP}&wildcard=ON&offline=NO"

if ! [ -f /tmp/dyndns.org-answer ]; then
  logger -t ${LOGGING_TAG} -- "Couldn't update ip-address for \"$ACCOUNT.dyndns.org\""
  logger -t ${LOGGING_TAG} -- "wget failed to download the file!"
  exit 2
fi

if [ "$(cat /tmp/dyndns.org-answer | awk '{printf("%s",$2);}')" != "${IP}" ]; then
  logger -t ${LOGGING_TAG} -- "Error while updating ip-address:"
  cat /tmp/dyndns.org-answer | logger -t ${LOGGING_TAG}
  rm -f /tmp/dyndns.org-answer
  exit 3
fi

rm -f /tmp/dyndns.org-answer

logger -t ${LOGGING_TAG} -- "IP address successfully updated to ${IP}"

exit 0
}}}


Using the very same NVRAM-saved settings as the inspirational script above, I remodeled the source to not rely on clumsy and awkward (no offense, mate! ;)) constructs abusing `grep` and `awk` in concatenations. I also implemented a trivial way of checking whether the account in questions needs to be updated with address data, so it's safe to run this every minute via cron. I chose to drop the error-message about lacking NVRAM entries for sake of brevity:

{{{#!/bin/sh
LOGGING_TAG="DYNDNS"
ACCOUNT=$(nvram get ddns_username)
PASS=$(nvram get ddns_passwd)
DOMAIN=$(nvram get ddns_hostname)
IFACE=ppp0

if [ "${ACCOUNT}" = "" -o "${PASS}" = "" -o "${DOMAIN}" = "" ]; then
  logger -t ${LOGGING_TAG} -- "DynDNS Updatescript $0 is not properly configured!"
  exit 4
fi

IP=$(ifconfig ${IFACE} | awk '/inet addr:/{ TMP=split($2,IP,":"); print IP[2]; }')

if [ $(nslookup ${DOMAIN} | awk '/^Address:/ && !/127.0.0.1$/ {print $2}') = "${IP}" ]; then
  #logger -t ${LOGGING_TAG} -- "No update for ${DOMAIN} needed."
  exit 0
fi

rm -f /tmp/dyndns.org-answer

if [ "${IP}" = "" ]; then
  logger -t ${LOGGING_TAG} -- "Couldn't get ip address for ${IFACE}."
  exit 1
fi

wget -q -O /tmp/dyndns.org-answer "http://${ACCOUNT}:${PASS}@members.dyndns.org/nic/update?system=dyndns&hostname=${DOMAIN}&myip=${IP}&wildcard=ON&offline=NO"

if ! [ -f /tmp/dyndns.org-answer ]; then
  logger -t ${LOGGING_TAG} -- "Couldn't update ip-address for \"${ACCOUNT}.dyndns.org\""
  exit 2
fi

if [ "awk '{printf("%s",$2);}') /tmp/dyndns.org-answer" != "${IP}" ]; then
  logger -t ${LOGGING_TAG} -- "Error while updating ip-address:"
  cat /tmp/dyndns.org-answer | logger -t ${LOGGING_TAG}
  rm -f /tmp/dyndns.org-answer
  exit 3
fi

rm -f /tmp/dyndns.org-answer

logger -t ${LOGGING_TAG} -- "IP address successfully updated to ${IP}"

exit 0
}}}
