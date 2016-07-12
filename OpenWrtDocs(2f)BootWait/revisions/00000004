= Via serial console =

With a serial connection to your WRT, you don't have to use the ping bug or change your Linksys firmware. You can set boot_wait from the console, using the commands

{{{
#nvram set boot_wait=on
#nvram get boot_wait           (just to confirm, should respond with "on")
#nvram commit                  (takes a few seconds to complete)
}}}

You can also set boot_wait from the [:OpenWrtDocs/Customizing/Firmware/CFE:CFE] boot loader (to enter CFE, reboot the router with "# reboot" while hitting {{{CTRL-C}}} continously)

{{{
CFE> nvram set boot_wait=on
CFE> nvram get boot_wait       (just to confirm, should respond with "on")
CFE> nvram commit              (takes a few seconds to complete)
}}}

Or via PMON (older models, hit {{{CTRL-C}}} repeatedly during powerup or reboot)

{{{
PMON> set boot_wait on
PMON> set nvram boot_wait
}}}
