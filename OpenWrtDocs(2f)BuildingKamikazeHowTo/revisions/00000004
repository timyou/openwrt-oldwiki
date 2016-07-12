== Requirements ==
GNU make 3.81

Lots more

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
