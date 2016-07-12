= 24XLGi =
The OSBRiDGE 24XLGi is a router used for long wireless links

== Hardware ==
The 24XLGi uses a Realtek RTL8186 SoC

{{{
SoC: RTL8186
CPU: R3000 V0.0
Switch: RTL8305SC
Ram: 16 MB (2x8MB)
Wireless:
}}}
== Photo ==
Here there is a photo of the board: http://img388.imageshack.us/img388/8409/osbridgecb5.jpg

== Serial ==
There are 6 pins on boards, but nobody has figured out how to attach a serial on the board

== Hacking ==
That's a long story, if you are curious read this: http://teknoraver.net/software/osbridge_hacking/

I managed to inject commands to the webif using this tool I wrote: [http://teknoraver.net/software/osbridge_hacking/inject.pl.txt inject.pl]

{{{
$ inject.pl cat /proc/cpuinfo
[~] cat /proc/cpuinfo
system type             : Philips Nino
cpu model               : R3000 V0.0
wait instruction        : no
microsecond timers      : no
extra interrupt vector  : no
hardware watchpoint     : no
VCED exceptions         : not available
VCEI exceptions         : not available
ll emulations           : 0
sc emulations           : 0
$ inject.pl uname -a
[~] uname -a
Linux (none) 2.4.18-MIPS-01.00 #653 �ro maj 23 11:38:56 CEST 2007 mips unknown
$ inject.pl cat /proc/modules
[~] cat /proc/modules
defos-driver            4600   0
$ inject.pl ps
[~] ps
  PID  Uid     VmSize Stat Command
    1 root        288 S   init
    2 root            SW  [keventd]
    3 root            SWN [ksoftirqd_CPU0]
    4 root            SW  [kswapd]
    5 root            SW  [bdflush]
    6 root            SW  [kupdated]
    7 root            SW  [mtdblockd]
    9 root        392 S   -sh
   40 root        304 S   mini_httpd -d /web -c cgi-bin/* -p 80 -u root
  140 root        204 S   osd -wd 0 -t 600 -ip 0.0.0.0 -hw 5 -wm 1
  141 root        212 S   osd -wd 0 -t 600 -ip 0.0.0.0 -hw 5 -wm 1
  142 root        176 S   osd -wd 0 -t 600 -ip 0.0.0.0 -hw 5 -wm 1
  143 root        200 S   osd -wd 0 -t 600 -ip 0.0.0.0 -hw 5 -wm 1
  145 root        168 S   osd -wd 0 -t 600 -ip 0.0.0.0 -hw 5 -wm 1
  216 root        624 S   /bin/pppoe-relay -S wlan0 -C br0
  476 root        320 S   /usr/sbin/udhcpd /tmp/udhcpd.conf
  496 root       1816 S   /bin/snmpd -f -c /tmp/snmpd.conf
  522 root        384 S   /bin/sh /bin/pppoe.sh eth0 sganga
  878 root            Z   [tftpd]
  879 root        244 S   tftpd -l -u root
23864 root        488 S   /bin/pppd pty /bin/pppoe -p /tmp/ppp/run/pppoe.conf-a
23866 root        360 S   sh -c /bin/pppoe -p /tmp/ppp/run/pppoe.conf-adsl.pid.
23867 root        244 S   /bin/pppoe -p /tmp/ppp/run/pppoe.conf-adsl.pid.pppoe
23918 root            Z   [mini_httpd]
23951 root        300 S N cgi
23952 root        372 S   mini_httpd -d /web -c cgi-bin/* -p 80 -u root
23953 root        360 S N sh -c /bin/ping -s 60 -c 1 127.0.0.1 ; ps >/proc/self
23955 root        308 R N ps
}}}
== Uploading the firmware ==
It's a mistery yet
