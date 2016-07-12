= httpd =
'''httpd''' is the binary, part of BusyBox, tool that start http daemon.

== Usage ==
The usage for '''httpd''' is :
{{{
Usage: httpd [options]

        ===== daemon options =====
        -c FILE         Specifies configuration file. (default httpd.conf)
                        = -c /etc/httpd.config
	                =  if -c is not set, an attempt will be made to open the 
                           default root configuration file.  
	                   If -c is set and the file is not found, the server 
                           exits with an error

        -p PORT         Server port (default 80)
                        = -p 80

        -r REALM        Authentication Realm for Basic Authentication
                        = -r "WRT54GS Router"
	                = default realm "Web Server Authentication"

        -h HOME         Specifies http HOME directory (default ./)
                        = -h /www


        ===== script options =====
        -m PASS         Crypt PASS with md5 algorithm
                        = foo=`httpd -m "astro"`  # MD5 string $1$$e6xMPuPW0w8dESCuffefU.
 
        -e STRING       Html encode STRING
                        = bar=`httpd -e "<Hello World>"`   # encode as "&#60Hello&#32World&#62"

        -d STRING       URL decode STRING
                        = foo=`httpd -d $foo`  # decode "Hello%20World" as "Hello World"


        ==== available but not used ? ====
        -u UID          Start httpd under UID
        -u user_name    Start httpd under UID of user_name user
        -v              Verbose (but show nothing) oposite of daemon mod
}}}

[:OpenWrtDocs/httpd.conf: Configuration file] may have any name, but it is good practice to be in /etc with name [:OpenWrtDocs/httpd.conf: httpd.conf].


'''httpd''' suport [:OpenWrtDocs/httpd_CGI_scripts: CGI script]. 
 
Note that multiple instances of httpd can be run, which would have different .conf files, e.g.

/usr/sbin/httpd -p 80 -h /www

/usr/sbin/httpd -p 8080 -h /www2 -c /etc/httpd2.conf

The first instance could be open for public viewing, the second password protected--see .conf settings
