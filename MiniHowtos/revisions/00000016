Here we can put up a couple of MiniHOWTOs for Users.

= Networking =
= Software =
This section should describe commonly-used packages, built-in Busybox tweaks, and things of that nature.

== Making getty work with serial console ==
To be written (by koitsu, h0h0h0)

= Useful details =
[:EditingRomFiles] Howto edit the original files that are read-only in the ROM image

[:HowtoEnableCron] Enable cron to run scheduled tasks

[:PublishYourWANIp] Howto publish your WAN IP address to a webserver instead of using DynDNS

= Build fails with "404 File Not Found" errors =
Please see the [http://openwrt.ksilebo.net/Bugs OpenWRT Bugs Page] for further details and workarounds.

= boot_wait - What it is, and how it works =
The information here is all verified against a WRT54G verion 1.0.  There are minor changes with various hardware revisions moving forward, but the general principles remain the same, and the final result is the same.  To really understand boot_wait, you need to understand the boot process on the WRT, and how arp tables work.  When the boot loader begins, it starts by validating the nvram data.  If this data is valid, it checks for the existence of the variable boot_wait.  If boot_wait=on, the loader will go into a state that we call 'the boot wait state' in #wrt54g.  It will sit in this state for 3 seconds, before proceeding with a normal boot.  The next step of the boot is to crc check the kernel and root file system.  If the crc check fails, the router falls back into boot_wait state, and stays there.  If the crc check passes, the router loads the kernel from flash, and executes it.

During the boot_wait state, the loader will be accepting ethernet packets on eth0 (which is normally configured to be the 4 port switch).  It does not contain a full ip stack, and is only looking for 2 types of packets.  An arp request addressed to the ethernet broadcast will be replied to with an address of 192.168.1.1, and it's own ethernet address in the packet.  A tftp packet that has an ethernet address corresponding to the router, will be accepted.  The router does no gratuitous arps to prime the switches during the boot.  In normal circumstances, if you just try tftp put a valid firmware file to the router during this 3 second period, it will accept the file, and once it's gathered the entire file, it'll do header and crc checks on it.  If they both pass, the file will be written to the flash, and the router restarted.

The easiest way to send a file during boot is to just start the tftp tranfer (binary mode) to 192.168.1.1 during the 3 second window of opportunity.  In particular in some situations on various networks, this is a bit problematic, because the arp tables are not updated correctly, or there are old stale arp entries laying around.  In that case, you can bypass the arp stage altogether, and just set a static arp entry for an otherwise unused ip on your lan, with a hardware address of the router.  Start the tftp put to that address, and it will happily accept the tftp transfer, it's looking only at the ethernet portion of packet addresses, and ignoring the ip.  By statically setting arps, you will be able to send it at any address.  The reason many folks are successful in sending a firmware to a different ip number, the one the router was configured for before reboot, is not because the router is responding to the ip, but because the arp tables are already in place.

The most common problem we hear about is folks under the mistaken impression that the tftp server requires a username and password to send a file during boot_wait state.  This is FALSE.  There is a tftp server inside the standard Linksys firmware load, that has that behaviour.  If you see that error message, then you missed the boot_wait timing, or, you dont have boot_wait set on the router to begin with.  In that case, you are really trying to upload firmware the hard way, and you may as well just go to the admin page on the router, and send it in as a 'firmware upgrade'.

Some known variations on the ip number.  Apparently the Version 2.0 units always respond to address 192.168.1.1 mode when in boot_wait state.  I dont know if this is because they are responding to the arps, or if its because they are sending a gratuitous arp to prime the tables on the network when they boot.  It's actually irrelavent, with a V2 or GS unit, sending to 192.168.1.1 will always get to the right place, and if it's not working, its because you have something else wrong in the system, most likely you dont have the boot_wait nvram variable set.

Another variation on boot_wait state that's been used to successfully recover 'dead' units is the fact it does a crc check on the kernel before loading and executing.  If you short the right pair of address lines on the flash during boot, the boot loader will read back fine, but, addresses farther down in memory will have read errors, and generate a crc failure, sending the router into the boot_wait state for good.  Remove the item causing the short on the address lines (normally a small screwdriver), and you can now tftp in a new firmware, and it'll get written to the flash.


