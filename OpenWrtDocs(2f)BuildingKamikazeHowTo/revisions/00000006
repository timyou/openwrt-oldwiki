== Requirements ==
GNU make 3.81

Lots more

'''Debian Etch:'''
{{{
apt-get install subversion g++ libncurses5-dev zlib1g-dev bison flex unzip autoconf gawk make
}}}


== Actual commands ==
{{{
cd ~
svn -q checkout https://svn.openwrt.org/openwrt/trunk/ kamikaze-trunk
cd kamikaze-trunk
./scripts/feeds update
make defconfig
make package/symlinks
make menuconfig          # Select your target, packages and other options. Only select the packages you need.
make world

make -jN world           # Enables parallel builds. Replace N with the number of logical CPUs you have on your system.
}}}
