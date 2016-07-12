= Linksys WGA54G =
Please refer to http://forum.openwrt.org/viewtopic.php?pid=35988 for thread details.

== Hardware ==
 * CPU: ARM based
 * RAM: 16MB
 * FLASH: 1MB
 * OS: ThreadX
 * WIFI: Prism54g

== Boot Loader ==
Unknown. Here is the boot menu (does anyone know what it is ?).
{{{
          Bootloader Version 00-02-03, Jul 15 2003 21:59:18
       Copyright 2003. All rights reserved. 

Press any key to stop auto-boot...
                        Main menu

        ?         - print this menu
        f         - load from Flash and go
        l         - load from TFTP server to SDRAM (no save to Flash, no go)
        L         - load from TFTP server to SDRAM and go (no save to Flash)
        @         - load from TFTP server to SDRAM,save to Flash and go
        g         - go from address
        b         - show boot parameters
        c         - change boot parameters
        d         - display factory default parameters
        m         - modify/set factory default parameters
        p         - ping test (ping other station from the target)
        r         - read memory
        s         - change mac address only
        w         - write memory
BOOT> 
}}}

== Serial console ==
J10 is 3,3v TTL

{{{
|
|                 __
|                |  |
|           __    --
| GND ->   |  |  |  |  <- TX
|           --    --
|          |  |  |  |
|    (J10)  --    --
|          |  |  |  |
|           --    --
| VCC ->   |  |  |  |  <- RX
|           --    --
|
|
}}}
Configure teminal with 19200 bauds, 8 bits, no parity, 1 stop bit (19200 8N1), hardware and software flow control both disabled.

== Boot log ==
{{{
Power-On Self Testing...
Testing SYS Controller...
Testing MEM Controller...
SDRAM Configuration:ROW12_COL8_BANK2
Testing SDRAM Memory ...
From 0x80000000 - 0x80FFFFFF
Testing CPU Data RAM...
Testing CPU Internal Registers...
Testing Timer 0...
Testing Timer 1...
Testing DMA Controller...
Testing INT Controller...
Testing PCMCIA Controller...
Testing USB Controller...
Testing Cardbus...
Testing PCI...
Power-On Self Test Passed
}}}

----
CategoryModel
