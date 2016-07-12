''''''

{{{

'''Information'''

}}}
1. The following Steps will show you how to upgrde Open-WRT with Compex Loader Ver 2.40 or above(Manual Upgrade).

2. If you wish to do the automatic upgrade you read "AUTOMATIC CONVERTER" Section.

----
{{{

'''NOTE !!!'''

}}}
----
'''''Make sure that you are using:'''''

 1. You are using WP546E model.
 1. Only WP546E guantees the support of Open-WRT. b. We do not bear any responsibility to any changes of other WP54. -
 1. Your curent Compex loader version is V2.4 or above. -
 1. Please ensure that ethernet connection is connected and able to ping address = 192.168.168.1 . -
 1. You are in the firmware upgrade mode
 ==> (By Press and hold the Reset button and plug-in the power adaptor).

 1. Get Ready to Section "Compex firmware to Open-WRT firmware."
----
'''''''''' '''

{{{

'''''Compex firmware to Open-WRT firmware.'''''

}}}
. =Start='''''''

 . . In Console(CMD/DOS) type command bellow.
 * Write OpenWrt image to flash.
  . > tftp -i 192.168.168.1 put flashwrt.cmd > tftp -i 192.168.168.1 put openwrt-wp54g-2.4-squashfs.trx
 (This might takes Up to 1 Minute, So please wait for awhile)
 * Change the partition table to load OpenWrt image format.
  . > tftp -i 192.168.168.1 put partwrt.cmd
 * Create a default NVRAM partition.
  . > tftp -i 192.168.168.1 put nvram-crt.cmd
 * Finish and Reboot the AP.
 * To test whether you are successful, in converting to Open-WRT,
  . Please do followings command in DOS
  . > telnet 192.168.1.1
 * The Open-WRT picture will be appeared if you are successfull. b. The first boot time will be alittle longer than usual, so please wait for awhile.
  . =End=''''' '''''
----

{{{

'''''AUTOMATIC CONVERTER'''''

}}}
----
 1. From the folder that contain all files, Run "Autoconvert.bat"
 1. Follow the steps and the command show in the Console (CMD/DOS form).
 1. It takes up to 2 minute for entire Process.
 1. Enjoy.
 1. To test whether you are successful in converting to Open-WRT, Please do the followings command in DOS
 > telnet 192.168.1.1

 1. The picture shows above will be appear if you are successful.
  . b. The first boot time will be alittle longer than usual,so please wait a momment.
 c. If you can't see the picture above, u can reboot the device and reinstall it.
----
'''''''''' '''

{{{
'''''Open-WRT to Compex Firmware '''''

}}}
If you wish to change back to Compex Firmware, Please follow the Steps below.

=Start= ''''''

 1. Go to the "LOADER MODE" by PRESS AND HOLD the reset button and plug in the adapter (LED will blink faster).

 1. Load the firmware to the WP54g or wp54ag
 > tftp -i 192.168.168.1 put <Firmware name>

 1. Finish and Reboot the AP.

 1. To test whether it is successfully installed. You can run U-Config Utility or
 Log on to [http://192.168.168.1/ Http://192.168.168.1/]
----
||||<tablewidth="677px" tablestyle="WIDTH: 677px; HEIGHT: 105px"style="TEXT-ALIGN: center">'''<FIRMWARE NAME>''' '''''' ||
||'''WP54AG ''' ||WP54AG_MSSID_V207_B0205.IMG or WP54AG_V151_B0131.IMG ||
||'''WP54 G ''' ||WP54G_MSSID_V207_B0205.IMG or WP54G1B_V151_B0131.IMG ||


----
 . . PLease use the latest firmware as it is available from
 http://www.compex.com.sg/
 . . =End=
----
.
