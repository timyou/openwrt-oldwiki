== Requirements ==
The build-system checks for the requirements and print what's missing on your system. Then install the packages.

To manually check the prerequisites run

{{{
$ make prereq
}}}

Note for Mac OS X Users:
To build your images on a Mac OS X Machine all you need is the package "fileutils" from the fink project. (Tested on Leopard 10.5.3)
== Actual commands ==
{{{
$ cd ~
$ svn checkout https://svn.openwrt.org/openwrt/trunk/ ~/kamikaze/
$ cd ~/kamikaze/
$ ./scripts/feeds update -a                 # Checkout the extra packages
$ ./scripts/feeds install <name_1> <name_2> # Creates the symlinks for the packages you like to install
$ make menuconfig                           # Select your target, packages and other options. Only select the packages you need.
$ make world
}}}

== Configuring a custom kernel ==
While you won't typically need to do this, if you need to modify the Linux kernel configuration, use this command to enter the regular Linux menuconfig:
{{{
$ make kernel_menuconfig
}}}
