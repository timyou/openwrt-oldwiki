'''Linksys WRT55AG'''

=== Hardware versions ===
There are two versions of the WRT55AG. You can get the version number from the sticker on the bottom of the device.

See Tom's Hardware guide for information: http://www.tomsnetworking.com/Reviews-47-ProdID-WRT55AG-2.php
Also see: http://www.tomsnetworking.com/Sections-article100-page3.php

==== WRT55AG v1.0 ====
We have no information about the internals of these units, yet, so they are '''NOT''' supported.

==== WRT55AG v2.0 ====
It seems as if Linksys also runs linux on this box.

===== Official Linksys GPL Firmware =====
Like all other official Linksys Firmware, this Firmware is located at their [http://www.linksys.com/support/gpl.asp GPL Code Center]
The current (3rd of June, 2005) version is 1.1 and can be obtained from the linksys website.
  
===== Dissassembly instruction =====
Detailed and correct Information, even the default webinterface are available [http://openwrt.org/downloads/wrt55ag_v2-deconstruction/ here]

===== Myth =====
"The WRT55AG v2.0 comes with firmware version 1.1 and appears to use VxWorks, not linux."
Hopefully this statement is not correct, the GPL firmware is to be checked soon for that issue.

===== Hardware notes =====

- Two pcs. of "YCL DUAL 10/100 BASE PTH FILTER MODULE MODEL:PH202484"
[[BR]](datasheet requested on 2005-03-05 via email)

- One pcs. of "LANKOM ELEC p/n LF-H17X"
[[BR]]datasheet: http://www.lankom.com.tw/search/product-images/LF-H17X.pdf

- One pcs. of "KENDIN KS8995M 5 Port 10/100 Integrated Managed Switch"
[[BR]]datasheet: http://www.micrel.com/_PDF/Ethernet/full_ds/ks8995m.pdf

- One pcs. of crystal with markings "25.000 | SIWARD 4J"
[[BR]](no datasheet / unable to identify)

- One pcs. of "ATHEROS p/n AR5312A-00"
[[BR]](datasheet requested on 2005-03-05 via email)

- Two pcs. of "G-LINK GLT5640L16-6TC"
[[BR]]GLT5640L16 datasheet: http://211.78.172.202/glinkeng/pdf/GLT5640L16-R3.3.pdf

- One pcs. of "SST39VF3201 (x16) Multi-Purpose Flash Plus (MPF+TM)"
[[BR]]picture: http://rockbox.rock-ed.net/39VF3201.JPG
[[BR]]datasheet: http://www.sst.com/downloads/datasheet/S71223.pdf

- Two pcs. of "AME8807AEHA Requlator"
[[BR]]datasheet: http://www.analogmicro.com/Datasheet/ame8807.pdf


''Serial:''
{{{
        o
GND - o o - RX
      o o
      o o
VCC   o o - TX
      JP1
}}}
9600 baud, hit enter for login; login is the same as the web (u:blank p:admin)

{{{
ar531x rev 0x00005742 firmware startup...
SDRAM TEST SKIPPED


Atheros AR5001AP default version 4.0.0.2
Bootloader version 1.00


 0
auto-booting...

Attaching to TFFS... done.
Loading /fl/apimg1...1395424
Starting at 0x804846e0...


FLASH IS 4M!
MACunit 0 enabled
MACunit 0 enabled
/fl/  - Volume is OK
Reading Configuration File "/fl/apcfg".
Configuration file checksum: 45780 is good
fopen /fl/dhcps_lease_entry fail !!!
Attaching interface lo0...done
DHCP server started.
wireless access point starting...
wlan0 Ready
wireless access point starting...
wlan1 Ready
Ready
Remote Web service ... disabled
start easyconf
Blocking WAN PING service ... disabled
vp0 macaddr = 00:0f:66:e8:16:50
vp65536 macaddr = 00:0f:66:e8:16:51
ae0 macaddr = 00:0f:66:e8:16:52
ae1 macaddr = 00:0f:66:e8:16:53

AP login:
Password: *****

Atheros Access Point Rev 3.3.1.25
wlan0 -> help
List of Access Point CLI commands:
 config wlan                        -- config wlanX
 connect bss                        -- connect to bssX
 del acl                            -- Delete Access Control List
 del key                            -- Delete Encryption key
 find bss                           -- Find BSS
 find channel                       -- Find Available Channel
 find all                           -- Find All BSS
 ftp                                -- Software update via FTP
 get acl                            -- Display Access Control List
 get aging                          -- Display Aging Interval
 get antenna                        -- Display Antenna Diversity
 get association                    -- Display Association Table
 get authentication                 -- Display Authentication Type
 get autochannelselect              -- Display Auto Channel Select
 get beaconinterval                 -- Display Beacon Interval
 get burstSeqThreshold              -- Display Max Number of frames in a Burst
 get burstTime                      -- Display Burst Time
 get channel                        -- Display Radio Channel
 get cipher                         -- Display Encryption cipher
 get config                         -- Display Current AP Configuration
 get countrycode                    -- Display Country Code
 get domainsuffix                   -- Display Domain Name Server suffix
 get dtim                           -- Display Data Beacon Rate (DTIM)
 get encryption                     -- Display Encryption Mode
 get fragmentthreshold              -- Display Fragment Threshold
 get frequency                      -- Display Radio Frequency (MHz)
 get gateway                        -- Display Gateway IP Address
 get groupkeyupdate                 -- Display Group Key Update Interval (in Sec
onds)
 get hardware                       -- Display Hardware Revisions
 get hostipaddr                     -- Display Host IP Address
 get ipaddr                         -- Display IP Address
 get ipmask                         -- Display IP Subnet Mask
 get key                            -- Display Encryption Key
 get keyentrymethod                 -- Display Encyrption Key Entry Method
 get keysource                      -- Display Source Of Encryption Keys
 get login                          -- Display Login User Name
 get minimumrate                    -- Display Minimum Rate
 get nameaddr                       -- Display IP address of name server
 get operationMode                  -- Display Operation Mode
 get pktLogEnable                   -- Display Packet Logging Mode
 get power                          -- Display Transmit Power Setting
 get radiusname                     -- Display RADIUS server name or IP address
 get radiusport                     -- Display RADIUS port number
 get rate                           -- Display Data Rate
 get reg                            -- Display the register contents at the give
n offset
 get remoteAp                       -- Display Remote Ap's Mac Address
 get rtsthreshold                   -- Display RTS/CTS Threshold
 get sntpserver                     -- Display SNTP/NTP Server IP Address
 get ssid                           -- Display Service Set ID
 get ssidsuppress                   -- Display SSID Suppress Mode
 get station                        -- Display Station Status
 get SuperG                         -- Display SuperG Feature Status
 get systemname                     -- Display Access Point System Name
 get tzone                          -- Display Time Zone Setting
 get uptime                         -- Display UpTime
 get wirelessmode                   -- Display Wireless LAN Mode
 get wlanstate                      -- Display wlan state
 help                               -- Display CLI Command List
 ping                               -- Ping
 pktLog                             -- Packet Log
 reboot                             -- Reboot Access Point
 run                                -- Run command file
 quit                               -- Logoff
 set acl                            -- Set Access Control List
 set aging                          -- Set Aging Interval
 set antenna                        -- Set Antenna
 set authentication                 -- Set Authentication Type
 set autochannelselect              -- Set Auto Channel Selection
 set beaconinterval                 -- Modify Beacon Interval
 set burstSeqThreshold              -- Set Max Number of frames in a Burst
 set burstTime                      -- Set Burst Time
 set channel                        -- Set Radio Channel
 set cipher                         -- Set Cipher
 set countrycode                    -- Set Country Code
 set domainsuffix                   -- Set Domain Name Server Suffix
 set dtim                           -- Set Data Beacon Rate (DTIM)
 set encryption                     -- Set Encryption Mode
 set factorydefault                 -- Restore to Default Factory Settings
 set fragmentthreshold              -- Set Fragment Threshold
 set frequency                      -- Set Radio Frequency (MHz)
 set gateway                        -- Set Gateway IP Address
 set groupkeyupdate                 -- Set Group Key Update Interval (in Seconds
)
 set hostipaddr                     -- Set Host IP address
 set ipaddr                         -- Set IP Address
 set ipmask                         -- Set IP Subnet Mask
 set key                            -- Set Encryption Key
 set keyentrymethod                 -- Select Encryption Key Entry Method
 set keysource                      -- Select Source Of Encryption Keys
 set login                          -- Modify Login User Name
 set minimumrate                    -- Set Minimum Rate
 set nameaddress                    -- Set Name Server IP address
 set operationMode                  -- Set operation Mode
 set password                       -- Modify Password
 set passphrase                     -- Modify Passphrase
 set pktLogEnable                   -- Enable Packet Logging
 set power                          -- Set Transmit Power
 set radiusname                     -- Set RADIUS name or IP address
 set radiusport                     -- Set RADIUS port number
 set radiussecret                   -- Set RADIUS shared secret
 set rate                           -- Set Data Rate
 set reg                            -- Set Register Value
 set remoteAP                       -- Set Remote AP's Mac Address
 set rtsthreshold                   -- Set RTS/CTS Threshold
 set sntpserver                     -- Set SNTP/NTP Server IP Address
 set ssid                           -- Set Service Set ID
 set ssidsuppress                   -- Set SSID Suppress Mode
 set SuperG                         -- Super G Features
 set systemname                     -- Set Access Point System Name
 set tzone                          -- Set Time Zone Setting
 set wlanstate                      -- Set wlan state
 set wirelessmode                   -- Set Wireless LAN Mode
 timeofday                          -- Display Current Time of Day
 version                            -- Software version
 nvram                              -- nvram utility
wlan0 ->
}}}


''Chip vendors:''

- YCL Electronics Corporation, Ltd.
[[BR]] http://www.yclusa.net

- LANKom Electronics Co.,Ltd.
[[BR]]http://www.lankom.com.tw

- Kendin Electronics (company bought by Micrel)
[[BR]]http://www.micrel.com

- Siward
[[BR]]http://www.siward.com

- G-Link Technology
[[BR]]http://www.glinktech.com

- Silicon Storage Technology, Inc.
[[BR]]http://www.sst.com

- Analog Microelectronics, Inc. (AME)
[[BR]]http://www.analogmicro.com
