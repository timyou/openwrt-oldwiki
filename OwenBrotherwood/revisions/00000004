'''Owen Brotherwood (oxo)'''
 Hello world!

[http://www.sitecenter.dk/o-o/sendemail/ Send email]
---------
[[TableOfContents(3)]]
= shellwrt =
== sshing setup ==
 {{{
#
#
#
# from favorit shell box...

MY_USER='root'
MY_UNAME=$(uname -a)
MY_SHELL=$SHELL

MY_PUBLICDIR="$HOME/.ssh"
MY_PUBLICFILE='id_dsa.pub'
MY_DEVAUTDIR='/etc/dropbear'
MY_DEVAUTFILE='authorized_keys'

debugmy(){
        for my in ${!MY_*};do
                eval echo ${my}
        done
}

setupssh(){
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
        return $?
}

{
        for device in $*;do
                setupssh "${MY_USER}@${device}" ${MY_PUBLICDIR} ${MY_PUBLICFILE} ${MY_DEVAUTDIR} ${MY_DEVAUTFILE}
        done
}
}}}
= ssh =
== o-o ==
 [http://wiki.openwrt.org/DropbearPublicKeyAuthenticationHowto authorized_hosts]
