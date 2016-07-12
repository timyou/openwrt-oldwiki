From [http://forum.openwrt.org/viewtopic.php?id=11301]

= Writing a startup script =

The boot process may be customized to add new daemons, provide alternate ways of starting existing daemons, or otherwise do things at startup and shutdown.

This, is /etc/init.d/example:

{{{
#!/bin/sh /etc/rc.common
# Example script
# Copyright (C) 2007 OpenWrt.org

START=10
STOP=15

start() {        
        echo start
        # commands to launch application
}                 
                  
stop() {          
        echo stop
        # commands to kill application 
}
}}}
After creating it, run "/etc/init.d/example enable", this will copy the script to the /etc/rc.d/ directory. The START=10 means that this will become /etc/init.d/S10example - the 10 signifies the order the script is to be executed, allowing it to be placed before or after existing scripts. The STOP=15 is optional and will create a /etc/rc.d/K15example.

On startup, all the scripts matching the pattern /etc/rc,d/S* are executed in the form of "<script> boot", which will run the commands in the start() section. On shutdown the /etc/rc.d/K* scripts are executed as "<script> stop" causing the stop() section to be run.

Here's a few commands to illustrate the use -

{{{
/etc/init.d/example
/etc/init.d/example enable
/etc/init.d/example boot
/etc/init.d/example start
/etc/init.d/example restart
/etc/init.d/example stop
/etc/init.d/example disable
}}}

Additionally, you can define a boot() section -

{{{
boot() {          
        echo boot
        # commands to run at boot

        # continue with the start() section
        start
 }
}}}
Now, running the script with the boot argument will trigger the boot() section (which then triggers the start section). This allows you to run additional commands at bootup, avoiding them on the restart command.



= Custom functions in init scripts =

/etc/init.d/example

{{{
#!/bin/sh /etc/rc.common
# Example script
# Copyright (C) 2007 OpenWrt.org

START=10
STOP=15

EXTRA_COMMANDS="custom"
EXTRA_HELP="        custom  HELP text for custom"

start() {
        echo start
        # commands to launch application
}

stop() {
        echo stop
        # commands to kill application
}

custom()  {
        echo custom function
        # do something
}
}}}

{{{
root@OpenWrt:/# /etc/init.d/example
Syntax: /etc/init.d/example [command]

Available commands:
        start   Start the service
        stop    Stop the service
        restart Restart the service
        reload  Reload configuration files (or restart if that fails)
        enable  Enable service autostart
        disable Disable service autostart
        custom  HELP text for custom
root@OpenWrt:/etc/init.d#
}}}

{{{
root@OpenWrt:/# /etc/init.d/example custom
custom function
root@OpenWrt:/#
}}}
