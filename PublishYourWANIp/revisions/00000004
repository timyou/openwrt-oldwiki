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
