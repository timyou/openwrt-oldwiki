~+'''Building Kamikaze !HowTo'''+~

__Valid for the following releases:__ Kamikaze, White Russian

[[TableOfContents]]

== Development Environment ==
If you are not used to a Linux development environment or not sure how to set it up correctly, then first check out the [:OpenWrtDocs/Development/SetupBuildEnvironmentHowTo: Setup Build Environment HowTo].

== Requirements ==
The build-system checks for the requirements and print what's missing on your system. Then install the packages.

To manually check the prerequisites run

{{{
$ make prereq
}}}
Note for Mac OS X Users: To build your images on a Mac OS X Machine all you need is the package "fileutils" from the fink project. (Tested on Leopard 10.5.3)

== Actual commands ==
Login with a normal user, not root!
Create a directory inside your home to hold the !OpenWrt code.
Then checkout the development code with Subversion ([http://svnbook.red-bean.com/ All about using Subversion]).
Accept the certificate when asked, you can verify its correctness with a browser and the same URL.
{{{
$ mkdir ~/kamikaze-trunk/
$ cd ~/kamikaze-trunk/
$ svn checkout https://svn.openwrt.org/openwrt/trunk/ .
}}}
Get all the extra packages, the ones for Luci and if you wish the ones for Xwrt too.
Then install the packages you need, so that you can choose them later in the menuconfig.
{{{
$ ./scripts/feeds update packages luci      # Checkout the extra packages
$ ./scripts/feeds install -a -p luci        # Install the LuCI WebUI (selected and included in the final image by default)
$ ./scripts/feeds install <name_1> <name_2> # Creates the symlinks for the packages you like to install
}}}
Call the configuration menu, set the desired target, select the wanted packages and save. Then start building with make.
{{{
$ make menuconfig                           # Select your target, packages and other options. Only select the packages you need.
$ make V=99 ; echo -e '\a'                       # The echo is a bell/beep/alert in BASH (here Debian GNU/Linux), when make finishes
}}}
== Configuring a custom kernel ==
While you won't typically need to do this, if you need to modify the Linux kernel configuration, use this command to enter the regular Linux menuconfig:

{{{
$ make kernel_menuconfig
}}}

== Customizing the Target Filesystem ==
Directions are available [http://downloads.openwrt.org/docs/buildroot-documentation.html#custom_targetfs here].

== Additional Documentation ==
 * BuildRoot
 * http://downloads.openwrt.org/docs/buildroot-documentation.html

== Packages that do not compile ==
 * '''Missing source code file, due to download problems'''.
 First check if the URL path in the make file contains a trailing slash, then try with it removed (helped several times).
 Otherwise try to download the source code manually and put it into ~/kamikaze-trunk/dl
 * '''dsl-qos-queue''' in revision 14750 ([https://dev.openwrt.org/ticket/4706 Ticket]) {{{
 ./scripts/feeds uninstall dsl-qos-queue}}}
 * '''kmod-ucmb''' in revision 14750 ([https://dev.openwrt.org/ticket/4711 Ticket]) {{{
 ./scripts/feeds uninstall kmod-ucmb}}}
 * '''quagga''' & '''quagga-unstable''' in revision 14750 (Ticket) {{{
 ./scripts/feeds uninstall quagga quagga-unstable}}}
 * '''qwo''' in revision 14750 (Ticket) {{{
 ./scripts/feeds uninstall qwo}}}
 * '''xsupplicant''' in revision 14750 (Ticket) {{{
 ./scripts/feeds uninstall xsupplicant}}}


CategoryHowTo
