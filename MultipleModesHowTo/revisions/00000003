== Introduction ==

=== What we want to do ===
I am using my Linksys WRT54GS as a switch with build-in AP by default. I wanted a way to switch back to its original router function without any time consuming configuration changes every time. In addition, I wanted a, as I call it, lanparty mode for using the WRT on a LAN-party (without internet). 
This HowTo describes a mechanism for easy switching between the different modes. At the end, you can just write "switchmode lanparty", unplug the power cable, go to your friend's LANparty, plug in again and have fun... ;)

Here is a short summary for the different modes I am using:

 * Switch mode:
   * WAN disabled, using all 5 ports for LAN
   * LAN configured by DHCP
   * Wireless interface bridged to the LAN, WPA2 encryption enabled
   * Disabled firewall, DHCP server and OpenWRT web interface
 * Router mode:
   * WAN enabled, using PPPoE
   * LAN uses fixed IP
   * Wireless config as in switch mode
   * All services enabled 
 * Lanparty mode: 
   * WAN disabled
   * LAN uses fixed IP
   * Wireless config different from the other modes
   * DHCP server enabled, firewall and OpenWRT web interface disabled
   * Running special LANparty web server (httpd2) (for example for pizza ordering ;) )


=== Requirements ===
* I have tested this with a WRT54G/S but it should work on any device running OpenWRT

== Configuration ==
=== Preparations ===
 * At first, we have to make copies of some init-scripts, because we will change their execute-flags later: {{{
cp /rom/etc/init.d/S05nvram /etc/init.d/
cp /rom/etc/init.d/S45firewall /etc/init.d/
cp /rom/etc/init.d/S50dnsmasq /etc/init.d/
cp /rom/etc/init.d/S50httpd /etc/init.d/
}}}
 * Then, we need to comment/remove the following (well known? ;) ) line from from '''''/etc/init.d/S05nvram''''': {{{
nvram set lan_proto="static" }}}    
 * If you want a separate "lanparty" webserver as I do, just create a /www2 dir and save the following init-script as /etc/init.d/S50httpd2. Otherwise, remove the appropriate lines from the script below. {{{
#!/bin/sh
httpd -p 80 -h /www2 -r OpenWrt
}}}
 * Create a new nvram-variable for saving the selected mode: {{{
nvram set mode=router
nvram commit
}}}
 * /!\ '''IMPORTANT:''' The script below only changes nvram variables that are actually nessesary to be changed. You have to set up all other required variables, for example these of DHCP server or your PPPoE connection. Don't forget to change ''wan_proto'' if you don't use PPPoE and make sure you have a DHCP server running when booting to ''switch'' mode, otherwise your WRT will not get any IP.

=== Init-Script ===
The actual switching is done after rebooting with the following init-script. It should be executed before {{{S05nvram}}} and {{{S10boot}}}, so you can save it as '''{{{S02mode_switch}}}'''. I'm sure you could write the script a lot more compact, but I think in this form it is very straight forward and easy to understand:

{{{
#!/bin/sh                                                                                                           
# This file handles the switching between different modes of the WRT, for example SWITCH, ROUTER, LANPARTY          
# The current mode is saved in 'mode' nvram variable...                                                             
                                                                                                                    
case "$(nvram get mode)" in                                                                                         
        switch) { # default                                                                                         
                nvram set lan_proto=dhcp                                                                            
                nvram set wan_proto=none                                                                            
                nvram set vlan1ports="5"                                                                            
                nvram set vlan0ports="0 1 2 3 4 5*"                                                                 
                nvram set wl0_ssid=wellenreiter3                                                                    
                nvram set wl0_wpa_psk=*****                                                             
                chmod -x /etc/init.d/S45firewall                                                                    
                chmod -x /etc/init.d/S50dnsmasq                                                                     
                chmod -x /etc/init.d/S50httpd                                                                       
                chmod +x /etc/init.d/S50httpd2          # only for testing                                          
        };;                                                                                                         
        router) {                                                                                                   
                nvram set lan_proto=static                                                                          
                nvram set wan_proto=pppoe                                                                           
                nvram set vlan1ports="0 5"                                                                          
                nvram set vlan0ports="1 2 3 4 5*"                                                                   
                nvram set wl0_ssid=wellenreiter3                                                                    
                nvram set wl0_wpa_psk=*****                                                              
                chmod -x /etc/init.d/S50httpd2                                                                   
                chmod +x /etc/init.d/S45firewall                                                                    
                chmod +x /etc/init.d/S50dnsmasq                                                                     
                chmod +x /etc/init.d/S50httpd                                                                       
        };;                                                                                                         
        lanparty) {                                                                                                 
                nvram set lan_proto=static                                                                          
                nvram set wan_proto=none                                                                            
                nvram set vlan1ports="5"                                                                            
                nvram set vlan0ports="0 1 2 3 4 5*"                                                                 
                nvram set wl0_ssid=freedom                                                                      
                nvram set wl0_wpa_psk=***                                                                    
                chmod -x /etc/init.d/S45firewall                                                                    
                chmod -x /etc/init.d/S50httpd                                                                       
                chmod +x /etc/init.d/S50dnsmasq                                                                     
                chmod +x /etc/init.d/S50httpd2                                                                      
        };;                                                                                                         
esac                                      
}}} 

=== Switching ===
The following little script is not really required, but makes life a little easier. When you save it as '''/sbin/switchmode''' for example, you can switch between the different modes by simple typing '''''switchmode newmode''''':
{{{
#!/bin/sh
# Mode switcher

case $1 in
        switch | router | lanparty)
          nvram set mode=$1
          nvram commit
          echo "New mode '$1' will be activated after next reboot!"
          echo ""
        ;;
        *)
          echo "Unknown mode! Only the following modes are implemented up to now: 'switch', 'router' and 'lanparty'.
          echo ""
          exit 1
        ;;
esac
}}}
