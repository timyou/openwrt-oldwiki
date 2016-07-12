'''Transfer files to and from the Wrt'''


[[TableOfContents]]


= Introduction =

Sometimes it's useful to exchange files between your PC and the Wrt
router. This is the case when you like to make a backup of some files
or install extra packages offline.


= Requirements =

 * You need to have !OpenWrt installed (should work with almost any version,
 old ones too)
 * The programs for the method you have chosen installed on your PC


= Methods to transfer files =

'''TIP:''' Remember to set a password with {{{passwd}}}.


== Transfer files onto the Wrt ==

=== via SCP (Secure Copy) ===

On the PC connected to the Wrt execute:

{{{
user@host:~$ scp /tmp/foobar.txt root@192.168.1.1:/tmp
}}}

This command copies the {{{/tmp/foobar.txt}}} file from the PC to the
Wrt with the IP address {{{192.168.1.1}}} into the {{{/tmp}}} directory.


== Receiving files from the Wrt ==

=== via SCP (Secure Copy) ===

{{{
user@host:~$ scp root@192.168.1.1:/tmp/foobar.txt /tmp
}}}

Copies a {{{/tmp/foobar.txt}}} from the Wrt to {{{/tmp}}} on the PC.


=== via wget ===

Start a second HTTPD webserver process on the Wrt with

{{{
httpd -p 81 -h /tmp -r OpenWrt
}}}

than use wget on your PC to receive the file

{{{
user@host:~$ wget http://192.168.1.1:81/foobar.txt
}}}

Recieve the file {{{foobar.txt}}} from your router at {{{192.168.1.1}}}
and port 81.


=== via a web browser ===

Start a second HTTPD webserver process (if not done already) on the Wrt with

{{{
httpd -p 81 -h /tmp -r OpenWrt
}}}

than point your favourite web browser to the URL:

{{{
http://192.168.1.1:81/foobar.txt
}}}
