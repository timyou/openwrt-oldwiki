= LED System Load Monitor =
Credit goes to SeRi for starting this mod. He had it use the wrt's white and amber LEDs (version 3 only) to show system load. I thought it was a very nifty mod, but I couldn't use it, as the white and amber LEDs are used for the read/write lines on the SD card mod. So what did I do? I modded the mod of course! Now anyone with a spare LED can use this mod. you just need to set the correct GPIO pin. For wrt54g's version 2-3, gpio 7 is for the DMZ LED, which is what I use. You can modify the source accordingly. This will flash the LED once per second under normal useage, twice per second under medium load, and when there is a high load on the system, the LED flashes 3 times per second.'' ''

'''NOTE: You will need to compile your kernel with the Busybox option for usleep enabled. This is what is used for the LED strobing'''

'''Installing Necessary Software'''

First of, grab the [http://downloads.openwrt.org/inh/programs/loadmon.sh loadmon.sh] script, and [mbm]'s [http://downloads.openwrt.org/gpio.tar.gz GPIO tool]. Then untar the gpio tool, and copy the files to your /usr/sbin directory. A typical way to do this on a jffs2 install would go as follows. If you are using squash fs, then you shoudl know what to do.

{{{
cd /tmp
wget http://downloads.openwrt.org/inh/programs/loadmon.sh
wget http://downloads.openwrt.org/gpio.tar.gz
gzip -d gpio.tar.gz
tar xvf gpio.tar
mv gpio /usr/sbin
mv loadmon.sh /usr/sbin
}}}

Now that everything is in place, you need to edit your configuration files to start up the script manually when the router boots. To do this, create a script in /etc/init.d to start loadmon.sh. Here's a simple way to do that:

{{{
echo "#!/bin/sh" > /etc/init.d/S60loadmon
echo "/usr/sbin/loadmon.sh &" >> /etc/init.d/S60loadmon
chmod +x /etc/init.d/S60loadmon
}}}

Now reboot and test it out :)

If you dont want to build your own firmware, and you own a router with the white and orange lights, you can try this script. It will show the white light if load is low, white and orange at medium load, and orange at high load:

{{{
#!/bin/sh

#Set GPIO to the GPIO of the LED you wish to use.
# Default is 7 for DMZ LED on most routers..
GPIOG=2
GPIOR=3
DELAY=2
HIGHLOAD="70"
MEDLOAD="30"

while sleep $DELAY; do
   load=$(cat /proc/loadavg | cut -d " " -f1 | tr -d ".")
   #echo $load

    if [ "$load" -gt "$HIGHLOAD" ]; then
        gpio enable $GPIOG
        gpio disable $GPIOR
    elif [ "$load" -gt "$MEDLOAD" ]; then
        gpio disable $GPIOG
        gpio disable $GPIOR
    else
        gpio disable $GPIOG
        gpio enable $GPIOR
    fi
done
}}}
