= How to Counting? =
This is only mini example data counting script in Perl and shell, you can download it here: http://opensource.smrtak.com/fdrouter/fdrouter_aplha01.tar .


== Requirement ==
* Perl 

'''ipkg install ftp://ftp.riss-telecom.ru/pub/openwrt/local/whiterussian/packages/perl/perl_5.8.7-1_mipsel.ipk'''

== Instalation ==
1. Copy folder "fdrouter" to /etc/.

2. Edit /etc/fdrouter/users.csv file, and enter persons in format:
IP;MAC-ADDR;USER-NAME
(i.e: 192.168.0.1;00:00:00:00:00:00;smrtak)

3. Copy init.d script from /fdrouter/scripts/S37fdrouter to /etc/init.d/ and give him permission for running.

'''cp /etc/fdrouter/scripts/S37fdrouter /etc/init.d/

chmod 774 /etc/init.d/S37fdrouter'''

4. Create file /etc/crontabs/root and put here this line:

'''*/5 * * * * /etc/fdrouter/stats.sh'''

5. Copy files from /fdrouter/web to /www and file /www/cgi-bin/data.sh must have permissions for running.

'''cp /etc/fdrouter/web/data.sh /www/cgi-bin/

chmod 774 /www/cgi-bin/data.sh'''

6. this is all

== Using web interface ==
Go to web server yours router (i.e. http://192.168.0.1/cgi-bin/data.sh )
You can see your data limit for month, when you are in users.csv.

You can too use adress http://192.168.0.1/cgi-bin/data.sh?ip=all and here is list all users for given month.

== Aditional information ==
This is only alfa version, but i want develope new function (QoS, Graphs, limits, better web int.... ).

Sorry for very bad english, someone can repair me :)

Contact: dev@smrtak.com
----
CategoryHowTo
