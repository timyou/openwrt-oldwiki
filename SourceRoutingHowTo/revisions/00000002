<html xmlns:o="urn:schemas-microsoft-com:office:office"
xmlns:w="urn:schemas-microsoft-com:office:word"
xmlns="http://www.w3.org/TR/REC-html40">

<head>
<meta http-equiv=Content-Type content="text/html; charset=windows-1252">
<meta name=ProgId content=Word.Document>
<meta name=Generator content="Microsoft Word 10">
<meta name=Originator content="Microsoft Word 10">
<link rel=File-List
href="source%20routing%20on%20OpenWrt%20How_files/filelist.xml">
<title>source routing on OpenWrt How-To</title>
<!--[if gte mso 9]><xml>
 <o:DocumentProperties>
  <o:Author>Private</o:Author>
  <o:LastAuthor>Private</o:LastAuthor>
  <o:Revision>1</o:Revision>
  <o:TotalTime>1</o:TotalTime>
  <o:Created>2007-07-19T18:19:00Z</o:Created>
  <o:LastSaved>2007-07-19T18:20:00Z</o:LastSaved>
  <o:Pages>1</o:Pages>
  <o:Words>1066</o:Words>
  <o:Characters>6079</o:Characters>
  <o:Company>private</o:Company>
  <o:Lines>50</o:Lines>
  <o:Paragraphs>14</o:Paragraphs>
  <o:CharactersWithSpaces>7131</o:CharactersWithSpaces>
  <o:Version>10.6714</o:Version>
 </o:DocumentProperties>
</xml><![endif]--><!--[if gte mso 9]><xml>
 <w:WordDocument>
  <w:GrammarState>Clean</w:GrammarState>
  <w:DrawingGridHorizontalSpacing>9,35 pt</w:DrawingGridHorizontalSpacing>
  <w:DisplayVerticalDrawingGridEvery>2</w:DisplayVerticalDrawingGridEvery>
  <w:Compatibility>
   <w:BreakWrappedTables/>
   <w:SnapToGridInCell/>
   <w:WrapTextWithPunct/>
   <w:UseAsianBreakRules/>
  </w:Compatibility>
  <w:BrowserLevel>MicrosoftInternetExplorer4</w:BrowserLevel>
 </w:WordDocument>
</xml><![endif]-->
<style>
<!--
 /* Style Definitions */
 p.MsoNormal, li.MsoNormal, div.MsoNormal
	{mso-style-parent:"";
	margin:0cm;
	margin-bottom:.0001pt;
	mso-pagination:widow-orphan;
	font-size:12.0pt;
	font-family:"Times New Roman";
	mso-fareast-font-family:"Times New Roman";
	mso-ansi-language:PT;}
@page Section1
	{size:841.7pt 595.45pt;
	mso-page-orientation:landscape;
	margin:89.85pt 72.0pt 89.85pt 72.0pt;
	mso-header-margin:36.0pt;
	mso-footer-margin:36.0pt;
	mso-paper-source:0;}
div.Section1
	{page:Section1;}
-->
</style>
<!--[if gte mso 10]>
<style>
 /* Style Definitions */
 table.MsoNormalTable
	{mso-style-name:"Table Normal";
	mso-tstyle-rowband-size:0;
	mso-tstyle-colband-size:0;
	mso-style-noshow:yes;
	mso-style-parent:"";
	mso-padding-alt:0cm 5.4pt 0cm 5.4pt;
	mso-para-margin:0cm;
	mso-para-margin-bottom:.0001pt;
	mso-pagination:widow-orphan;
	font-size:10.0pt;
	font-family:"Times New Roman";}
</style>
<![endif]-->
</head>

<body lang=EN-US style='tab-interval:36.0pt'>

<div class=Section1>

<p class=MsoNormal><span lang=PT>source routing on OpenWrt How-To<o:p></o:p></span></p>

<p class=MsoNormal><span lang=PT><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal><span lang=PT>the purpose of source routing:<o:p></o:p></span></p>

<p class=MsoNormal><span lang=PT>to decide, on basis of the source address of
packets, through which interface those packets should leave the router.<o:p></o:p></span></p>

<p class=MsoNormal><span lang=PT><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal><span lang=PT>example of its use:<o:p></o:p></span></p>

<p class=MsoNormal><span lang=PT>a system with multiple routes towards the
internet. <o:p></o:p></span></p>

