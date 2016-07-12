= Buffalo WBR2-B11 =

== Installation ==

I recently came across two of these and successfully upgraded both of them. As mentioned many times, make sure to reset the unit to factory default before starting and to manually set your IP address to 192.168.11.2 and subnet to 255.255.255.0.

 * 1st Unit - Used the same TFTP method as for the WBR2-G54.
 * 2nd Unit - Used the windows TFTP program, set it to retry 20 times, waited until it was past the first try, plugged in the WBR2-B11 and watched it catch the window somewhere between try 8 and try 14.

Something of note is that both units were not able to update the HTTP Password when accessing them the first time over the web so I had to telnet into each of them and execute the following commands which fixed the problem easily.

nvram set http_passwd = "password" 

nvram commit 
 
