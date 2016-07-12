#pragma section-numbers off
||<tablebgcolor="#f1f1ed" tablewidth="40%" tablestyle="margin: 0pt 0pt 1em 1em; float: right; font-size: 0.9em;"style="padding: 0.5em;">[[TableOfContents]]||

= Linksys WRT54G3G =

The WRT54G3G falls under the new Linksys form-factor, appearing externally similar to the [:OpenWrtDocs/Hardware/Linksys/WRTP54G:WRTP54G], the [:OpenWrtDocs/Hardware/Linksys/WRTSL54GS:WRTSL54GS], the [:OpenWrtDocs/Hardware/Linksys/AG310:AG310] and others.  Marketed worldwide, its distinguishing characteristics are a PCMCIA slot (usually used for 3G WAN) and the ubiquitous brcm43xx wireless.

Although sold under three specifications ([http://www.linksys.com/servlet/Satellite?c=L_Product_C2&childpagename=US%2FLayout&cid=1175237934633&pagename=Linksys%2FCommon%2FVisitorWrapper&lid=3463339789B06 AT], [http://www.linksys.com/servlet/Satellite?c=L_Product_C2&childpagename=US%2FLayout&cid=1160093298732&pagename=Linksys%2FCommon%2FVisitorWrapper&lid=9873239789B03 ST], and [http://www.linksys.com/servlet/Satellite?c=L_Product_C2&childpagename=US%2FLayout&cid=1175242816711&pagename=Linksys%2FCommon%2FVisitorWrapper&lid=1671139789B07 VT]), the hardware appears to be the same and only differs on the firmware flashed to it.  From a software vantage point, it appears to be a typical [:OpenWrtDocs/Hardware/Linksys/WRT54G:WRT54G] with an added !CardBus/PCMCIA port.

== Specifications ==
4-Port router with wireless and PCMCIA

 * Power: 12v @ ?A
 * Bootloader: ?
 * CPU: Broadcom [http://www.broadcom.com/products/Wireless-LAN/802.11-Wireless-LAN-Solutions/BCM4712 4712] @ 200MHz
  * Flash: 4MB
  * SDRAM: 16MB
 * Switch: 6-port Broadcom ?
  * External ports: 4
 * Wireless: Broadcom ?
 * Ethernet transformer: ?
 * PCMCIA slot: Texas Instruments ?

== Additional software ==

Using the 3G WAN functionality under OpenWRT requires installing the 'comgt' package.  Although the documentation only indicates GPRS-family 3G support, the version in trunk has added support for CDMA and EVDO connections.

== Notes ==

This device works fine with OpenWRT Kamikaze 7.06 and later.  Earlier versions may the base device but not the PCMCIA slot.

As of 2008/07/20, the PCMCIA slot does not work under the 2.6 kernel; as a result, anyone needing to use this device for 3G connections will need to use the brcm-2.4 platform.

The button on the front of the device is a GPIO usually used for initiating the WAN connection; in other devices of this form factor it is used for powering the device and cannot be customized.

=== Known working PCMCIA cards ===
 * Huawei E600 (Linksys original firmware does not support)
 * Sierra Wireless !AirCard 595
 * Merlin U630

=== Availability ===
Reported sources for the WRT54G3G:
 * Off-the-shelf product
 * Vodafone (with a Merlin U630)
 * Sprint Wireless in the US (business section, usually uses !AirCard 595)
 * CDW (both AT and ST models)

=== Off-wiki information ===
The following two threads on the OpenWRT forums have additional details and discussion:
 * [http://forum.openwrt.org/viewtopic.php?id=3276 Cardbus Support on WRT54G3G]
 * [http://forum.openwrt.org/viewtopic.php?id=3220 WRT54G with 3G interface?]

The EVDOForums has [http://www.evdoforums.com/thread6621-0-asc-480.html additional information] on a port of OpenWRT for the WRT54G3G.  As of March 2008, release r82 of that port (from WhiteRussian 0.9) is reportedly successfully used by many forum members.  It still has several reported bugs (unconfirmed here):
 a. info.sh in the webif needs permissions changed to +x
 a. APN line has to be commented out in /etc/chatscripts/3g-generic.chat
 a. firewall startup in /etc/init.d/S??firewall   has to have forwarding and masquerading entry for ppp0

A registration-required site provides current build images of the EVDOForums port: [http://xo54g3gst.qcslufkin.com].

Simon Josefsson wrote some notes on installing this device at [http://josefsson.org/grisslan/internet.html his home page].

== Serial port ==
attachment:WRT54G3G_Serial.jpg

Serial port requires level converter at 3.3V:

{{{
Pin 1 = +3.3V
Pin 2 = TXD
Pin 3 = RXD
Pin 4 = unused
Pin 5 = GND}}}
If you use a''' Nokia DLR-3P''' cell phone datacable you can use this color coding - will NOT match if you use different cable.

{{{
Pin 2 = TXD (GRAY)
Pin 3 = RXD (GREEN)
Pin 5 = GND (BLACK+SHIELD)}}}
Same for use with a '''Siemens C35''' data cable:

{{{
Pin 2 = TXD (BLUE)
Pin 3 = RXD (WHITE)
Pin 5 = GND (ORANGE)}}}
Use this terminal setting:'''115200, 8, n, 1 with software flow-contol '''(= none).

== OpenWRT Firmware ==
||'''Hardware[[BR]]revision'''||'''Serial[[BR]]prefix'''||'''Version[[BR]]magic'''||'''kamikaze-7.09'''||'''trunk'''||
|| v1 || unknown || ???? ||<:> (./) || (./) ||
|| v1.1 || CKI11F9 || W54F ||<:> (./) || (./) ||
|| v2.0 || CKI11G4 || W3GN ||<:> (./) || (./) ||
----
CategorySupportedInTrunk
CategoryModel
