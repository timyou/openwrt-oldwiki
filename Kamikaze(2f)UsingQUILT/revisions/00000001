= Using QUILT to add patches =

{{{
cd trunk/
make package/busybox-{clean,prepare} V=99 QUILT=1
cd build_dir/i386/busybox-1.8.1
quilt new 530-gunzip_src_fd.patch
quilt add 530-gunzip_src_fd.patch
EDITOR=mousepad quilt edit archival/libunarchive/decompress_unzip.c    # make the changes and save and exit the editor
quilt refresh
cd trunk/
make package/busybox-update V=99                                       # copies the new patch to package/busybox/patches/530-gunzip_src_fd.patch
make package/busybox-{clean,compile}
}}}
