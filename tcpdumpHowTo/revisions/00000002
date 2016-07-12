i've set up a script /etc/init.d/S98tcpdump
{{{
tcpdump -F /etc/tcpdump.conf -i br0 -w /tmp/log/tcpdump 2>/dev/null &
}}}
the F option use a configuration file for the filters:
{{{
(host 192.168.1.101 and not tcp src port( 80 or 443)) or (host 192.168.1.102 and not tcp src port (80 or 443))
}}}
the -i option use the interface br0 for the capture so it can capture both from the wired switch and from the wireless interface[[br]]
and i used the -w option in order to write a log to a file[[br]]
in order to view the file you can download it with openssh-sftp-server:
on the router:
{{{
ipkg install openssh-sftp-server
}}}
on your computer(change the port according to your settings...if you don't changed anything port 22 is ok) the following command copy the file to your desktop:
{{{
scp -P 22 root@router:/tmp/log/tcpdump ~/Desktop/
}}}
or view it with:
{{{
tcpdump -r /tmp/log/tcpdump
}}}
