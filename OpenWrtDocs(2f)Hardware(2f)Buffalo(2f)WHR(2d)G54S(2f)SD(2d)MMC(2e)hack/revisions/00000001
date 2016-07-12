'''Buffalo WHR-G54S SD/MMC Hack'''

----

''.''


'''GPIO Information for Buffalo WHR-G54S'''[[BR]] These information are very useful for SD hack described below and for your own custom hacking on special I/O

{{{
PIN     Usage   Original Use
----------------------------------------------------------------
GPIO 0  Input   AOSS Button
GPIO 1  Output  Bridge led
GPIO 2  Output  Wlan Led
GPIO 3  Output  Extra Led (unknown use) between wlan and bridge
GPIO 4  Input   Reset Button
GPIO 5  Input   Bridge/Auto switch
GPIO 6  Output  AOSS Led
GPIO 7  Output  Diag Led
GPIO 8  N/A     don't know, i didn't find it
GPIO 9  Output  Power Led
}}}
Please note it's very important to understand original buffalo usage doesn't affect the way you use IOs, all ports are basically structured to work in Input as well as Output.

'''NOTE''': Using GPIO 4 is NOT a good idea :)

''(Ben)''

''.''


----
'''SD/MMC Hack'''[[BR]] This hack is very popular with other APs (eg.Linksys) and can be applied to Buffalo WHR-G54S as well, things are slightly different because of different usage of GPIO but there's a binary kernel module mmc.o optimized and fully working for Linksys as well as Buffalo

For this hack i've used these I/O (please see table described above)

{{{
Signal     GPIO
----------------
Data IN    5
Data OUT   6
Clock      3
CS         7
}}}
I've created a new wiki page with some photos of my hack, Hope it helps, send me some notes if you need more information on my job''' NOTE''': Using GPIO 4 (like linksys WRT models) is NOT a good idea here (reset button... :) )

''(Andrea Ben Benini)''

''.''

''.''

----
CategoryModel CategoryModel
