'''Buffalo WBR2-G54'''

The WBR2-G54 is based on the Broadcom 4712 board. It has a 200MHz CPU, 4Mb flash and 16Mb RAM.
The wireless NIC is integrated to the board. `boot_wait` is on by default.

Please keep in mind that for now we can't control the LEDs.
If you brick WBR2-G54 and need to restore to factory settings you should use 2.32 firmware as others wil not work (constant reboots).

/!\ '''This router sits on 192.168.11.1 as default, but flashable always on the last IP You have set up, so You have to TFTP to that address.'''

= Installing =
 * Download the firmware image (openwrt-brcm-2.4-squashfs.trx)
 * Plug the ethernet cable directly into lan port #1 on the router.
 * Open a terminal window, and ping the router on 192.168.11.1. This is the default address for this router.
{{{
      64 bytes from 192.168.11.1: icmp_seq=660 ttl=64 time=0.865 ms
}}}
   If you don't get reponses like above then you will need to make sure that you've got everything plugged in correctly, and that you have valid ips and the like. Leave this ping command running, it will be important in a minute.
 * Open another terminal window, make sure that you're in the same directory as the downloaded firmware, and fire up tftp. Enter the following, but don't hit return on the last command, we want it ready to fire in the several second window that we'll have.
{{{
      tftp 192.168.11.1
      tftp> binary
      tftp> trace
      tftp> rexmt 1
      tftp> timeout 60
      tftp> put openwrt-brcm-2.4-squashfs.trx 
}}}
 * Now, press and hold the INIT button on the router, 5 seconds or so. The DIAG led should flash slowly. Watch the window with the ping running, and you should see something like:
{{{
      64 bytes from 192.168.11.1: icmp_seq=663 ttl=64 time=0.867 ms
      64 bytes from 192.168.11.1: icmp_seq=664 ttl=64 time=0.900 ms
      64 bytes from 192.168.11.1: icmp_seq=671 ttl=100 time=2.351 ms
      64 bytes from 192.168.11.1: icmp_seq=672 ttl=100 time=0.992 ms
      64 bytes from 192.168.11.1: icmp_seq=673 ttl=100 time=1.732 ms
      64 bytes from 192.168.11.1: icmp_seq=674 ttl=100 time=2.032 ms
}}}
   There are 2 things to note here, there is a gap of 5 seconds or so between the second and third line, and the third line has a ttl of 100, rather than 64. This is an indicator that the router is listening for tftp connections and can load the firmware.
 * When you see the ttl=100 line in the ping output, hit return in the other window to start the tftp process. If all goes well, you should see
{{{
      tftp> put openwrt-brcm-2.4-squashfs.trx
      sent WRQ <file=open2.trx, mode=octet>
      received ACK <block=0>
      sent DATA <block=1, 512 bytes>
      received ACK <block=1>
      ...
}}}
 * Sit tight for a few minutes, don't interrupt the power or you could wind up with a half flashed brick. The router should reboot, respond to the pings again, and be accessible through telnet or http.

----
(Instructions taken from http://www.wiredfool.com/discuss/msgReader$2460)

= misc =
J5 is is the serial interface, pinout as follows:

{{{
     CPU

TX    o
RX    o
VCC   o
GND   o

     LEDS
}}}

J10 is the usual EJTAG.


----
CategoryModel
