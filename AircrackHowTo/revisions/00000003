'''Aircrack Quick Guide for the WRT54G'''


[[TableOfContents]]


= Introduction =

== What is Aircrack? ==

Aircrack is a suite of tools that enables traffic wireless monitoring and
penetration testing.


== Where is the Official Homepage? ==

The official page for Aircrack is currently [http://www.cr0.net:8040/code/network/aircrack/ here].


= Requirements =

 * A WRT54G
 * The following packages and the packages they depend upon
 * aircrack
 * the {{{wl}}} utility
 * A place to store large files (i.e. an NFS drive, or a CIFS drive)
 * Please refer to the [:RemoteFileSystemHowTo] for instructions on how to do this


= Installation =

At the time of writing this, Aircrack is not listed in the official package
lists, so you must get it via a URL directly. To install Aircrack run the
following command:

{{{
ipkg install \
     http://openwrt.org/downloads/people/nico/testing/ \
     mipsel/packages/aircrack_2.3-1_mipsel.ipk
}}}

Another utility that is necessary to capture wireless traffic is {{{wl}}}. To
get this package just run:

{{{
ipkg install wl
}}}


= Configuring Your WRT54G to Monitor =

Now that you have Aircrack installed and ready to start capturing traffic you
have to tell your WRT54G to listen to all traffic and not just traffic of its
own. To do this you will use the {{{wl}}} utility:

{{{
wl monitor 1
ifup prism0
}}}


= Start Capturing =

Start off by changing into the directory that you want to store the dump file in.
This must be the directory that is either a CIFS mount or a NFS mount. This is
because the dump files can get quite large and you don't want to overwhelm
the router. Another reason for storing the dump file on another computer is so
processing of the dump can be done in parallel with the capturing.

Once you are in the directory that you want to store the dump file in, run the
following commands:

{{{
airodump prism0 test 0 1
}}}

What the above command does is:
 * prism0 - Use device {{{prism0}}}
 * test - Output to the file {{{test.cap}}} (the {{{.cap}}} is added automatically)
 * 0 - Listen on all channels
 * 1 - Write only the IVs found and drop everything else

We want to only write the IVs found because they are the packets that can be
used to break the WEP encryption.

After the command is run the Aircrack program starts to display information
about the surrounding networks to the user. The user will see what the ESSIDs
of the surrounding networks are and how many packets those networks are sending.

During capture the user can run the aircrack program on the {{{test.cap}}} file
using the computer that the file is actually on. Using this method the
Airodump program and the Aircrack program can be run in parallel, each not
interfering with the other.

Once you have enough packets logged just hit {{{CTRL+C}}} to break execution of
airodump.
