= LED System Load Monitor =

== pre-Kamikaze (WhiteRussian) ==

Credit goes to SeRi for starting this mod. He had it use the wrt's white and amber LEDs (version 3 only) to show system load. The project was looking a little out of date, and it didnt work with most routers. I figured id fix it up a little. This script will cause the front light to be off with load below 0.20, white above 0.20 and below 0.40, A light orange (looks yellow to me) from 0.40 to 0.70, orange from 0.70 to 1.0, and blinking orange above 1.0.

'''Adding the scripts'''

Add the following script to /usr/sbin/loadmon.sh

{{{
#!/bin/sh
# this script flashes the LEDs the hard way - see below for
# the Kamikaze version that uses the LED "flash" feature

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

== Kamikaze scripts ==

=== Kamikaze script start-up ===

Create /usr/sbin/loadmon.sh as given above, or use the enhanced version given below. But to start at boot, create /etc/init.d/loadmon
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

=== Kamikaze more elegant LED flashing ===

I'm not sure if this works under WhiteRussian, so only adding it as a note for now.
{{{
...
if [ "$load" -gt "$VERYHIGHLOAD" ]; then
                echo "0" > /proc/diag/led/ses_white
                echo "f" > /proc/diag/led/ses_orange
        elif [ "$load" -gt "$HIGHLOAD" ]; then
...
}}}
Is a more elegant way to make the orange LED flash. This also enables you to set the polling time of the script higher (I use 5 seconds) without influencing the speed of the flashing LED.

=== Kamikaze enhanced script ===

Below is a similar loadmon.sh script, with the unnecessary "cat" removed, led state caching added, LED reset on kill, and the most common case (low load) placed first to minimize CPU impact:

{{{
#!/bin/sh -u
# Load monitor for OpenWrt Kamikaze with the /proc/diag/led/ interface.
# This one by Ian! D. Allen - idallen@idallen.ca - www.idallen.com

# choose your own sleep time and load numbers
SLEEP=1
CRAZYLOAD="60"
VERYVERYHIGHLOAD="50"
VERYHIGHLOAD="40"
HIGHLOAD="30"
MEDLOAD="20"
LOWLOAD="10"

# cache the led state to avoid the unnecessary I/O operation
white=''
orange=''

White () {
        [ "$white" = "$1" ] && return
        echo "$1" > /proc/diag/led/ses_white || exit $?
        white=$1
}

Orange () {
        [ "$orange" = "$1" ] && return
        echo "$1" > /proc/diag/led/ses_orange || exit $?
        orange=$1
}

# turn the LEDs off if the script gets killed
trap 'White 0 ; Orange 0 ; exit' 0 1 2 15

while sleep "$SLEEP" ; do
        load=$( cut -d " " -f1 /proc/loadavg | tr -d "." )

        # test the most common cases (low load) first
        if [ "$load" -lt "$LOWLOAD" ]; then
                White 0
                Orange 0
        elif [ "$load" -lt "$MEDLOAD" ]; then
                White 1
                Orange 0
        elif [ "$load" -lt "$HIGHLOAD" ]; then
                White 1
                Orange 1
        elif [ "$load" -lt "$VERYHIGHLOAD" ]; then
                White 0
                Orange 1
        elif [ "$load" -lt "$VERYVERYHIGHLOAD" ]; then
                White f
                Orange 0
        elif [ "$load" -lt "$CRAZYLOAD" ]; then
                White 0
                Orange f
        else
                # invalidate cache so both LEDs are set to flash at the same time
                white=''
                orange=''
                White f
                Orange f
        fi

done
}}}


CategoryHowTo
