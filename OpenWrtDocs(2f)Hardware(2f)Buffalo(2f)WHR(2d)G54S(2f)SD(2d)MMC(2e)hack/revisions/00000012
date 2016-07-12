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
attachment:mmc.png [[BR]]
you don't need to connect other SD pins[[BR]]
See SD Card Slot Picture


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
These three guys are taken on rear of AP Leds, they're quite easy to find but solder points are very thin, take care on them, see photo for details[[BR]][[BR]]
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

&nbsp;

'''Step 5: Assembling all together'''

----
Now mod is finished, you only need to test it with current mmc.o module (with Buffalo Hack), look at forum if you need an updated one or drop me an email if you need source code or a compiled version, please it's important to note the right pinout as mentioned before:
{{{
Signal             Type        SD Card Slot Pin
-----------------------------------------------
Chip Select (CS)   GPIO 7      1
Data In            GPIO 5      2
Ground             AP Ground   3
Vcc                AP Vcc      4
Clock              GPIO 3      5
SD Sleep Mode      AP Ground   6
Data Out           GPIO 6      7
}}}

Now turn your motherboard and gently position your SD card slot on top of it, use an insulated material between them and attach it[[BR]]

attachment:sdfront.jpg

[[BR]]

'''Step 6: Other hacks and result'''

----
If you need to make other hacks or evaluate your board is now time to do it, from my photos you can see also the serial port modification, WHR-G54S has one inside[[BR]]
I've made a small PCB with a MAX232 chip to get proper input from AP and convert it to a true RS232 Serial interface, flipped and used some insulation material between motherboard and Max so i can close the AP and have a good result, i've also placed an heat sink on top of CPU for safety (and overclocking as well)[[BR]]

attachment:sdandserial.jpg attachment:serial.back.jpg

[[BR]]

[[BR]]

'''Step 7: Final'''

----
Now place your modded AP inside its lower case, gently cut the case to have space for inserting SD cards

attachment:onbox.jpg

Cut front panel

attachment:buffalo.front.jpg

And insert SD to test it properly, as you can see you've SD out on the right side so it's very easy to insert and extract it

attachment:sd.front.inserted.jpg

In this detail you can also see serial port connector on top of WHR, use a cross over cable to connect to a PC

attachment:serial.mounted.jpg

[[BR]][[BR]][[BR]][[BR]]

== And here's final result :-) ==

attachment:work.done.jpg

[[BR]]
Hope information provided can help you, this AP is very cheap but powerful, you can have SD, Serial and even I2C on spare GPIO.[[BR]]
Reach me on openwrt forum for details or drop me an email on my account: (user: andreabenini    domain: gmail &nbsp;&nbsp; D o t &nbsp;&nbsp; com)

Have Fun[[BR]]

'''''Andrea (Ben) Benini'''''
