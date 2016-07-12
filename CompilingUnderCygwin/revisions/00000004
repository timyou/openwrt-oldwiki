== Compiling under Cygwin ==
This is still a work in progress. To date, I do not believe that the complete image has been build under Cygwin. I can get past the toolchain build, so that you can cross-compile your programs. 

=== Requirements ===
 * [http://www.cygwin.com/ Cygwin] 
 * Some updated libaries. You can get these from either a Linux machine that has/can compile OpenWrt, or if you ask Eagle_Fire nicely, he might send you his.
 * [ftp://alpha.gnu.org/gnu/make/ Make 3.81 Beta 4]

=== More Prerequisites ===
 * In Cygwin, make sure that /bin or /usr/bin comes before Windows. This defaults for some, not for others. You can verify this with "which find":
{{{
$ which find
/usr/bin/find
}}}
If you get Windows find, then you have to change the path. You can do this inside Cygwin, but your changes will be temporary: just type
{{{
$ export PATH=/usr/bin/:$PATH
}}}
Now if you "echo $PATH" you should get /usr/bin/: as the first of a list of colon-separated directories.
* Right-click on "My Computer" and go to Properties, then Advanced, and click "Environment Variables". On the bottom window, "System Variables", find "PATH". Click "Edit" and add your cygwin bin directory, by default C:\cygwin\bin\, to the beginning of the path, remembering to add a semicolon after the path.

 * Compile and copy make. Four steps:
 1. ./configure
 2. make
 3. make install
 4. cp make.exe /usr/local/bim/make

 * The libraries. Having no available Linux box (my current one had hard drive troubles), I scrabled around websites, mostly www.opensolaris.org, looking for whichever file Cygwin complianed about. Eagle_Fire was nice enough to send me his. Thanks again!

=== Compiling ===

If you did this right, you should get past the inital startup and it'll start downloading the kernel. It kept going for about an hour and a half. It failed after building the cross compiler, while building the debugger. If this is all you need.. fine. I'm going for gold. It fails because it expects gdb to be called gdb, instead it's called gdb.exe. To fix this, edit openwrt/toolchain/gdb/Makefile

{{{
$ vim ~/openwrt/toolchain/gdb/Makefile
}}}

Here's the problem area:

{{{
     45 $(GDB_CLIENT_DIR)/gdb/gdb: $(GDB_CLIENT_DIR)/.configured
     46         $(MAKE) -C $(GDB_CLIENT_DIR)
     47         strip $(GDB_CLIENT_DIR)/gdb/gdb
     48
}}}

Change line 47, adding ".exe" to the end:

{{{
     45 $(GDB_CLIENT_DIR)/gdb/gdb: $(GDB_CLIENT_DIR)/.configured
     46         $(MAKE) -C $(GDB_CLIENT_DIR)
     47         strip $(GDB_CLIENT_DIR)/gdb/gdb.exe
     48
}}}

This will get you past the GDB, and it'll fail while patching the LZMA files.

{{{
#
patch -d /home/Yasha/openwrt/build_mipsel/lzma -p1 < lzma-406-zlib-stream.patch
#
patching file SRC/7zip/Compress/LZMA/LZMADecoder.cpp
#
Hunk #1 FAILED at 288.
}}}

Eagle_Fire got it to work by manually applying the patch, and editing the makefile to remove the automatic patching. I haven't tried it yet.

That's about it. If you have any ideas, find Flyashi on #openwrt. I'd appreciate the help... thanks!
