'''Dynalink RTA770W - Siemens SE515'''


'''There is no running OpenWrt up to now!'''

The original sources can be requested on the homepage for this router.

And the sources for the Siemens ["Hardware/Siemens/SE515"] are availible.


They contains the same board, but siemens ships it with a different case and firmware.
By default, Dynalink puts in an Annex A firmware, while Siemens uses Annex B.

/!\ '''boot_wait should be on by default.'''

You can check it looking at the "Test" led on boot. If it lights for about 5 seconds, boot_wait is on.

/!\ '''THIS PORT IS STILL EXPERIMENTAL'''

Nothing will work, at the moment there is only a kernel that boots. Stop. There is need for testers.

'''Serial port'''

A serial port (TTL levels, you need a TTL/232 level shifter, very simple to build) can be found inside it.
The pinout refers to the board seen from above, with connectors on top and leds on bottom.
{{{
Serial connector

   1 2 3 4
   _______
  |o o o o|
   --   --

1) Vcc (3.3V)
2) GND
3) Tx (data from the router to the serial port)
4) Rx (data from the serial port to the router)
}}}


----
CategoryModel ["CategoryBCM63xx"]
