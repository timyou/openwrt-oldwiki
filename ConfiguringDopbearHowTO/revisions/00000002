We will see how to configure Dropbear ssh in White russian:[BR]
here are the options of dropbear ssh:
{{{
# /usr/sbin/dropbear --help
Unknown argument --help
Dropbear sshd v0.48
Usage: /usr/sbin/dropbear [options]
Options are:
-b bannerfile   Display the contents of bannerfile before user login
                (default: none)
-d dsskeyfile   Use dsskeyfile for the dss host key
                (default: /etc/dropbear/dropbear_dss_host_key)
-r rsakeyfile   Use rsakeyfile for the rsa host key
                (default: /etc/dropbear/dropbear_rsa_host_key)
-F              Don't fork into background
-E              Log to stderr rather than syslog
-m              Don't display the motd on login
-w              Disallow root logins
-s              Disable password logins
-g              Disable password logins for root
-j              Disable local port forwarding
-k              Disable remote port forwarding
-a              Allow connections to forwarded ports from any host
-p port         Listen on specified tcp port, up to 10 can be specified
                (default 22 if none specified)
-i              Start for inetd
}}}

with theses options we will modify the script,here we changed the port with the -p argument and disabled the port forwarding as i don't use the webif using the -j and -k switch:
{{{
# cat /etc/init.d/S50dropbear
#!/bin/sh

[ ! -f /etc/dropbear/dropbear_rsa_host_key ] && {
        for type in rsa dss; do {
                # check for keys
                key=/tmp/dropbear/dropbear_${type}_host_key
                [ ! -f $key ] && {
                        # generate missing keys
                        mkdir -p /tmp/dropbear
                        [ -x /usr/bin/dropbearkey ] && {
                                /usr/bin/dropbearkey -t $type -f $key 2>&- >&- && exec $0 $*
                        } &
                        exit 0
                }
        }; done
        lock -w /tmp/.switch2jffs
        mkdir -p /etc/dropbear
        mv /tmp/dropbear/dropbear_* /etc/dropbear/
}

/usr/sbin/dropbear -j -k -p 24
}}}


or if you want to use the webif trough the port forwarding of ssh add  the -a switch (untested) to the following line:
{{{
/usr/sbin/dropbear
}}}
then connect with the following command:
{{{
ssh -L 80:localhost:80 root@192.168.1.1
}}}
