= Howto use GDB to debug =
Note: This howto reflects the usage of Kamikaze

= Compiling Tools =
in menuconfig select

{{{
Advanced configuration options (for developers) [enter] ---> Toolchain Options  --->  [*]   Build gdb  }}}
Activate gdbserver

{{{
Utilities ---> gdbserver }}}
after running make you have a gdb in toolchain_ARCH/gdb-.../gdb/ you can use. The gdbserver package (resists under bin/packages/gdbserver-...) has to be installed on your board.

= Using GDB =
[http://sourceware.org/gdb/current/onlinedocs/gdb_18.html#SEC161 GDB Docs on remote debugging]

You can run programs in gdbserver on your target platform, while running the debugger under a different architecture and/or host. I usually start a screen shell and execute:

{{{
while true; do gdbserver [localip]:2222 PROGRAMM ARGS; sleep 5; done }}}
if you kill your programm it gets restarted automaticly.

Now to the host side:

{{{
# gdb
Copyright 2004 Free Software Foundation, Inc. GDB is free software, covered by the GNU General Public License, and you are welcome to change it and/or distribute copies of it under certain conditions. Type "show copying" to see the conditions. There is absolutely no warranty for GDB.  Type "show warranty" for details. This GDB was configured as "--host=i486-linux-gnu --target=powerpc-linux-uclibc".
(gdb) }}}
now you have a gdb shell. (# means now a gdb command)

{{{
# cd ../build_powerpc/package/...
}}}
this is important, so gdb can finde the source files

{{{
# symbol-file EXE}}}
 loads the symbols from the executable. This means, you don't have to run programs with symbol tables on your target !

{{{
# help files
}}}
gdb internal help is very usefull, under topic files you find other usefull tools, like loading symbols form libs  FIXME: how :)

now you can connect to your remote target

{{{
# target remote [localip]:2222
}}}
The program immediatly starts and waits.

{{{
# continue
}}}
let the program run until it crashes or you press ctrl+c to let it sleep again.

{{{
# bt
}}}
bt (Backtrace) is the most important function of gdb, it shows the complete stack, which gives a lot of information to a developer

PS: This is not a GDB Howto, just how to use GDB on openwrt.
