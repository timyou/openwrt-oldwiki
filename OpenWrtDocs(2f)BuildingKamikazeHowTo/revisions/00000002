== Building Kamikaze - Jan 2008 ==


I am a newbie trying to get involved in openwrt/x-wrt. I had difficulty figuring out how to set up a build environment. Instructions found in the x-wrt wiki at http://wiki.x-wrt.org/index.php/Compile_Kamikaze_with_Webif%5E2 were outdated and did not work for me on Sun 6 Jan 2008. 

With assistance from `forum2006` on the freenode.net #openwrt IRC channel I was able to get `kamikaze` to compile. 

=== Failure ===

I thought that I would be better off with `kamikaze_7.09` because I was afraid of an unstable trunk. So, that is the path that I started down, using the instructions from the aforementioned web page. 

I ran into conflicts with packages. If I did not symlink the packages under the build tree then `kamikaze_7.09` would compile OK. But, if I did the symlinks there were problems:

 * some conflicts with symlinks
 * `make menuconfig` would segmentation fault 

`trunk` had a number of problems with the symlinks when I tried to follow the instructions at the wiki page mentioned above. 

=== IRC help is on the way ===

I went to the `#openwrt` IRC channel on freenode.net and asked. I was told the following by `forum2006`:

 * there are no svn tags for the packages associated with kamikaze_7.09 release. there may have been at one point, but they were deleted
 * `kamikaze_7.09` is now ancient
 * I was encouraged to check out and compile `trunk`
 * I was given the following instructions `forum2006`:
{{{
##### Compiling Kamikaze Trunk from source

cd ~
svn -q checkout https://svn.openwrt.org/openwrt/trunk/ ~/trunk/
cd ~/trunk/
./scripts/feeds update
make defconfig
make package/symlinks
make menuconfig          # Select your target, packages and other options. Only select the packages you need.
make world

make -jN world           # Enables parallel builds. Replace N with the number or core CPUs you have on your system.
}}}

I tweaked these steps slightly, choosing to make an `openwrt` subdir in my home directory.

==== Update on this at 12 Jan 2008 ====

For some reason the procedure mentioned above keeps webif out of the feeds package.
To fix, this is my way of compiling:

{{{
$ svn co https://svn.openwrt.org/openwrt/trunk/
$ cd trunk
$ ./scripts/feeds update
$ make defconfig
$ make package/symlinks
$ cd package
$ ln -s ../feeds/xwrt xwrt
$ cd ..
$ make menuconfig
$ make 
}}}

=== GNU make v3.81 required ===

I started on an old (but reliable) machine running Fedora Core 4. When I got to the first `make defconfig` command because of a GNU make version dependency. FC4 with current yum updates only had GNU make v3.80 installed, but v3.81 was required to build OpenWrt. So, I switched to a Fedora 7 machine with GNU make v3.81 installed and started the process over. 

=== Successful compile ===

Compilation seems to have gone OK. Not sure how long the build took ... 30 minutes < OpenWrtBuildTime < 2 hours for me. 

Now I just need to get up the nerve to try to install it on my WRT54GS ... Yikes! :)
