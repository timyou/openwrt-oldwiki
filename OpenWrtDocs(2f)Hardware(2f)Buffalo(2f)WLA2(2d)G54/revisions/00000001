'''Buffalo WLA2-G54'''

The WLA2-G54 is based on the Broadcom 4710 board. It has a 125MHz CPU, 4Mb flash and 16Mb RAM. The wireless NIC well-soldered into a miniPCI slot on the board.

I was unable to send this device firmware via TFTP, so I modified the .trx OpenWrt firmware image to include a header matching the Buffalo firmware. Then I simply "upgraded" the firmware via the Buffalo web-interface to the modified OpenWrt firmware, which worked very well.

I used my hex editor to prepend the following string to the .trx file to create a .bin file (name is unimportant, however) that the device accepted: 

"WLA2-G54 1.50 4.02WR<LF>filelen=2162688<LF>" (no quotes)

The version number 1.50 is arbitrary, although I made sure to pick one greater than the current firmware version 1.30.

<LF> is a linefeed character: ASCII 0x0A.

The filelen is the size of what follows the .bin header and should match the size in bytes of the original .trx image.

The rest of the string matches the Buffalo file I got exactly.

HDR0 (the beginning of the .trx image) should follow immediately after the second <LF>.

----
CategoryModel
