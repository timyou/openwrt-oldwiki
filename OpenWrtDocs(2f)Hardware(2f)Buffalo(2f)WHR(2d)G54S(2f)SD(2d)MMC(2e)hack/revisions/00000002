'''Buffalo WHR-G54S SD/MMC Hack'''

----
 . Here are some photos on this hack, these comes from my device, quality is poor but i think these could be useful for you to see something.
''' '''

''' '''

'''Step 1: Disassemble your access point'''

----
 Power off your device, open your access point, remove case, antenna, and get your MoBo on a table, Locate on the back 6 points where you should solder some wires, you'll need to locate these points:

 * VCC from AP for SD card
 * GND from AP for SD card
 * Data In (using GPIO 5)
 * Data Out (using GPIO6)
 * Clock (using GPIO3)
 * C/S (using GPIO7)
Do not use GPIO 4 as i've already explained on WHR wiki page (Buffalo uses it for reset) Please see mine already hacked (quite good hack quality, poor photo).

----
 . .  .  .  . Example code
'''SD/MMC Hack'''[[BR]] This hack is very popular with other APs (eg.Linksys) and can be applied to Buffalo WHR-G54S as well, things are slightly different because of different usage of GPIO but there's a binary kernel module mmc.o optimized and fully working for Linksys as well as Buffalo

For this hack i've used these I/O (please see table described above)

{{{
Signal     GPIO
----------------
Data IN    5
Data OUT   6
Clock      3
CS         7
}}}
I've created a new wiki page with some photos of my hack, Hope it helps, send me some notes if you need more information on my job''' NOTE''': Using GPIO 4 (like linksys WRT models) is NOT a good idea here (reset button... :) )

''(Andrea Ben Benini)''

''.''

aaabbb

''.''

----
 . CategoryModel
