'''Some more notes on Kamikaze boot sequence'''

= Introduction =
There is very little documentation on the boot sequence of Kamikaze, so I'm leaving my notes here in case someone is interested.

= NOTES =
These notes are based on Kamikaze trunk svn as downloaded in August 2008

These are continuing notes from [:OpenWrtDocs/OpenWrtDocs/KamikazeBootHowTo:Kamikaze Boot Sequence Notes]

= Common Functions Scripts =
Since there are common functions used by many of the scripts in Kamikaze (not just for starting/shutdown/reboot), let's see what's there.

== /etc/functions.sh ==
This shell script is nothing more than a repository of common functions and variables that make shell scripting in Kamikaze easier. Here are the relevant parts of the script:

 * If $IPKG_INSTROOT is not defined AND /lib/config/uci.sh exists, include functions from /lib/config/uci.sh

=== Defined Variables ===
 * '''alias debug=${DEBUG:-:}'''
  * Allows the use of "$debug" as an option to "$DEBUG" for displaying debugging information. Defaults to ":".

 * '''N="\n"''' (\n used for example only)
  * Allows the use of "$N" for creating cross-compile use of the newline character. Some architectures use a different code for the newline character, so this allows you to output a newline regardless of the system.

 * '''_C=0'''
  * Used for internal state checks

 * '''NO_EXPORT=1'''
  * Defines whether helper scripts will export variables to children processes

 * '''LOAD_STATE=1'''

=== Defined Functions ===
 * '''append()'''  $1=VARIABLE $2=VALUE [optional $3=SEPARATOR]
 * '''config()''' $1=CONFIGTYPE $2=NAME
 * '''config_clear()''' $1=CONFIGSECTION
 * '''config_foreach()''' $1= $@
 * '''config_get()''' $1=CONFIGNAME $2=CONFIGSECTION [ optional $3=CONFIGOPTION ]
 * '''config_get_bool()''' $1= $2= $3= $4=
 * '''config_load()''' $@
 * '''config_rename()''' $1=OLDCONFIG $2=NEWCONFIG
 * '''config_set()''' $1= $2= $3=
 * '''config_unset()''' $1=CONFIG $2=OPTION
 * '''find_mtd_part()''' $1=
 * '''hotplug_dev()''' $1=ACTION $2=INTERFACE
 * '''include()''' $1=
 * '''jffs2_mark_erase()''' $1=
 * '''list_contains()''' $1=VARIABLE $2=STRING returns [ true | false ]
 * '''list_remove()''' $1=VARIABLE $2=STRING
 * '''load_modules()''' $*
 * '''option()''' $1=VARIABLENAME $2=VALUE
 * '''package()''' returns 0
 * '''reset_cb()'''
 * '''strtok()''' $1= $2= $* returns $COUNT
 * '''uci_apply_defaults()'''

== /lib/config/uci.sh ==
This script contains wrapper functions for making it easier to manipulate configuration files as used by UCI

=== Defined Variables ===
 * '''CONFIG_APPEND='''

=== Defined Functions ===
 * '''uci_add()''' $1=PACKAGE $2=TYPE $3=CONFIG
 * '''uci_commit()''' $1=PACKAGE
 * '''uci_load()''' $1=PACKAGE
 * '''uci_remove()''' $1=PACKAGE $2=CONFIG $3=OPTION
 * '''uci_rename()''' $1=PACKAGE $2=CONFIG $3=VALUE
 * '''uci_revert_state()''' $1=PACKAGE $2=CONFIG $3=OPTION
 * '''uci_set()''' $1=PACKAGE $2=CONFIG $3=OPTION $4=VALUE
 * '''uci_set_default()''' $1=PACKAGE
 * '''uci_set_state()''' $1=PACKAGE $2=CONFIG $3=OPTION $4=VALUE

== /etc/rc.common ==
This shell script is some common functions that are used for the startup/shutdown sequences.

 * Imports functions from /etc/functions.sh

 * Optionally, execute $1=INITSCRIPT $2=ACTION (start, stop, etc.)

 * Optionally, execute $EXTRA_COMMANDS

=== Placeholder Functions ===
In most cases, these functions used for boot scripts that don't have them defined due to not being needed.

For example, the /etc/init.d/umount boot script only needs to define the stop() function since it's only purpose is to cleanly unmount storage media before the system halts/reboots.

 * '''boot()'''
 * '''depends()'''
 * '''reload()'''
 * '''restart()'''
 * '''shutdown()'''
 * '''start()'''
 * '''stop()'''

=== Defined Functions ===

 * '''disable()'''
  * Removes the link[s] in /etc/rc.d for package $NAME in /etc/init.d
 * '''enable()'''
  * Creates the link[s] in /etc/rc.d for package $NAME in /etc/init.d
 * '''enabled()'''
  * Returns whether the $NAME link in /etc/rc.d is executable
 * '''help()'''
  * Shows list of possible function calls for an initialization script

= Boot Scripts =
The boot scripts follow the SysVInit style ( similar to RedHat(tm) ).

The script files are located in the /etc/init.d directory. The actual magic occurs via links to these scripts that are located under the /etc/rc.d directory.

Initialization scripts are executed at both power-up and shutdown. The main difference is when they are called and what options are passed to them.

== Design Of Boot Scripts ==

The boot script itself has a specific layout in order to work properly. The main requirements are:

 * Scripts will include the /etc/rc.common scripts for standard functions
 * Scripts will also, as needed, use the /etc/functions.sh for additional common functions
 * Startup scripts will include a "START" variable with the sequence number
 * Shutdown/reboot scripts will include a "STOP" variable with the sequence number
 * Scripts will define appropriate functions to call at invocation

== Boot Script Naming ==
A basic description of the startup/shutdown scripts directories are /etc/init.d contains the actual scripts, and /etc/rc.d contains a link to the file in /etc/init.d but the name includes either an "S" for "START", or "K" for "KILL", followed by a sequence number, then the rest of the script name.

The links and 'S##' and 'K##' portions of the link names in /etc/rc.d are autogenerated from variables contained in the scripts, so you should not have to do anything in the /etc/rc.d directory. This information is here for reference purposes only.

The format of the script name is "X##nnnn" where:

 * X = either "S" for "Start" or "K" for "Kill"
 * ## = a sequence number with a leading zero (0-9 will be named 00 through 09)
 * nnnn = the script name as found in /etc/init.d
For example - the real script /etc/init.d/network is the script that brings up/takes down network interfaces. The relevant startup link is /etc/rc.d/S40network and the shutdown link is /etc/rc.d/K40network.


=== /etc/init.d/network Script ===
For this example, I will use the /etc/init.d/network script since it is called at both power-up and shutdown/reboot.

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
