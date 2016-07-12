= LED System Load Monitor =
Credit goes to SeRi for starting this mod. He had it use the wrt's white and amber LEDs (version 3 only) to show system load. The project was looking a little out of date, and it didnt work with most routers. I figured id fix it up a little. This script will cause the front light to be off with load below 0.20, white above 0.20 and below 0.40, A light orange (looks yellow to me) from 0.40 to 0.70, and orange above 0.70.

'''Adding the scripts'''

Add the following script to /usr/sbin/loadmon.sh

{{{
#!/bin/sh

DELAY=1
HIGHLOAD="70"
MEDLOAD="40"
LOWLOAD="20"

while sleep $DELAY; do
        load=$(cat /proc/loadavg | cut -d " " -f1 | tr -d ".")
        echo $load
      
        if [ "$load" -gt "$HIGHLOAD" ]; then
                echo "0" > /proc/diag/led/ses_white
                echo "1" > /proc/diag/led/ses_orange
        elif [ "$load" -gt "$MEDLOAD" ]; then
                echo "1" > /proc/diag/led/ses_white
                echo "1" > /proc/diag/led/ses_orange
        elif [ "$load" -gt "$LOWLOAD" ]; then
                echo "1" > /proc/diag/led/ses_white
                echo "0" > /proc/diag/led/ses_orange
        else
                echo "0" > /proc/diag/led/ses_white
                echo "0" > /proc/diag/led/ses_orange
        fi
done
}}}

Now set the new script as executable, and add it to be started at boot time.

{{{
chmod +x /usr/sbin/loadmon.sh
echo "#!/bin/sh" > /etc/init.d/S60loadmon
echo "/usr/sbin/loadmon.sh &" >> /etc/init.d/S60loadmon
chmod +x /etc/init.d/S60loadmon
}}}

Now reboot and test it out :)
