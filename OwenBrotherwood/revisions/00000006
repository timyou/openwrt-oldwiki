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
= ssh =
== o-o ==
 [http://wiki.openwrt.org/DropbearPublicKeyAuthenticationHowto authorized_hosts]
