 * save config
 * extract config.tar.gz
 * to etc/samba/smb.conf from config.tar.gz add: 
{{{
[all]
use receivefile=yes
create mask=0775
path=/
directory mask=0775
writeable=yes
available=1
use sendfile=yes
root preexec = "cat /etc/inetd.conf.old >/etc/inetd.conf; killall inetd; /usr/sbin/inetd
}}}
 * restore from modifid config.tar.gz
 * reboot
 * conntet to samba-share all
 * and now you can telnet your box. (user: root no password!) 
