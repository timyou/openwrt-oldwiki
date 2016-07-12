## ##############################################
## Tip: Please write the howto more generic because OpenWrt runs on
## more routers than just the WRT54G and use a linebreak on char 80 makes
## the page source a lot easier to read and editable.
##
## Again, thanks for your help!


'''Aircrack Quick Guide for the WRT54G/S'''


[[TableOfContents]]


= Introduction =

== What is Aircrack? ==

Aircrack is a suite of tools that enables wireless traffic monitoring and
penetration/security testing.


== Where is the Official Homepage? ==

The official page for Aircrack is [http://www.cr0.net:8040/code/network/aircrack/ here].


= Requirements =

 * A WRT54G/S
 * The following packages and the packages they depend upon
 * aircrack
 * the {{{wl}}} utility
 * A place to store large files (i.e. an NFS drive, or a CIFS drive)
 * Please refer to the [:RemoteFileSystemHowTo] for instructions on how to set this up


= Installation =

At the time of writing this, Aircrack is not listed in the official package
lists, so you must get it via a URL directly. Aircrack can easily be installed in an ssh session with your router by running the following commands from /tmp:

{{{
wget http://openwrt.org/downloads/people/nico/testing/mipsel/packages/aircrack_2.3-1_mipsel.ipk
ipkg install aircrack_2.3-1_mipsel.ipk
}}}

Another utility that is necessary to capture wireless traffic is {{{wl}}}. This can be installed through ssh by using the following commands:

{{{
ipkg update
ipkg install wl
}}}


= Configuring Your WRT54G/S to Monitor =

Now that Aircrack is installed and ready to start capturing traffic, you
have to tell your WRT54G/S to listen to all traffic and not just traffic of its own. To do this you will use the {{{wl}}} utility:

{{{
wl monitor 1
ifup prism0
}}}


= Start Capturing =

Begin by changing into the directory that you want to store the dump file in. This is most likely the directory that is either a CIFS or NFS mount. The dump files can get large, and to capture a useful amount of data you will need more storage than what comes stock on these routers. Another reason and advantage for storing the dump file on another computer is so the processing of the dumpfile can be done in parallel with capturing.

Once you are in the directory that you want to store the dump file in, run the following commands:

{{{
airodump prism0 test 0 1
}}}

What the above command does is:
 * prism0 - Use device {{{prism0}}}
 * test - Output to the file {{{test.cap}}} (the {{{.cap}}} is added automatically)
 * 0 - Listen on all channels
 * 1 - Write only the IVs found and drop everything else

We want to only write the IVs found because they are the packets that can be
used to crack the WEP encryption.

After the command is run the Aircrack program starts to display information
about the surrounding networks to the user. The user will see the ESSIDs of the surrounding networks and how many packets those networks are sending.

During capture, the user can run the aircrack program on the {{{test.cap}}} file using the computer that is hosting the network storage. Using this method, both airodump and aircrack can be run in parallel, without
interfering with eachother.

Once you have enough packets logged just hit {{{CTRL+C}}} to quit airodump.
If you get stumped, there are lots of good resources at the official aircrack [http://www.cr0.net:8040/code/network/aircrack/ website].


= Airodump Usage =

{{{
usage: airodump <interface name or pcap filename> <output prefix> <channel> [IVs flag]
}}}
