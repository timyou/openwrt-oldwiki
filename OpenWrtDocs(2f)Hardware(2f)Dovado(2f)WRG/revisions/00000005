= Dovado WRG =
This device is currently (January 2007) unsupported. XScale port is in progress so adding support should be fairly easy.

Stock firwmare is based on Linux 2.6.14.2 and Busybox. Device is designed by Swedish company named Teleca tse AB. XScale CPU is located on separate processor board. There's plenty of unpopulated connectors onboard so JTAG is likely present. VoIP interface is done using Myson Century chip and appears to be connected to XScale CPU using Ethernet. Myson chip seems to be completely independent embedded computer for VoIP and XScale part only provides routing and wifi. Bootloader is Redboot.

After you have shell access on WRG you can access Myson side of device with HTTP to 192.168.254.2. Physical ethernet of WRG is 192.168.0.1 and private ethernet interfaced towards Myson is 192.168.254.1.

Probably easiest way to access VoIP side is logon to WRG using serial port and enter following command: 'iptables -P INPUT ACCEPT; iptables -P OUTPUT ACCEPT; iptables -P FORWARD ACCEPT; iptables -F' and then just open http://192.168.254.2 from your PC. Just make sure WRG is your default gateway. You'll find device called 'WRG2' with more VoIP parameters to tweak than generic VoIP access you can get thru 'WRG' pages.

== Hardware ==
 * Intel IXP420 266MHz
 * 16MB FLASH
 * 32MB RAM
 * One ethernet port (NPE-C)
 * Atheros AR2413 WLAN on MiniPCI (WMIA-165g)
 * Texas Instruments Cardbus controller PCI1510
 * MYSON CENTURY CS6220 VoIP MCU
 * Two FXS ports for analog phones / faxes
 * TTL serial port onboard (J1: 1=Ground, 2=Input from PC, 3=Output from WRG, 4=3,3V, 115200bps)

== Links ==
 * [http://www.dovado.com/Portfolio_WRG.html Manufacturers page]
 * [http://www.sukkamehulinko.romikselle.com/openwrt/dovado/dovado-console.txt Bootlog]
 * [http://www.sukkamehulinko.romikselle.com/openwrt/dovado/firmware/ Latest firmware] with guide howto extract it.
 * [http://www.myson.com.tw/products.php?op=pdetail&flang=EN&ProductKind=2&ProductNo=119 VoIP MCU info]