<p class=MsoNormal><span lang=PT>Examples: <o:p></o:p></span></p>

<p class=MsoNormal><span lang=PT>1) Two routers, each with an an adsl link and
interconnected via lan, and each serving via their shared lan or a secondary
lan a number of clients; but you want some clients to go out through one adsl
line, and other clients through the other.<o:p></o:p></span></p>

<p class=MsoNormal><span lang=PT>2) A router with two adsl connections, ppp0
and ppp1, and you want some clients to use ppp0 , and others to use ppp1.<o:p></o:p></span></p>

<p class=MsoNormal><span lang=PT><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal><span lang=PT>prerequisites:<o:p></o:p></span></p>

<p class=MsoNormal><span lang=PT>ip package (use 'ipkg install')<o:p></o:p></span></p>

<p class=MsoNormal><span lang=PT><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal><span lang=PT>example script that should be executed upon
boot; in Whiterussian place in //etc/init.d e.g. as S80routes_2ISPS<o:p></o:p></span></p>

<p class=MsoNormal><span lang=PT><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal><span lang=PT>#!/bin/sh<o:p></o:p></span></p>

<p class=MsoNormal><span lang=PT>########################################################################<o:p></o:p></span></p>

<p class=MsoNormal><span lang=PT>### S80routes_2ISPS ; script for OpenWrt by
'doddel'<o:p></o:p></span></p>

<p class=MsoNormal><span lang=PT>### separate traffic between two adsl
connections, one on this router ('HERE') and the other on a router <o:p></o:p></span></p>

<p class=MsoNormal><span lang=PT>### that is reached via vlan2 and has in this
example ip address 192.168.2.14 ('THERE')<o:p></o:p></span></p>

<p class=MsoNormal><span lang=PT>### assumption is that this router talks to
clients through vlan0 (lan) and through eth1 (wifi)<o:p></o:p></span></p>

<p class=MsoNormal><span lang=PT>### I normally do not use the bridge br0 as it
pollutes the scarce radio channel resource with<o:p></o:p></span></p>

<p class=MsoNormal><span lang=PT>### Unnecessary traffic but this is unrelates
to the essentials of source routing.<o:p></o:p></span></p>

<p class=MsoNormal><span lang=PT>### This router 'HERE'is assumed to have
following interfaces:<o:p></o:p></span></p>

<p class=MsoNormal><span lang=PT>### ppp0 ; dynamical ip address, assigned by
isp<o:p></o:p></span></p>

<p class=MsoNormal><span lang=PT>### vlan0 ; the lan with ip address
192.168.10.10/24<o:p></o:p></span></p>

<p class=MsoNormal><span lang=PT>### vlan1 ; used by pppd to create ppp0<o:p></o:p></span></p>

<p class=MsoNormal><span lang=PT>### vlan2 ; the lan2 used to connect to the
other router that also has adsl; ip address HERE 192.168.2.10<o:p></o:p></span></p>

<p class=MsoNormal><span lang=PT>### eth1 ; wifi, with ip address 192.168.6.10,
talking per radio to router 192.168.6.100 that serves clients<o:p></o:p></span></p>

<p class=MsoNormal><span lang=PT>### IMPORTANT: modify<span
style='mso-spacerun:yes'>  </span>//sbin/ifup.pppoe: change 'defaultroute'
option into 'nodefaultroute';<o:p></o:p></span></p>

<p class=MsoNormal><span lang=PT>### when adsl gets connected the routing
settings. made by this script, do not get overwritten by pppd <o:p></o:p></span></p>

<p class=MsoNormal><span lang=PT>########################################################################<o:p></o:p></span></p>

<p class=MsoNormal><span lang=PT><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal><span lang=PT># the client's ip addresses<o:p></o:p></span></p>

<p class=MsoNormal><span lang=PT>client1_lan=&quot;192.168.10.0/24&quot;<span
style='mso-tab-count:1'> </span># just an example of a group of clients on
'lan'(vlan0) to be routed equally <o:p></o:p></span></p>

<p class=MsoNormal><span lang=PT>client2_wlan=&quot;192.168.12.1/32&quot;<span
style='mso-tab-count:1'>           </span># just another example of a unique
client reached per radio here and needing unique routing<o:p></o:p></span></p>

<p class=MsoNormal><span lang=PT># add the list of clients <o:p></o:p></span></p>

