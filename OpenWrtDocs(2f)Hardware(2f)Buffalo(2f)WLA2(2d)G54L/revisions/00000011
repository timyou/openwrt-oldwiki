'''Buffalo WLA2-G54L'''

The WLA2-G54L is based on the Broadcom 4712 board. It has a 200MHz CPU, 4Mb flash and 16Mb RAM.
The wireless NIC is integrated to the board. `boot_wait` is on by default.

CFE version used on WLA2-G54L resets switch VLAN settings to default on boot. Partial fix is adding VLAN configuration to init-scripts. However, since all four ethernet ports are switched together until init-scripts run this is not good solution.

/!\ '''This router sits on 192.168.11.100 (or 192.168.11.1) as default, but flashable always on the last IP You have set up, so You have to TFTP to that address.'''

J5 is is the serial interface, pinout as follows:

{{{
     CPU

TX    o
RX    o
VCC   o
GND   o

     LEDs
}}}
----
CategoryModel
