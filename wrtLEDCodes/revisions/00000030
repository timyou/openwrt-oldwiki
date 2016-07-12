##language:en
== WRT LED Codes Analysis ==
Some LED sequences explained.
||'''flash''' ||LED goes on and off at intervals of 1 second or less ||
||'''alternate''' ||LED changes state with a long interval. ||
||'''on''' ||LED stays on ||
||'''off''' ||LED stays off ||


=== POWER flashes ===
||POWER ||flashes. ||
'''''Reason''''':[[BR]] The power led can flash for a number of reasons; a flashing power led by itself is rarely cause for concern. The power led will flash on bootup until the firmware stops the flashing, but it may start flashing again with certain wireless settings (eg: configured as wifi client, not connected)

=== DMZ lights ===
||DMZ ||on ||
'''''Reason''''':[[BR]] !OpenWrt uses the DMZ led to signal bootup. Once the kernel has booted !OpenWrt will turn on the DMZ led; it won't turn off again until after !OpenWrt has processed all the startup scripts in /etc/init.d. If it doesn't turn off then there is a problem with one of the startup scripts.

=== POWER flashes, DMZ alternates ===
||POWER ||flashes. ||
||DMZ ||alternates slowly ||
'''''Reason''':[[BR]] You flashed a '''corrupt''' image.[[BR]] This might be because you did not set the binary flag on your tftp program, or have a bad image, or your upload was interrupted. ''

'''''Solution''''':[[BR]] Just reflash, and make sure your tftp program is configured right. Check your image.

== Controlling the LEDs ==
Some of the front panel LEDs can be controlled by writing to /proc/sys/diag. A single hex value written here will control the state of the LEDs, e.g.

 . echo "0x01" > /proc/sys/diag
The values are bitfields, so add up the ones you want in the table below to control the desired LEDs.
||Value ||Action ||Known to work with ||
||0x00 ||Defaults ||- ||
||0x01 ||DMZ LED on ||WRT54G v1.1, v2.0, v3.0, v4.0 and WRT54GS ||
||0x04 ||Power LED flashing ||WRT54G v1.1, v2.0, v3.0, v4.0 and WRT54GS ||


For example, if you want the power LED to flash (0x04) and the DMZ LED to light up (0x01) you'd echo "0x05" > /proc/sys/diag

On RC5, the CISCO LED found on some linksys routers is now supported. Here's a table of bitfields that work for me
||Value ||Action ||Known to work with ||
||0x00 ||Defaults ||- ||
||0x01 ||DMZ LED on ||WRT54G v1.1, v2.0, v3.0, v4.0 and WRT54GS ||
||0x04 ||Power LED flashing ||WRT54G v1.1, v2.0, v3.0, v4.0 and WRT54GS ||
||0x08 ||White Cisco LED ON ||WRT54G v3.1, WRT54GS v4.0, WRT54GL ||
||0x10 ||Orange Cisco LED ON ||WRT54G v3.1, WRT54GS v4.0, WRT54GL ||


Feel free to edit this out of here, but I put together this chart which helps me. I didn't list the values in hexadecimal as my scripts use ''cat /proc/sys/diag'' and it doesn't return a hex value. Also I see no need for the hex value as ''echo "8" > /proc/sys/diag'', etc. works just as well without me doing hex math. Also I cannot confirm the versions these codes work for, but I'm running a v1.0 & v3.0 wrt54g.
||'''Value''' ||'''Cisco''' ||'''Power''' ||'''DMZ''' ||
||0 (default) ||Off ||On ||Off ||
||1 ||Off ||On ||On ||
||4 ||Off ||Flashing ||Off ||
||5 ||Off ||Flashing ||On ||
||8 ||White ||On ||Off ||
||9 ||White ||On ||On ||
||12 ||White ||Flashing ||Off ||
||13 ||White ||Flashing ||On ||
||16 ||Orange ||On ||Off ||
||17 ||Orange ||On ||On ||
||20 ||Orange ||Flashing ||Off ||
||21 ||Orange ||Flashing ||On ||
||24 ||White & Orange ||On ||Off ||
||25 ||White & Orange ||On ||On ||
||28 ||White & Orange ||Flashing ||Off ||
||29 ||White & Orange ||Flashing ||On ||


I also noticed this thread: http://forum.openwrt.org/viewtopic.php?id=4796 which has a simple script from vincentfox to check diag bits.