<p class=MsoNormal><span lang=PT><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal><span lang=PT><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal><span lang=PT>### abbreviations used filling the 'main'
routing table using 'route' commands <o:p></o:p></span></p>

<p class=MsoNormal><span lang=PT>HERE=&quot;netmask 255.255.255.0 gw
192.168.6.100 dev eth1&quot;<span style='mso-tab-count:1'>  </span># define the
gateway that serves the clients reached per radio<o:p></o:p></span></p>

<p class=MsoNormal><span lang=PT>THERE=&quot;netmask 255.255.255.0 gw
192.168.2.14 dev vlan2&quot; # define the route to the second router <o:p></o:p></span></p>

<p class=MsoNormal><span lang=PT><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal><span lang=PT># define routes to subnets hidden behind
routers reached via radio<o:p></o:p></span></p>

<p class=MsoNormal><span lang=PT>route add -net 192.168.11.0 ${HERE} # one subnet
reachable via eth1 and gateway 192.168.6.100 <o:p></o:p></span></p>

<p class=MsoNormal><span lang=PT>route add -net 192.168.12.0 ${HERE} # another
subnet reachable via eth1 and gateway 192.168.6.100 <o:p></o:p></span></p>

<p class=MsoNormal><span lang=PT># .... more<o:p></o:p></span></p>

<p class=MsoNormal><span lang=PT><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal><span lang=PT># define routes to subnets that are reacheable
via the other adsl router<o:p></o:p></span></p>

<p class=MsoNormal><span lang=PT>route add -net 192.168.4.0<span
style='mso-spacerun:yes'>   </span>${THERE} # one subnet reachable via vlan2
and gateway 192.168.2.14 <o:p></o:p></span></p>

<p class=MsoNormal><span lang=PT>route add -net 192.168.57.0<span
style='mso-spacerun:yes'>  </span>${THERE} # one subnet reachable via vlan2 and
gateway 192.168.2.14 <o:p></o:p></span></p>

<p class=MsoNormal><span lang=PT># .....more<o:p></o:p></span></p>

<p class=MsoNormal><span lang=PT><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal><span lang=PT>### get current ip numbers of the ppp0
interface<o:p></o:p></span></p>

<p class=MsoNormal><span lang=PT>pubip=$(ifconfig ppp0 | grep 'inet addr' | awk
'{print $2}' | sed -e 's/.*://') # public dynamic IP<o:p></o:p></span></p>

<p class=MsoNormal><span lang=PT>gwyip=$(ifconfig ppp0 | grep 'inet addr' | awk
'{print $3}' | sed -e 's/.*://') # ISP P-t-p gateway IP<o:p></o:p></span></p>

<p class=MsoNormal><span lang=PT><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal><span lang=PT>### abbreviations used filling the tables
'200' '201' and '202' using 'ip route ' commands <o:p></o:p></span></p>

<p class=MsoNormal><span lang=PT>### table 200 is always checked and has all
internal routes, table 201 will be checked only for those source addresses<o:p></o:p></span></p>

<p class=MsoNormal><span lang=PT>### that should leave via THERE and contains
THERE as default route, 202 contains HERE as default route<o:p></o:p></span></p>

<p class=MsoNormal><span lang=PT>HERE='via 192.168.6.100 dev eth1 table 200'<o:p></o:p></span></p>

<p class=MsoNormal><span lang=PT>THERE='via 192.168.2.14 dev vlan2 table 200'<o:p></o:p></span></p>

<p class=MsoNormal><span lang=PT>THERE202='via 192.168.2.14 dev vlan2 table
202'<o:p></o:p></span></p>

<p class=MsoNormal><span lang=PT><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal><span lang=PT>### populate the table [200] with routes equal
for all (know to reach all clients)<o:p></o:p></span></p>

<p class=MsoNormal><span lang=PT>ip route flush table 200<o:p></o:p></span></p>

<p class=MsoNormal><span lang=PT>### the native interfaces (are set by OS in
table 'main' but need being set manually in table [200]) <o:p></o:p></span></p>

<p class=MsoNormal><span lang=PT>ip route add to $gwyip dev ppp0 protocol
kernel scope link src $pubip table 200<span style='mso-tab-count:5'>                                                          </span>#
ppp0<o:p></o:p></span></p>

