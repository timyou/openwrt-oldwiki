{{{
VOIP>> help
?       - alias for 'help'
autoscr - run script from memory
base    - print or set address offset
bdinfo  - print Board Info structure
boot    - boot default, i.e., run 'bootcmd'
bootd   - boot default, i.e., run 'bootcmd'
bootm   - boot application image from memory
bootp   - boot image via network using BootP/TFTP protocol
bubt    - Burn an image on the Boot Flash.
bumfg   - Burn mfg data on the mtdblock2.
cmp     - memory compare
cmpm    - Compare Memory
coninfo - print console devices and informations
cp      - memory copy
crc32   - checksum calculation
dcache  - enable or disable data cache
e_cy
echo    - echo args to console
env_info
erase   - erase FLASH memory
flinfo  - print FLASH memory information
g       - start application at cached address 'addr'(default addr 0x40000)
go      - start application at address 'addr'
help    - print online help
icache  - enable or disable instruction cache
iminfo  - print header information for application image
imls    - list all images found in flash
in      - read data from an IO port
itest    - return true/false on integer compare
ixp     - burn boot code(xxx.bin) or image(xxx.img)
loadb   - load binary file over serial line (kermit mode)
loads   - load S-Record file over serial line
loop    - infinite loop on address range
md      - memory display
mii     - MII utility commands
mm      - memory modify (auto-incrementing)
mtest   - simple RAM test
mw      - memory write (fill)
nfs    - boot image via network using NFS protocol
nm      - memory modify (constant address)
out     - write datum to IO port
ping    - send ICMP ECHO_REQUEST to network host
printenv- print environment variables
printnvram - print nvram
protect - enable or disable FLASH write protection
pt
rarpboot- boot image via network using RARP/TFTP protocol
reset   - Perform RESET of the CPU
run     - run commands in an environment variable
saveenv - save environment variables to persistent storage
savenvram - save nvram
setenv  - set environment variables
setnvram - set nvram
sleep   - delay execution for some time
sysinfo - ptintf System Information
tftpboot- boot image via network using TFTP protocol
version - print monitor version
VOIP>> printenv
bootargs=console=ttyS0,115200 root=/dev/mtdblock0 ro noinitrd ip=192.168.15.1:19
2.168.15.4:::MV88W8518:eth0:none console_state=unlocked cy_flash_size=0x800000 c
y_flash_block_size=0x10000 full_image_addr=ff9c0000 half_image_addr=ff800000 boo
t_image=1
bootcmd=setenv bootargs console=ttyS0,115200 root=/dev/mtdblock0 ro noinitrd ip=
$(ipaddr):$(serverip)$(bootargs_end) $(cy_flash_info) $(boot_info) boot_image=$(
boot_image);bootm $(boot_addr);
standalone_mtd=fsload $(default_load_addr) $(image_name);setenv bootargs $(boota
rgs) root=/dev/mtdblock0 rw rootfstype=jffs2 ip=$(ipaddr):$(serverip)$(bootargs_
end);bootm $(default_load_addr);
bootargs_end=:::MV88W8518:eth0:none console_state=unlocked init=/bin/sh
crypt_key=CEB9412451474CE22DF360F9C2ACE0CADFBB8FA947D12535311FC485238B6398
cy_flash_info=cy_flash_size=0x800000 cy_flash_block_size=0x10000
filesize=2a5d44
boot_info=full_image_addr=ff9c0000 half_image_addr=ff800000
console_state=unlocked
fileaddr=400000
serverip=192.168.15.4
shadow_data=admin:YhCA9pXTYavMg:0:0:99999:7:::
model_name=WRP400
wps_pin=22367600
serial_number=CR301H101420
hash_dir=dqngPMavFo
wlan1addr=00:1E:E5:2E:A5:2B
wlanaddr=00:1E:E5:2E:A5:2A
eth1addr=00:1E:E5:2E:A5:29
ethaddr=00:1E:E5:2E:A5:28
admin_pwd=ABWPOsqBBMagI
codepattern=WGTL
ethact=eth0
cy_boot_code_ver=0.00.10 (Sep 27 2007 - 14:42:24)
boot_image=1
boot_addr=ff9c0000
half_image_addr=ff800000
full_image_addr=ff9c0000
flash_size=00800000
initrd_size=400000
initrd_load_addr=800000
initrd_name=ramdisk.image.gz
bootfile=uImage
image_name=uImage
bootargs_root=root=/dev/nfs rw init=/linuxrc
default_load_addr=0x00400000
usbMode=host
ethprime=eth0
stderr=serial
stdout=serial
stdin=serial
rootpath=/tftpboot/rootfs_arm
ipaddr=192.168.15.1
baudrate=115200
bootdelay=1
VOIP>> printnvram
wl_country=EUROPE
wl0_country=EUROPE
wl_country_code=ALL
wl0_country_code=ALL
filter_id=1
wl_active_add_mac=0
ddns_interval=60
wl_temp_auto_channel=8
wsc_service_current_ssid=0
wl1_wsc_enable=0
ping_size=32
wl_lazywds=1
wl0_lazywds=1
os_version=2.6.16.16-88w8xx8
os_date=Jan  9 2008
timer_interval=3600
ntp_enable=1
time_zone=-08 1 1
daylight_time=1
log_level=0
upnp_enable=1
upnp_config=1
upnp_internet_dis=0
upnp_keep_portmap=0
force_igmp_version=2
NTPServer1=209.81.9.7
NTPServer2=207.46.130.100
NTPServer3=192.36.144.23
upnp_ssdp_interval=60
upnp_max_age=180
ezc_enable=1
is_default=1
console_loglevel=1
router_disable=0
fw_disable=0
log_enable=0
log_ipaddr=0
lan_ifname=br0
lan_ifnames=eth0 wlan0
lan_dhcp=0
lan_proto=dhcp
lan_ipaddr=192.168.15.1
lan_netmask=255.255.255.0
lan_lease=86400
lan_stp=0
wan_ifname=eth1
wan_ifnames=eth1
wan_hwaddr=00:1E:E5:2E:A5:29
wan_service=other
wan_proto=dhcp
username_freeDSL_realm=frn6/
username_STRATO_realm=internet1/
wan_ipaddr=0.0.0.0
wan_netmask=0.0.0.0
wan_gateway=0.0.0.0
wan_dns_en=1
wan_lease=0
wan_primary=1
wan_unit=0
filter_macmode=deny
filter=on
filter_services=$NAME:003:DNS$PROT:003:udp$PORT:005:53:53<&nbsp;>$NAME:004:Ping$
PROT:004:icmp$PORT:003:0:0<&nbsp;>$NAME:004:HTTP$PROT:003:tcp$PORT:005:80:80<&nb
sp;>$NAME:005:HTTPS$PROT:003:tcp$PORT:007:443:443<&nbsp;>$NAME:003:FTP$PROT:003:
tcp$PORT:005:21:21<&nbsp;>$NAME:004:POP3$PROT:003:tcp$PORT:007:110:110<&nbsp;>$N
AME:004:IMAP$PROT:003:tcp$PORT:007:143:143<&nbsp;>$NAME:004:SMTP$PROT:003:tcp$PO
RT:005:25:25<&nbsp;>$NAME:004:NNTP$PROT:003:tcp$PORT:007:119:119<&nbsp;>$NAME:00
6:Telnet$PROT:003:tcp$PORT:005:23:23<&nbsp;>$NAME:004:SNMP$PROT:003:udp$PORT:007
:161:161<&nbsp;>$NAME:004:TFTP$PROT:003:udp$PORT:005:69:69<&nbsp;>$NAME:003:IKE$
PROT:003:udp$PORT:007:500:500<&nbsp;>
dmz_enable=0
dmz_src_any=1
dmz_src_ip=0.0.0.0 0
dmz_dst_ip=1
dmz_ipaddr=0
dmz_mac=00:00:00:00:00:00
dhcp_start=100
rtsp_enable=0
multiip_same_mac=0
www_bkcolod=blue
dhcp_num=50
dhcp_lease=0
dhcp_domain=wan
dhcp_wins=wan
http_username=admin
http_passwd=password
idle_time=10
http_wanport=8080
http_lanport=80
http_enable=1
https_enable=0
http_access=0
http_Allow=0
http_Allow_IP=0.0.0.0:0.0.0.0
http_method=post
web_wl_filter=0
ppp_idletime=5
pppoe_idletime=5
ppp_keepalive=0
pppoe_keepalive=0
ppp_demand=1
pppoe_demand=1
ppp_redialperiod=30
ppp_mtu=1492
ppp_static=0
pppoe_static=0
ppp_static_ip=0.0.0.0
pppoe_static_ip=0.0.0.0
upnp_passthrough=0
wl_ifname=wlan0
wl0_ifname=wlan0
wl_phytype=g
wl0_phytype=g
wl_ssid_flag=0
wl_radio=1
wl0_mode=ap
wl0_radio=1
wl_closed=0
wl0_closed=0
sending_power=100
wl_ap_isolate=0
wl0_ap_isolate=0
wl_mode=ap
wl_wds_timeout=1
wl_wep=disabled
wl0_wep=disabled
wl_auth=0
wl0_auth=0
wl_key=1
wl0_key=1
wl_macmode=disabled
wl0_macmode=disabled
wl_macmode1=disabled
wl_channel=11
wl0_channel=11
d11g_channel=11
wl_rate=0
wl0_rate=0
d11g_rate=0
wl_mrate=0
wl_rateset=default
wl0_rateset=default
d11g_rateset=default
wl_frag=2346
wl0_frag=2346
d11g_frag=2346
wl_rts=2347
wl0_rts=2347
d11g_rts=2347
wl_dtim=1
wl0_dtim=1
d11g_dtim=1
wl_bcn=100
wl0_bcn=100
d11g_bcn=100
wl_plcphdr=long
wl0_plcphdr=long
wl_net_mode=mixed
wl_channel_bonding=0
wl_network_performance=0
wl_gmode=1
wl0_gmode=1
d11g_mode=1
wl_gmode_protection=auto
wl0_gmode_protection=auto
wl_afterburner=off
wl0_afterburner=off
wl_frameburst=off
wl0_frameburst=off
wl_wme=off
wl0_wme=off
wl_antdiv=-1
wl_infra=1
wl_wep_bit=5
wl_nmcsidx=-1
dual_ssid=0
wl1_net_mode_tmp=0
wl_wep_key_type=1
wl_wep_input_type=0
wl_security_mode2=wpa2_personal
wl_security_mode=psk psk2
wl_auth_mode=none
wl0_auth_mode=none
wl_wpa_gtk_rekey=3600
wl0_wpa_gtk_rekey=3600
wl_radius_port=1812
wl0_radius_port=1812
wl_crypto=tkip+aes
wl0_crypto=tkip+aes
wl_net_reauth=36000
ses_enable=1
ses_event=2
gpio2=ses_led
gpio3=ses_led2
gpio4=ses_button
ses_led_assertlvl=0
ses_client_join=0
ses_sw_btn_status=DEFAULTS
ses_count=0
wl_wme_sta_bk=15 1023 7 0 0 off
wl0_wme_sta_bk=15 1023 7 0 0 off
wl_wme_sta_be=15 1023 3 0 0 off
wl0_wme_sta_be=15 1023 3 0 0 off
wl_wme_sta_vi=7 15 2 6016 3008 off
wl0_wme_sta_vi=7 15 2 6016 3008 off
wl_wme_sta_vo=3 7 2 3264 1504 off
wl0_wme_sta_vo=3 7 2 3264 1504 off
wl_wme_ap_bk=15 1023 7 0 0 off
wl0_wme_ap_bk=15 1023 7 0 0 off
wl_wme_ap_be=15 63 3 0 0 off
wl0_wme_ap_be=15 63 3 0 0 off
wl_wme_ap_vi=7 15 1 6016 3008 off
wl0_wme_ap_vi=7 15 1 6016 3008 off
wl_wme_ap_vo=3 7 1 3264 1504 off
wl0_wme_ap_vo=3 7 1 3264 1504 off
wl_wme_no_ack=off
wl0_wme_no_ack=off
wl_maxassoc=128
wl_unit=0
wl0_unit=0
wl_dcs_enable=1
wl1_ifname=wlan1
wl1_phytype=g
wl1_radio=0
wl1_closed=0
wl1_ap_isolate=0
wl1_mode=ap
wl1_lazywds=1
wl1_wds_timeout=1
wl1_wep=disabled
wl1_auth=0
wl1_key=1
wl1_macmode=disabled
wl1_macmode1=disabled
wl1_rate=0
wl1_mrate=0
wl1_rateset=default
wl1_frag=2346
wl1_rts=2347
wl1_dtim=1
wl1_bcn=100
wl1_plcphdr=long
wl1_net_mode=mixed
wl1_channel_bonding=0
wl1_network_performance=0
wl1_gmode=1
wl1_gmode_protection=auto
wl1_afterburner=off
wl1_frameburst=off
wl1_wme=off
wl1_antdiv=-1
wl1_infra=1
wl1_wep_bit=5
wl1_wep_key_type=1
wl1_wep_input_type=0
wl1_security_mode2=disabled
wl1_security_mode=disabled
wl1_auth_mode=none
wl1_wpa_gtk_rekey=3600
wl1_radius_port=1812
wl1_crypto=tkip
wl1_net_reauth=36000
wl1_wsc_ie=disabled
wl1_wsc_config=0
restore_defaults=0
router_name=WRP400
ntp_mode=auto
block_loopback=0
block_wan=1
ident_pass=0
block_proxy=0
block_java=0
block_activex=0
block_cookie=0
multicast_pass=1
telnet_enable=0
multicast_immediate_leave=0
multicast_snp=0
ipsec_pass=1
pptp_pass=1
l2tp_pass=1
pppoe_pass=1
remote_management=0
remote_upgrade=0
remote_ip_any=1
remote_ip=0.0.0.0 0
remote_mgt_https=0
mtu_enable=0
wan_mtu=1500
upnp_content_num=12
upnp_content0=0:1:80:80:0:0:HTTP
upnp_content1=0:1:21:21:0:0:FTP
upnp_content2=0:1:22:22:0:0:FTP
upnp_content3=0:1:23:23:0:0:Telnet
upnp_content4=0:1:25:25:0:0:SMTP
upnp_content5=0:2:69:69:0:0:TFTP
upnp_content6=0:1:79:79:0:0:finger
upnp_content7=0:2:123:123:0:0:NTP
upnp_content8=0:1:110:110:0:0:POP3
upnp_content9=0:1:119:119:0:0:NNTP
upnp_content10=0:2:161:161:0:0:SNMP
upnp_content11=0:1:2401:2401:0:0:CVS
wk_mode=gateway
dr_setting=0
dr_lan_tx=0
dr_lan_rx=0
dr_wan_tx=0
dr_wan_rx=0
mac_clone_enable=0
def_hwaddr=00:00:00:00:00:00
ddns_enable=0
ddns_service=dyndns
ddns_wildcard=OFF
ddns_backmx=NO
aol_block_traffic=0
aol_block_traffic1=0
aol_block_traffic2=0
skip_amd_check=0
skip_intel_check=0
wan_gateway_buf=0.0.0.0
wan_speed=4
QoS_wan_speed=51200
QoS_lan_speed=61440
QoS_lan_ctl=0
QoS_wan_ctl=1
QoS=1
rate_mode=1
manual_rate=50000
sel_qosport1=0
sel_qosport2=0
sel_qosport3=0
sel_qosport4=0
sel_qosport5=0
sel_qosport6=0
sel_qosport7=0
sel_qosport8=0
qos_appport1=0
qos_appport2=0
qos_appport3=0
qos_appport4=0
qos_appport5=0
qos_appport6=0
qos_appport7=0
qos_appport8=0
qos_devpri1=0
qos_devpri2=0
qos_devmac1=00:00:00:00:00:00
qos_devmac2=00:00:00:00:00:00
port_priority_1=0
port_flow_control_1=1
port_rate_limit_1=0
port_priority_2=0
port_flow_control_2=1
port_rate_limit_2=0
port_priority_3=0
port_flow_control_3=1
port_rate_limit_3=0
port_priority_4=0
port_flow_control_4=1
port_rate_limit_4=0
enable_game=0
wl_wsc_enable=1
wl_wsc_ie=enabled
wl_wsc_ap_role=proxy
wl_wsc_count=0
wl_wsc_config=0
wl_wsc_result=0
wl_wsc_security_auto=1
wl_wsc_reg_pin=51498269
wl_wsc_ap_uuid=001ee52ea529001ee52fa52800000000
manual_boot_nv=0
lan_mac=00:1E:E5:2E:A5:28
wan_mac=00:1E:E5:2E:A5:29
uses_usb=disable
pv_test=100
is_modified=0
QoS_cnt=0
wl_ssid=linksysA52A
wl0_ssid=linksysA52A
serial_number=CR301H101420
wl_wsc_count2=0
wan_run_mtu=1500
upnp_igd_url=http://192.168.15.1:2869/gatedesc.xml
upnp_igd_udn=uuid:001e-e52e-a528022ea529
wan_iface=eth1
wsc_enrolleeSM_status=0
wsc_regSM_status=0
wsc_ap_sm_status=Config Not inited
wsc_reg_sm_status=Config Not inited
wan_qos_rate=0
http_client_ip=192.168.15.4
http_client_mac=00:E0:29:98:47:FD
http_from=lan
submit_button=Management
chk_action=3
ddns_update=0
wl_wsc_nwkey=password
filter_summary=0
log_type=olog
wsc_trigger_pbc_from_button=0
wl_wsc_enr_pin=00000000
VoiceDefaults=1
FactoryDefaults=1
os_name=linux
wl0_hwaddr=00:1E:E5:2E:A5:2A
wl1_hwaddr=00:1E:E5:2E:A5:2B
lan_hwaddr=00:1E:E5:2E:A5:28
wl_wpa_psk=password
wl0_wpa_psk=password
wl_akm=psk psk2
wl0_akm=psk psk2
action_service=management
Total Size [7778] bytes
VOIP>> imls
Image at FF800000:
   Image Name:   cybertan_half_bin
   Image Type:   ARM Linux Multi-File Image (uncompressed)
   Data Size:    1647868 Bytes =  1.6 MB
   Load Address: 00008000
   Entry Point:  00008000
   Contents:
   Image 0:   873712 Bytes = 853.2 kB
   Image 1:   774144 Bytes = 756 kB
   Verifying Checksum ... OK
Image at FF9C0000:
   Image Name:   cybertan_rom_bin
   Image Type:   ARM Linux Multi-File Image (uncompressed)
   Data Size:    3918104 Bytes =  3.7 MB
   Load Address: 00008000
   Entry Point:  00008000
   Contents:
   Image 0:  1005836 Bytes = 982.3 kB
   Image 1:  2912256 Bytes =  2.8 MB
   Verifying Checksum ... OK
VOIP>> bdinfo
arch_number = 0x0000020F
env_t       = 0x00000000
boot_params = 0x00000100
DRAM bank   = 0x00000000
-> start    = 0x00000000
-> size     = 0x02000000
ethaddr     = 00:00:00:00:00:00
ip_addr     = 192.168.15.1
baudrate    = 115200 bps
VOIP>> env_info
64  bytes  sec num[227],sec index[84],data num[39]
128 bytes  sec num[60],sec index[8],data num[3]
256 bytes  sec num[30],sec index[19],data num[3]
VOIP>> sysinfo
CPU Clock : 360 MHZ
CyberTan Version : 0.00.10
VOIP>> flinfo

Bank # 1: Spansion S29GL064AR3 8Mx16 TopB
  Size: 8 MB in 135 Sectors
  Sector Start Addresses:
    FF800000      FF810000      FF820000      FF830000      FF840000
    FF850000      FF860000      FF870000      FF880000      FF890000
    FF8A0000      FF8B0000      FF8C0000      FF8D0000      FF8E0000
    FF8F0000      FF900000      FF910000      FF920000      FF930000
    FF940000      FF950000      FF960000      FF970000      FF980000
    FF990000      FF9A0000      FF9B0000      FF9C0000      FF9D0000
    FF9E0000      FF9F0000      FFA00000      FFA10000      FFA20000
    FFA30000      FFA40000      FFA50000      FFA60000      FFA70000
    FFA80000      FFA90000      FFAA0000      FFAB0000      FFAC0000
    FFAD0000      FFAE0000      FFAF0000      FFB00000      FFB10000
    FFB20000      FFB30000      FFB40000      FFB50000      FFB60000
    FFB70000      FFB80000      FFB90000      FFBA0000      FFBB0000
    FFBC0000      FFBD0000      FFBE0000      FFBF0000      FFC00000
    FFC10000      FFC20000      FFC30000      FFC40000      FFC50000
    FFC60000      FFC70000      FFC80000      FFC90000      FFCA0000
    FFCB0000      FFCC0000      FFCD0000      FFCE0000      FFCF0000
    FFD00000      FFD10000      FFD20000      FFD30000      FFD40000
    FFD50000      FFD60000      FFD70000      FFD80000      FFD90000
    FFDA0000      FFDB0000      FFDC0000      FFDD0000      FFDE0000
    FFDF0000      FFE00000      FFE10000      FFE20000      FFE30000
    FFE40000      FFE50000      FFE60000      FFE70000      FFE80000
    FFE90000      FFEA0000      FFEB0000      FFEC0000      FFED0000
    FFEE0000      FFEF0000      FFF00000      FFF10000      FFF20000
    FFF30000      FFF40000      FFF50000      FFF60000      FFF70000
    FFF80000      FFF90000      FFFA0000      FFFB0000      FFFC0000
    FFFD0000      FFFE0000      FFFF0000      FFFF2000      FFFF4000
    FFFF6000      FFFF8000      FFFFA000      FFFFC000      FFFFE000
VOIP>> reset

Booting...

  _____        _               _______         _   _
 / ____|      | |             |__   __| /\    | \ | |
| |     _   _ | |__    ___  _ __ | |   /  \   |  \| |
| |    | | | || '_ \  / _ \| '__|| |  / /\ \  | .   |
| |____| |_| || |_) ||  __/| |   | | / ____ \ | |\  |
 \_____|\__, ||_.__/  \___||_|   |_|/_/    \_\|_| \_|
         __/ |
        |___/
__      __    _____  _____    _______
\ \    / /   |_   _||  __ \  |__   __|
 \ \  / /___   | |  | |__) |    | |  ___   __ _  _ __ __ _
  \ \/ // _ \  | |  |  ___/     | | / _ \ / _  ||  _   _  \
   \  /| (_) |_| |_ | |         | ||  __/| (_| || | | | | |
    \/  \___/|_____||_|         |_| \___| \__,_||_| |_| |_|


MARVELL MV88W8518 AP32V.
Based on Feroceon Core with ARM926 LE CPU(360 MHZ)


U-Boot 1.1.1 (Sep 27 2007 - 14:42:26)
Marvell version: 1.1.1.5 MTL

U-Boot code: 00F00000 -> 00F1F734  BSS: -> 00F2D6F4
RAM Configuration:
Bank #0: 00000000 32 MB
Flash:  8 MB
Env Version[0.1]
In:    serial
Out:   serial
Err:   serial
nvram header magic[464c5348]
Net:   Please wait, this takes a while ...
eth0 [PRIME]
--- << CONSOLE_STATE IS unlocked >> ---
 Hit any key to stop autoboot:  1
 0
Checking Boot image at ff9c0000 ...
## Booting image at ff9c0000 ...
   Image Name:   cybertan_rom_bin
   Image Type:   ARM Linux Multi-File Image (uncompressed)
   Data Size:    3918104 Bytes =  3.7 MB
   Load Address: 00008000
   Entry Point:  00008000
   Contents:
   Image 0:  1005836 Bytes = 982.3 kB
   Image 1:  2912256 Bytes =  2.8 MB
OK

Starting kernel ...

Uncompressing Linux.............................................................
........ done, booting the kernel.
                                  Linux version 2.6.16.16-88w8xx8 (kevin@svn.sip
ura.com) (gcc version 3.4.6) #1 PREEMPT Wed Jan 9 20:05:25 PST 2008
CPU: ARM926EJ-Sid(wb) [41069260] revision 0 (ARMv5TEJ)
Machine: MV88W8518
Using U-Boot passing parameters structure - U-Boot release 1.1.1.5
Memory policy: ECC disabled, Data cache writeback
CPU0: D VIVT write-back cache
CPU0: I cache: 32768 bytes, associativity 1, 32 byte lines, 1024 sets
CPU0: D cache: 32768 bytes, associativity 4, 32 byte lines, 256 sets
Built 1 zonelists
Kernel command line: console=ttyS0,115200 root=/dev/mtdblock0 ro noinitrd ip=192
.168.15.1:192.168.15.4:::MV88W8518:eth0:none console_state=unlocked cy_flash_siz
e=0x800000 cy_flash_block_size=0x10000 full_image_addr=ff9c0000 half_image_addr=
ff800000 boot_image=1
PID hash table entries: 256 (order: 8, 4096 bytes)
Dentry cache hash table entries: 8192 (order: 3, 32768 bytes)
Inode-cache hash table entries: 4096 (order: 2, 16384 bytes)
Memory: 32MB = 32MB total
Memory: 30220KB available (1760K code, 320K data, 76K init)
Mount-cache hash table entries: 512
CPU: Testing write buffer coherency: ok
NET: Registered protocol family 16
MV88W8XX8 LSP release 11 for kernel 2.6.16.16
Marvell USB EHCI Host controller
Marvell USB Gadget device controller
TC classifier action (bugs to netdev@vger.kernel.org cc hadi@cyberus.ca)
squashfs: version 3.1 (2006/08/19) Phillip Lougher
we use LZMA workspace is 15980, and original zlib ws is 46912
Initializing Cryptographic API
io scheduler noop registered
io scheduler deadline registered (default)
HDLC line discipline: version $Revision: 4.8 $, maxframe=4096
N_HDLC line discipline registered.
Serial: 8250/16550 driver $Revision: 1.90 $ 2 ports, IRQ sharing enabled
serial8250: ttyS0 at MMIO 0xf800c840 (irq = 11) is a 16550
PPP generic driver version 2.4.2
NET: Registered protocol family 24
PHY found at addr 16,  ID 1410c89,  mii_status 78c9
eth0: mv88w8xx8 FEC @ 80008000, 00:09:11:22:33:45 irq 9
eth1: mv88w8xx8 FEC @ 80008000, 00:09:11:22:33:46 irq 9
full_image_addr [ff9c0000]
half_image_addr [ff800000]
boot_image [1]
k_size= 000f590c
f_size= 002c7000
pad k_size= 000f590c
p_size=c2a4004c,p_base_addr=c2a40000
fs_offset= 000f5958
mv88w8xx8 flash: Found 1 x16 devices at 0x0 in 16-bit bank
 Amd/Fujitsu Extended Query Table at 0x0040
mv88w8xx8 flash: Swapping erase regions for broken CFI table.
number of CFI chips: 1
cfi_cmdset_0002: Disabling erase-suspend-program due to code brokenness.
Creating 8 MTD partitions on "mv88w8xx8 flash":
0x002b5958-0x006e0000 : "LINUX_ROOTFS"
mtd: partition "LINUX_ROOTFS" doesn't start on an erase block boundary -- force
read-only
0x00000000-0x001c0000 : "HALFIMAGE"
0x001c0000-0x006e0000 : "ROMIMAGE"
0x006e0000-0x00720000 : "FPAR"
0x00720000-0x00760000 : "LANG"
0x00760000-0x00780000 : "MFG_DATA"
0x00780000-0x007a0000 : "NVRAM"
0x007a0000-0x00800000 : "UBOOT"
Linux telephony interface: v1.00
tdu_init()
si3215 enable Daisy Chain
slicConfigure() reading f0 from slic 0 devId 1
slicConfigure() reading 30 from slic 0 devId 1
slicConfigure() reading f0 from slic 0 devId 1
slicConfigure() reading f0 from slic 0 devId 1
slicConfigure() reading f0 from slic 0 devId 1
slicConfigure() reading f0 from slic 0 devId 1
slicConfigure() reading f0 from slic 0 devId 1
slicConfigure() reading f0 from slic 0 devId 1
slicConfigure() reading f0 from slic 0 devId 1
slicConfigure() reading f0 from slic 0 devId 1
slicConfigure() reading f0 from slic 0 devId 1
slicConfigure() reading f0 from slic 0 devId 1
slicConfigure() reading f0 from slic 0 devId 1
slicConfigure() reading f0 from slic 0 devId 1
slicConfigure() reading f0 from slic 0 devId 1
slicConfigure() reading f0 from slic 0 devId 1
slicConfigure() reading f0 from slic 0 devId 1
slicConfigure() reading f0 from slic 0 devId 1
slicConfigure() reading f0 from slic 0 devId 1
slicConfigure() reading f0 from slic 0 devId 1
Si3215 Initialization Failure !!!!Si3215 Init Failure#### Si3215Mode control; mo
de=1
slicConfigure() reading f0 from slic 1 devId 2
slicConfigure() reading f0 from slic 1 devId 2
slicConfigure() reading f0 from slic 1 devId 2
slicConfigure() reading f0 from slic 1 devId 2
slicConfigure() reading f0 from slic 1 devId 2
slicConfigure() reading f0 from slic 1 devId 2
slicConfigure() reading f0 from slic 1 devId 2
slicConfigure() reading f0 from slic 1 devId 2
slicConfigure() reading f0 from slic 1 devId 2
slicConfigure() reading f0 from slic 1 devId 2
slicConfigure() reading f0 from slic 1 devId 2
slicConfigure() reading f0 from slic 1 devId 2
slicConfigure() reading f0 from slic 1 devId 2
slicConfigure() reading f0 from slic 1 devId 2
slicConfigure() reading f0 from slic 1 devId 2
slicConfigure() reading f0 from slic 1 devId 2
slicConfigure() reading f0 from slic 1 devId 2
slicConfigure() reading f0 from slic 1 devId 2
slicConfigure() reading f0 from slic 1 devId 2
slicConfigure() reading f0 from slic 1 devId 2
Si3215 Initialization Failure !!!!Si3215 Init Failure#### Si3215Mode control; mo
de=1
phone_mrvl: initialized
GACT probability on
Mirror/redirect action on
u32 classifier
    Perfomance counters on
    input device check on
    Actions configured
Netfilter messages via NETLINK v0.30.
NET: Registered protocol family 2
IP route cache hash table entries: 512 (order: -1, 2048 bytes)
TCP established hash table entries: 2048 (order: 1, 8192 bytes)
TCP bind hash table entries: 2048 (order: 1, 8192 bytes)
TCP: Hash tables configured (established 2048 bind 2048)
TCP reno registered
GRE over IPv4 tunneling driver
ip_conntrack version 2.4 (256 buckets, 2048 max) - 220 bytes per conntrack
ctnetlink v0.90: registering with nfnetlink.
ip_conntrack_pptp version 3.1 loaded
ip_nat_pptp version 3.0 loaded
ip_tables: (C) 2000-2006 Netfilter Core Team
TCP bic registered
NET: Registered protocol family 1
NET: Registered protocol family 17
802.1Q VLAN Support v1.8 Ben Greear <greearb@candelatech.com>
All bugs added by David S. Miller <davem@redhat.com>
p=squashfs
VFS: Mounted root (squashfs filesystem) readonly.
Freeing init memory: 76K
sysinit....
Using /lib/modules/cy_netfilter.ko
Using /lib/modules/cy_fifolog.ko
signal init ....
init nvram....
Name to be unset = wl0_hwaddr=00:1E:E5:2E:A5:2A
Name to be unset = action_service=management
restore_defaults nvram....
New length = 8168
The boot is UNKNOWN
The boot is UNKNOWN
Load CA Data
killall: httpd: no process killed
Using /lib/modules/led_driver.ko
Using /lib/modules/env_driver.ko
cy_env : Init
cy_env : Get UBOOT MTD
cy_env : Init Env
cy_env : Env Version[0.1]
cy_env : Init ENV Device Ok

log_change....log_enable==0
*** log_change done ***
++ RPPLINK: waiting on voice . . .
RPPLINK_CLIENT_INIT_OK
New length = 8197
name=[eth0] lan_ifname=[br0]
=====> set br0 hwaddr to eth0
expect on/off for argument
name=[wlan0] lan_ifname=[br0]
Using /lib/modules/ap-linux.ko
Set MVAP done...
Configuration file: /tmp/wireless_security_file
read mtd5
<6>Allocate memory for User Buffer( 0xc1900000 982016[0x0efc00])
<6>SRAM Allocation for WLAN module 0xfc015000 size 41984
<6>MODULE: defer_triggers created: 0xc02bd000 size: 280)
<6>MODULE: StnQingInfo created: 0xc1f1e000 size: 4760)
<6>MODULE: AssocTable created: 0xc1f28000 size: 10428)
<7>mvWLAN: Registered netdevice wlan0
Already using this reigster handle: 0
Alloc and Init the WLAN device
<7>wlan0: Registered netdevice wlan0ap for AP use
<7>wlan0: mvWLAN_open
<7>wlan0ap: mvWLAN_open
Using interface wlan0 with hwaddr 00:1e:e5:2e:a5:2a and ssid 'linksysA52A'
<7>unsupported ioctl(0x8946)
device wlan0 entered promiscuous mode
unsupported ioctl(0x8946)
Flushing old station entries
Deauthenticate all stations
l2_packet_receive - recvfrom: Network is down
wlan0: STA ff:ff:ff:ff:ff:ff IEEE 802.11: deassociated
wlan0: STA ff:ff:ff:ff:ff:ff IEEE 802.11: deassociated
SIPURA: OAL module initing
SIPURA: OAL Timer module initing
SIPURA: OAL Timer module inited:0
SIPURA: OAL module inited
WIRELESS_ON
SYSTEM_WIRELESS_SES_SECURED
br0: File exists
tdu_nstd_ioctl PHONE_REC_START/PHONE_PLAY_START 1
tdu_nstd_ioctl PHONE_REC_START/PHONE_PLAY_START 1
tdu_nstd_ioctl PHONE_REC_START/PHONE_PLAY_START 0
tdu_nstd_ioctl PHONE_REC_START/PHONE_PLAY_START 0
ioctl failed: Cannot assign requested address
VOICE_PHONE1_OFF
VOICE_PHONE2_OFF
device wlan0 is already a member of a bridge; can't enslave it to bridge br0.
expect on/off for argument
br0: port 2(wlan0) entering learning state
br0: port 1(eth0) entering learning state
br0: topology change detected, propagating
br0: port 2(wlan0) entering forwarding state
br0: topology change detected, propagating
br0: port 1(eth0) entering forwarding state
Busybox configured w/o syslogd
lo: File exists
br0 192.168.15.100  86400
info, udhcp server (v0.9.8-r3230) started
~~~~~ start upnpd ....
zebra disabled.
get lan ipaddr:10fa8c0, netmask:ffffff
disable nev multiple times?
web enabled:1
Name to be unset = wl_wsc_config_method=pin
tftpd: tftp server started
tftpd: tftpd: standalone socket
ioctl failed: Cannot assign requested address
AUD_startCollectDigit(0)
AUD_startCollectDigit(1)
flash_task
RPPLINK_INIT_OK
RPPLINK SP Started
VOICE_PHONE2_OFF
Jan  1 00:00:16 : 5bUpnpd-v010 start!!!

