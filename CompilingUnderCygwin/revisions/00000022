== Compiling under Cygwin ==
This is still a work in progress. To date, I do not believe that the complete image has been build under Cygwin. I can get past the toolchain build, so that you can cross-compile your programs. 

=== Setup cygwin ===
 * Obviously we need [http://www.cygwin.com/ Cygwin].  Required packages are at least tar, sed, flex, gcc, vim, wget, unzip, ncurses-devel, perl, patch and make.

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

=== What else do we need ===

 * Obviously the [http://downloads.openwrt.org/whiterussian/newest/ OpenWrt source].

{{{
cd ~
wget http://downloads.openwrt.org/whiterussian/newest/whiterussian_rc4.tar.bz2
tar -xvjf whiterussian_rc4.tar.bz2
}}}

 * A really up to date make version: [ftp://alpha.gnu.org/gnu/make/ Make 3.81 Beta 4]

{{{
cd ~
wget ftp://alpha.gnu.org/gnu/make/make-3.81beta4.tar.bz2
tar -xvjf make-3.81beta4.tar.bz2

cd make-3.81beta4
./configure
make
make install
cp make.exe /usr/bin
cd ~
}}}

 * Some updated header files. 
  * /usr/include/elf.h
  * /usr/include/byteswap.h
  * /usr/include/bits/*
You can get these from either a Linux machine that has/can compile OpenWrt, or you can grab them from Nate True's website [http://devices.natetrue.com/openwrt/cygwin-include-x86.zip].  Note that these files are likely to need to be from a system of the same CPU type.  The ones on Nate True's site are for the Intel x86 32-bit or compatible architecture.

{{{
cd ~
wget http://devices.natetrue.com/openwrt/cygwin-include-x86.zip
cd /usr/include
unzip ~/cygwin-include-x86.zip
cd ~
}}}

 * The libraries. Having no available Linux box (my current one had hard drive troubles), I scrabled around websites, mostly www.opensolaris.org, looking for whichever file Cygwin complianed about. Eagle_Fire was nice enough to send me his. Thanks again!

=== Compiling ===

==== Start the configuration ====
{{{
$ make menuconfig
}}}
Leave all defaults and save the configuration to the default file.

==== Start compiling ====
{{{
$ make
}}}

If make causes an error relating to wildcards, you need to edit openwrt/rules.mk

Find this section:

{{{
     ifeq ($(BR2_TAR_VERBOSITY),y)
     TAR_OPTIONS=-xvf
     else
     TAR_OPTIONS=-xf
     endif
}}}

Add "--wildcards" to two lines, as shown below.

{{{
     ifeq ($(BR2_TAR_VERBOSITY),y)
     TAR_OPTIONS=--wildcards -xvf
     else
     TAR_OPTIONS=--wildcards -xf
     endif
}}}

 * If you did this right, you should get past the inital startup and it'll start downloading the kernel. It kept going for about an hour and a half. It failed after building the cross compiler, while building the debugger. If this is all you need.. fine. I'm going for gold. It fails because it expects gdb to be called gdb, instead it's called gdb.exe. To fix this, edit openwrt/toolchain/gdb/Makefile

{{{
$ vi ~/openwrt/toolchain/gdb/Makefile
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

==== Patching ====

{{{
#
patch -d /home/Yasha/openwrt/build_mipsel/lzma -p1 < lzma-406-zlib-stream.patch
#
patching file SRC/7zip/Compress/LZMA/LZMADecoder.cpp
#
Hunk #1 FAILED at 288.
}}}

Eagle_Fire got it to work by manually applying the patch, and editing the makefile to remove the automatic patching. I got it to work a different way.

I was manually applying the patch, and noticed ^M's at the end of the patch file. tojoe on IRC told me that they were misinterpreted linebreaks, and dos2unix fixed that. I ran:
{{{
$ dos2unix target/lzma/lzma-406-zlib-stream.patch
target/lzma/lzma-406-zlib-stream.patch: done.
}}}

and the patching worked. Thanks tojoie!

The same patching must also be done to the following two files, at least:

{{{
$ dos2unix target/linux/linux-2.4/patches/generic/105-netfilter_TTL.patch
target/linux/linux-2.4/patches/generic/105-netfilter_TTL.patch: done.

$ dos2unix target/linux/linux-2.4/patches/generic/000-linux_mips.patch
target/linux/linux-2.4/patches/generic/000-linux_mips.patch: done.
}}}

Or just use:
{{{
target/linux/linux-2.4/patches/generic/*.patch
}}}

==== Patching the patches ====

Then the patches need to be patched. Yes! This is because the file ipt_CONNMARK.c is the same ipt_connmark.c under windows, but not under Linux.
I did this with vi for "105-netfilter_TTL.patch" with
{{{
:1,$s/ipt_TTL\./ipt_TTL_target\./gIc
}}}

And for "112-netfilter_connmark.patch" with
{{{
:1,$s/ipt_CONNMARK\./ipt_CONNMARK_target\./gIc
:1,$s/ipt_TTL\.o/ipt_TTL_target\.o/gIc
}}}

That brought me through the patching. (Maybe - i can't remember if not - see  below)

BUT the error is caused for more files because there are more of them having the same name in uppercase and lowercase. So an unpack script is needed to unpack "linux-2.4.30.tar.bz2" to give these files an differnt name. Then this script needs to be injected into the existing Makefiles.

----

I've written an makefile that does the most oft the patching. Some of the Makefiles need to be patched too. It's not tested for correct handling with directorys (may not work when openwrt tar is unpacked into a different directory, but it should). And, against my hope there are some include files from real linuxes needed for compilation.
So i need someone with some time to test this, having an real linux available for bringing this hole thing to end. Mail me (m_kanter {[alt/gr][q]} web {.} de) if you want the files.

----

That's all I have so far. If you have any ideas, find Flyashi on #openwrt. I'd appreciate the help... thanks!

Oh and HUGE thanks to Eagle_Fire for most of these insructions! And tojoe for the patch file fix. Thanks guys!
