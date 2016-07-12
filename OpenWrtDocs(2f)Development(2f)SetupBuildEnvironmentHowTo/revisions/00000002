~+'''Setup Build Environment !HowTo'''+~

__Valid for the following releases:__ Kamikaze, White Russian

[[TableOfContents]]

= Foreword =
This !HowTo will use [http://www.debian.org/ Debian GNU/Linux] as the development platform inside a virtual machine on Windows with [http://www.virtualbox.org VirtualBox].
Linux users should be able to distinguish between Windows and Linux to filter the information they really need.

= Initial Virtual Machine Setup and Debian Installation =
To setup the development system download [http://www.debian.org/distrib/ Debian] (here  5.0), only DVD #1 is needed, and install it inside a virtual machine (VM) of [http://www.virtualbox.org VirtualBox].
 * In the VM creation assistent use Linux, Debian, 768MB RAM, 8GB virtual harddisk
 * If a personal firewall is used, make sure that !VirtualBox can access the internet and act as a server for the trusted zone (LAN). Permanently or temporary as preferred. This is necessary to install the latest updates and to access the VM via SSH later.
 * Set the boot options to only boot from harddisk.
 * Assign the Debian DVD image to the VM's CD/DVD-ROM drive
 * For installation start the VM, hit F12 to access the boot menu and choose CD-ROM.

During the Debian installation...
 * Choose English as the system's language, as it is best for international projects (e.g. bug reports, etc.)
 * Choose your correct country (e.g. via others) and keyboard layout (keymap)
 * Please include a network mirror near to you (for the latest updates)
 * Only the standard system is needed. No desktop environment, etc.
Otherwise all the defaults are ok.

= Further Debian Setup and Configuration =
After Debian installed...
 * Login as the root user (=Super-Admin in Linux/Unix)
 * Mount the DVD-ROM image again, check if it got mounted, maybe /etc/fstab has to be corrected (/dev/hdc could be wrong) and if wished can later be unmounted
{{{mount /dev/hdc     # hdc could also be hdb, look via ls -la /dev/hd* | grep cd
ls /cdrom

nano /etc/fstab

umount /cdrom}}}
 * Refresh the package list, install OpenSSH server and poweroff the virtual machine
{{{aptitude update
aptitude install openssh-server
poweroff}}}

= Further Virtual Machine Configuration =
 * Add access to the SSH port of the Debian virtual machine in !VirtualBox (see manual chapter 6.4.1 and chapter 8)
{{{cd /d "%ProgramFiles%\Sun\xVM VirtualBox"
vboxmanage setextradata "<VM name|GLOBAL>" "VBoxInternal/Devices/pcnet/0/LUN#0/Config/guestssh/Protocol" TCP
vboxmanage setextradata "<VM name|GLOBAL>" "VBoxInternal/Devices/pcnet/0/LUN#0/Config/guestssh/GuestPort" 22
vboxmanage setextradata "<VM name|GLOBAL>" "VBoxInternal/Devices/pcnet/0/LUN#0/Config/guestssh/HostPort" 22}}}
Start the Debian virtual machine again.
You should now be able to login via SSH (e.g via [http://www.chiark.greenend.org.uk/~sgtatham/putty/ Putty] or [http://www.winscp.net/ WinSCP]) from the host system to the virtual machine (localhost:22).

= Setting Up the Build Environment =
 * Install [http://subversion.tigris.org/ Subversion] (short: svn) to get the latest source or a specific revision,  the typical build tools and screen if you want to put the compilation into the background
{{{aptitude install subversion build-essential screen
}}}
 * Follow the instructions of the [:OpenWrtDocs/BuildingKamikazeHowTo: Building Kamikaze HowTo].
 * After compilation you will find the build in the bin folder. Copy it with [http://www.winscp.net/ WinSCP] to the host system for easier flashing.

== Table of known prerequisites and their corresponding packages ==
{{{make menuconfig}}} will tell you if more packages have to be installed via APT by the root user.
Here's a table with the package name for each prerequisite separated for different Linux distributions.

||'''Prerequisite'''||'''Debian'''||'''Suse'''||'''Red Hat'''||
||ncurses||ncurses-dev||?||?||
||zlib||zlib1g-dev||?||?||
||GNU awk||gawk||?||?||
||GNU bison||bison||?||?||
||flex||flex||?||?||
||unzip||unzip||?||?||
||GNU autoconf||autoconf||?||?||

Installation example for a fresh Debian 5.0r0: {{{aptitude install ncurses-dev zlib1g-dev gawk bison flex unzip autoconf}}}

Notes:
 * Ubuntu = Debian
 * In Debian use {{{apt-cache search "<prerequisite>"}}} to find a fitting package for a prerequisite

CategoryHowTo
