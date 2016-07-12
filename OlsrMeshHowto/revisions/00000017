__Introduction__''' '''

Mesh networks are networks which are self arranging and auto configure them selves on basis of topology changes in cases like one node fails or a a new route emerges or a low traffic route is availble etc.The concept of mesh network is not new Internet is a huge mesh network in itself.So whats new? Well mesh networks with wireless simply rocxx.

Well OLSR is one of the routing protocol available for Mobile Adhoc Network(MANET) or rather is general terms a wireless Mesh network.The OLSR code developed by [http://www.olsr.org Andreas Tønnesen] is the best suited for our case.

Actually if the objective is just to have a quick mesh you should be looking at Freifunk firmware or [:http:what-a-mesh] firmware which is openwrt+olsr. But if you want to do it all your self which was as in my case you can follow the below methods

The Network

                        


                                  Wired to Lan Client (HNA4)
                (WAN)                    |
                   |                     / 
 Internet---------->Node1- - - - - - -Node2 
                            ^           \ - - wifi to Client (Olsr/Non Olsr running client)
                            | 
                            |
                     Wifi Link with olsr 



Both Nodes(WRTs) need to have olsr installed.Same is the case for any n number of nodes participating.OLSR has to run on WIFI interface running it on wired interface is optional tho it wont be of much help.The non olsr interfaces (like WAN and wired client in the above case) are added by entering the network/ip address in the HNA4  field of the olsrd.conf file.

__'''HOW TO''' __ __ __ __ __ __ __

1.The Base Configuration:

 . The base configuration is install the olsr package on a OpenWrt router in Ad Hoc mode with Lan and Wifi seperate (ie. no br0)
  . {{{
  ipkg update
  ipkg install olsrd_0.4.10-1_mipsel.ipk  }}}
 2.Edit the /etc/olsrd.conf file
  . In the lower side of the olsrd.conf file you see Interface "XXX" just change XXX to your wireless interface which was eth1 in my case

''''''

{{{
  Interface "eth1" 
{  #IPv4 broadcast address to use.The 
   #one usefull example would be 255.255.255.255

}}}

 . Then you just need to run the command olsrd and it should take the default values and run.

[Todo: firewall startup and explanation of HNA4  ,plugins ,negetive weights etc ]

Refrence::

[http://www.olsr.org www.olsr.org] :Read main thesis and rfc

http://wiki.openwrt.org/OpenWrtDocs :Everything and anything in it

----
 . CategoryHowTo             
