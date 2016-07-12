'''Some more notes on Kamikaze boot sequence'''

= Introduction =
There is very little documentation on the boot sequence of Kamikaze, so I'm leaving my notes here in case someone is interested.

= NOTES =
These notes are based on Kamikaze trunk svn as downloaded in August 2008

These are continuing notes from [:OpenWrtDocs/OpenWrtDocs/KamikazeBootHowTo:Kamikaze Boot Sequence Notes]

= Common Functions =
Since there are common functions used by many of the scripts in Kamikaze (not just for starting/shutdown/reboot), let's see what's there.

== /etc/functions.sh ==
This shell script is nothing more than a repository of common functions that make shell scripting in Kamikaze easier. Here are the relevant parts of the script:

 * 
= Boot Scripts =
The boot scripts follow the SysVInit style ( similar to RedHat(tm) ).

The actual scripts are located in the /etc/init.d directory. The actual magic occurs via links to these scripts that are located under the /etc/rc.d directory.

== Boot Script Names ==
Initialization scripts are executed at both power-up and shutdown. The main difference is when they are called and what options are passed to them.

The boot script itself has a specific layout in order to work properly. The main requirements are:

 * Scripts will include the /etc/rc.common scripts for standard functions
 * Scripts will also, as needed, use the /etc/functions.sh for additional common functions
 * Startup scripts will include a "START" variable with the sequence number
 * Shutdown/reboot scripts will include a "STOP" variable with the sequence number
 * Scripts will define appropriate functions to call at invocation

For this example, I will use the /etc/init.d/network script since it is called at both power-up and shutdown/reboot.

=== /etc/init.d/network Script ===

{{{
1.  #!/bin/sh /etc/rc.common
2.  # Copyright (C) 2006 OpenWrt.org
3. 
4.  START=40
5.  STOP=40
6. 
7.  boot() {
8.      setup_switch() { return 0; }
9.
10.     include /lib/network
11.     setup_switch
12.     [ -s /etc/config/wireless ] || \
13.          /sbin/wifi detect > /etc/config/wireless
14.     /sbin/wifi up
15. }
16.
17. start() {
18.      ifup -a
19.      /sbin/wifi up
20. }
21.
22. restart() {
23.      setup_switch() { return 0; }
24.
25.      include /lib/network
26.      setup_switch
27.      ifup -a
28.      /sbin/wifi up
29. }
30.
31. stop() {
32.      ifdown -a
33. }
34.
}}}
----
CategoryHowTo
