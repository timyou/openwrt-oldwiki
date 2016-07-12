'''''WP18: Running '''OpenWrt''''' on Compex loader Information''''' ''

1. The following Steps will show you how to upgrde Open-WRT with Compex Loader Ver 2.40 or above(Manual Upgrade).

2. If you wish to do the automatic upgrade you read "AUTOMATIC CONVERTER" Section.

----
'''NOTE !!!'''

----
Make sure that you are using:

 * You are using WP18 model loaded with Compex loader V2.4 or above.
 * Please ensure that Ethernet connection is connected you should able to
  . ==> ping 192.168.168.1 .
 * You are in the firmware upgrade mode
  . ==> (By Press and hold the Reset button and plug-in the power adaptor).
 * Get Ready to Section "Compex firmware to Open-WRT firmware."
----
'''''Start'''''

Go to the Console (CMD/DOS) Open the folder that contain files required.

Then follow the steps below.

1. Write OpenWrt image (kernel) to flash

 . > tftp -i 192.168.168.1 put flashwrt-kernel.cmd > tftp -i 192.168.168.1 put openwrt-ixp4xx-2.6-zImage
2. Write OpenWrt image (rootfs) to flash

 . > tftp -i 192.168.168.1 put flashwrt-jffs.cmd > tftp -i 192.168.168.1 put openwrt-ixp4xx-2.6-jffs2-128k.img
3. Change the partition table to load OpenWrt image format

 . > tftp -i 192.168.168.1 put partwrt.cmd
4. Create a RedBoot style fconfig area

 . > tftp -i 192.168.168.1 put fconfig-crt.cmd
5. Write a RedBoot style fis area

 . > tftp -i 192.168.168.1 put flashwrt-fis.cmd > tftp -i 192.168.168.1 put fis.bin
6. Finish and Reboot the AP.

7. To test whether you are successful, in converting to Open-WRT,

 . Please do followings command in DOS
  . > telnet 192.168.1.1
  * The picture shows below will be appear if you are successfull.
  * The first boot time will be alittle longer than usual, so please wait for awhile
8. FINISH. The device already load with OpenWRT version.

----

----
'''''AUTOMATIC CONVERTER (Easier Method )'''''

----
From the folder that contain all files, Run "Autoconvert.bat"

 1. Follow the steps and the command show in the Console (CMD/DOS form).
 1. It takes up to 2 minute for entire Process.
 1. Enjoy.
 1. To test whether you are successful in converting to Open-WRT,
  . Please do the followings command in DOS
  > telnet 192.168.1.1
  * The picture shows above will be appear if you are successful. b. The first boot time will be alittle longer than usual,so please wait a momment. c. If you can't see the picture above, u can reboot the device and reinstall it.
----
 .
----
'''''Open-WRT to Compex Firmware'''''

----
If you wish to change back to Compex Firmware, Please follow the Steps below.

 . =Start=
 * Go to the "LOADER MODE" by PRESS AND HOLD the reset button and plug in the adapter
  . (LED will blink faster).
 * Load the firmware to the WP18.
  . > tftp -i 192.168.168.1 put <Firmware name>
 * Finish and Reboot the AP.
 * To test whether it is successfully installed. You can run U-Config Utility or
  . Log on to Http://192.168.168.1/
<FIRMWARE NAME> WP18 = WP18_V208_B0103.IMG

 . PLease use the latest firmware as it is available from
  . http://www.compex.com.sg/
  . . =End=
  . . .
----
Updated 16 March 2006
