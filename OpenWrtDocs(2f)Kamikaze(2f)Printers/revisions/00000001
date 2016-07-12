= HowTo run HP LaserJet 1018/1020/1022 on OpenWRT Kamikaze 7.06 =
At first a install foo2zjs  drivers from http://foo2zjs.rkkda.com/ on linux box.

It's instruction from  http://foo2zjs.rkkda.com/

{{{
„Click the link, or cut and paste the whole command line below to download the driver.
    $ wget -O foo2zjs.tar.gz http://foo2zjs.rkkda.com/foo2zjs.tar.gz
Now unpack it:
Unpack:
    $ tar zxf foo2zjs.tar.gz
    $ cd foo2zjs
Now compile and install it. The INSTALL file contains more detailed instructions; please read it now.
Compile:
    $ make
Get extra files from the web, such as .ICM profiles for color correction,
and firmware.  Select the model number for your printer:
    $ ./getweb 2430     # Get Minolta 2430 DL .ICM files
    $ ./getweb 2300     # Get Minolta 2300 DL .ICM files
    $ ./getweb 2200     # Get Minolta 2200 DL .ICM files
    $ ./getweb cpwl     # Get Minolta Color PageWorks/Pro L .ICM files
    $ ./getweb 1020     # Get HP LaserJet 1020 firmware file
    $ ./getweb 1018     # Get HP LaserJet 1018 firmware file
    $ ./getweb 1005     # Get HP LaserJet 1005 firmware file
    $ ./getweb 1000     # Get HP LaserJet 1000 firmware file
Install driver, foomatic XML files, and extra files:
    $ su                        OR      $ sudo make install
    # make install
(Optional) Configure hotplug (USB; HP LJ 1000/1005/1018/1020):
    # make install-hotplug      OR      $ sudo make install-hotplug
(Optional) If you use CUPS, restart the spooler:
    # make cups                 OR      $ sudo make cups ”
}}}
Next you must transfer  sihp1020.dl to your Asus box.

On Asus You should install packages :

{{{
 ipkg install kmod-usb-printer
 ipkg install p910nd
}}}
When do you have problem with depends  kmod-nls-base. You should edit /usr/lib/ipkg/lists and remove depends for your pacage.

Next:

{{{
/etc/init.d/p910nd enable
/etc/default/p910nd I leave without any changes !!!!
}}}
Next you need to create script that uploads the firmware to your printer after you've plugged it it.

Create a new file /etc/hotplug.d/usb/hplj1020:

{{{
#!/bin/sh
FIRMWARE="/mnt/pendrive/sihp1020.dl"
 < -- place where you have your .dl file.
if [ "$PRODUCT" = "3f0/2b17/100" ]
then
        if [ "$ACTION" = "add" ]
        then
                echo "`date` : Sending firmware to printer..." > /var/log/hp
                cat $FIRMWARE > /dev/usb/lp0
                echo "`date` : done." > /var/log/hp
          fi
}}}
You must change parameter 3f0/2b17/100 for your printer.

3f0/517/120 it is idVendor/idProduct/bcdDevice, from device descriptor. Numbers are hexadecimal, without leading '0x' or zeros.

This parameters you can get from ls with v option. More info you can find at http://linux-hotplug.sourceforge.net/?selected=usb .

=== Using WRT54G(S/L) SES button for Radio Control ===
This is a remake of a code that is found on http://wiki.openwrt.org/OpenWrtDocs/Customizing/Software/WifiToggle

Step 1: Create the button/ folder inside /etc/hotplug.d/ if it doesn't exist

Step 2: cd to this dir and edit a new file named 01-radio-toggle

Step 3: Paste this code inside the file

{{{
if [ "$BUTTON" = "ses" ] ; then
        if [ "$ACTION" = "pressed" ] ; then
                WIFI_RADIOSTATUS=$(wlc radio)
                case "$WIFI_RADIOSTATUS" in
                0)
                        echo 2 > /proc/diag/led/power
                        wlc radio 1
                        wifi
                        echo 1 > /proc/diag/led/ses_white
                        echo 1 > /proc/diag/led/power ;;
                1)
                        echo 2 > /proc/diag/led/power
                        wlc radio 0
                        echo 0 > /proc/diag/led/ses_white
                        echo 2 > /proc/diag/led/wlan
                        echo 1 > /proc/diag/led/power ;;
                esac
        fi
fi
}}}
Step 4: Save the file and just test it, it will light Wlan and White SES Led when radio is on, and turn both off when radio is off
