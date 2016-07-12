'''MailingEncryptedFilesHowTo'''

 1. Overview
  1.1 Security Notes
 2. Requirements
 3. Installation
    3.1 Encryption 
   3.2 Mailclient
 4. Configuration
    4.1 aespipe
   4.2 ssmtp/mutt
 5. Examples
 6. Troubleshooting
 7. Links

== Overview ==
This howto describes how to mail data in a secure way.
The security is based on a SSL/TLS connection to your
emailhub and encrypted files. Due to storage restrictions
gnupg isn't used which otherwise would be first choice.

=== Security Notes ===
 * AES with 256 bit key size and SHA-512 for hashing
 * The symmetric encryption requires a password (at least 20 characters)
 * Additionally password seed and iteration count are used to slow down optimized dictionary attacks
 * SSL over SMTP und StartTLS are supported


== Requirements ==
 * WHITE RUSSIAN RC5
 * approximately 300 kBytes (plus libpthread, libopenssl(libssl), if not installed)
 * Packages: libpthread, libopenssl(libssl), ssmtp, mutt, aespipe

== Installation ==
Make sure you have libpthread and libopenssl installed. You can use the official white russian rc5 source for both.
=== Encryption ===
To install aespipe do the following ...
{{{
cd /tmp
wget http://openwrt.alphacore.net/aespipe_2.3a_mipsel.ipk
ipkg install ./aespipe_2.3a_mipsel.ipk
}}}
=== Mailclient ===
Install ssmtp and mutt ...
{{{
cd /tmp
wget http://openwrt.alphacore.net/ssmtp_2.61_mipsel.ipk
wget http://openwrt.alphacore.net/mutt_1.4.2.1_mipsel.ipk
ipkg install ./ssmtp_2.61_mipsel.ipk
ipkg install ./mutt_1.4.2.1_mipsel.ipk
}}}
NOTE: Don't use the ssmtp package from the official whiteRussian RC5 tree, because it can't handle SSL.

== Configuration ==
=== aespipe ===
To make things easier I've written a script which ... 
 1. creates a tar archive 
 2. gzips that archive
 3. and encrypts it with a password which is stored in a file (without any user action)
You only have to change the values for the seed (SEEDSTR) and the passwordfile (textfile with a at least 20 characters long password in it)
{{{
#!/bin/sh
ENCRYPTION=AES256
HASHFUNC=SHA512
ITERCOUNTK=100
WAITSECONDS=10
PASSFILE=/etc/password.txt
SEEDSTR=87nCxFIp0uAkd+Vs9FHk0hvJ
# creates a random seed
# head -c 18 /dev/urandom | uuencode -m - | head -n 2 | tail -n 1
COMPRESS=gzip
TAR=tar
AESPIPE=aespipe

usage () {
	echo "Decrypting : ${0} d [file]" 
	echo "Encrypting : ${0} e [inputfile] [outputfile]"
}

if [ $# != 2 ] && [ $# != 3 ]
then
	usage
	exit 1
fi

case "$1" in
	d)
		${AESPIPE} -d -p 5 -e ${ENCRYPTION} -H ${HASHFUNC} -S ${SEEDSTR} -C ${ITERCOUNTK} <${2} 5<${PASSFILE} | ${COMPRESS} -d -q | ${TAR} xvpf -
		;;
	e)
		${TAR} cvf - ${2} | ${COMPRESS} | ${AESPIPE} -p 5 -e ${ENCRYPTION} -H ${HASHFUNC} -S ${SEEDSTR} -C ${ITERCOUNTK} -w ${WAITSECONDS} >${3} 5<${PASSFILE}
		;;
	*)
		usage
		exit 1
		;;
esac
exit 0
}}}
Name and copy that script somewhere suitable (e.g. /usr/bin). Now you should be able to easily encrypt and decrypt your files. Note that you need aespipe, the script and  of course the passwordfile to read those files on a different machine.
=== ssmtp/mutt ===
ssmtp expects its two configuration files named "revaliases" and "ssmtp.conf" under /etc/ssmtp. Both are self-explaining, so I post a basic configuration.
{{{
# /etc/ssmtd/ssmtp.conf

root=arnold@gmx.net
mailhub=mail.gmx.net:465
rewriteDomain=gmx.net
hostname=gmx.net
FromLineOverride=YES
UseTLS=YES
#UseSTARTTLS=YES
}}}
{{{
# /etc/ssmtd/revaliases
# Format: local_account:outgoing_address:mailhub

root:arnold@gmx.net:mail.gmx.net:465
}}}
The global configuration file for mutt is /etc/Muttrc. Here is a sufficient configuration.
{{{
# /etc/Muttrc
mailboxes /tmp/mail

set sendmail="/usr/bin/ssmtp -auarnold@gmx.net -ap123password456"
set from="arnold@gmx.net"

# Mail folder setup.
set folder=/tmp/mail
set mbox_type=mbox
set spoolfile=+inbox
set mbox=+received
set postponed=+postponed
set record=+sent
}}}
= Examples =
''The scriptname is targzaes and its location is /usr/bin.''
Encrypt and send /var/log/messages.
{{{
targzaes e /var/log/messages /tmp/messages.aes
mutt -a /tmp/messages.aes -s syslog someguy@qmail.com
}}}
Decrypt mail attachment on a different machine where aespipe, the script and the passwordfile are available.
{{{
targzaes d messages.aes
}}}
= Troubleshooting =

----
CategoryHowTo
