= boot_wait - What it is, and how it works =
Information here was verified with a WRT54G 1.0.  There are minor changes with each variable hardware revision (1.0 vs. 1.1 vs. 2.0 vs. GS), but the general principles remain the same, as well as the final result.  To really understand {{{boot_wait}}}, you need to understand the boot process on the WRT, and how ARP tables work.

When the boot loader begins (PMON on v1.x and CFE on v2.x), it starts by validating the nvram data (configuration data that is stored at the end of flash).  If this data is valid, it checks for the existence of the variable {{{boot_wait}}}.  If {{{boot_wait}}} is set to {{{on}}} ({{{nvram set boot_wait=on}}}), the loader will go into a "boot_wait state".

The WRT will remain in this state for 3 seconds before proceeding with loading the kernel. The next step of the bootstrap is to do a CRC check on the trx file stored in flash (trx contains kernel and root file-system; bin file is trx with some extra headers).  If the CRC check fails, the router falls back to the boot loader and stays there, waiting for a new firmware.  If the CRC check passes, the router loads the kernel from flash and executes it.

During the 3 second {{{boot_wait}}} state, or if the CRC fails, the loader will be accepting Ethernet packets.  '''It does not contain a fully-working IP stack''', and is only looking for 2 types of packets: ARP broadcasts and incoming TFTP attempts.

An ARP is an "Address Resolution Protocol" which converts an IP address into a mac address (machine address / hardware address), used for basic ethernet communication. An ARP request for 192.168.1.1 will return the mac address of the router. While in boot_wait, the router will accept any packet with the correct mac address, regardless of IP address. In particular in some situations on various networks, this is a bit problematic, because the ARP tables are not updated correctly or there are old stale ARP entries laying around (on another switch, or on the client PC; most layer-2 equipment does some form of ARP caching).  In this case, you can bypass the ARP stage altogether and set a static ARP entry for an otherwise unused IP on your LAN with the MAC address of the router.

If you TFTP put a valid firmware image during the 3-5 second window, the unit will accept the file, and flash the file and proceed to boot -- which will then check the CRC. The easiest way to send a file during boot is to just start the TFTP tranfer (binary mode) to 192.168.1.1 during the 3-5 second window of opportunity.

The most common problem we hear about is folks under the mistaken impression that the TFTP server requires a username and password to send a file during boot_wait state.  '''This is FALSE.'''  There is a TFTP server enabled within the stock Linksys firmware; '''this is not the same thing as {{{PMON}}} or {{{CFE}}}'''.  If you attempt to TFTP a firmware image to the unit while the Linksys TFTP server is running, you'll receive an error message claiming "incorrect password" or something of that nature.  If you see that error message, then you missed the {{{boot_wait}}} window of opportunity or you didn't set {{{boot_wait}}} to on.  In this case, you can still update the firmware via the Web-based "Firmware Upgrade" page.  Note that without boot_wait set, recovery is tricker, so once you've upgraded it's highly recommended that you do enable {{{boot_wait}}}.

If you have a v2 or GS unit, during the {{{CFE}}} phase, '''you will always be able to reach the unit at IP 192.168.1.1'''.  If this doesn't work for you, you likely forgot to enable {{{boot_wait}}}.

If you do end up with a 'dead' WRT unit due to not enabling {{{boot_wait}}}, there's still hope. Please see [http://voidmain.is-a-geek.net:81/redhat/wrt54g_revival.html VoidMain's WRT54G Revival Page].
== Setting Via the console ==

With a serial connection to your WRT, you don't have to use the ping bug or change your Linksys firmware. You can set boot_wait from the console, using the commands

{{{
#nvram set boot_wait=on
#nvram get boot_wait           (just to confirm, should respond with "on")
#nvram commit                  (takes a few seconds to complete)
}}}

You can also set boot_wait from the [:OpenWrtDocs/Customizing/Firmware/CFE:CFE] boot loader (to enter CFE, reboot the router with "# reboot" while hitting {{{CTRL-C}}} continously)

{{{
CFE> nvram set boot_wait=on
CFE> nvram get boot_wait       (just to confirm, should respond with "on")
CFE> nvram commit              (takes a few seconds to complete)
}}}

Or via PMON (older models, hit {{{CTRL-C}}} repeatedly during powerup or reboot)

{{{
PMON> set boot_wait on
PMON> set nvram boot_wait
}}}