killall: wsc: no process killed

J>>>>>> START WSC  >>>>>>>>>>>
SYSTEM_LAN_UP
received netlink event: 2 with par (5)
received netlink event: 2 with par (5)
tallest:=====( wan_or_lan=wan )=====
tallest:=====( wan_or_lan=wan is wan !!)=====
ioctl failed: Cannot assign requested address
info, udhcp client (v0.9.8-r3230) started

Hit enter to continue...

login: CreateSSDPNotifySocket(192.168.15.1)
 MAC get =00:1E:E5:2E:A5:2A ==================
001EE52EA52A ==================

 ~~~~~~~  enrolleeInfo: auth=2000 ,encry=800 ~~~~~~~~~~

=== debug: InitWSCEnrolleeSM ===

=== debug: InitWSCEnrolleeSM ===

 uuid=001ee52e-a529-001e-e52f-a52800000000  ===================================

 ############  UPnPSetState_WFAWLANConfig_STAStatus!!! ##############

#########  UPnPSendEvent   ###################

#########  UPnPSetState_WFAWLANConfig_APStatus   ###################

#########  UPnPSendEvent   ###################

 ############  UPnPSetState_WFAWLANConfig_WLANEvent!!! ##############

#########  UPnPSendEvent   ###################
hostapd pid is 161
hostapd pid is 161
Dumping Message Received:WscIE.c--line 478, (msgLen 22)ap_config_commit

