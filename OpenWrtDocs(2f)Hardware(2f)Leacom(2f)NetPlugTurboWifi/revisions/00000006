= Leacom NetPlug Turbo Wi-Fi 85Mbps =

== Hardware ==

This device is a Wireless Access Point / PowerLine Communication gateway.

{{{
OS : VxWorks
CPU : Atheros AR2313A
Wi-Fi : Atheros AR2112a RF
Flash : MX29LV160C (2 Mb)
PLC CPU : Intellon INT5500A1G connected via a Kendin PHY
PLC PHY : Intellon INT2000A0G connected via MII to the INT55000
Ethernet Switch : Realtek RTL8201CP connected via MII to the INT5500 and the Kendin PHY
}}}

== How does it work ? ==

It took me a while to understand :

{{{
 * The CPU sends ethernet frame using its MAC to the Kendin PHY
 * The Realtek switch sends this frame to the Intellon 5500
 * The Intellon 5500 encrypts frames with 56-bit DES (HomePlug 1.0/1.1) then sends it to the Int 2000 PLC Phy
 * The Intellon 2000 does the proper modulation and sends it on the AC line
}}}

== Why a switch ? ==

Good question, mostly because there are 2 kinds of Ethernet frames : classic Ethernet PLC (EtherType 0x8800), and PLC management Ethernet frames. This is the reason for making this distinction.

List of commands :