<p class=MsoNormal><span lang=PT>ip route add to 192.168.10.0/24<span
style='mso-tab-count:1'>           </span>dev vlan0<span style='mso-tab-count:
1'>          </span>protocol kernel scope link src 192.168.10.10<span
style='mso-tab-count:1'>   </span>table 200<span style='mso-tab-count:1'>          </span>#
lan <o:p></o:p></span></p>

<p class=MsoNormal><span lang=PT>ip route add to 192.168.2.0/24<span
style='mso-tab-count:1'> </span>dev vlan2<span style='mso-tab-count:1'>          </span>protocol
kernel scope link src 192.168.2.10<span style='mso-tab-count:1'>     </span>table
200<span style='mso-tab-count:1'>          </span># vlan2 <o:p></o:p></span></p>

<p class=MsoNormal><span lang=PT>ip route add to 192.168.6.0/24<span
style='mso-tab-count:1'> </span>dev eth1<span style='mso-tab-count:1'>           </span>protocol
kernel scope link src 192.168.6.10<span style='mso-tab-count:1'>     </span>table
200<span style='mso-tab-count:1'>          </span># eth1<o:p></o:p></span></p>

<p class=MsoNormal><span lang=PT><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal><span lang=PT>### always forced towards or via ISP via local
adsl<o:p></o:p></span></p>

<p class=MsoNormal><span lang=PT>ip route add to &lt;subnet of isp dns&gt;/24<span
style='mso-tab-count:1'>  </span>via $gwyip dev ppp0 table main<span
style='mso-tab-count:2'>                        </span># reach isp's dns
servers via local adsl<o:p></o:p></span></p>

<p class=MsoNormal><span lang=PT>ip route add to &lt;subnet of dynamic
dns&gt;/24<span style='mso-tab-count:1'>      </span>via $gwyip dev ppp0 table
main<span style='mso-tab-count:1'>            </span># reach the the dynamic
dns servers<o:p></o:p></span></p>

<p class=MsoNormal><span lang=PT>ip route add to &lt;subnet of isp dns&gt;/24<span
style='mso-tab-count:1'>  </span>via $gwyip dev ppp0 table 200<span
style='mso-tab-count:2'>             </span># same in table 200 as in table
main<o:p></o:p></span></p>

<p class=MsoNormal><span lang=PT>ip route add to &lt;subnet of dynamic
dns&gt;/24<span style='mso-tab-count:1'>      </span>via $gwyip dev ppp0 table
200<span style='mso-tab-count:1'> </span># same in table 200 as in table main<o:p></o:p></span></p>

<p class=MsoNormal><span lang=PT><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal><span lang=PT>### the routes via HERE wifi network<o:p></o:p></span></p>

<p class=MsoNormal><span lang=PT>ip route add to 192.168.11.0/24 ${HERE}<span
style='mso-tab-count:2'>                  </span># clients reached via local
radio<o:p></o:p></span></p>

<p class=MsoNormal><span lang=PT>ip route add to 192.168.12.0/24 ${HERE}<span
style='mso-tab-count:2'>                  </span># more clients reached via
local radio<o:p></o:p></span></p>

<p class=MsoNormal><span lang=PT># more ...<o:p></o:p></span></p>

<p class=MsoNormal><span lang=PT><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal><span lang=PT># the routes via THERE wifi and/or lan network<o:p></o:p></span></p>

<p class=MsoNormal><span lang=PT>ip route add to 192.168.4.0/24<span
style='mso-spacerun:yes'>   </span>${THERE}<span style='mso-tab-count:1'>    </span>#
clients reached via THERE<o:p></o:p></span></p>

<p class=MsoNormal><span lang=PT>ip route add to 192.168.57.0/24<span
style='mso-spacerun:yes'>  </span>${THERE}<span style='mso-tab-count:1'>   </span>#
more clients reached via THERE<o:p></o:p></span></p>

<p class=MsoNormal><span lang=PT># more ....<o:p></o:p></span></p>

<p class=MsoNormal><span lang=PT><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal><span lang=PT>### populate table [201], the default HERE
gateway<o:p></o:p></span></p>

<p class=MsoNormal><span lang=PT>ip route flush table 201<o:p></o:p></span></p>

<p class=MsoNormal><span lang=PT>ip route add to default via $gwyip dev ppp0
table 201<o:p></o:p></span></p>

