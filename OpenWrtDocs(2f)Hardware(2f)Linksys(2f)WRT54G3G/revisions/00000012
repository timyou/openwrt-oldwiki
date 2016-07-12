= Linksys WRT54G3G =

This device works fine with OpenWRT Kamikaze 7.06 and 7.07.  Earlier versions may not fully support this device.

This device seems to be a normal ["OpenWrtDocs/Hardware/Linksys/WRT54G"] with a !CardBus.

The WRT54G3G is currently marketed by:

 * Off the shelf product.  My eletricity company bought me one, and I'm using it with the Swedish Tele2/Comviq's Huawei E600 successfully.  (Note that Linksys's original firmware doesn't support the E600!)

 * Vodafone for their 3G UMTS networks.  It uses a Merlin UMTS modem:
{{{
root@OpenWrt:/# cardctl info
PRODID_1="Novatel Wireless"
PRODID_2="Merlin UMTS Modem"
PRODID_3="U630"
PRODID_4=""
MANFID=00a4,0276
FUNCID=2
root@OpenWrt:/#
}}}
 * Sprint Wireless in the US, using a modem provided by the consumer.  It is marketed towards business users.
Please use the [http://forum.openwrt.org/viewtopic.php?id=3276 Cardbus Support on WRT54G3G] thread or the [http://forum.openwrt.org/viewtopic.php?id=3220 WRT54G with 3G interface?] thread in the forum if you have more details.

Please contribute useful information here.

The v1.1 has a Broadcom BCM4712 CPU (200MHz) and ~14MB RAM.

There's different 3G data cards bundled with this device. "Vodafone Mobile Connect 3G/GPRS data card" has NEC USB2 controller with two generic USB ports builtin. 3G side is connected to those ports.

I wrote some instructions on installing this device at [http://josefsson.org/grisslan/internet.html my home page].

= Serial port =
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

= Other Info =
== Supported Versions ==
||||<style="text-align: center;"> (!) '''Please contribute to this list.''' (!) ||||<style="text-align: center;">'''!OpenWrt''' ||
||'''Model''' ||<style="text-align: center;"> '''S/N prefix''' ||<style="text-align: center;"> '''Code pattern''' ||<style="text-align: center;">  '''Stable[[BR]]White Russian''' ||<style="text-align: center;">  '''Development[[BR]]Kamikaze''' ||
||WRT54G3G v1 || || W54F? ||<style="text-align: center;"> (./) ||<style="text-align: center;"> (./) ||
||WRT54G3G v1.1 || CKI11F9... || W54F ||<style="text-align: center;"> ? ||<style="text-align: center;"> (./) ||
||WRT54G3G-EM v2.0 || CKI11G4... || W3GN ||<style="text-align: center;"> ? ||<style="text-align: center;"> (./) ||
----
 . CategoryModel