dd 0e 00 50 f2 04 10 4a : 00 01 10 10 44 00 01 01 :
00 00 00 00 00 00
Dumping Message Received:WscIE.c--line 590, ap_config_commit
(msgLen 128)
dd 78 00 50 f2 04 10 4a : 00 01 10 10 44 00 01 01 :
10 3b 00 01 03 10 47 00 : 10 00 1e e5 2e a5 29 00 :
1e e5 2f a5 28 00 00 00 : 00 10 21 00 0c 4c 69 6e :
6b 73 79 73 20 49 6e 63 : 2e 10 23 00 06 57 52 50 :
34 30 30 10 24 00 07 31 : 2e 30 30 2e 30 34 10 42 :
00 0c 43 52 33 30 31 48 : 31 30 31 34 32 30 10 54 :
00 08 00 06 00 50 f2 04 : 00 01 10 11 00 06 57 52 :
50 34 30 30 10 08 00 02 : 00 88 fc 77 04 00 00 00 :

SYSTEM_WIRELESS_SES_SECURED
ioctl failed: Cannot assign requested address
++ RPPLINK: voice up, starting router server . . .
router : RPPLINK SP Started
received netlink event: 2 with par (8)
ioctl failed: Cannot assign requested address
wlan0: STA ff:ff:ff:ff:ff:ff IEEE 802.11: deassociated
ioctl failed: Cannot assign requested address
ioctl failed: Cannot assign requested address
<<<signal:11 received
SIPURA: OAL module initing
SIPURA: OAL Timer module initing
SIPURA: OAL Timer module inited:0
SIPURA: OAL module inited
tdu_nstd_ioctl PHONE_REC_START/PHONE_PLAY_START 1
tdu_nstd_ioctl PHONE_REC_START/PHONE_PLAY_START 1
tdu_nstd_ioctl PHONE_REC_START/PHONE_PLAY_START 0
tdu_nstd_ioctl PHONE_REC_START/PHONE_PLAY_START 0
get lan ipaddr:10fa8c0, netmask:ffffff
VOICE_PHONE1_OFF
VOICE_PHONE2_OFF
disable nev multiple times?
web enabled:1
AUD_startCollectDigit(0)
AUD_startCollectDigit(1)
flash_task
RPPLINK_INIT_OK
RPPLINK SP Started
VOICE_PHONE2_OFF
ioctl failed: Cannot assign requested address
login:
Password:
!!!!!! Login incorrect !!!!!!

}}}
