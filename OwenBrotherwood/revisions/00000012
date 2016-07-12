'''Owen Brotherwood (oxo)'''
 Hello world!

[http://www.sitecenter.dk/o-o/sendemail/ Send email]
---------
[[TableOfContents(3)]]
= shellwrt =
 Well multi-web needs some research ...
== /usr/bin/shellwrt ==
 {{{
 $shellwrt root@192.168.1.1 root@192.168.1.2
}}}
 {{{
#
# shellwrt
#
# v000: just do keys ..

MY_ROOT="$HOME/src/shellwrt/"

MY_UNAME=$(uname -a)
MY_SHELL=$SHELL
MY_SHELLWRTLIB="${MY_ROOT}usr/lib/shellwrt"
MY_LIBS='shellwrt.lib'

{
        for lib in ${MY_LIBS};do
                . ${MY_SHELLWRTLIB}/${lib}
        done

        for device in $*;do
                setupssh ${device} ${MY_PUBLICDIR} ${MY_PUBLICFILE} ${MY_DEVAUTDIR} ${MY_DEVAUTFILE}
        done
}
}}}
== /usr/lib/shellwrt/shellwrt.lib ==
 {{{
#
#doc#shellwrt.lib
#doc#source this file
#todo#allow ssh from Openwrt box to Openwrt box

MY_PUBLICDIR="$HOME/.ssh"
MY_PUBLICFILE='id_dsa.pub'
MY_DEVAUTDIR='/etc/dropbear'
MY_DEVAUTFILE='authorized_keys'

debugmy(){      #doc#todo just shoe MY_'s
        for my in ${!MY_*};do
                eval echo ${my}
        done
        return 0        #doc#
}

setupssh(){     #doc#scp public key to device
        MY_DEVICE=$1
        MY_PUBLICDIR=$2
        MY_PUBLICFILE=$3
        MY_DEVAUTDIR=$4
        MY_DEVAUTFILE=$5

        MY_PUBLIC="$2/$3"
        MY_DEVAUT="$4/$5"

        MY_TEMP='/tmp'
        MY_SSHCMDS="
                cp ${MY_DEVAUT} ${MY_TEMP};
                cat ${MY_TEMP}/$3 >>${MY_TEMP}/$5;
                sort -u ${MY_TEMP}/$5 >$4/$5;
                chmod 0600 $4/$5;
                "

        scp ${MY_PUBLIC} ${MY_DEVICE}:${MY_TEMP}
        ssh ${MY_DEVICE} ${MY_SSHCMDS}
        return $?       #doc#return $? from ssh cmd
}

{
        return 0
}
}}}
= ssh (dropbear)=
It is easy to ssh from a ssh box to an OpenWrt box. However it has so far not been possible for me to ssh from an OpenWrt box to another OpenWrt box with a key :(

Maybe it is because the dropbear key generation with -y does not place a someone@somwhere at the end of the public key ...

== dropbear README ==
 {{{
In the absence of detailed documentation, some notes follow:
============================================================================

Server public key auth:

You can use ~/.ssh/authorized_keys in the same way as with OpenSSH, just put
the key entries in that file. They should be of the form:

ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAIEAwVa6M6cGVmUcLl2cFzkxEoJd06Ub4bVDsYrWvXhvUV+ZAM9uGuewZBDoAqNKJxoIn0Hyd0Nk/yU99UVv6NWV/5YSHtnf35LKds56j7cuzoQpFIdjNwdxAN0PCET/MG8qyskG/2IE2DPNIaJ3Wy+Ws4IZEgdJgPlTYUBWWtCWOGc= someone@hostname

You must make sure that ~/.ssh, and the key file, are only writable by the
user. Beware of editors that split the key into multiple lines.

NOTE: Dropbear ignores authorized_keys options such as those described in the
OpenSSH sshd manpage, and will not allow a login for these keys.

============================================================================

Client public key auth:

Dropbear can do public key auth as a client, but you will have to convert
OpenSSH style keys to Dropbear format, or use dropbearkey to create them.

If you have an OpenSSH-style private key ~/.ssh/id_rsa, you need to do:

dropbearconvert openssh dropbear ~/.ssh/id_rsa  ~/.ssh/id_rsa.db
dbclient -i ~/.ssh/id_rsa.db <hostname>

Currently encrypted keys aren't supported, neither is agent forwarding. At some
stage both hopefully will be.

============================================================================

If you want to get the public-key portion of a Dropbear private key, look at
dropbearkey's '-y' option.

============================================================================

To run the server, you need to generate server keys, this is one-off:
./dropbearkey -t rsa -f dropbear_rsa_host_key
./dropbearkey -t dss -f dropbear_dss_host_key

or alternatively convert OpenSSH keys to Dropbear:
./dropbearconvert openssh dropbear /etc/ssh/ssh_host_dsa_key dropbear_dss_host_key

============================================================================
}}}
== /etc/init.d/S50dropbear ==
 {{{
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
}}}
== Public key ==
 {{{
DROPBEARDIR='/etc/dropbear'
DROPBEARFILE='dropbear_dss_host_key'
DROPBEARDSS="${DROPBEARDIR}/${DROPBEARFILE}"
DROPBEARPUB="${DROPBEARDSS}.pub"
SEDSEARCH='ssh-dss'

dropbearkey  -t dss -y -f ${DROPBEARDSS}|sed -n -e "/${SEDSEARCH}/p">${DROPBEARPUB}
}}}
== o-o ==
 [http://wiki.openwrt.org/DropbearPublicKeyAuthenticationHowto authorized_hosts]
