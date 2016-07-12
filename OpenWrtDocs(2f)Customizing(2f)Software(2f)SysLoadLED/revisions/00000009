= LED System Load Monitor =
Credit goes to SeRi for starting this mod. He had it use the wrt's white and amber LEDs (version 3 only) to show system load. The project was looking a little out of date, and it didnt work with most routers. I figured id fix it up a little. This script will cause the front light to be off with load below 0.20, white above 0.20 and below 0.40, A light orange (looks yellow to me) from 0.40 to 0.70, orange from 0.70 to 1.0, and blinking orange above 1.0.

'''Adding the scripts'''

Add the following script to /usr/sbin/loadmon.sh

{{{
#!/bin/sh

DELAY=1
VERYHIGHLOAD="100"
HIGHLOAD="70"
MEDLOAD="40"
LOWLOAD="20"

while sleep $DELAY; do
        load=$(cat /proc/loadavg | cut -d " " -f1 | tr -d ".")

        if [ "$load" -gt "$VERYHIGHLOAD" ]; then
                echo "0" > /proc/diag/led/ses_white
                orange_state=$(cat /proc/diag/led/ses_orange)
                if [ "$orange_state" -gt "0" ]; then
                        echo "0" > /proc/diag/led/ses_orange
                else
                        echo "1" > /proc/diag/led/ses_orange
                fi
        elif [ "$load" -gt "$HIGHLOAD" ]; then
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

== on kamikaze ==
create /usr/sbin/loadmon.sh as outlined above. But to start at boot, create /etc/init.d/loadmon
{{{
#!/bin/sh /etc/rc.common

START=99
STOP=01
start() {
        echo "f" > /proc/diag/led/ses_white
        [ -f /usr/sbin/loadmon.sh ] && /usr/sbin/loadmon.sh &
}

stop() {
        killall loadmon.sh
        echo "0" > /proc/diag/led/ses_white
        echo "0" > /proc/diag/led/ses_orange
}
}}}
This will flash the LED white at start so you see something is happening, then the script takes over. And when stopped it makes sure the LED is off.

Finally, enable the init script
{{{
chmod 755 /etc/init.d/loadmon
/etc/init.d/loadmon enable
}}}

CategoryHowTo
