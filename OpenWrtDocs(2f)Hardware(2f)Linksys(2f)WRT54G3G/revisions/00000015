#pragma section-numbers off
||<tablebgcolor="#f1f1ed" tablewidth="40%" tablestyle="margin: 0pt 0pt 1em 1em; float: right; font-size: 0.9em;"style="padding: 0.5em;">[[TableOfContents]]||

= Linksys WRT54G3G =

The WRT54G3G falls under the new Linksys form-factor, appearing externally similar to the [:OpenWrtDocs/Hardware/Linksys/WRTP54G:WRTP54G], the [:OpenWrtDocs/Hardware/Linksys/WRTSL54GS:WRTSL54GS], the [:OpenWrtDocs/Hardware/Linksys/AG310:AG310] and others.  Marketed primarily in North America, its distinguishing characteristics are a PCMCIA slot (usually used for 3G WAN) and the ubiquitous brcm43xx wireless.

Although sold under three specifications ([http://www.linksys.com/servlet/Satellite?c=L_Product_C2&childpagename=US%2FLayout&cid=1175237934633&pagename=Linksys%2FCommon%2FVisitorWrapper&lid=3463339789B06 AT (AT&T)], [http://www.linksys.com/servlet/Satellite?c=L_Product_C2&childpagename=US%2FLayout&cid=1160093298732&pagename=Linksys%2FCommon%2FVisitorWrapper&lid=9873239789B03 ST (Sprint)], and [http://www.linksys.com/servlet/Satellite?c=L_Product_C2&childpagename=US%2FLayout&cid=1175242816711&pagename=Linksys%2FCommon%2FVisitorWrapper&lid=1671139789B07 VT (Verizon)]), the hardware appears to be the same and only differs on the branding and possibly individual card support.  From a software vantage point, it appears to be a typical [:OpenWrtDocs/Hardware/Linksys/WRT54G:WRT54G] with an added !CardBus/PCMCIA port.

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

== 3G Functionality ==

Most current 3G modems present as a USB device, regardless of what they plug in as (USB, PCMCIA, !ExpressCard, etc.).  Hence, you must have the driver for the base connection (kmod-pcmcia-core for WRT54G3G), the USB bus (usb-kmod-ohci for most Sierra Wireless PCMCIA cards), the USB-serial driver for managing the connection (kmod-usb-serial) and the end device driver if it exists (kmod-nozomi, kmod-usb-serial-sierra, and so on).

Use of the 3G WAN functionality under OpenWRT is supported by installing the `comgt` package.  Although the documentation only indicates GPRS-family 3G support, the version in trunk (r10347 and later) has added support for CDMA and EVDO connections.  Custom PPP scripts are certainly usable but those in `comgt` provide a well-tested default that should suffice for most installations.

The following are several widespread misconceptions about 3G modems and [hopefully] helpful explanations:

 * '''Serial speed matters''' or '''The connection will be limited to XXX.000bps'''
  The serial channel is only used for initiating and managing the connection to the modem.  Once the dialing is  completed and a PPP connection is initiated, your 3G modem will perform at the highest speed it can, regardless of the serial setting in your PPP configuration.  A trivial way to prove this is to configure your connection for a relatively low speed (19200) and perform a series of speed tests.  Re-configure and re-negotiate at a much higher speed (115200) and re-run the tests.  The difference between the tests should be statistically insignificant; if isn't, please leave a note with a link to your testing process.
 * '''You have to modify the buffer size on usbserial to get any reasonable performance'''
  Since 2006, USB serial device drivers needing high-speed connections have been increasing their buffer size from 64 bytes (the problematic size that started this rumor) to 2048 and even 4096 bytes.  Unless one or more of the following conditions are true, the buffer size is already set or negotiated to a reasonable size for your hardware:
   * Your kernel is extremely old
   * Your 3G device is not directly supported by a driver and you have to use usb-serial as a generic driver
   * Your USB endpoint does not report an appropriate !MaxPacketSize to the operating system
 * '''My card advertises 7.2Mbps performance, I should expect that out of my connection'''
  Unfortunately, most cellular ISPs are no different from terrestrial ones in that they oversell their bandwidth and are typically incapable of providing the speed their clients' devices are capable of using.  Most North American consumers connect to their terrestrial broadband providers with 100Mbps or 1Gbps ethernet ports, but few providers (if any) provide that level of speed to consumers.

== Notes ==

This device works fine with OpenWRT Kamikaze 7.06 and later.  Earlier versions may support the base device but not the PCMCIA slot.

As of 2008/07/20, the PCMCIA slot does not work under the 2.6 kernel; as a result, anyone needing to use this device for 3G connections will need to use the brcm-2.4 platform.  Commits #11898 and 11899 officially added Sierra Wireless support for the brcm-2.4 platform.

The button on the front of the device is a GPIO usually used for initiating the WAN connection but can be customized to perform a specific action; in other devices of this form factor it is used for powering the device and cannot be customized.

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