{{{
Access Point CPL wlan1 -> help
List of Access Point CLI commands:
 clear ecl                          -- Clear ethernet client list
 config wlan                        -- config wlanX
 connect bss                        -- connect to bssX
 find bss                           -- Find BSS
 find channel                       -- Find Available Channel
 find all                           -- Find All BSS
 get 11gonly                        -- Display 11g Only Allowed
 get 11goptimize                    -- Display 11g Optimization Level
 get 11goverlapbss                  -- Display Overlapping BSS Protection
 get aeswpa                         -- Display AES WPA type
 get aeswpattlsuser                 -- Display AES WPA-TTLS username
 get aeswpattlspwd                  -- Display AES WPA-TTLS password
 get aeswpattlsauth                 -- Display AES WPA-TTLS AuthType
 get aeswpapeapuser                 -- Display AES WPA-PEAP username
 get aeswpapeappwd                  -- Display AES WPA-PEAP password
 get aeswpapeapauth                 -- Display AES WPA-PEAP AuthType
 get aeswpapskpassphrase            -- Display AES WPA-PSK PassPhrase
 get aeswpapskhex                   -- Display AES WPA-PSK Hex Digital
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
 get ctsmode                        -- Display CTS mode
 get ctsrate                        -- Display CTS rate
 get ctstype                        -- Display CTS type
 get dhcpc                          -- Display DHCP Client Mode
 get domainsuffix                   -- Display Domain Name Server suffix
 get dtim                           -- Display Data Beacon Rate (DTIM)
 get ethclient                      -- Display Ethernet Client List
 get encryption                     -- Display Encryption Mode
 get extendedchanmode               -- Display Extended Channel Mode
 get fragmentthreshold              -- Display Fragment Threshold
 get frequency                      -- Display Radio Frequency (MHz)
 get gateway                        -- Display Gateway IP Address
 get groupkeyupdate                 -- Display Group Key Update Interval (in Seconds)
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
 get remoteAp                       -- Display Remote Ap's Mac Address
 get rtsthreshold                   -- Display RTS/CTS Threshold
 get shortpreamble                  -- Display Short Preamble Usage
 get shortslottime                  -- Display Short Slot Time Usage
 get sntpserver                     -- Display SNTP/NTP Server IP Address
 get ssid                           -- Display Service Set ID
 get ssidsuppress                   -- Display SSID Suppress Mode
 get station                        -- Display Station Status
 get SuperG                         -- Display SuperG Feature Status
 get systemname                     -- Display Access Point System Name
 get telnet                         -- Display Telnet Mode
 get timeout                        -- Display Telnet Timeout
 get tkipwpa                        -- Display TKIP WPA type
 get tkipwpattlsuser                -- Display TKIP WPA-TTLS username
 get tkipwpattlspwd                 -- Display TKIP WPA-TTLS password
 get tkipwpattlsauth                -- Display TKIP WPA-TTLS Auth Type
 get tkipwpapeapuser                -- Display TKIP WPA-PEAP username
 get tkipwpapeappwd                 -- Display TKIP WPA-PEAP password
 get tkipwpapeapauth                -- Display TKIP WPA-PEAP Auth Type
 get tkipwpapskpassphrase           -- Display TKIP WPA-PSK PassPhrase
 get tkipwpapskhex                  -- Display TKIP WPA-PSK Hex Digital
 get tzone                          -- Display Time Zone Setting
 get uptime                         -- Display UpTime
 get wirelessmode                   -- Display Wireless LAN Mode
 get wlanstate                      -- Display wlan state
 help                               -- Display CLI Command List
 ping                               -- Ping
 pktLog                             -- Packet Log
 reboot                             -- Reboot Access Point
 clearBootLine                      -- Reboot Access Point
 run                                -- Run command file
 quit                               -- Logoff
 set 11gonly                        -- Set 11g Only Allowed
 set 11goptimize                    -- Set 11g Optimization Level
 set 11goverlapbss                  -- Set Overlapping BSS Protection
 set aeswpa                         -- Set AES WPA type
 set aeswpattlsuser                 -- Set AES WPA-TTLS username
 set aeswpattlspwd                  -- Set AES WPA-TTLS password
 set aeswpattlsauth                 -- Set AES WPA-TTLS AuthType
 set aeswpapeapuser                 -- Set AES WPA-PEAP username
 set aeswpapeappwd                  -- Set AES WPA-PEAP password
 set aeswpapeapauth                 -- Set AES WPA-PEAP AuthType
 set aeswpapskpassphrase            -- Set AES WPA-PSK PassPhrase
 set aeswpapskhex                   -- Set AES WPA-PSK Hex Digital
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
 set ctsmode                        -- Set CTS Mode
 set ctsrate                        -- Set CTS Rate
 set ctstype                        -- Set CTS Type
 set dhcpc                          -- set DHCP Client Mode
 set domainsuffix                   -- Set Domain Name Server Suffix
 set dtim                           -- Set Data Beacon Rate (DTIM)
 set encryption                     -- Set Encryption Mode
 set extendedchanmode               -- Set Extended Channel Mode
 set factorydefault                 -- Restore to Default Factory Settings
 set fragmentthreshold              -- Set Fragment Threshold
 set frequency                      -- Set Radio Frequency (MHz)
 set gateway                        -- Set Gateway IP Address
 set groupkeyupdate                 -- Set Group Key Update Interval (in Seconds)
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
 set pktLogEnable                   -- Enable Packet Logging
 set power                          -- Set Transmit Power
 set radiusname                     -- Set RADIUS name or IP address
 set radiusport                     -- Set RADIUS port number
 set radiussecret                   -- Set RADIUS shared secret
 set rate                           -- Set Data Rate
 set remoteAP                       -- Set Remote AP's Mac Address
 set rtsthreshold                   -- Set RTS/CTS Threshold
 set shortpreamble                  -- Set Short Preamble
 set shortslottime                  -- Set Short Slot Time
 set sntpserver                     -- Set SNTP/NTP Server IP Address
 set tzone                          -- Set Time Zone Setting
 set ssid                           -- Set Service Set ID
 set ssidsuppress                   -- Set SSID Suppress Mode
 set SuperG                         -- Super G Features
 set systemname                     -- Set Access Point System Name
 set telnet                         -- Set Telnet Mode
 set timeout                        -- Set Telnet Timeout
 set tkipwpa                        -- Set TKIP WPA type
 set tkipwpattlsuser                -- Set TKIP WPA-TTLS username
 set tkipwpattlspwd                 -- Set TKIP WPA-TTLS password
 set tkipwpattlsauth                -- Set TKIP WPA-TTLS Auth Type
 set tkipwpapeapuser                -- Set TKIP WPA-PEAP username
 set tkipwpapeappwd                 -- Set TKIP WPA-PEAP password
 set tkipwpapeapauth                -- Set TKIP WPA-PEAP Auth Type
 set tkipwpapskpassphrase           -- Set TKIP WPA-PSK PassPhrase
 set tkipwpapskhex                  -- Set TKIP WPA-PSK Hex Digital
 set wlanstate                      -- Set wlan state
 set wirelessmode                   -- Set Wireless LAN Mode
 timeofday                          -- Display Current Time of Day
 version                            -- Software version
 applycfg                           -- Apply configuration changes
}}}
