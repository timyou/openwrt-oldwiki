= BusyBox httpd CGI scripts =

The http daemon expects that CGI script is in subdirectory '''cgi-bin''' under main web directory set by options ''-h'' (default /www and CGI in /www/cgi-bin).
CGI script must have permision for execute (min mode 700).

== CGI ==
Standard set of Comon Gateway Interface environment variable are :
{{{
CONTENT_TYPE=application/x-www-form-urlencoded
GATEWAY_INTERFACE=CGI/1.1
REMOTE_ADDR=192.168.1.180
QUERY_STRING=Zbr=1234567&SrceMB=&ime=jhkjhlkh+klhlkjhlk+%A9%D0%C6%AE%C6%AE&prezime=&sektor=OP
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
REMOTE_USER=[http basic auth username]
}}}

/cgi-bin/test

{{{
#!/bin/sh
echo "Content-type: text/html"
echo ""
echo "<HTML><HEAD><TITLE>Sample CGI Output</TITLE></HEAD>"
echo "<BODY>"
echo "<pre>"
env
echo "</pre>"
echo "</BODY></HTML>"
}}}

Environment variables are set up and the script is invoked with pipes for stdin/stdout.  

== HTML Forms ==

If a post is being done the script is fed the POST data in addition to setting the QUERY_STRING variable (for GETs or POSTs).

Prefered way to do forms in CGI is POST.

=== POST ===

Example how to use POST in form.

/www/form-post.html

{{{
<html>
<head>
<title>CGI Test</title>
</head>

<body>
<form name="form1" method="post" action="/cgi-bin/test-post">
  <p>Text field
    <input name="Text_Field" type="text" id="Text_Field">
  </p>
  <p>Radio button  </p>
  <p>
    <input name="Radio_Button" type="radio" value="1"> 1 
  </p>
  <p>
    <input name="Radio_Button" type="radio" value="2"> 2
  </p>
  <p>
    <input name="Radio_Button" type="radio" value="3"> 3
  </p>
  <p>Some text </p>
  <p>
    <textarea name="Text_Area" id="Text_Area"></textarea>
  </p>
  <p>&nbsp;</p>
  <p>
    <input type="submit" name="Submit" value="Submit">
    <input type="reset" name="Reset" value="Reset">
  </p>
  <p>&nbsp;</p>
  <p>&nbsp;</p>
</form>
</body>
</html>
}}}

/www/cgi-bin/test-post

{{{
#!/bin/sh
echo "Content-type: text/html"
echo ""
echo "<HTML><HEAD><TITLE>Sample CGI Output</TITLE></HEAD>"
echo "<BODY>"
echo "<pre>"
echo "Environment variables"
echo ""
env
echo ""
echo "========================================================="
echo ""
echo "Form variables :"
echo ""
read QUERY_STRING
eval $(echo "$QUERY_STRING"|awk -F'&' '{for(i=1;i<=NF;i++){print $i}}')
tmp=`httpd -d $Text_Field`
echo "Text_Field=$tmp"
tmp=`httpd -d $Radio_Button`
echo "Radio_Button=$tmp"
tmp=`httpd -d $Text_Area`
echo "Text_Area=$tmp"
echo "</pre>"
echo "</BODY></HTML>"
}}}

=== GET ===

Text area fields (and any other field that may contain \n are very hard to menage).

Example how to use GET in form.

/www/form-get.html

{{{
<html>
<head>
<title>CGI Test</title>
</head>

<body>
<form name="form1" method="get" action="/cgi-bin/test-get">
  <p>Text field
    <input name="Text_Field" type="text" id="Text_Field">
  </p>
  <p>Radio button  </p>
  <p>
    <input name="Radio_Button" type="radio" value="1"> 1 
  </p>
  <p>
    <input name="Radio_Button" type="radio" value="2"> 2
  </p>
  <p>
    <input name="Radio_Button" type="radio" value="3"> 3
  </p>
  <p>&nbsp;</p>
  <p>
    <input type="submit" name="Submit" value="Submit">
    <input type="reset" name="Reset" value="Reset">
  </p>
  <p>&nbsp;</p>
  <p>&nbsp;</p>
</form>
</body>
</html>
}}}

/www/cgi-bin/test-get
{{{
#!/bin/sh
echo "Content-type: text/html"
echo ""
echo "<HTML><HEAD><TITLE>Sample CGI Output</TITLE></HEAD>"
echo "<BODY>"
echo "<pre>"
echo "Environment variables"
echo ""
env
echo ""
echo "========================================================="
echo ""
echo "Form variables :"
echo ""
eval $(echo "$QUERY_STRING"|awk -F'&' '{for(i=1;i<=NF;i++){print $i}}')
tmp=`httpd -d $Text_Field`
echo "Text_Field=$tmp"
tmp=`httpd -d $Radio_Button`
echo "Radio_Button=$tmp"
echo "</pre>"
echo "</BODY></HTML>"
}}}
