= BusyBox httpd CGI scripts =

Daemon expect that CGI script is in subdirectory '''cgi-bin''' under main web directory set by options ''-h'' (default /www and CGI in /www/cgi-bin).
CGI script must have permision for execute (min mode 700).

== CGI ==
Standard set of Comon Gateway Interface environment variable are :
{{{
CONTENT_TYPE=application/x-www-form-urlencoded
GATEWAY_INTERFACE=CGI/1.1
REMOTE_ADDR=192.168.1.180
QUERY_STRING=Zbr=1234567&SrceMB=&ime=jhkjhlkh+klhlkjhlk+%A9%D0%C6%AE%C6%AE&prezime=&sektor=OP&textfield=&uid=&email=&textfield=&submit=Smisli
REMOTE_PORT=2292
CONTENT_LENGTH=128
REQUEST_URI=/cgi-bin/test
SERVER_SOFTWARE=busybox httpd/1.35 6-Oct-2004
PATH=/bin:/sbin:/usr/bin:/usr/sbin
HTTP_REFERER=http://192.168.1.1/index1.html
SERVER_PROTOCOL=HTTP/1.0
PATH_INFO=
REQUEST_METHOD=POST
PWD=/www/cgi-bin
SERVER_PORT=80
SCRIPT_NAME=/cgi-bin/test
}}}
