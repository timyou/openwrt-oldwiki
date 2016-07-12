[[TableOfContents]]


= Introduction =
This guide is intended for beginners to Linux and/or !OpenWrt.  This guide is dedicated to installing a single or dual serial ports on the !LinkSys WRT54GL router and !OpenWrt.  This information is specific to the WRT54GL, however, it can be applied to all routers that are compatible with !OpenWrt.  For information on installing !OpenWrt please visit InstallingWrt54gl.  This article assumes you have installed !OpenWrt.

= Wrt54gl Serial Port Mod =
The Wrt54gl has a 10 pin connection slot on the board called JP1.  This slot provides two TTL serial ports at 3.3V.  Neither of the ports use hardware flow control, you need to use software flow control instead.  Other routers may have similar connections.  These two TTL serial ports on the Wrt54gl router can be used as standard Serial Ports similiar to the serial ports you may have on your PC.  In order to do this though you need a line driver chip that can raise the signal levels to RS-232 levels.  You can not directly connect a serial port header to the board and expect it to work.  That method will only work with devices that can connect to TTL serial ports at 3.3V.

Once the modification is made you can have at most two serial ports to use for connecting devices etc.  By default, !OpenWrt uses the first serial port to access the built-in serial console on the router.  You can connect to it at 115200,8,N,1 using a windows hyperterminal for example.  This is helpful because if you have problems communicating with your router this method will allow you easy access connecting over a hyperterminal.  By default this leaves you with one serial port left, however, there is a method to turn the console off giving you access to both ports if you really need them.  It isn't recommended but it can be done.

In progress...


= Other pages by dRax =

 *InstallingWrt54gl
 *UpdatingWrt54gl
