= NFS Root =
There are a few ways to do it.  One is the typical linux way: modify the kernel to have NFS and DHCP support, then specify the {{{nfsroot}}} on the kernel command line.  If the bootloader doesn't allow this, the root path can be compiled into the kernel.

A less-traditional approach is to switch roots during the boot process.

== Switching roots ==
=== Creating a new root ===
First, follow the RemoteFileSystemHowTo to set up an NFS mount.

Mount the path you want to use for a root and copy your old root to the new one.  For this example, the NFS server is 192.168.1.2 and the root will be stored on /share/roots/192.168.1.1

{{{
mkdir /mnt/nfs_root
mount -t nfs 192.168.1.2:/share/roots/192.168.1.1 /mnt/nfs_root -o nolock

cp -a /bin /etc /lib /sbin /usr /mnt/nfs_root
}}}

Now, create stub directories that will get remounted, later.
{{{
cd /mnt/nfs_root
mkdir dev jffs proc rom sys var
}}}

And some others
{{{
cd /mnt/nfs_root
mkdir tmp home root
}}}

Remove init scripts that will have already been run.  The switch is done after the network is set up, so remove all scripts preceding network.
{{{
cd /mnt/nfs_root/etc/rc.d

# assuming network is S40network
rm S0* S1* S2* S3* S40network
}}}

When the firewall starts, it will kill existing connections.  To prevent this, use an old OpenWrt firewall with two key modifications.  The policy mus be set ''after'' established connections are accepted.  Failing to make this change will cause the nfs connection to drop and the init to fail.

/etc/init.d/firewall
{{{
#!/bin/sh /etc/rc.common
# Copyright (C) 2006 OpenWrt.org

## Please make changes in /etc/firewall.user
START=45
start() {
        include /lib/network
        scan_interfaces
        config_load /var/state/network

        config_get WAN wan ifname
        config_get WANDEV wan device
        config_get LAN lan ifname

        ## CLEAR TABLES
        for T in filter nat; do
                iptables -t $T -F
                iptables -t $T -X
        done

        iptables -N input_rule
        iptables -N input_wan
        iptables -N output_rule
        iptables -N forwarding_rule
        iptables -N forwarding_wan

        iptables -t nat -N NEW
        iptables -t nat -N prerouting_rule
        iptables -t nat -N prerouting_wan
        iptables -t nat -N postrouting_rule

        iptables -N LAN_ACCEPT
        [ -z "$WAN" ] || iptables -A LAN_ACCEPT -i "$WAN" -j RETURN
        [ -z "$WANDEV" -o "$WANDEV" = "$WAN" ] || iptables -A LAN_ACCEPT -i "$WANDEV" -j RETURN
        iptables -A LAN_ACCEPT -j ACCEPT

        ### INPUT
        ###  (connections with the router as destination)

        # base case
        iptables -A INPUT -m state --state INVALID -j DROP
        iptables -A INPUT -m state --state RELATED,ESTABLISHED -j ACCEPT
        iptables -A INPUT -p tcp --tcp-flags SYN SYN --tcp-option \! 2 -j  DROP

        #################################################################
        #################################################################
                                  CHANGE HERE
        #################################################################
        #################################################################
        iptables -P INPUT DROP

        #
        # insert accept rule or to jump to new accept-check table here
        #
        iptables -A INPUT -j input_rule
        [ -z "$WAN" ] || iptables -A INPUT -i $WAN -j input_wan

        # allow
        iptables -A INPUT -j LAN_ACCEPT # allow from lan/wifi interfaces
        iptables -A INPUT -p icmp       -j ACCEPT       # allow ICMP
        iptables -A INPUT -p gre        -j ACCEPT       # allow GRE

        # reject (what to do with anything not allowed earlier)
        iptables -A INPUT -p tcp -j REJECT --reject-with tcp-reset
        iptables -A INPUT -j REJECT --reject-with icmp-port-unreachable

        ### OUTPUT
        ### (connections with the router as source)

        # base case
        iptables -A OUTPUT -m state --state INVALID -j DROP
        iptables -A OUTPUT -m state --state RELATED,ESTABLISHED -j ACCEPT

        #################################################################
        #################################################################
                                  CHANGE HERE
        #################################################################
        #################################################################
        iptables -P OUTPUT DROP

        #
        # insert accept rule or to jump to new accept-check table here
        #
        iptables -A OUTPUT -j output_rule

        # allow
        iptables -A OUTPUT -j ACCEPT            #allow everything out

        # reject (what to do with anything not allowed earlier)
        iptables -A OUTPUT -p tcp -j REJECT --reject-with tcp-reset
        iptables -A OUTPUT -j REJECT --reject-with icmp-port-unreachable

        ### FORWARDING
        ### (connections routed through the router)

        # base case
        iptables -P FORWARD DROP
        iptables -A FORWARD -m state --state INVALID -j DROP
        iptables -A FORWARD -p tcp --tcp-flags SYN,RST SYN -j TCPMSS --clamp-mss-to-pmtu
        iptables -A FORWARD -m state --state RELATED,ESTABLISHED -j ACCEPT

        #
        # insert accept rule or to jump to new accept-check table here
        #
        iptables -A FORWARD -j forwarding_rule
        [ -z "$WAN" ] || iptables -A FORWARD -i $WAN -j forwarding_wan

        # allow
        iptables -A FORWARD -i $LAN -o $LAN -j ACCEPT
        [ -z "$WAN" ] || iptables -A FORWARD -i $LAN -o $WAN -j ACCEPT

        # reject (what to do with anything not allowed earlier)
        # uses the default -P DROP

        ### MASQ
        iptables -t nat -A PREROUTING -m state --state NEW -p tcp -j NEW
        iptables -t nat -A PREROUTING -j prerouting_rule
        [ -z "$WAN" ] || iptables -t nat -A PREROUTING -i "$WAN" -j prerouting_wan
        iptables -t nat -A POSTROUTING -j postrouting_rule
        [ -z "$WAN" ] || iptables -t nat -A POSTROUTING -o $WAN -j MASQUERADE

        iptables -t nat -A NEW -m limit --limit 50 --limit-burst 100 -j RETURN && \
                iptables -t nat -A NEW -j DROP

        ## USER RULES
        [ -f /etc/firewall.user ] && . /etc/firewall.user
        [ -n "$WAN" -a -e /etc/config/firewall ] && {
                export WAN
                awk -f /usr/lib/common.awk -f /usr/lib/firewall.awk /etc/config/firewall | ash
        }
}

stop() {
        iptables -P INPUT ACCEPT
        iptables -P OUTPUT ACCEPT
        iptables -P FORWARD ACCEPT
        iptables -F
        iptables -X
        iptables -t nat -P PREROUTING ACCEPT
        iptables -t nat -P POSTROUTING ACCEPT
        iptables -t nat -P OUTPUT ACCEPT
        iptables -t nat -F
        iptables -t nat -X
}
}}}

