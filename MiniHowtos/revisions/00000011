Here we can put up a couple of MiniHOWTOs for Users.

= Networking =
= Software =
= Useful details =
[:EditingRomFiles] Howto edit the original files that are read-only in the ROM image

[:HowtoEnableCron] Enable cron to run scheduled tasks

[:PublishYourWANIp] Howto publish your WAN IP address to a webserver instead of using DynDNS

= Build fails on bridge utils/dnsmasq =
(Maybe this is the wrong place to put this information, but it's the best place I could
find.)
Build tries to download bridge-utils from sourceforge, but that fails due to an
outdated url. One working url is
http://heanet.dl.sourceforge.net/sourceforge/bridge/bridge-utils-0.9.6.tar.gz
. After build aborted on that url I downloaded the package by hand, and started build
again.
The same for:
http://thekelleys.org.uk/dnsmasq/dnsmasq-2.7.tar.gz

The version 2.6, which is what the build system is actually looking for, has been moved to http://thekelleys.org.uk/dnsmasq/archive/dnsmasq-2.6.tar.gz - the system seems to fail when using it, however: it gunzip's at some point but preserves the .tar.gz extension. If the build fails, simply cd sources/dl && mv dnsmasq-2.6.tar.gz dnsmasq-2.6.tar && gzip dnsmasq-2.6.tar then restart the build.

coax's note: I just replicated the above info by creating a [:Bugs] page. I agree that this is not the first place that one would look for such info ;) I'll leave it to others to decide which should be deleted.
