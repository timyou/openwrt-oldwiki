[[TableOfContents]]

= Linksys WAG54G2 v1.0 =
NOTE: The Linksys WAG54G2 is NOT version 2 of the WAG54G, it's totally different hardware.

WAG54G2 is an ADSL gateway router with 4 (available) port 10/100 ethernet switch, ADSL 2+ modem, 802.11g Wireless access point.

OpenWRT doesn't support this platform yet, but i'm going to have a go at getting it running. So, for now, this page is preliminary info.

== Hardware == Based on the Conexant CX94610 ADSL2plus chipset, which is a SoC with an ARM1026EJ core. Ethernet switch is an IC+ IP175 5 port, 4 ports are available on the back panel. WLAN: unknown Conexant, WLAN chips are covered by an aluminium screen on the board 16 MB SDRAM 4 MB Flash

== Serial Console ==
''will add photo later''

Serial Console is available as a header on board (mine was covered with soldermask which needed scraping before I could solder it). The board runs at 3.3V, but I had success with the serial console with a Maxim MAX232CPE (which is nominally 5V rated). Connect at 38,400 8N1 with no flow control.

= Software =
The linksys software is based on kernel 2.6.11 with plenty of patching. GPL code is available from linksys [ftp://ftp.linksys.com/opensourcecode/wag54g2/1.00.10/WAG54G2_GPL_v1.00.10_AnnexA.tgz here].

You can get root from the serial console just by pressing enter- no login needed.

== Boot Loader ==
The boot loaded is 'PS Boot' - conexant specific. Have a look ["OpenWrtDocs/Bootloaders/PS Boot"]

== Boot Log ==
{{{ to come later }}}
