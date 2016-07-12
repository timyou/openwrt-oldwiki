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
 5. Notes
 6. Links

== Overview ==
This howto describes how to mail data in a secure way.
The security is based on a SSL/TLS connection to your
emailhub and encrypted files. Due to storage restrictions
gnupg isn't used which otherwise would be first choice.

=== Security Notes ===
 * AES with 256 bit key size and SHA-512
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

to be continued (NOT YET FINISHED)
----
CategoryHowTo
