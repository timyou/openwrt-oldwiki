

3.4. Select SquashFS or JFFS2

You will notice that in that same directory, where we have <type> you will find "SquashFS" and "JFFS2"

    * SquashFS - SquashFS files include a small compressed filesystem within the firmware itself. The disadvantage is that Squashfs is a readonly filesystem, to save changes and make the filesystem appear writable a separate JFFS2 partition has to be used; the advantage is that Squashfs takes up slightly more space than JFFS2, and you'll always have the original files on the readonly filesystem which can be used as a boot device for recovery.
    * JFFS2 - JFFS2 make the entire filesystem JFFS2. The disadvantage is that this takes slightly more space; the advantage is that changes to included files nolonger leaves behind an old copy on the readonly filesystem.

FileSystem i would like to build a cat :)
