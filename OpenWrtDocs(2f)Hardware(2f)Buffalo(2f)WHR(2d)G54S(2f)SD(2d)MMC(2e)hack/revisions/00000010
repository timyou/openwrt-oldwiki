'''Buffalo WHR-G54S SD/MMC Hack'''

----

Here are some photos of this hack, these comes from my device, quality is poor but i think these could be useful for you to see something.[[BR]]
Covered information are provided on an "as is" basis, without warranty of any kind, either expressed or implied, if you create your own web page please refer to me as original author but don't worry i don't want to charge you money :)

&nbsp;

'''Step 1: Disassemble your access point'''

----

Power off your device, open your access point, remove case, antenna, and get your motherboard on a table[[BR]]
Locate on the back 6 points where you should solder some wires, you'll need to locate these points:
 * VCC from AP for SD card
 * GND from AP for SD card
 * Data In (using GPIO 5)
 * Data Out (using GPIO6)
 * Clock (using GPIO3)
 * C/S (using GPIO7)

Do not use GPIO 4 as i've already explained on WHR-G54S wiki page (Buffalo uses it for reset)[[BR]]
Please see mine already hacked (quite good hack quality, poor photo).

attachment:back.jpg

See this table for connection details:
{{{
Signal             Type        SD Card Slot Pin
Chip Select (CS)   GPIO 7      1
Data In            GPIO 5      2
Ground             AP Ground   3
Vcc                AP Vcc      4
Clock              GPIO 3      5
SD Sleep Mode      AP Ground   6
Data Out           GPIO 6      7
}}}
you don't need to connect other SD pins[[BR]]
See SD Card Slot Picture
attachment:mmc.png

&nbsp;

&nbsp;

'''Step 2: Connecting VCC, GND, Data In'''

----
Now you need to solder VCC and GND,[[BR]]
Ground is available quite everywhere, no matter where you take it, i've taken close to power supply input because is very easy[[BR]]
...but is better to get VCC where i've taken, on rear of power supply input because i've got some troubles with some SD cards and somewhere on board when AP is powered on you get 3.1...3.2V and sometimes is not enough (very strict tolerance), it's better to take 3.3...3.4V as they comes from DC input.[[BR]]
Connect VCC to pin 4 on SD card slot, connect GND to pins 3 and 6 of SD card slot (with one or two wires as you prefer, no matter); now you can power your SD slot.[[BR]]
Data IN signal is labeled as "2" on photo, you need to connect this to Pin 2 on sd card slot[[BR]]
See photo below for details

attachment:part1.jpg

&nbsp;

&nbsp;

'''Step 3: Connecting Data Out, Clock, Chip Select'''

----
These three guys are taken on rear of AP Leds, they're quite easy to find but solder points are very thin, take care on them see, photo for details[[BR]]
attachment:part2.jpg [[BR]]
Solder Point 1 is Chip Select (CS, Pin 1 on SD)[[BR]]
Solder Point 5 is Clock (Pin 5 on SD)[[BR]]
Solder Point 7 is Data Out (Pin 7 on SD)[[BR]]

&nbsp;

&nbsp;

'''Step 4: Soldering SD Card Slot'''

----
Now you need to connect all your wires to an SD Card Slot, i've used an old connector brutally extracted from an old piece of hardware, connector is very bad but photo shows you where pins are (like previous one)[[BR]][[BR]]

attachment:overall.jpg attachment:sdmmc.jpg

'''' Don't have time today to finish tutorial, i'll be back tomorrow, please give me few hours...''''

BEN

----
