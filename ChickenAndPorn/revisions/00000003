##master-page:HomepageTemplate
#format wiki
== Allan Clark AKA ChickenAndPorn ==
Email: [[MailTo(allanc@chickenandporn//dot//com)]]

Dude, what's with the name?  A joke, well, stuck to me.  Note that this wiki seems to think my name is evil (it seems to not like chicken)

Currently bricking:
||grey01 ||[:Hardware/Linksys/WRTSL54GS:wrtsl54gs] ||WhiteRussian-rc6 ||need to WPA, UPnP, USB, SIP, and connect via Motorola HT820 :) ||
||grey02 ||[:Hardware/Linksys/WRTSL54GS:wrtsl54gs] ||||<style="text-align: center;">successfully bricked, HairyDairyMaid-proof ||
||blue ||[:Hardware/Linksys/WRT54G:wrt54g v4] ||WhiteRussian-rc5 ||BridgingAccessPointHowto ||


The SDK doesn't quite work on MacOSX

=== WRTSL54GS Post-ISL work ===
WRTSL54GS required some post-ISL edits (so I remember):

 * ipkg install lsusb kmod-vfat kmod-usb-storage kmod-usb-ohci (easier: install my cnp-wrtsl54gs ipk)
 * reboot ("insmod kmod-usb-ohci" seems to hang)
 * mounts whatever it finds on the USB chain, even through HUBs (unlike Linksys and XBox)
 * still no UPnP, Gaim/Adium via NAT seems to go
=== Install My Work ===
If you want to use my stuff, go ahead!

 1. edit {{{/etc/ipkg.conf}}} add {{{src cnp http://allanc.chickenandpoXX.com/openwrt }}}( s/XX/rn/ - openwrt thinks ... err... pork is still marked as such)
 1. "System", "Installed Software", "Update package lists"
 1. click to install "cnp-wrtsl54gs"
 1. if I update my setup (including getting aMule to work) you'll get the updates :)
=== Todo ===
 1. SMB server
 1. aMule port (currently completed packages/amule, working on packages/wxwidgets)
----
 CategoryHomepage
