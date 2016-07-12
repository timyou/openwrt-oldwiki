'''Programmers Guide to Webif(^2)'''

The OpenWrt web interface is based on a set of shell and awk scripts and the form processing is done with haserl. It uses the Busy``Box HTTPD server and is commonly called Webif.[[FootNote(An interesting [http://forum.openwrt.org/viewtopic.php?pid=12558#p12558 historical document] in the Openwrt forum.)]]

 [http://www.x-wrt.org/ Webif^2] is based on Openwrt's web administration tool, Webif, with the thought that there is no need to reinvent the wheel. Webif`^`2 tries to add functions that can help novice users quicker into Openwrt. Much of the included code is taken from Webif`^`2 code at some stage of its developement.

 The "Programmers Guide to Webif" is the only documentaion available, unless you read the code... It is a Dummy's guide based on this dummy's research as an outsider to the webif(^2) developement.

 If you feel that you can make a difference, post a NEW topic in [http://forum.x-wrt.org X-Wrt's forum] saying which module you may be able to do and see if someone else is doing the same thing: maybe cooperate.

 Or if you are a good shell programmer with no original ideas (like me), look thru the code to see if there are many repeats of code that could be made as library functions. I'm sure the guys at X-Wrt are busy solving problems and creating new features and may sometimes not have the time to go the code with a critical (but constructive) eye.

'''Feedback'''
 Suggestions for the guide gratefully received preferably via [http://forum.x-wrt.org X-Wrt's forum]

'''Thanks for feedback from:'''
 * thepeople
 * dude
 * guymarc
'''irc'''
 * irc.freenode.net #x-wrt
'''X-ref'ed'''
 * [:OpenWrtDocs/xwrt:X-Wrt page on openwrt]
----
 [[TableOfContents(4)]]
= What IS a webif page? =
A webif page is essentially an HTML page with embedded shell script.

Core functions, like the page header/footer and settings forms are implemented by an AWK back-end. For example, see /usr/lib/webif/form.awk, which implements 'display_form' calls in the webif pages.[[FootNote(Is this up to date or relevant- I haven't found out yet, this is just taken as is from org wiki ...)]]
  {{{
The 'Save' button on a page causes a submit event which the page can handle as it loads.
When FORM_submit is not-empty, the page saves itself through a series of calls to 'save_setting GROUP SETTING' or alternate functions.
Conversly, a page should always load its settings via 'load_settings GROUP' to make sure any saved but not yet applied changes are indicated on the page.
}}}
== File and directory structure ==
||||<style="text-align: center;">/www contains... ||
||index.html || with redirect to cgi-bin/webif.sh ||
|| ||css files ||
||.version || the svn revision number used in update functions ||
||||<style="text-align: center;">/cgi-bin contains... ||
||webif.sh ||"exec ./webif/info.sh" ||
||||<style="text-align: center;">/webif contains... ||
|| ||a lot of .sh files: the fun part including info.sh ||
||.categories || which we will come back to as it is a bit of hidden magic ||
=== info.sh ===
  {{{
#!/usr/bin/webif-page
<?
. /usr/lib/webif/webif.sh
header "Info" "System Information" "@TR<<System Information>>" '' ''
# A lot of shell code ....
footer
?>
<!--
##WEBIF:name:Info:1:System Information
-->
}}}
  * The first line tells us that the program that is called a binary program /usr/bin/webif-page - webif-page is a suprisingly small in c : see latter in conection with translation
  * The second line <? is a bit of magic so we can combine html and shell scripts - Its sister, ?> at the end finishes that magic show.
  * The third line means we have some nice library functions that can be drawn on in /usr/lib/webif  - there are more: have a look.
  * The fourth line gives a title  - @TR: see latter in connection with localisation (TRanslation)
  * Then a lot of nice shell scripting - header and footer are NOT football terms but examples of the nice functions we can re-use
  * The file closes with a cryptic ##WEBIF: which is used as housekeeping for the menu structure of Webif.   /www/cgi-bin/.catogories contains the order of categpries.
  {{{
##WEBIF:category:Info
##WEBIF:category:Status
##WEBIF:category:System
##WEBIF:category:Network
##WEBIF:category:VPN
##WEBIF:category:HotSpot
##WEBIF:category:Graphs
##WEBIF:category:Reboot
}}}
== Hello world! ==
 The classic example - or do nothing with style

   * add to .categories
   {{{
##WEBIF:category:HelloWorld
}}}
   * cp info.sh to helloworld.sh in cgi-bin/webif
   * alter the corresponding lines
   {{{
 . header "Info" "System Information" "@TR<<System Information>>" '' ''
##WEBIF:name:Info:1:System Information
}}}
   {{{
header "HelloWorld" "Hello World" "@TR<<Hello World>>" '' ''
##WEBIF:name:HelloWorld:1:Hello World
}}}
 Please remember that header text has to match the ##WEBIF line.

 Congratulations, you just made your first do nothing Webif module.Point your browser at your box (maybe reload with no cache) and see your own greeting.

 You can now basically make any status page you want.


 If you want, the category can be added by your script and the category will be ordered last
  {{{
<!--
##WEBIF:category:HelloWorld
##WEBIF:name:HelloWorld:1:Hello World
-->
}}}
== File and directory structure revisited ==
Apart from the /www structure, we have
||/usr/lib/webif/ ||the webif core: source-able functions are defined here plus awk code ||
||/usr/lib/webif/lang/*/common.txt ||language translations for the webif ||
=== lang ===
Ahh, localisation. So lets just quote from other sources here:

{{{
Localization is accomplished by a pre-processor which replaces all '@TR<<symbolname>>' variables with the corresponding symbol value in the currently active language symbol file.
If no symbol is found, the symbol name itself is used for the text.
Therefore, simply using many @TR<<text>> macros for strings is all that initially needs to be done to make a webif page ready for localization. Translators can later add the symbols to the localized symbol file.
The localized symbol files are, as of White Russian RC6, stored in seperate packages instead of all being included in the base webif set.
}}}
The translation is done by webif-page. It either uses a nvram get "language" (if you use nvram) or if exists /etc/config/webif, finds "lang"

Also, webif-page accepts any *.txt in the laungage directory. Which is a big help. So understand "common.txt" as it is and try and reuse text. Specialized txt can be added without changing common.txt

=== /usr/lib/webif ===
A quick grep[[FootNote(grep '().*{' *|sed -e 's/^\(.*\):\(.*\){/||`\1`||`\2`||`doc`||/'  function() {  #doc# does this   would make documentation easier ...)]] of the .sh files gives  an idea of the functions available:
||{{{apply.sh}}} ||{{{reload_wifi_enable() }}} ||Only to be used in apply.sh ||
||{{{apply.sh}}} ||{{{reload_wifi_disable() }}} ||Only to be used in apply.sh ||
||{{{apply.sh}}} ||{{{reload_network() }}} ||Only to be used in apply.sh ||
||{{{apply.sh}}} ||{{{reload_wireless() }}} ||Only to be used in apply.sh ||
||{{{apply.sh}}} ||{{{reload_cron() }}} ||Only to be used in apply.sh ||
||{{{apply.sh}}} ||{{{reload_syslog() }}} ||Only to be used in apply.sh ||
||{{{apply.sh}}} ||{{{ getPID()}}} ||{{{doc}}} ||
||{{{apply.sh}}} ||{{{reload_system() }}} ||Only to be used in apply.sh ||
||{{{apply.sh}}} ||{{{is_read_only() }}} ||{{{doc}}} ||
||{{{apply.sh}}} ||{{{reload_hotspot() }}} ||Only to be used in apply.sh ||
||{{{apply.sh}}} ||{{{reload_shape() }}} ||Only to be used in apply.sh ||
||{{{apply.sh}}} ||{{{reload_pptp() }}} ||Only to be used in apply.sh ||
||{{{apply.sh}}} ||{{{reload_log() }}} ||Only to be used in apply.sh ||
||{{{functions.sh}}} ||{{{empty() }}} ||{{{doc}}} ||
||{{{functions.sh}}} ||{{{equal() }}} ||{{{doc}}} ||
||{{{functions.sh}}} ||{{{neq() }}} ||{{{doc}}} ||
||{{{functions.sh}}} ||{{{exists() }}} ||{{{doc}}} ||
||{{{functions.sh}}} ||{{{is_bcm947xx() }}} ||{{{doc}}} ||
||{{{functions.sh}}} ||{{{remove_lines_from_file() }}} ||{{{doc}}} ||
||{{{functions.sh}}} ||{{{load_settings() }}} ||Loads settings out of the temporary files Syntax: load_settings filename||
||{{{functions.sh}}} ||{{{validate() }}} ||{{{doc}}} ||
||{{{functions.sh}}} ||{{{save_setting() }}} ||Used to save nvram variables. The filename is used for the name of the temporary file used to hold the settings until they are applied. The files are stored in /tmp/.webif/ Syntax: save_setting filename nvram-variable "setting to save"  ||
||{{{hs.sh}}} ||{{{has_required_pkg() }}} ||{{{doc}}} ||
||{{{pkgfuncs.sh}}} ||{{{is_package_installed() }}} ||This function will only check to see if one package is installed. It will return 0 if the package is installed. Example is_package_installed olsrd ||
||{{{pkgfuncs.sh}}} ||{{{install_package() }}} ||{{{doc}}} ||
||{{{pkgfuncs.sh}}} ||{{{remove_package() }}} ||{{{doc}}} ||
||{{{pkgfuncs.sh}}} ||{{{update_package_list() }}} ||{{{doc}}} ||
||{{{pkgfuncs.sh}}} ||{{{add_package_source() }}} ||{{{doc}}} ||
||{{{webif.sh}}} ||{{{categories() }}} ||{{{doc}}} ||
||{{{webif.sh}}} ||{{{subcategories() }}} ||{{{doc}}} ||
||{{{webif.sh}}} ||{{{show_validated_logo() }}} ||Placed right above the footer on pages that pass the w3c validater. ||
||{{{webif.sh}}} ||{{{ShowWIPWarning() }}} ||Placed immediately under header on pages that are a Work In Progress.  ||
||{{{webif.sh}}} ||{{{ShowUntestedWarning() }}} ||Placed immediately under header on pages that are are untested. ||
||{{{webif.sh}}} ||{{{update_changes() }}} ||{{{doc}}} ||
||{{{webif.sh}}} ||{{{has_pkgs() }}} ||Used to check to see if a package is installed. If the package is not installed it will display a install message on the page, if the page is installed it will return nothing. It will except and number of packages by seperating them with a space Example: haspkgs olsrd chillispot||
||{{{webif.sh}}} ||{{{mini_header() }}} ||{{{doc}}} ||
||{{{webif.sh}}} ||{{{header() }}} ||{{{doc}}} ||
||{{{webif.sh}}} ||{{{footer() }}} ||{{{doc}}} ||
||{{{webif.sh}}} ||{{{apply_passwd() }}} ||{{{doc}}} ||
||{{{webif.sh}}} ||{{{display_form() }}} ||{{{doc}}} ||
||{{{webif.sh}}} ||{{{list_remove() }}} ||{{{doc}}} ||
||{{{webif.sh}}} ||{{{handle_list() }}} ||{{{doc}}} ||


There are also awk files.

{{{
browser.awk        categories.awk     common.awk         editor.awk         form.awk           languages.awk      subcategories.awk  validate.awk
}}}
form.awk gives you predefinded forms to use in you webif page. Most of these are used like formname|input

The current forms are as listed:

||start_form||doc||
||onchange||doc||
||onclick||doc||
||field||doc||
||button||doc||
||checkbox||doc||
||radio||doc||
||select||Drop down menu use the option form directly below it to add options to it. menu_variable is the name of the menu, $variable is used to load which variable is currently from the options in the menu. You must set $variable somewhere in the file previous to it being used. Syntax: select|menu_variable|$variable||
||option||Options for the drop down menu Syntax: option|option_variable|Displayed Text||
||txtfile||doc||
||listedit||doc||
||caption||doc||
||string||doc||
||textarea||doc||
||progressbar||doc||
||password||doc||
||upload||doc||
||submit||doc||
||helpitem||doc||
||helptext||doc||
||helplink||doc||
||end_form||doc||

Normal parameters:

{{{
# $1 = type # $2 = form variable name # $3 = form variable value # $4 = (radio button) value of button # $5 = string to append # $6 = additional attributes
}}}
Finally there is one csv file: timezones.csv[[FootNote(I can't help but think this is misplaced. Timezone information in connection with clock settings aren't dependant on a GUI : they should be a standard part of OpenWrt without having to install webif. The normal /usr/share/zoneinfo files are binary so a waste of flash space on a reduced storage box so some reduced text version in some /usr/share/ directory would be better)]]

= Programmer environment =
== httpd and cgi ==
{{{
The OpenWrt web interface is based on a set of shell and awk scripts and the form processing is done with haserl. It uses the BusyBox HTTPD server.
}}}
[[FootNote(From OpenWrt's Faq: still investigating)]]
{{{
root@oxo-t:/www/cgi-bin/webif# webif-page
This is haserl version 0.8.0
This program runs as a cgi interpeter, not interactively.
Bug reports to: Nathan Angelacos <nangel@users.sourceforge.net>
root@oxo-t:/www/cgi-bin/webif# haserl
This is haserl version 0.8.0
This program runs as a cgi interpeter, not interactively.
Bug reports to: Nathan Angelacos <nangel@users.sourceforge.net>
}}}
 As stated earlier, webif-page is a pre-processor to ... haserl. webif-page is "just" the translator.[[FootNote(There are translations but ... help is sparce, the technical terms and the help for them could be in a wiki page ...)]]
{{{
webif-page.c:   char *proc = "/usr/bin/haserl";
}}}
== ash - the shell ==
 $(<file) doesn't work $(cat file) does - apart from that very like bash but there are probably more gotcha's
== testing ==
 "vi" can be a pain on your AP box  test your logic as much as possible in a local bash or preferably,busybox/ash environment.

 Or mount the AP's filesystem on your favorit computer and test on the real thing.
{{{
To use your router as an active development box, do the following:
  * Mount an NFS or SAMBA share somewhere onto your router. (i.e. to /mnt/myshare).
  * Copy /www and /usr/lib/webif folders recursively to your network share. (i.e. cp -r /www /mnt/myshare/).
  * Remove old /www and /usr/lib/webif folders (i.e. rm -rf /www).
  * Symlink the www folder on your network share to the /www folder on your router (i.e. ln -s /mnt/myshare/www /www).
  * Symlink the usr/lib/webif folder on your network share to the /usr/lib/webif folder on your router (i.e. ln -s /mnt/myshare/usr/lib/webif /usr/lib/webif).
Afterwards, restart the httpd or reboot your router.
This change will persist, so from now on you can work on webif pages by simply editing them on the network share. Changes are shown in real-time as you access the webif on the router.
}}}
== webif_latest.ipk ==
 To get the latest nice clean copy of webif^2 complete package on your shell programming environment:

  * download latest webif^2 package:

  * ftp://ftp.berlios.de/pub/xwrt/webif_latest.ipk

  * tar zxvf webif_0.2-1_mipsel.ipk

 You then tar zxvf the tar.gz files: ./debian-binary ./data.tar.gz ./control.tar.gz

 Then you have the package and can poke around :)
{{{
$ ls -R
.:
bin  control  debian-binary  etc  lib  postinst  preinst  sbin  usr  www
./bin:
uci
./etc:
dnsmasq.options  ez-ipupdate  functions-net.sh  functions_ex.sh  httpd.webif  init.d  ppp
./etc/ez-ipupdate:
ez-ipupdate-ok.sh
./etc/init.d:
S01syslog  S50openvpn      S60ntp          S90pptp            S90webif_firmwareid  x60cron.webif
S41ipkg    S52ez-ipupdate  S66upnpd_webif  S90webif_deviceid  x50dnsmasq.webif
./etc/ppp:
functions.sh
./lib:
config
./lib/config:
uci-update.awk  uci.sh
./sbin:
runsyslogd
./usr:
bin  lib
./usr/bin:
bstrip  webif-page  wepkeygen
./usr/lib:
webif
./usr/lib/webif:
apply-ez-ipupdate.sh  categories.awk  form.awk      languages.awk      timezones.csv
apply.sh              common.awk      functions.sh  pkgfuncs.sh        validate.awk
browser.awk           editor.awk      hs.sh         subcategories.awk  webif.sh
./www:
cgi-bin  colorize.js  favicon.ico  images  index.html  svggraph  themes  webif.js
./www/cgi-bin:
webif  webif.sh
./www/cgi-bin/webif:
config.sh                network-logread-ez-ipupdate.sh        status-openvpn.sh
data.sh                  network-logread-ez-ipupdate_frame.sh  status-pppoe.sh
graphs-cpu.sh            network-misc.sh                       status-pptp.sh
graphs-if.sh             network-qos.sh                        status-qos.sh
graphs-subcategories.sh  network-services.sh                   status-usb.sh
hs.sh                    network-vlan.sh                       status-wlan-survey.sh
iframe.mini-info.sh      network-wakeonlan.sh                  system-confman.sh
index.sh                 network-wan-lan.sh                    system-cron.sh
info-about.sh            network-wifi-lan.sh                   system-crontabs.sh
info.sh                  network-wlan-advanced.sh              system-editor.sh
ipkg.sh                  network-wlan.sh                       system-ipkg.sh
log-browse.sh            qos-nbd.inc                           system-nvram.sh
log-read.sh              qos-rudy.inc                          system-password.sh
log-read_frame.sh        reboot.sh                             system-settings.sh
log-setup.sh             status-asterisk.sh                    system-startup.sh
network-dhcpiface.sh     status-basic.sh                       system-upgrade.sh
network-dhcpsettings.sh  status-connection.sh                  vpn-openvpn.sh
network-ez-ipupdate.sh   status-conntrackread.sh               vpn-pptp.sh
network-firewall.sh      status-interfaces.sh
network-hosts.sh         status-leases.sh
./www/images:
openwrt-logo.png
./www/svggraph:
graph_cpu.svg  graph_if.svg
./www/themes:
xwrt
./www/themes/xwrt:
color_black.css  color_brown.css   color_green.css     color_white.css  webif.css
color_blue.css   color_common.css  color_navyblue.css  ie_lt7.css
}}}
= X-Wrt trunk =
== Recommendation ==
 '''The recommended thing to do...'''

  You do not need to flash X-Wrt to take advantage of our work. The best thing to do is flash OpenWrt White Russian, then install our packages. That is the beauty of OpenWrt, is an extensible system. Recommended instructions to install X-Wrt packages on top of OpenWrt are here: http://www.bitsum.com/xwrt.asp .

 '''The unrecommended thing to do...'''

  For those who actually want to install X-Wrt firmware images instead of OpenWrt, an action not recommended or supporrted at present, browse our ftp directory and find the .rar that contains an archive of all X-Wrt firmware images. This archive of a mere 5.5MB contains all variants of X-Wrt firmware images. Once you've downloaded it, extract it using RAR and TAR, then flash the image appropriate for your device (in accordance with the same naming rules that govern OpenWrt). If you can't figure out what this babble means, then please do not flash X-Wrt and instead see the first paragraph of this post.

 '''Advantages of X-Wrt over OpenWrt+Webif^2:'''

  Busybox 1.2.1 instead of Busybox 1.0.0 - for most users this hardly matters. More common packages included by default. Will save space flash space for most users who don't use the image builder to pre-install their desired packages.

 '''Disadvantages of X-Wrt over OpenWrt+Webif^2:'''

  Less well tested. In a state of flux at present.

 '''Things that are NOT affected'''

  All X-Wrt packages work equally well either way.
== Quick guide to building X-wrt ==
 Get the code:
  * svn checkout svn://svn.berlios.de/xwrt/trunk
  * cd the trunk
 (you could also cd package/webif to see the source package of webif^2)
  * make menuconfig - just say exit and yes: then you "probably" have default config
  * make
 The results are in bin
=== Ubuntu ===
 Make X-Wrt trunk needs extra pkg's compared to Openwrt on my eduubuntu:
  * uuencode
= Packaging =
 Under contstruction Need feedback

 In order to make it easier to integrate your new module it is important to :

?? ?? ??

 From guymarc who made a [http://www.bitsum.com/smf/index.php?topic=373.msg1684#msg1684/ module] What happened his package in the developement tree:
{{{
these files have been modified:
apply.sh: added reload_logwrt() function
.categories: added a new menu entry "Log"
webif.preinst: added the rm -f S01syslog command to make the system clear before an update
these files have been added:
added /sbin/runsyslogd: the script for launching syslogd with the right command line
added file S01syslog: starting syslogd at boot-time with the options selected in webif
log-browse.sh and log-setup.sh off course
Do these infos meet your needs ?
About our discussion yesterday, I think that webif is modular except for the apply.sh file. I can clrify this point.
In fact, we do not have a utility allowing to safely alter apply.sh (for adding or removing a service), and adding a service at preinst or postinst time seems quite difficult for me.
You have to insert a line here to enable your function. You will find mine:
HANDLERS_config='
   wireless) reload_wireless;;
   network) reload_network;;
   system) reload_system;;
   cron) reload_cron;;
   syslog) reload_syslog;;
   wifi-enable) reload_wifi_enable;;
   wifi-disable) reload_wifi_disable;;
   hotspot) reload_hotspot;;
   shape) reload_shape;;
   pptp) reload_pptp;;
   log) reload_log;;
        ^^^^^^^^^
'
HANDLERS_file='
   hosts) rm -f /etc/hosts; mv $config /etc/hosts; killall -HUP dnsmasq ;;
   ethers) rm -f /etc/ethers; mv $config /etc/ethers; killall -HUP dnsmasq ;;
   firewall) mv /tmp/.webif/file-firewall /etc/config/firewall && /etc/init.d/S??firewall;;
   dnsmasq.conf) mv /tmp/.webif/file-dnsmasq.conf /etc/dnsmasq.conf && /etc/init.d/S50dnsmasq;;
'
and then add the code of your function, reload_log() for me, in the body of the file (this can be easy if simply appended at the end of the file).
}}}
= Diverse =
== NG-style UCI config vs. nvram ==
 OpenWrt is migrating away from nvram, with it completely removed from buildroot-ng. The webif is doing the same. There are new config functions able to load and store files in the UCI config file format.
=== Using NVRAM config functions ===
 These functions load and store nvram variables (untyped tuples). An example invocation of saving an nvram varaible is: 'save_setting GROUPNAME VARIABLE=VALUE'.
=== Using UCI config functions ===
 See /usr/lib/webif/functions.sh , the '_ex' functions for further information. [/quote]
 Needs feedback
== CSS Theme Rules ==
 We now support multiple CSS themes in the webif. Contributors of new themes should adhere to these rules:
{{{
The CSS theme must adhere to the existing class/id structure.
Changes to class/id names or addition of new ones should be done only if there are no other options, and requires approval of the group.
The class/id structure we use should be robust enough to handle various themes.
In short, your CSS should adhere to the webif, not the other way around.
The CSS theme must support the color switcher. We can have seperate color CSSes for each theme, but it must support all 6 colors.
The CSS theme must work in IE 6, IE 7, Opera, and Firefox. You must test it in each.
It will not be considered at all for the default theme if it does not work in all browsers. It will be your responsibility to fix bugs and maintain the CSS.
}}}
=== How to create a new CSS theme ===
 CSS themes exist in a dedicated subdirectory of /www/themes.

 To add a new theme:
  * create a subdirectory named after your theme.
  * Copy all CSS files from an existing theme into your new directory. Then, start modifying the CSS files. That is all there is to it .

 Or, just delete the default css file and get WHITE Russian: would be nice with a choice for no css theme ...
== Security- last again ==
 Don't forget the config file that determines what pages require a password.  It's actually determined by the busybox httpd that comes standard, but it's relevant to webif users.

 The config file is in /etc/httpd.conf.[[FootNote(Could do with a bit morw info with busyboxes http server)]]

 Most lines are of the form path: user:password which means that to access the path the specified user & password must be provided.

 The top level (/www on the file system) can be referred to as "/"  (i.e. the paths are with respect to /www). [/quote]

 Some people would like the first ("welcome" / status ) page not to have user/pass.

 The present hasn't this, the past may have http://forum.openwrt.org/viewtopic.php?pid=12670#p12670
= o-o =
 * [http://www.busybox.net/downloads/BusyBox.html busybox]
 * [http://matt.ucc.asn.au/dropbear/dropbear.html dropbear]
 * [http://haserl.sourceforge.net/haserl.html haserl]
= Footnotes =
