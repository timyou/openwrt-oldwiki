[:OpenWrtDocs]
[[TableOfContents]]

= uPnP =

'''This page still under development!!!'''

If you're a Windows user and find yourself using either MSN Messenger or Windows Messenger, you have probably already had problems getting audio and video conversations
to work.  For various reasons (poor design probably being one of them), the multimedia features of the messenger client require that UDP and TCP ports be dynamically
opened and closed in your firewall as these audio/video conversations are negotiated, happen, and then are finished.  

For folks running their modem (cable or DSL) directly into their PC, and using the Microsoft Windows XP Firewall (either SP1 or SP2), this is fine because the MSN Messenger software asks the firewall to open the ports and - by default - it is allowed to do so.  The same thing can be done with other "Application Aware" firewalls such as ZoneAlarm and Kerio Personal Firewall, because these tools can detect that the MSN Messenger application is trying to listen for or make connections and prompt the user to allow these activities.

But this is all useless drivel for us folks running OpenWRT; as soon as you place your Internet connection behind a firewall, you suddenly have an application which needs the firewall to allow connections from the Internet, through your router, translate the addresses, and send them on to your PC.  This all has to happen automatically,
in realtime, with no intervention by the user.  When the audio/video conversation ends, the firewall must then disallow these connections, therefore going back to its previous security configuration.

== uPnP on your WRT ==

uPnP can be installed to run on your WRT.  Information in this guide assumes you are using a Linksys WRT54G/GS, however it should translate just as well to any other manufacturer so long as you're running OpenWRT.

=== What are my options ===

You can either use the pre-compiled '''upnp''' binary from the Linksys firmware or the source-compiled copy of the Linux-IGD project as provided by yani.  More information on both is available in this thread: http://forum.openwrt.org/viewtopic.php?id=85.

The pre-compiled Linksys binary is more elegant (read that as two binary files and one script) and will be detected by your Windows XP PCs.  With the Linksys binary, you are also able to manually open ports in your firewall via Windows using the Internet Gateway Properties page.

The Linux-IGD code is more generic and your mileage may vary on getting it to talk to IPTables (the firewall software) to open the required ports.  It also will not let you open ports in the firewall via Windows.

=== Where do I get the binaries? ===

You can get yani's compiled version of the Linux-IGD daemon from his website at http://openwrt.wojjie.net/packages/linux-igd_0.92_mipsel.ipk

The package for the Linksys binary is currently being worked on. However if you know how to mount the Linksys firmware image in Linux, you can extract the files '''upnp''' and '''libshared.so''' from it and copy these to OpenWRT.  Configuration instructions will also soon follow. :)


== Overview of Universal Plug & Play ==

Universal Plug and Play is not just a means of opening holes in firewalls.  Actually, uPnP is a '''suite''' of standards defined by the uPnP forum (www.upnp.org) on making devices interopate with  each other automatically, without you needing to get involved and configure it by hand.

=== What's an Internet Gateway Device (IGD)? ===

One of the many standards defined by the uPnP forum is the Internet Gateway Device - or IGD (http://www.upnp.org/standardizeddcps/igd.asp).  This little "device" is what we need to have running on our firewalls if we want to make MSN Messenger allow audio and video conversations.  However, since none of us currently use any uPnP standards other than the IGD, it ends up getting generically called "uPnP".  Be aware of this when you're sniffing round the Internet for information on the IGD - you'll need to search for both names.

==== Microsoft and uPnP/IGD ====

Microsoft implemented the IGD in their "Internet Connection Sharing" (ICS) system in Windows XP.  Prior to the introduction of Windows XP, the only Microsoft solution to share your Internet connection was the first generation ICS, which did not support uPnP.  If you wanted to allow connections from the Internet back into your network (such as for an FTP server), you had to manually hack some .INF files.  When Windows XP came out, Internet Connection Sharing included an IGD, and the XP Firewall. Suddenly, your Internet-connected PC became the network firewall, and you could use uPnP-aware applications to ask the firewall to allow connections from the Internet to your PC, all without you having to get involved (security folks feel free to have a heart attack at this point). :P

=== Hardware routers and the IGD ===

Once people started buying hardware routers, it became important (from a marketing perspective) that these devices could also act as an IGD, and respond to uPnP requests for access through the firewall in the router. And so, vendors began to create their own Internet Gateway Devices (IGD's) based on the standards available from the uPnP forum.  Each implementation is a little bit different, to cater for the different types of firewalls that the IGD software must communicate with.  

When we talk about all the hardware routers based on the Broadcom chipset (Linksys, Belkin, Asus, etc), the IGD software has been written to communicate with the Netfilter (IPTables) Linux firewall and write variables to nvram when required.  Most of this code is based on the Linux IGD project over at Sourceforge.

=== Security Warning!!! ===

Let's not pull any punches here; the IGD is inherently '''NOT SECURE'''.  The uPnP framework does not cater for any authentication whatsoever.  This basically means that '''ANY''' computer, '''ANY''' person, or '''ANY''' application in your network can say "Hey firewall, open these ports".  And the worst part about that is that when the ports are opened, '''ANYONE''' on the Internet can connect to them.  

You think trojans are bad now?  Just wait until everyone is running uPnP on their firewall, then all of a sudden every trojan that manages to infect your PC will tell your firewall to allow anyone to connect to it.  Looks like that firewall just became worthless!

==== So what should I do? ====

Quite simply, if you do not have a drastic need to use MSN audio and video conversations, do NOT run the IGD/uPnP on your router.  There are currently no other major applications that support or need uPnP, although I believe BitTorrent is about to support it.

==== I think I need uPnP, but the gurus will flame me in the forums for using it!! ====

Here's my perspective.  I work in the IT Security industry. I've taught security courses for the SANS Institute. I spend my working hours going round to customer after customer, implementing solutions to fix often disastrous mistakes that our penetration testing team has discovered.
And I use uPnP - an insecure piece of software that increases my risk of being spanked by malicious code.

Being aware of the risk is the biggest security step you will ever make; if you're going to use any software that increases your risk, take precautions.  Encrypt all sensitive information with tools like PGP, and backup all your critical information to a writeable CD/DVD.  After that, just be aware of what '''might''' happen if the weaknesses in uPnP were exploited.  If you ever get wind of malicious software that exploits uPnP, shut it down for a while.
