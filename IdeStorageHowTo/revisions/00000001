'''IDE Storage HowTo'''

Some devices supported by !OpenWrt have an IDE interface.  To configure this:

 * install the ''kmod-ide'' package,
 * install the ''kmod-ext3'' package if you wish to use an EXT3 filesystem,
 * configure ''/etc/modules'' to load kernel modules in the correct order, for example:
 {{{
ide-core
pdc202xx_old
ide-detect
ide-disk
wl
jbd
ext3
}}}
 * load the modules manually using ''insmod'' or reboot,
 * check that the IDE drive is detected; the file ''/proc/partitions'' will contain a line for the whole disk and a line for each partition,
 * see LocalFileSystemHowTo for how to create filesystems and make them available to other hosts.
