== X-Wrt ==

[http://www.bitsum.com/xwrt.htm X-Wrt] is a project to enhance the end user experience of OpenWrt. It is currently under active development. X-Wrt is developed by a different group than is the base OpenWrt firmware and is therefore not affiliated with OpenWrt, nor is it supported by OpenWrt. Since many users may be interested what X-Wrt has to offer, some basic information about it is included here.

'''X-Wrt Links:'''

 * [http://www.bitsum.com/xwrt.asp X-Wrt Information]
 * [http://developer.berlios.de/projects/xwrt/ Project Hosting (repository, mailing lists, etc..)]
 * [http://www.bitsum.com/smf/index.php?board=17.0 User Forums]
 * ["OpenWrtDocs/xwrt" This X-Wrt Wiki]

=== Packages ===

At present, unless otherwise specified, these packages are for White Russian.

==== webif^2: Enhanced HTTP management console ====

'''webif^2^''' is an enhanced webif (HTTP based management console). It offers a large number of new features and is constantly  being improved. Some of the more popular additions are the real-time traffic and CPU graphs. 

 * [http://www.bitsum.com/smf/index.php?topic=267.0 Screenshots] (not necessarily up-to-date with latest build)

To install the latest daily build of webif^2^:

{{{
ipkg install http://ftp.berlios.de/pub/xwrt/webif_latest.ipk
}}}

=== Developing for X-Wrt ===

==== Developing the Webif ====

To date, no documentation has been written on how to write webif pages. The webif system is a combination of shell, awk, html, and javascript (a little). 

To use your router as an active development box, do the following:

  * Mount an NFS or SAMBA share somewhere onto your router. (i.e. to /mnt/myshare).
  * Copy /www and /usr/lib/webif folders recursively to your network share. (i.e. cp -r /www /mnt/myshare/).
  * Remove old /www and /usr/lib/webif folders (i.e. rm -rf /www).
  * Symlink the www folder on your network share to the /www folder on your router (i.e. ln -s /mnt/myshare/www /www).
  * Symlink the usr/lib/webif folder on your network share to the /usr/lib/webif folder on your router (i.e. ln -s /mnt/myshare/usr/lib/webif /usr/lib/webif).
