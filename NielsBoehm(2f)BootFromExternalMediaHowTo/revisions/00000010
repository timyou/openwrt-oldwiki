#PRAGMA section-numbers off

= Boot from external media HowTo =

This is about how to swap in external media, such as MMC/SD cards or USB drives, as the root filesystem using the existing init.d/rc.d and uci/config infrastructure. In contrast to OpenWrtDocs/KamikazeConfiguration/PackagesOnExternalMediaHowTo, this is done without replacing files and will keep the original /etc tree in place in order to ensure consistency of your configuration.

== Motivation ==

While OpenWrtDocs/KamikazeConfiguration/PackagesOnExternalMediaHowTo also describes a way to use your mass storage devices on your router for package installation etc., I felt I wanted to use a more robust way to achieve that and also wanted to have consistent configuration, no matter if my SD card was mounted as / or not.

So my first idea was to stack another mini_fo filesystem on top of the existing one (which overlays /jffs over /rom), which would enable me to keep both the files from the read only squashfs partition plus the changes I made on the jffs2 partition while writing subsequent changes to my SD card. Unfortunately, this turned out to crash my system and I suspect mini_fo being unable to provide 2 instances at the same time (at least on top of each other).

Well, the alternative that remains is that you first have to duplicate most of the original filesystem tree to the mass storage device, so that you don't shoot yourself in the foot when pivoting to the new root.

Unfortunately, duplicating all of it would mean you would have two separate configurations under /etc, one when the original filesystem is in place and the other when the mass storage devices takes over. This is not a good idea not only since it would be headache to keep in sync, but also because the new root is not swapped in at the very beginning - at the time our script gets executed we're already in the middle of the /etc/rc.d/* process and /etc/init.d/rcS has already determined the scripts to execute and would thus be umimpressed by changes under rc.d due to a pivoted root, meaning it would not notice scripts that have newly appeared (due, for instance, to a service which you installed on your mass storage device) and would try to execute scripts that have vanished. Also, the scripts executed before this bootext script may have referred to configuration on the original tree while scripts executed thereafter will refer to configuration on the mass storage device.

This is calling for trouble, so our solution is to bind mount the original /etc tree to the same place on the new root. This works quite well (also for squashfs+jffs2-images with mini_fo overlay) and means you only have to deal with a single config at all times, mass storage swapped in or not.

----

[[Include(NielsBoehm/EtcConfigBootExt,,editlink)]]
