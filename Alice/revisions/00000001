==What is Alice==
Alice is an Italian internet provider previously known as telecom italia...
==The problem==
The problem is that you receive a modem/router (alice gate) that by default act like a router...and OpenWrt doesn't run on it...and you want your openwrt router to be directly connected to the internet so you can provides services such as openssh,openvpn or open ports for p2p or msn,ekiga
==The Setup of the internet==
as i never succeeded to use the wifi we will connect trough the cable
so:
1. connect trough an ethernet cable
2. go to a website and you will be redirected to a page telling you to register for a mail
3. i used don't accept as there told you that there are adds inside your mailbox if you accepted and at the end it worked
4. restart the alice gate pressing the red button on the alice gate...and do it again until you have the internet...


== The transformation of the router in modem ==
1.open your browser to http://192.168.1.1


== OpenWrt's setup ==
1. connect your openwrt router to the alice-gate with a normal(non cross) ethernet cable
2. modify the wan configuration inside /etc/config/network:
 #### WAN configuration
 config interface        wan
         option ifname   "eth0.1"
         option proto    pppoe
         option username "username"
         option password "password"
----
CategoryHowTo
