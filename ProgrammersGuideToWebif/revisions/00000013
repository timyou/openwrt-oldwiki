'''Programmers Guide to webif^2'''
 by Owen Brotherwood, Denmark 2006



[[TableOfContents(3)]]

= Introduction =
 http://xwrt.berlios.de/xwrt.asp is based on 'Openwrt's' web administration tool, Webif, with the thought that there is no need to reinvent the wheel.

Webif^2 tries to add functions that can help novice users quicker into Openwrt.

An interesting [url=http://forum.openwrt.org/viewtopic.php?pid=12558#p12558/ historical document] in the Openwrt forum.

"Programmers Guide to webif" is the only documentaion available, unless you read the code. It is the Dummy's guide based on this dummy's research as an outsider to the webif^2 developement.

IF you feel that you can make a difference, post a NEW topic in [http://www.bitsum.com/smf/index.php?board=17.0 / X-Wrt's forum] saying which module you may be able to do and see if someone else is doing the same thing: maybe cooperate and make 'OpenFriends'.

OR if you are a good shell programmer with no original ideas (like me), look thru the code to see if there are many repeats of code that could be made as library functions. I'm sure the guys at X-Wrt are busy solving problems and creating new features and may sometimes not have the time to go the code with a critical (but constructive) eye.

Suggestions for the guide gratefully received preferably via [http://www.bitsum.com/smf/index.php?board=17.0 / X-Wrt's forum]

Personnel comments (lobbying) and bad humour copywrong the author.

X-ref'ed to:

* OpenWrtDocs/xwrt

* [http://forum.openwrt.org/viewtopic.php?id=7910]http://forum.openwrt.org/viewtopic.php?id=7910]

= What IS a webif page? =

A webif page is essentially an HTML page with embedded shell script. 

Core functions, like the page header/footer and settings forms are implemented by an AWK back-end. For example, see /usr/lib/webif/form.awk, which implements 'display_form' calls in the webif pages.

The 'Save' button on a page causes a submit event which the page can handle as it loads. 

When FORM_submit is not-empty, the page saves itself through a series of calls to 'save_setting GROUP SETTING' or alternate functions. 

Conversly, a page should always load its settings via 'load_settings GROUP' to make sure any saved but not yet applied changes are indicated on the page.

?Is this up to date?

== File and directory structure ==

||<-2>/www contains...||
||index.html      || with redirect to cgi-bin/webif.sh css files .version the svn revision number used in update functions||
||<-2>/cgi-bin contains...||
||webif.sh        ||"exec ./webif/info.sh" ||
||<-2>/webif contains... ||
||                ||a lot of .sh files: the fun part including info.sh .categories which we will come back to as it is a bit of hidden magic||

=== info.sh ===
{{{
#!/usr/bin/webif-page <? . /usr/lib/webif/webif.sh header "Info" "System Information" "@TR<<System Information>>" '' ''

# A lot of shell code ....

footer

?> <!--

##WEBIF:name:Info:1:System Information -->
}}}
The first line tells us that the program that does the work is a binary program /usr/bin/webif-page - webif-page is a suprisingly small in c (when it's not compiled :) )

The second line <? is a bit of magic so we can combine html and shell scripts - Its sister, ?> at the end finishes that magic show.

The third line means we have some nice library functions that can be drawn on in /usr/lib/webif  - there are more: have a look.

The fourth line gives a title  - @TR: see latter in connection with localisation (TRanslation ?)

Then a lot of nice shell scripting - header and footer are NOT football terms but examples of the nice functions we can re-use

The file closes with a cryptic ##WEBIF: which is used as housekeeping for the menu structure of Webif - have a look in /www/cgi-bin/.catogories and there is the answer:
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

add to .categories
{{{
##WEBIF:category:HelloWorld
}}}
cp info.sh to helloworld.sh in cgi-bin/webif

alter the corresponding lines
{{{
 . header "Info" "System Information" "@TR<<System Information>>" '' ''
##WEBIF:name:Info:1:System Information
}}}
to
{{{
header "HelloWorld" "Hello World" "@TR<<Hello World>>" '' ''

##WEBIF:name:HelloWorld:1:Hello World
}}}
Please remember that header text has to match the ##WEBIF line.

Congratulations!

You just made your first do nothing Webif module !!!! Point your browser at your box (maybe reload with no cache) and see your own greeting.

== Info.sh revisited ==

Lobby:)  

Original info.sh
{{{
#!/usr/bin/webif-page <? . /usr/lib/webif/webif.sh header "Info" "System" "@TR<<System>>" '' ''

this_revision=$(cat "/www/.version")

if [ -n "$FORM_update_check" ]; then

 . tmpfile=$(mktemp "/tmp/.webif.XXXXXX")
 wget http://ftp.berlios.de/pub/xwrt/.version -O $tmpfile 2> /dev/null >> /dev/null cat $tmpfile | grep "doesn't exist" 2>&1 >> /dev/null if [ $? = 0 ]; then
  . revision_text="<div id=\"update-error\">ERROR CHECKING FOR UPDATE</div>"
 else
  . latest_revision=$(cat $tmpfile) if [ "$this_revision" != "$latest_revision" ]; then
   . revision_text="<div id=\"update-available\">webif^2 update available: r$latest_revision (you have r$this_revision)</div>"
  else
   . revision_text="<div id=\"update-unavailable\">You have the latest webif^2: r$latest_revision</div>"
  fi
 fi rm -f "$tmpfile"
fi

if [ -n "$FORM_install_webif" ]; then

 . echo "Please wait, installation may take a minute ... <br />" echo "<pre>" ipkg install http://ftp.berlios.de/pub/xwrt/webif_latest.ipk echo "</pre>" this_revision=$(cat "/www/.version")
fi

_version=$(nvram get firmware_version) _kversion="$( uname -srv )" _mac="$(/sbin/ifconfig eth0 | grep HWaddr | cut -b39-)" board_type=$(cat /proc/cpuinfo | sed 2,20d | cut -c16-) device_name=$(nvram get device_name) empty "$device_name" && device_name="unidentified" device_string=$(echo $device_name && ! empty $device_version && echo $device_version) user_string=$REMOTE_USER equal $user_string "" && user_string="not logged in"

echo "<pre>" cat '/etc/banner' echo "</pre><br />" cat <<EOF <table> <tbody>

 . <tr>
  . <td><strong>@TR<<Firmware>></strong></td><td>     </td> <td>$_firmware_name - $_firmware_subtitle $_version</td>
 </tr> <tr>
  . <td><strong>@TR<<Webif>></strong></td><td> </td> <td>webif<sup>2</sup> r$this_revision $revision_text</td>
<td colspan="2"> <form action="" enctype="multipart/form-data" method="post"> <input type="submit" value=" @TR<<Check_Upgrade|Check For Webif^2 Update>> " name="update_check" /> <input type="submit" value=" @TR<<Upgrade_Webif|Upgrade Webif^2>> "  name="install_webif" /> </form> </td> </tr>

 . <tr>
  . <td><strong>@TR<<Kernel>></strong></td><td> </td> <td>$_kversion</td>
 </tr> <tr>
  . <td><strong>@TR<<MAC>></strong></td><td> </td> <td>$_mac</td>
 </tr> <tr>
  . <td><strong>@TR<<Device>></strong></td><td> </td><td> $device_string</td>
 </tr> <tr>
  . <td><strong>@TR<<Board>></strong></td><td> </td><td> $board_type</td>
 </tr> <tr>
  . <td><strong>@TR<<Username>></strong></td><td> </td> <td>$user_string</td>
 </tr> <tr><td><br /><br /></td></tr>
</tbody> </table> EOF

show_validated_logo footer

?> <!--

##WEBIF:name:Info:1:System
-->
}}}
Phew that was long !

Now add a new shared library info.lib
{{{#!
# a lib to be sourced

HTTP_HOME='http://ftp.berlios.de' HTTP_LATEST='/pub/xwrt/webif_latest.ipk' HTTP_VERSION='/pub/xwrt/.version' FILE_VERSION='/www/.version' THIS_VERSION="$(cat ${FILE_VERSION})"

installupdate(){

 . LATEST_VER="${HTTP_HOME}${HTTP_LATEST}" if ipkg install ${LATEST_VER};then
  . return 0
 else
:<<comment

Well sh*t happens and we are now in an unknow state check: any files in /www and lib directories what do we trust so as not to leave a novice user with a 404  one could cat >/www/index.html a nice message to login and install by hand with the ipkg etc text (I keep having to go to home page as I can never remember it) Was there storage so that we could have mv /www/cgi-bin to safe and mv back again before we got here ... comment

 . return 1
 . fi
}

chkforupdate(){

 . this_revision=$1 HOME_VER="${HTTP_HOME}${HTTP_VERSION}" tmpfile=$(mktemp "/tmp/webif.XXXXXX") wget -q -O $tmpfile ${HOME_VER} if [ $? = 0 ]; then
  . latest_revision=$(cat ${tmpfile}) if [ "$this_revision" != "$latest_revision" ]; then
   . txt="${latest_revision}" ret='0'
  else
   . txt="${this_revision}" ret='1'
  fi
 else
  . txt='0' ret='1'
 fi rm -f "$tmpfile" echo ${txt} return ${ret}
}
}}}
Testing? - simply do  . info.lib and call the now "inbuild" function chkforupdate 1001

Now for a new info.sh
{{{
#!/usr/bin/webif-page <? # the shelly bit ... . /usr/lib/webif/webif.sh

header "Info" "System Information" "@TR<<System Information>>" '' ''

. /usr/lib/webif/info.lib

available_version="$(chkforupdate ${THIS_VERSION})" available_return=$?

# some stuff that I don't look to much into ... I_Webif2=${THIS_VERSION} I_Firmware=$(nvram get firmware_version) I_Kernel="$( uname -srv )" I_MAC="$(/sbin/ifconfig eth0 | grep HWaddr | cut -b39-)" I_Board=$(cat /proc/cpuinfo | sed 2,20d | cut -c16-) I_Device=$(nvram get device_name) empty ${I_Device} && I_Device="unidentified" I_Device_String=$(echo $device_name && ! empty $device_version && echo $device_version) I_Username=$REMOTE_USER equal ${I_Username} "" && I_Username="not logged in"

if [ -n "$FORM_install_webif" ]; then

 . echo "<pre>" installupdate echo "</pre>"
#do refresh to clean System Information but how :) fi

#The GUI bit ...go to it guys. This is a mockup cat <<EOF <pre> $(cat '/etc/banner') <pre> <br /> <table> <tbody> $( # yep this should be a subroutine ...mk2colhtml...and yep I cheat :) for line in $(set | grep '^I_'|tr ' ' _);do

 . name=${line%%=''*} name=${name#I_} name=$(echo ${name}|tr _ ' ') value=${line#*=''} value=$(echo ${value}|tr _ ' '|tr -d \') echo "<tr><td>$name</td><td>$value</td></tr>"
done ) </tbody> </table> EOF

if [ "${available_version}" != '0' ]; then cat <<EOF <form action="" enctype="multipart/form-data" method="post"> <input type="submit" value=" @TR<<Upgrade_Webif|Upgrade/Reinstall  Webif^2 r${available_version}>> "  name="install_webif" /> </form>

But I think the button should be in System->Upgrade ... EOF fi

footer

?> <!--

##WEBIF:name:Info:1:System Information
-->
}}}
Calling from info.sh would remove the most of shell from GUI code  and also make available a routine that can be called from GUI OR commandline - the best of both worlds?

Some may prefer the original, others mine: Flame at last :)

== File and directory structure revisited ==
Apart from the /www structure, we have

||/usr/lib/webif/||the webif core: source-able functions are defined here plus awk code||
||/usr/lib/webif/lang/*/common.txt||language translations for the webif||

=== lang ===
Ahh, localisation. So lets just quote from other sources here:

Localization is accomplished by a pre-processor which replaces all '@TR<<symbolname>>' variables with the corresponding symbol value in the currently active language symbol file. If no symbol is found, the symbol name itself is used for the text. Therefore, simply using many @TR<<text>> macros for strings is all that initially needs to be done to make a webif page ready for localization. Translators can later add the symbols to the localized symbol file.
The localized symbol files are, as of White Russian RC6, stored in seperate packages instead of all being included in the base webif set.

The translation is done by webif-page by a hash. It either uses a nvram get "language" (if you use nvram) or if exists /etc/config/webif, finds "lang" (and overwrites the lang it found via nvram ...)

Also, webif-page accepts any *.txt in the laungage directory.

=== /usr/lib/webif ===

A quick grep of the .sh files gives  an idea of the functions available:

{{{
apply-hs.sh:reload_hotspot() { apply-hs.sh:reload_shape() { apply-pptp.sh:reload_pptp() { apply.sh:reload_wifi_enable() { apply.sh:reload_wifi_disable() { apply.sh:reload_network() { apply.sh:reload_wireless() { apply.sh:reload_cron() { apply.sh:reload_syslog() { apply.sh:getPID(){ apply.sh:reload_system() { apply.sh:is_read_only() { functions.sh:load_settings_ex() { functions.sh:save_setting_ex() { functions.sh:commit_settings_ex() {( functions.sh:   option_cb() { functions.sh:load_settings() { functions.sh:validate() { functions.sh:save_setting() { hs.sh:has_required_pkg() { pkgfuncs.sh:is_package_installed() { pkgfuncs.sh:install_package() { pkgfuncs.sh:remove_package() { pkgfuncs.sh:update_package_list() { pkgfuncs.sh:add_package_source() { webif.sh:empty() { webif.sh:equal() { webif.sh:neq() { webif.sh:exists() { webif.sh:categories() { webif.sh:subcategories() { webif.sh:show_validated_logo() { webif.sh:ShowWIPWarning() { webif.sh:update_changes() { webif.sh:has_pkgs() { webif.sh:mini_header() { webif.sh:header() { webif.sh:footer() { webif.sh:apply_passwd() { webif.sh:display_form() { webif.sh:list_remove() { webif.sh:handle_list() { webif.sh:is_bcm947xx() {
}}}
Lobby:  Now wouldn't it have been great if the the functions had started as
{{{
footer() {   # show footer and maybe do something else
}}}
Then I could have made a quick grep '()' * and documented the functions - never mind.

There are also awk files.
{{{
browser.awk        categories.awk     common.awk         editor.awk         form.awk           languages.awk      subcategories.awk  validate.awk
}}}
form.awk gives you predefinded forms to use in you webif page. Most of these are used like formname|input

The current forms are as listed:
{{{
onchange onclick option start_form field button checkbox radio select txtfile option listedit caption string textarea progressbar password upload  submit helpitem helptext helplink checkbox end_form
}}}
Normal parameters:
{{{
# $1 = type # $2 = form variable name # $3 = form variable value # $4 = (radio button) value of button # $5 = string to append # $6 = additional attributes
}}}
Finally there is one csv file: timezones.csv

Lobby: I can't help but think this is misplaced. Timezone information in connection with clock settings aren't dependant on a GUI : they should be a standard part of OpenWrt without having to install webif. The normal /usr/share/zoneinfo files are binary so a waste of flash space on a reduced storage box so some reduced text version in some /usr/share/ directory would be better ...

= Programmer environment =

== ash - the shell ==

$(<file) doesn't work $(cat file) does - apart from that very like bash but there are probably more gotcha's

== testing ==
"vi" can be a pain on your AP box  test your logic as much as possible in a local bash or preferably,busybox/ash environment.

Or mount the AP's filesystem on your favorit computer and test on the real thing. - but beware of a gotcha: a new webif^2 will rm all webif files: including those you work on (I hope this will change) Update: it did

== webif_latest.ipk ==

To get the latest nice clean copy of webif^2 complete package on your shell programming environment:

download latest webif^2 package: 

ftp://ftp.berlios.de/pub/xwrt/webif_latest.ipk

tar zxvf webif_0.2-1_mipsel.ipk

You then tar zxvf the tar.gz files: ./debian-binary ./data.tar.gz ./control.tar.gz

Then you have the package and can poke around :)

== Best Programming Practises ==

Lobby: 

It is allways nice to get code from others but why on earth does he only use 2 spaces for indent or tab or ... Keeping BPP small and necessary speeds implementation of others code.

The BPP for X-Wrt are unknown but could include:

* Indent space using  ? ? ? 
* Don't define a css in your code as for example system-nvram.sh

== X-Wrt trunk ==

Make X-Wrt trunk needs extra pkg's compared to Openwrt on my eduubuntu:

uuencode

Quick guide to building X-wrt

Get the code:

svn checkout svn://svn.berlios.de/xwrt/trunk

cd the trunk

make menuconfig - just say exit and yes: then you "probably" have default config

make

The results are in bin

= Packaging =

Under contstruction Need feedback

In order to make it easier to integrate your new module it is important to :

?? ?? ??

From guymarc who made a [http://www.bitsum.com/smf/index.php?topic=373.msg1684#msg1684 / module] What happened his package in the developement tree:
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

== NG-style UCI config vs. nvram ==
OpenWrt is migrating away from nvram, with it completely removed from buildroot-ng. The webif is doing the same. There are new config functions able to load and store files in the UCI config file format.

=== Using NVRAM config functions ===

These functions load and store nvram variables (untyped tuples). An example invocation of saving an nvram varaible is: 'save_setting GROUPNAME VARIABLE=VALUE'.

=== Using UCI config functions ===

 . See /usr/lib/webif/functions.sh , the '_ex' functions for further information. [/quote]
Needs feedback

== CSS Theme Rules ==

We now support multiple CSS themes in the webif. Contributors of new themes should adhere to these rules:
{{{
The CSS theme must adhere to the existing class/id structure. Changes to class/id names or addition of new ones should be done only if there are no other options, and requires approval of the group. The class/id structure we use should be robust enough to handle various themes. In short, your CSS should adhere to the webif, not the other way around. The CSS theme must support the color switcher. We can have seperate color CSSes for each theme, but it must support all 6 colors. The CSS theme must work in IE 6, IE 7, Opera, and Firefox. You must test it in each. It will not be considered at all for the default theme if it does not work in all browsers. It will be your responsibility to fix bugs and maintain the CSS.
}}}
== How to create a new CSS theme ==

CSS themes exist in a dedicated subdirectory of /www/themes. To add a new theme, create a subdirectory named after your theme. Copy all CSS files from an existing theme into your new directory. Then, start modifying the CSS files. That is all there is to it .

== Security- last again ==

Don't forget the config file that determines what pages require a password.  It's actually determined by the busybox httpd that comes standard, but it's relevant to webif users.

The config file is in /etc/httpd.conf.  Most lines are of the form path: user:password

which means that to access the path the specified user & password must be provided.  The top level (/www on the file system) can be referred to as "/"  (i.e. the paths are with respect to /www). [/quote]

Some people would like the first ("welcome" / status ) page not to have user/pass.

The present hasn't it the past it could have been [url=http://forum.openwrt.org/viewtopic.php?pid=12670#p12670]http://forum.openwrt.org/viewtopic.php?pid=12670#p12670[/url]

== Thanks to ==

Thanks for feedback from: 
* thepeople 
* dude 
* guymarc
