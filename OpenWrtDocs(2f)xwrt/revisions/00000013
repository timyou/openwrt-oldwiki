== X-Wrt ==

[http://www.bitsum.com/xwrt.htm X-Wrt] is a project to enhance the end user experience of OpenWrt. It is currently under active development. X-Wrt is developed by a different group than is the base OpenWrt firmware and is therefore not affiliated with OpenWrt, nor is it supported by OpenWrt. Since many users may be interested what X-Wrt has to offer, some basic information about it is included here.

'''X-Wrt Links:'''

 * [http://www.bitsum.com/xwrt.asp X-Wrt Information]
 * [http://developer.berlios.de/projects/xwrt/ Project Hosting (repository, mailing lists, etc..)]
 * [http://www.bitsum.com/smf/index.php?board=17.0 User Forums]

=== X-Wrt Packages ===

Packages documented here are only those in the X-Wrt repository that are not included in the OpenWrt White Russian repository, or have been updated.

The X-Wrt White Russian repository is here: ftp://ftp.berlios.de/pub/xwrt/packages/

==== webif^2: Enhanced HTTP management console ====

'''webif^2^''' is an enhanced webif (HTTP based management console). It offers a large number of new features and is constantly  being improved. Some of the more popular additions are the real-time traffic and CPU graphs. 

 * [http://www.bitsum.com/smf/index.php?topic=267.0 Screenshots] (not necessarily up-to-date with latest build)

To install the latest daily build of webif^2^:

{{{
ipkg install http://ftp.berlios.de/pub/xwrt/webif_latest.ipk
}}}

==== UPNP: Linksys's IGD ====

'''WARNING:''' Not well tested at all.

You can install UPNP by installing linux-igd (and libupnp) from the X-Wrt repository.

linux-igd package: ftp://ftp.berlios.de/pub/xwrt/packages/libupnp_1.2.1a_mipsel.ipk

=== Webif Developer Documentation ===

To date, no documentation has been written on how to write webif pages. The webif system is a combination of shell, awk, html, and javascript (a little). At present, all that can be suggested is to use the existing webif pages as guides and start playing around until you understand how the system works. It's not complex at all, but is a little different than what many may be used to - especially web developers.

==== What is a webif page? ====

A webif page is essentially an HTML page with embedded shell script. Core functions, like the page header/footer and settings forms are implemented by an AWK back-end. For example, see /usr/lib/webif/form.awk, which implements 'display_form' calls in the webif pages.

The 'Save' button on a page causes a submit event which the page can handle as it loads. When FORM_submit is not-empty, the page saves itself through a series of calls to 'save_setting GROUP SETTING' or alternate functions. Conversly, a page should always load its settings via 'load_settings GROUP' to make sure any saved but not yet applied changes are indicated on the page.

==== Using your router for real-time development ====

To use your router as an active development box, do the following:

  * Mount an NFS or SAMBA share somewhere onto your router. (i.e. to /mnt/myshare).
  * Copy /www and /usr/lib/webif folders recursively to your network share. (i.e. cp -r /www /mnt/myshare/).
  * Remove old /www and /usr/lib/webif folders (i.e. rm -rf /www).
  * Symlink the www folder on your network share to the /www folder on your router (i.e. ln -s /mnt/myshare/www /www).
  * Symlink the usr/lib/webif folder on your network share to the /usr/lib/webif folder on your router (i.e. ln -s /mnt/myshare/usr/lib/webif /usr/lib/webif).

Afterwards, restart the httpd or reboot your router. 

This change will persist, so from now on you can work on webif pages by simply editing them on the network share. Changes are shown in real-time as you access the webif on the router.

==== NG-style UCI config vs. nvram ====

OpenWrt is migrating away from nvram, with it completely removed from buildroot-ng. The webif is doing the same. There are new config functions able to load and store files in the UCI config file format.

===== Using NVRAM config functions =====

These functions load and store nvram variables (untyped tuples). An example invocation of saving an nvram varaible is: 'save_setting GROUPNAME VARIABLE=VALUE'.

===== Using NG config functions =====

See /usr/lib/webif/functions.sh , the '_ex' functions for further information.

==== CSS ====

Webif^2^ makes extensive use of CSS. In fact, everything style related should be defined in the CSS. Pages that define their own styles are considered non-conformant and should be changed. 

The CSS is spread out over a few files in /www. The '/www/webif.css' file contains the core CSS style. Over-rides for specific browsers, like Internet Explorer, may also exist in this folder under different names. Color themes are named after their representative colors, of which there are currently 6.
