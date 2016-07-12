[[TableOfContents]]

----

= Telnet Console =
Some ["OpenWrtDocs/Hardware/Netgear"] routers run a telnet daemon which can be accessed from any computer on its local subnet after unlocking it (see below). The following devices are currently known or assumed to support this:

 * WGR614 v9: works, gives access to a busybox console w/o authentication
 * WGR614 v8: aka WGR614L, works, access to a busybox console w/o authentication (unlock procedure made using Gentoo Linux)
 * WGR614 v7: known to work (if it does not work for you, try to hardreset your router first)
 * WGR614 v3,v4,v5,v6: known to work
 * WGR614 v1-2: unknown, may well work
 * WGT624 V3H1: worked, after 6-12 try, reboot, try again cycles.
 * WPN824 v1: known to work
 * WPN824 V2.0.15_1.0.11 : works!
 * WG602 (unknown version): [http://www.cve.mitre.org/cgi-bin/cvename.cgi?name=2006-1002 assumed to work]
  . Tried from a Gentoo box on a WG602v3: does not work.
  {{{
# ./telnetenable 172.30.0.253 XXXXXXXXXXXX Gearguy Geardog
Cm£ÅÀó¬*@yI£ndsf]üg:ÜV£ndsf£ndsf£ndsf£ndsf£ndsf£ndsf£ndsf£ndsf£ndsf
}}}
 * WGT624 v2: known to work
 * WGT624 v3: known to work
 * WGT624 (unknown version): [http://www.cve.mitre.org/cgi-bin/cvename.cgi?name=2006-1002 assumed to work]
 * WNR3500: known to work
Please add to this list, so people will know which are supported and which are not!

Loginname/password(casesensitive): Gearguy/Geardog

The password can be changed after logging in using the {{{passwd}}} command.

== Unlocking the Telnet Console ==
=== On Windows ===
Netgear provides a developer tool for unlocking the console access from a Windows client. Windows NT and later versions are assumed to work, administrator privileges are required. This was successfully tested on Windows XP SP2.

Here's the process:

 * Download the file wpn824_ko_2.12_1.2.9.zip file from [http://www.netgear.co.kr/Support/Product/FileInfo.asp?IDXNo=155 the Korean Netgear support website (scroll down)] or from the other locations I found it at ([http://www.sebone.de/download.php?file=47e892f71fa9d1036a5615e3b7045190 mirror 1], [http://www1.file-upload.net/download_10.05.06/2di5co.zip.html mirror 2], UPDATE: Get it here http://files.to/get/349970/64662/telnetEnable.rar) and unzip it. A new link that does work for the time being: http://rapidshare.com/files/71670434/telnetEnable.zip.
 * Login to Windows using an account which has administrative privileges (needed for sending custom crafted network packets which this tool does)
 * You will see a M$ Word doc which contains screenshots and instructions in korean language, a firmware update (you don't need this) and the telnetEnable.exe tool
 * Open a command line (windows console) window. To do so, press and hold windows key, then press R once and release both. In the new windows, type ''cmd'', then press enter)
 * Get the MAC address of your Netgear router. You can use either 'arp -a' and use the 'physical address' or look it up on the [http://192.168.1.1/RST_status.htm web interface of your router] (''Maintenance'' -> ''Router status'' -> ''LAN port'' -> ''MAC Address'')
 * Copy or type the MAC address to a text editor such as Notepad, Wordpad or Write
 * Remove any minus signs (-) or colons (:), replace all characters by their upper case representation (a -> A, d-> D etc.)
 * Copy the result of your editing to the clipboard and return to the command line window
 * type (without quotes) "{{{telnetenable.exe }}}", the IP address of your router (e.g. "{{{192.168.1.1}}}"), add another space ("{{{ }}}"), paste the contents of the clipboard, and append " Gearguy Geardog". These are the default username and password ''for telnet console access'' (they differ from those of the web interface), you need to modify them appropriately if you changed them previously. The result should look similar to this:
{{{
telnetEnable.exe 192.168.1.1 000FB5A2BE26 Gearguy Geardog
}}}
 . Correct character case is important here.
 * Now press Enter to run the tool. It should return to the shell pretty quickly with no error. If it takes a long time and returns a 'send failed' error message, just try again.
 * You should now be able to login to the router via telnet from any computer in your local subnet (including the one you just used to activate the listening mode). To do so, type the following (no quotes): "{{{telnet }}}", append the IP of your router and press enter (e.g. {{{telnet 192.168.1.1}}})
 * You will be prompted for a login and a password. For the login, type {{{Gearguy}}}, for the password, type {{{Geardog}}}. Correct character case is important here.
 * After successful authentication you will be presented a prompt such as
{{{
U12H02900>
}}}
 * For available commands, type {{{help}}} or {{{?}}}. To quit the console, type {{{exit}}}.
=== On Un*x ===
Netgear uses free software to make their products, but has not provided information or free software tools to enable them to be used. One needs to either use the Windows binary-only program or reverse engineer its operation in order to discover what magic packets Netgear's tool sends to the router to enable the telnet interface.

Unfortunately, there is no ready to go tool for Un*x, - yet. However, thanks to yoshac_at_member_dot_fsf_dot_org, the Windows telnetenable has been reverse engineered. The following could be determined on the data format and transforms performed by Netgear's telnetEnable.exe and a work is in progress to implement the entire tool as open source. The current implementation is attached to this document.

==== Download ====
Source code for a 'C' re-implementation of telnetenable.exe's algorithms has been released by yoshac_at_member_dot_fsf_dot_org under the GPL, for use as the basis of a Un*x version of the tool currently in development. The resulting telnetenable binary will operate exactly the same as the original Windows tool, except that it currently does not actually send the raw TCP frame to the router. Network support is left as an exercise for the reader ;-)

The implementation does not provide network connectivity to finish the process from a *nix box, follow the instructions in the README to compile the software, then, run

{{{
telnetenable 192.168.1.1 000FB5A2BE26 Gearguy Geardog > modpkt.pkt}}}
 . Then to send the packet to the router type
{{{
nc 192.168.1.1 23 < modpkt.pkt
}}}
Then telnet as shown above.

Please read the README file contained in the [attachment:telnetenable.zip attached ZIP archive].

== The algorithm ==
A probe packet is built using the data supplied on the command line, and is then signed using the RCA MD5 hashing algorithm. After signing, the entire probe packet is encrypted using the Blowfish algorithm, using a private key.

The probe packet payload format is as follows:

{{{
struct payload
{
char signature[0x10];
char mac[0x10];
char username[0x10];
char password[0x10];
char reserved[0x40];
}
}}}
The above payload format is transformed by the tool algorithms as follows:

The MD5 checksum is calculated for the contents of the probe payload MAC, username and password fields only, and is done using the normal 3 passes (MD5init, MD5update, MD5final) with the default RCA seed. The resulting 16 byte MD5 checksum/hash is then stored into the signature array of the probe payload.

The entire probe payload (including the reserved area, which is always null for this example) is then ENCRYPTED using the blowfish algorithm. The secret key used for the blowfish encryption is: AMBIT_TELNET_ENABLE but prior to encryption, a '+' followed by the password is appended to the secret key.

The encrypted probe packet is then sent to telnet port (23) on the router using raw TCP sockets in the standard manner. Curiously, the telnetenable.exe program also includes the necessary support to decode packets incoming from the router, but there does not appear to be any two-way handshake implemented, it is simple a raw TCP send from the client to the router.

Note: The encrypted probe packet is sized as char output_Buf[0x640] but only an encoded data length of size of 0x80 appears to be used by the code. It is unknown what other capabilities may be similarly enabled via the 'reserved' field, or by other passwords.

== Troubleshooting ==
If you aren't able to login anymore, which may occur after firmware updates or telnet-session timeouts/connection losses, repeat the unlocking procedure.
