[[TableOfContents]]


/!\ '''WARNING  LOADING AN UNOFFICIAL FIRMWARE WILL VOID YOUR WARRANTY''' /!\

= Introduction =
This guide is intended for beginners to Linux and/or !OpenWrt.  This guide is dedicated for updating !OpenWrt on the !LinkSys WRT54GL router and the experiences gained by it.  This information is specific to the WRT54GL, however, it can be applied to all routers that are compatible with OpenWrt.  For information on installing !OpenWrt please visit InstallingWrt54gl.  This article assumes you have installed OpenWrt before as there would be no other need to update.

/!\ '''Reflashing with OpenWrt WILL RESET THE FILESYSTEM''' /!\

= Updating OpenWrt =
You may wish to reflash the WRT54GL or router of your choice for any number of reasons.  It can be done two different ways such as through the web interface or using tftp (or atftp).

=== Updating using Router Web Interface ===
To update !Open Wrt using the router's web interface simply access the web interface page at 192.168.1.1.

If you have problems accessing the web interface page first try clearing your browser cache.  If that doesn't work it may be possible that your version of !OpenWrt does not support the web interface or it may not be available for other reasons.  If you cannot access the web interface page please use the next updating method.  If you can access the web interface page continue with this section.


Then go to system - > administration - > firmware upgrade.  Locate the !OpenWrt Firmware Image file and that's it.  Be sure that the power supply is stable and not disconnected during transfer.  After your installation depending on the type of !OpenWrt you chose you may need to restart you router.  Many people have reported inconsistent results.  RussNelson notes that v4.30.0 gave the "Upgrade are failed!" error, but upgrading to Linksys.com's v4.30.5 reflashed OpenWRT just fine.

=== Updating using tftp ===
Before updating your WRT54GL using tftp you need to make sure BOOT_WAIT option is on.

==== Turn BOOT_WAIT ON ====
By default, boot_wait is "off" on the WRT54GL routers, in fact, most routers have boot_wait "off" by default. Turning boot_wait "on" simply increases the time it takes to boot.  Turning Boot_wait "on" increases that window of opportunity and makes it easier to catch and install OpenWrt.
Apparently, on some routers you can install older firmware that enables a ping exploit where commands can be typed directly into the routers Web Interface to turn Boot_wait "on" or "off". This does not work with WRT54GL so do not try to roll back the firmware, it is not recommended. In fact, turning Boot_wait "on" for installing OpenWrt on the WRT54GL using tftp is not necessary (but it helps). 

There atleast three different ways to turn BOOT_WAIT ON.

1.  Easiest - Access the web interface on the WRT54GL and turn the BOOT_WAIT option on.  You should actually do this immediately after installing !OpenWrt for the first time.

2.  Moderate - You can telnet into your router by typing "telnet 192.168.1.1" which allows you access to the console.  At this point type "nvram get BOOT_WAIT" into the console.  It will reply telling you yes or no. If it says "yes" you are fine, leave it alone.  If it says "no" type "nvram set  BOOT_WAIT=on".  To confirm, type "nvram get BOOT_WAIT=on" and verify that it says "yes".  Afterwards, you need to commit it to memory.  Type "nvram commit".  And that's it.  BOOT_WAIT is on!

3.  Hard - The only reason this is hard is because the WRT54GL does not have a standard serial port ready to connect to.  You need to modify your board in order to install one.  For more information on installing a serial port to your WRT54GL check out this page InstallSerialWrt54gl.  If you have one connected simply plug it into the serial port of another PC (Linux or Windows) and open a hyperterminal.  Connect at 9600 baud and then turn on your router.  You'll notice that the everything gets dumped to the terminal including information prior to !OpenWrt loading.  Once you get access to the console follow the steps above in the Moderate section for connecting using telnet.  It's the same method at this point.


Boot_wait console information can also be obtained from http://wiki.openwrt.org/OpenWrtDocs/BootWait?highlight=%28bootwait%29.

==== tftp Transfer ====
The reason tftp is useful is because overall it is fast, it can all be done on the command line.

tftp is mainly recommended for those looking to install their own self compiled images of !OpenWrt, because it can also be used to recover from a problem and allow you to put on another Firmware Image, whether it is !OpenWrt or the original from !LinkSys.  This is only relevant in the event that something happens to the router, the install was interrupted or the code causes the router to crash.  You can then use tftp to reflash the router with another firmware.  If something happens to you router the Web Interface may not be available to you.  This is where tftp shines!

atftp is the same as tftp except it's supposedly an advanced version.

Updating !OpenWrt is the same as installing !OpenWrt.

This is the process I use when updating !OpenWrt.  I use a self-compiled image called JFFS2 because I want to be able to write to the system.    Set everything up so that you can telnet (or ssh) into the router.  Make the connections but do not turn your router on.

On another PC with Linux open a terminal and type the following command:

atftp --trace --option "timeout 1" --option "mode octet" --put --local-file openwrt-xxx-x.x-xxx.bin 192.168.1.1 (where the x's are you version)

Then hit enter. (keep your router off during this)

Now hit control-C to cancel.

Now turn on your router.

Now type "telnet 192.168.1.1"  (if it doesn't connect the first time you may have tried connecting to early, simply try again)

When you are connected you should be in the !OpenWrt console,type "reboot".

At this point you are back in the linux terminal, hit the up arrow twice to bring the "atftp --trace..." command back on the screen.  Hit enter.

Timing is everything at this point.  You have to be quick.  If you take too long you will miss the window (that BOOT_WAIT gives you).  And it's easier to miss than you think.  This is why I make sure to keep the "atftp ..." command in memory.  It makes it easier and quicker to bring up.  You could very easily just have it ready in another terminal.  What ever your preference is the idea is that you have to be quick and in order to be quick you need to have the "atftp ..." command previously typed.

You know you made it in time when you see your PC transfer over the image in 512mb blocks.  Wait for it to finish before doing anything else.  And make sure the power does not get disconnected.

Because I deal with the JFFS2 !OpenWrt image I have an extra reboot step.  You have to wait around 30-40 seconds after the transfer is complete.  At that point you will see the power light flash on the WRT54GL router.  Only then should you power it down and power it back up (basically, turn it off and on).  At this point it is ready to go.  Telnet into it again and you're in your updated !OpenWrt.