<p class=MsoNormal><span lang=PT><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal><span lang=PT>### populate table [202], the alternative
THERE gateway<o:p></o:p></span></p>

<p class=MsoNormal><span lang=PT>ip route flush table 202<o:p></o:p></span></p>

<p class=MsoNormal><span lang=PT>ip route add to default ${THERE202}<o:p></o:p></span></p>

<p class=MsoNormal><span lang=PT><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal><span lang=PT>### now define rules for table selection,
starting with highest priority<o:p></o:p></span></p>

<p class=MsoNormal><span lang=PT>### find internal destination, this table gets
checked for any source address [200]<o:p></o:p></span></p>

<p class=MsoNormal><span lang=PT>ip rule delete from 0/0 priority 50 table 200<o:p></o:p></span></p>

<p class=MsoNormal><span lang=PT>ip rule add from 0/0 priority 50 table 200<o:p></o:p></span></p>

<p class=MsoNormal><span lang=PT># more ... delete/add pairs, one for each
client that should use THERE<o:p></o:p></span></p>

<p class=MsoNormal><span lang=PT><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal><span lang=PT>### what comes in via HERE's lan and wifi <o:p></o:p></span></p>

<p class=MsoNormal><span lang=PT>### decide what should go out THERE and
therefore should use table [202]<o:p></o:p></span></p>

<p class=MsoNormal><span lang=PT>ip rule delete<span style='mso-tab-count:1'>     </span>from
${client1_lan}<span style='mso-tab-count:1'>      </span>iif vlan0<span
style='mso-tab-count:1'> </span>priority 51 table 202<o:p></o:p></span></p>

<p class=MsoNormal><span lang=PT>ip rule add<span style='mso-tab-count:1'>        </span>from
${client1_lan}<span style='mso-tab-count:1'>      </span>iif vlan0<span
style='mso-tab-count:1'> </span>priority 51 table 202<span style='mso-tab-count:
1'>     </span># client1 uses THERE's adsl to reach internet<o:p></o:p></span></p>

<p class=MsoNormal><span lang=PT><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal><span lang=PT>### rest must go out HERE and should therefore
check table [201]<o:p></o:p></span></p>

<p class=MsoNormal><span lang=PT>ip rule delete<span style='mso-tab-count:1'>     </span>from
0/0<span style='mso-tab-count:4'>                                               </span>priority
52 table 201<o:p></o:p></span></p>

<p class=MsoNormal><span lang=PT>ip rule add<span style='mso-tab-count:1'>        </span>from
0/0<span style='mso-tab-count:4'>                                               </span>priority
52 table 201<o:p></o:p></span></p>

<p class=MsoNormal><span lang=PT>ip rule delete<span style='mso-tab-count:1'>     </span>iif
lo<span style='mso-tab-count:5'>                                                      </span>priority
53 table 201<o:p></o:p></span></p>

<p class=MsoNormal><span lang=PT>ip rule add<span style='mso-tab-count:1'>        </span>iif
lo<span style='mso-tab-count:5'>                                                      </span>priority
53 table 201<o:p></o:p></span></p>

<p class=MsoNormal><span lang=PT>ip rule delete<span style='mso-tab-count:1'>     </span>from
127.0.0.0/8<span style='mso-tab-count:3'>                                  </span>priority
54 table 201<o:p></o:p></span></p>

<p class=MsoNormal><span lang=PT>ip rule add<span style='mso-tab-count:1'>        </span>from
127.0.0.0/8<span style='mso-tab-count:3'>                                  </span>priority
54 table 201<span style='mso-tab-count:1'>     </span># anything else is HERE
default<o:p></o:p></span></p>

<p class=MsoNormal><span lang=PT><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal><span lang=PT>### now client1's traffic will use the adsl of
the other router while client2's traffic goes out here locally.<o:p></o:p></span></p>

<p class=MsoNormal><span lang=PT>### when adding more rules make sure that the
priorities are unique per client and increase per rule (higher priority number
is checked later, so the internal destinations are always checked first, then
whatever should leave THERE, and what remains must leave HERE)<o:p></o:p></span></p>

<p class=MsoNormal><span lang=PT><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal><span lang=PT>### make the rules active, deleting old stuff <o:p></o:p></span></p>

<p class=MsoNormal><span lang=PT>ip route flush cache</span></p>

</div>

</body>

</html>
