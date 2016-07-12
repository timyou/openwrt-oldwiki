[:OpenWrtDocs]
[[TableOfContents]]
= Using the Jffs2 root filesystem =
This page is about some of the practical issues of using the new Jffs2 root filesystem
available in the experimental version of OpenWrt.

= Choice of root filesystems =
The "experimental" version of the OpenWrt firmware includes a choice of two root filesystems (selected by choosing the right firmware image):

 * SquashFS Root -- this is the "classic" layout, also used in the "stable" version of the firmware
 * Jffs2 Root -- this is a new layout

If you use the SquashFS root, you end up with two filesystems in Flash RAM.  
The SquashFS itself is a read-only filesystem (which ends up mounted as /rom) that is part of the firmware image and is not changed except when upgrading firmware.  
The unusued portions of the Flash RAM are used to create a separate Jffs2 filesystem, which is writeable. 
This Jffs2 filesystem is initialised with softlinks that point back to the SquashFS ROM.  These links can be removed and new files can be loaded in their place.
The Jffs2 filesystem is normally preserved after firmware upgrades (although it will be lost if the image gets significantly larger).
This layout has the advantage of preserving changes at the cost of some extra complexity (all the softlinks) and some small amount of wasted space (ROM files which are replaced still take up space).

    Note: as of White Russian RC4, the jffs2 filesystem is [http://forum.openwrt.org/viewtopic.php?pid=22502 always reinitialised] when you replace the squashfs filesystem.

If you use the Jffs2 root, you end up with a single filesystem containing all the files stored in the Flash RAM.
This filesystem is writeable but all changes are lost if the firmware is upgraded.

In both cases, of course, there is also a ''ramfs'' filesystem mounted on ''/tmp'' which uses ordinary RAM -- this is lost on every reboot.
For more information about the two roots, see the explanation from '''mbm''' in [:OpenWrtDocs/Installing].

The rest of this page is about practical ways to make use of the Jffs2 root.

= Loading a Jffs2 image =
It is important, when using the Jffs2 root, to use an image built for the correct Flash RAM size.  
For example, when using a Jffs2 image with an Asus WL500G, which has a 4MB Flash, use the ''openwrt-generic-jffs2-4MB'' image.

Once the image is loaded it will boot for the first time.  
This takes some time (about a minute in my experience) before you can telnet into the system.
The time is spent doing some magic to the Flash RAM layout to separate the Jffs2 root from the kernel.

When you telnet into the system you will see that the root filesystem is read-only, so you can't make any changes to it. 
The '''mount''' command will include the following line:

{{{
/dev/root on / type jffs2 (ro)
}}}

The Flash RAM layout displayed by looking at ''/proc/mtd'' will appear to be something like:

{{{
dev:    size   erasesize  name
mtd0: 00040000 00010000 "pmon"
mtd1: 003b0000 00010000 "linux"
mtd2: 00190000 00010000 "rootfs"
mtd3: 00010000 00002000 "nvram"
mtd4: 001a0000 00010000 "OpenWrt"
}}}

This is perfectly normal.  You now need to reboot the system.

After the reboot, you can telnet in again and the system will now be modifiable.  The '''mount''' command will now show:

{{{
/dev/root on / type jffs2 (rw)
}}}

And ''/proc/mtd'' will now show something like:

{{{
dev:    size   erasesize  name
mtd0: 00040000 00010000 "pmon"
mtd1: 003b0000 00010000 "linux"
mtd2: 00330000 00010000 "rootfs"
mtd3: 00010000 00002000 "nvram"
}}}

You can now make changes to the root filesystem.  These changes will be preserved across reboots (as long as they are not in the ''/tmp'' or ''/var'' directories)
but '''will all be lost if the firmware is reloaded'''.
The way to preserve changes when loading a new image is to make changes in the image itself.

Note that loading a new image is easily done using Openwrt itself, rather than using the bootloader.  Once you have built your new image, with your new filesystem included, you copy the image into the ''/tmp'' directory on the router.  For example:

{{{
scp bin/openwrt-generic-jffs2-4MB.trx asus:/tmp
}}}

Then, on the router, use '''mtd''' to load the image into flash and reboot:

{{{
mtd -r write /tmp/openwrt-generic-jffs2-4MB.trx linux
}}}

The '''-r''' is important as the replacement of the running system filesystem will mean that the system will be very confused if it is not immediately rebooted!

= Changing the files in the image =

To change files in the image you need to have the OpenWrt Buildroot installed.  
Within that kit, there is documentation in the ''docs/buildroot-documentation.html'' file.  
This explains that there are two ways to customise the filesystem.
This page only explains using the ''target/default/target_skeleton/'' method, as the goal is to make changes which will last even if the software is rebuilt.

== Packages ==

The best way to have custom packages installed is to use the facilities already present in the build environment.  
This is documented in the ''docs/buildroot-documentation.html'' file.

== The target skeleton ==

The filesystem is initialised by copying the contents from the ''target/default/target_skeleton/'' directory in the Buildroot.
Note that hidden files (with a leading dot) do not seem to be copied.
Also note that not '''all''' files on the resulting filesystem are stored in this skeleton: some are created during the build process itself
(this includes the SSH host key, which is regenerated on each build).

The most common change is likely to be to add additional procedures to be run on startup.  
These can just be added to the ''target/default/target_skeleton/etc/init.d'' directory.

== Rebuilding ==

If you make changes to the target skeleton, you can rebuild the filesystem just by issuing a ''make'' command.  
You should then test your changes by loading them onto your target system

= System-specific changes =

If you have more than one OpenWrt system, you will need to have a way to make changes that are specific to each system.
The way to do this is to set each system's hostname in the NVRAM (by setting the ''wan_hostname'' variable) and then to use that name to load specific changes.

You can then use the hostname to run specific startup scripts that make particular changes to the system.
To do this, create a script in the ''target/default/target_skeleton/etc/init.d'' directory called ''S60host-specific'' and give it the following content:

{{{
#!/bin/sh
HOST=$(uname -n)
for i in /etc/init.d/$HOST-* ;do
  $i start 2>&1 | logger -s -p 6 -t ''
done
}}}

Do not forget to make it executable ({{{chmod +x S60host-specific}}}).

This script will then search for and execute any scripts in the ''/etc/init.d'' directory which start with the hostname followed by a hyphen.

For example, to set a host called ''alex'' up to use another system as a DNS resolver, you could create a script called ''alex-dns'' containing:

{{{
#!/bin/sh
#
# Create the correct resolv.conf for a normal node
#
rm -f /etc/resolv.conf
echo "search home.cobb.me.uk" >/etc/resolv.conf
echo "nameserver 192.168.0.252" >>/etc/resolv.conf
}}}

= Backing up files =

Of course, changing the files in the loadable image is not the only way to preserve files during upgrades.

Recent OpenWrt firmware ships with two scripts (''/sbin/backup'' and ''/sbin/restore'') which backup and restore your /etc directory and list of installed packages.
This can be very useful but remember that it will restore everything in your /etc directory.
This does not work very well with Jffs2 images because it ends up saving and restoring everything, including the files which are part of the system and which may have changed for good reasons.
For that reason, it is more useful with SquashFS images where it does not save anything that you have left unmodified.
