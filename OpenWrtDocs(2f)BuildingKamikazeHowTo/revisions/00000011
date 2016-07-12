== Requirements ==
The build-system checks for the requirements and print what's missing on your system. Then install the packages.

To manually check the prerequisits run

{{{
$ make prereq
}}}
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