=== Modifying the normal init sequence ===
During the init sequence, after the network is configured, a new root is mounted to /mnt/nfs_root.  The following script accomplishes it:

/etc/rc.d/S41nfs_root
{{{
#! /bin/sh /etc/rc.common

START=41

start() {
        mount -t nfs 192.168.1.2:/share/roots/192.168.1.1 /mnt/nfs_root -o nolock

        if [ $? -eq 0 ]
        then
                mount --bind /dev /mnt/nfs_root/dev
                mount --bind /dev/pts /mnt/nfs_root/dev/pts
                mount --bind /jffs /mnt/nfs_root/jffs
                mount --bind /proc /mnt/nfs_root/proc
                mount --bind /rom /mnt/nfs_root/rom
                mount --bind /sys /mnt/nfs_root/sys
                mount --bind /var /mnt/nfs_root/var

                chroot /mnt/nfs_root /etc/init.d/rcS S boot

                kill $PPID
        fi
}
}}}

$PPID is the original init process.  It's killed to prevent multiple instances of dropbear, httpd, etc. from starting.

=== What to do if your device doesn't come up ===
If you can't access your device after making these changes, first try disabling the NFS server (or restricting access to the OpenWrt device).
  * If the device has a static IP, unplugging it from the network, then plugging it back in after booting will prevent the nfsroot init script from killing the normal init script.
  * If the device uses DHCP, creating a special entry or modifying an existing entry on the DHCP server to place the device in a different subnet than the NFS server would recover the device.

If all else fails, try entering failsafe mode.  See ["OpenWrtDocs/Troubleshooting"].  There might also be device recovery information specific to your device.  See TableOfHardware.

=== Possible improvements ===
/var probably doesn't need to be mounted with the --bind option.

Replacing {{{kill $PPID}}} with {{{mount | grep /mnt/nfs_root && kill $PPID}}} would prevent crashes due to firewall bugs.  There might also be ways to check to see if the script finished, like creating a file with {{{/etc/init.d/done}}}.
----

CategoryHowTo
