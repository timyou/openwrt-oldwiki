'''D-Link G604T flashing'''

So let's start. I'll describe the easiest OpenWRT installing method.
You're have a D-Link DSL-G604T device.

First of all you what you need: 

1) Linux machine or shell account;

2) Windows machine for flashing;

3) Yeah, a modem;

4) Old, but V2 utility for flashing ftp://dlink.ru/pub/ADSL/DSL-G604T/Firmware/ADSL2+/V2.00B01T01.EU.20050930/DLinkEU_DSL-G604T_V2.00B01T01.EU.20050930_upgradeB10.exe ;

5) Simple hex editor like XVI.

'''Compiling OpenWRT firmware'''

Goto Linux console and type:

''svn co https://svn.openwrt.org/openwrt/trunk''

My revision was Kamikaze 7629. If your want to specify revision number type:

''svn -r REVISIONNUMBER co https://svn.openwrt.org/openwrt/trunk''

Now go to ''trunk'' directory and type ''make menuconfig''.

In configuration mode we need select those options:

''Target System (TI AR7 [2.6])''

''Target Profile (Texas Instruments WiFi (default))'' - usually set's by default.

''Base system'' -> ''br2684ctl''

''Libraries'' -> ''linux-atm''

''Kernel modules'' -> ''Network Devices'' -> ''kmod-sangam-atm-annex-a''

Then input ''make'' and wait long time (it's depends of your machine's capatibles).
