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

= `boot_wait` - What it is, and how it works =
The information here is all verified against a WRT54G version 1.0.  There are minor changes with each variable hardware revision (1.0 vs. 1.1 vs. 2.0 vs. GS), but the general principles remain the same, as well as the final result.  To really understand `boot_wait`, you need to understand the boot process on the WRT54G, and how ARP tables work.

When the boot loader begins, it starts by validating the nvram data (configuration data that is stored in Flash).  If this data is valid, it checks for the existence of the variable `boot_wait`.  If `boot_wait` is set to `on` (boot_wait=on), the loader will go into a state that we call 'the boot wait state' on #wrt54g (IRC).  This state is also referred to as PMON.

The WRT54G will remain in this state for 3-5 seconds before proceeding with loading the kernel.  The next step of the bootstrap is to do a CRC check of the kernel and root file-system.  If the CRC check fails, the router falls back to PMON and stays there.  If the CRC check passes, the router loads the kernel from flash and executes it.

During the `boot_wait` state, the loader will be accepting Ethernet packets on eth0 (which is normally configured to be the 4 port switch).  '''It does not contain a fully-working IP stack''', and is only looking for 2 types of packets: ARP broadcasts and incoming TFTP attempts.

An ARP request addressed to the Ethernet broadcast will be replied to with an address of 192.168.1.1, and it's own Ethernet address in the packet.  A TFTP packet that has an Ethernet address corresponding to the router, will be accepted.  Under normal circumstances, if you TFTP put a valid firmware image during the 3-5 second window, the unit will accept the file, and once finished receiving it, will execute header and CRC checks on it.  If both pass, the firmware is written to Flash, and the unit is restarted.

The easiest way to send a file during boot is to just start the TFTP tranfer (binary mode) to 192.168.1.1 during the 3-5 second window of opportunity.  In particular in some situations on various networks, this is a bit problematic, because the ARP tables are not updated correctly or there are old stale ARP entries laying around (on another switch, or on the client PC; most layer-2 equipment does some form of ARP caching).  In this case, you can bypass the ARP stage altogether and set a static ARP entry for an otherwise unused IP on your LAN with the MAC address of the router.  Once you've added a static ARP entry for that MAC, you should be able to communicate with the WRT54G regardless of what IP it has.

The most common problem we hear about is folks under the mistaken impression that the TFTP server requires a username and password to send a file during boot_wait state.  '''This is FALSE.'''  There is a TFTP server enabled within the stock Linksys firmware; '''this is not the same thing as PMON'''.  If you attempt to TFTP a firmware image to the unit while it's TFTP server is running, you'll receive an error message claiming "incorrect password" or something of that nature.  If you see that error message, then you missed the `boot_wait` window of opportunity or you didn't set `boot_wait` to on.  In this case, you can still update the firmware via the Web-based "Firmware Upgrade" page.  Note that once you've upgraded, it's highly recommended that you do enable `boot_wait` anyways.

Some known variations on the IP number.  Apparently the Version 2.0 units always respond to address 192.168.1.1 mode when in boot_wait state.  I dont know if this is because they are responding to the arps, or if its because they are sending a gratuitous arp to prime the tables on the network when they boot.  It's actually irrelavent, with a V2 or GS unit, sending to 192.168.1.1 will always get to the right place, and if it's not working, its because you have something else wrong in the system, most likely you dont have the boot_wait nvram variable set.

Another variation on boot_wait state that's been used to successfully recover 'dead' units is the fact it does a crc check on the kernel before loading and executing.  If you short the right pair of address lines on the flash during boot, the boot loader will read back fine, but, addresses farther down in memory will have read errors, and generate a crc failure, sending the router into the boot_wait state for good.  Remove the item causing the short on the address lines (normally a small screwdriver), and you can now tftp in a new firmware, and it'll get written to the flash.


