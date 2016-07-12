##language:en
== WRT LED Codes Analysis ==
Some LED sequences explained.

||'''flash'''||LED goes on and off at intervals of 1 second or less||
||'''alternate'''||LED changes state with a long interval.||
||'''on'''||LED stays on||
||'''off'''||LED stays off||

=== POWER flashes, DMZ alternates ===
||POWER||flashes.||
||DMZ||alternates at about '''20''' seconds.||

'''''Reason''''':[[BR]]
You flashed a '''corrupt''' image.[[BR]]
This might be because you did not set the binary flag on your tftp program, or have a bad image, or your upload was interrupted.

'''''Solution''''':[[BR]]
Just reflash, and make sure your tftp program is configured right. Check your image.

== Controlling the LEDs ==
Some of the front panel LEDs can be controlled by writing to /proc/sys/diag.  A single hex value written here will control the state of the LEDs, e.g.

 echo "0x01" > /proc/sys/diag

The values are bitfields, so add up the ones you want in the table below to control the desired LEDs.

||Value||Action||Known to work with||
||0x00||Defaults||-||
||0x01||DMZ LED on||WRT54G v1.1, v2.0, v3.0 and WRT54GS||
||0x04||Power LED flashing||WRT54G v1.1, v2.0, v3.0 and WRT54GS||

For example, if you want the power LED to flash (0x04) and the DMZ LED to light up (0x01) you'd echo "0x05" > /proc/sys/diag

----
----
CategoryCategory
