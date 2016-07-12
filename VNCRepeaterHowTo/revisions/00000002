'''VNC Repeater howto'''

[[TableOfContents]]
= Introduction =
I'm sure many of you are asking, "What is a VNC Repeater?" Well, say you have 2 computers in your house, and you want to be able to connect to both of them from the internet. You would have to forward 2 ports (not including the viewer applet which adds another port each) the default port for this is 5900. Well, what a VNC Repeater does, is you forward one port to it, and when it recieves a viewer connection, it then forwards the port to the appropriate vnc server. Thus, you can have many computers behind a NAT router and only have to forward one port.

Full documentation on the repeater is available at [http://ultravnc.sourceforge.net/addons/repeater.html ultravnc]

= Installation =
To install the repeater, simply type
{{{
ipkg install http://www.rit.edu/~reh5586/openwrt/packages/vncrepeater/vncrepeater_0.12-2_mipsel.ipk
}}}
You may want to check if a new version is available [http://www.rit.edu/~reh5586/openwrt/packages/vncrepeater/ here]

= Configuration =
Configuration is pretty straightforward, The file /etc/vncrepeater.conf is the config file. (please note that I know about the ^M charachters you see when editing the file in vim and I am working to fix it)

The config file is as follows:
{{{
[general]
;Ports
viewerport = 5800
serverport = 5900

;Listen Ip address (of repeater itself) in case your server happens to have several
;ip addresses (for example, one physical machine running several virtual
;machines each having their own ip address)
;default (0.0.0.0 = INADDR_ANY = uses all addresses) is the same that
;older repeater versions (before 0.12) did
;Notice ! This IS NOT address of server or viewer, but repeater itself !
listeneripaddress = 0.0.0.0

;How many sessions can we have active at the same time ?
;values can be [1...1000]
;Notice: If you actually *have* computer(s) capable
;of 1000 simultaneous sessions, you are probably a *very big company*,
;so please invite me to visit and admire your server(s) ;-)
maxsessions = 100

;If program is started as root (to allow binding ports below 1024),
;it changes to this user after ports have been bound in startup
;You need to create a suitable (normal, non-privileged) user/group and change name here
runasuser = root

;Allowed modes for repeater
;0=None, 1=Only Mode 1, 2=Only Mode 2, 3=Both modes
;Notice: If you set allowedmodes = 0, repeater will run without listening to any ports,
;it will just wait for your ctlr + c ;-)
allowedmodes = 2

;Logging level
;0 = Very little (fatal() messages, relaying done)
;1 = 0 + Important messages + Connections opened / closed
;2 = 1 + Ini values + exceptions in logic flow
;3 = 2 + Everything else (very detailed and exhaustive logging == BIG log files)
logginglevel = 1

[mode1]
;0=All
allowedmode1serverport = 0

;0=Allow connections to all server addressess,
;1=Require that server address (or range of addresses) is listed in
;srvListAllow[0]...srvListAllow[SERVERS_LIST_SIZE-1]
requirelistedserver = 0

;List of allowed server addresses / ranges
;Ranges can be defined by setting corresponding number to 0, e.g. 10.0.0.0 allows all addresses 10.x.x.x
;Address 255.255.255.255 (default) does not allow any connections
;Address 0.0.0.0 allows all connections
;Only IP addresses can be used here, not DNS names
;There can be max SERVERS_LIST_SIZE (default 50) srvListAllow lines
srvListAllow0 = 10.0.0.0        ;Allow network 10.x.x.x
srvListAllow1 = 192.168.0.0     ;Allow network 192.168.x.x

;List of denied server addresses / ranges
;Ranges can be defined by setting corresponding number to 0, e.g. 10.0.0.0 denies all addresses 10.x.x.x
;Address 255.255.255.255 (default) does not deny any connections
;Address 0.0.0.0 denies all connections
;Only IP addresses can be used here, not DNS names
;If addresss/range is both allowed and denied, it will be denied (deny is stronger)
;There can be max SERVERS_LIST_SIZE (default 50) srvListDeny lines
srvListDeny0 = 10.0.0.0         ;Deny network 10.x.x.x
srvListDeny1 = 192.168.2.22     ;Deny host 192.168.2.22

[mode2]
;0=Allow all IDs, 1=Allow only IDs listed in idList[0]...idList[ID_LIST_SIZE-1]
requirelistedid = 0

;List of allowed ID: numbers
;Value 0 means "this authenticates negatively"
;If value is not listed, default is 0
;Values should be between [1...LONG_MAX-1]
;There can be max ID_LIST_SIZE (default 100) idList lines
idlist0 = 1111
idlist1 = 2222
idlist2 = 0
idlist3 = 0
idlist4 = 0
idlist5 = 0
idlist6 = 0
idlist7 = 0
idlist8 = 0
idlist9 = 0
}}}

Everything is pretty straightforward, the one thing you may want to take note of are the lines:
viewerport = 5800
serverport = 5900
The viewerport is the port on the wan side which your viewer will connect to.
The serverport is the port on the lan side whuch the repeater will connect to the server on.

= Usage =
NOTE: This is INCOMPATIBLE with the Java based viewer. You MUST use a vnc viewer that supports proxy servers in order to use this repeater.

In order to use the repeater, (sa I said above) you're viewer must support a proxy server. A great viewer I suggest is the standalone viewer available from [http://ultravnc.sourceforge.net/ ultravnc]: Get it [http://prdownloads.sourceforge.net/ultravnc/UltraVnc-Viewer-101.zip?download here]. The proxy server will be configured to be your wan address (Dyndns is good for this) and the port the repeater is running on (ex. home.dyndns.org:5800). The server address is the LOCAL address of the computer you want to connect to (ex. 192.168.1.2).

That's it!

= Notes =

I hope you find the repeater useful, i decided to port it to the openwrt (MANY thanks to florian_ for helping to get it to compile) cuz i really needed it (i want to get rid of my server).
If you have any comments/suggestions, you can reach me at the [http://forum.openwrt.org/profile.php?id=4786 forum]
