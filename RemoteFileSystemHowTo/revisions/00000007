[:OpenWrtDocs]
[[TableOfContents]]

== Intro ==
This HOWTO describes how to mount remote filesystems on your router, so that you can use files on remote machines as if they were stored locally.

== CIFS ==
CIFS (Common Internet File System) is a network filesystem used mainly by Windows machines.  Use it if you have Windows or Samba servers nearby.

You must first install the {{{kmod-cifs}}} and {{{cifsmount}}} packages:
{{{
ipkg install kmod-cifs
ipkg install cifsmount
}}}

Then load the {{{cifs}}} module:
{{{
insmod cifs
}}}
~-'''Note:''' this module is automagically loaded at boot after the {{{kmod-cifs}}} package is installed.-~

Then you can mount the remote filesystem:
{{{
mount -t cifs //my-pc/share /mnt/point -o unc=//my-pc\\share,ip=192.168.1.100,user=john,pass=doe,dom=workgroup
}}}
This will mount the folder shared as {{{share}}} on the machine {{{my-pc}}} with the ip address {{{192.168.1.100}}} in the directory {{{/mnt/point}}} on the router. To connect to the machine {{{my-pc}}}, it will use the username {{{john}}}, the password {{{doe}}} and the domain / workgroup {{{workgroup}}}.

Alternatively, you can create a file to contain your credentials for logging on. For example create the file {{{/etc/my-pc.cifs}}}:

{{{
username=john
password=doe
}}}

And your mount command would be:

{{{
mount -t cifs //my-pc/share /mnt/point -o unc=//my-pc\\share,ip=192.168.1.100,credentials=/etc/my-pc.cifs
}}}
~-'''Nico:''' this does not work for me, with cifsmount installled or not.-~

In RC4:
with cifsmount installed mount.cifs //192.168.1.100/share /mnt/point -o user=xxx pass=xxx work.
mount -t cifs comes back with an invalid argument.

Once mounted with mount.cifs.
mount -t cifs returns:
//192.168.1.77/HDD_1_1_1 on /mnt type cifs (rw,mand,nodiratime,unc=\\192.168.1.100\share,username=root,domain=,rsize=16384,wsize=16384)

Something isn't quite right but you can make it work'ish (no fstab, no style points.)

Note the {{{\}}} separator in {{{unc}}} is escaped ({{{\\}}}) because it is interpreted by the shell.

== NFS ==

NFS (Network File System) is a network filesystem found on nearly all *nix systems.  Use it if you have an NFS server nearby; but only if you trust the network path to be secure.

You must first install the {{{kmod-nfs}}} package:
{{{
ipkg install kmod-nfs
}}}

Then load the {{{sunrpc}}}, {{{lockd}}} and {{{nfs}}} modules:
{{{
insmod sunrpc
insmod lockd
insmod nfs
}}}
~-'''Note:''' these modules are automatically loaded at boot after the {{{kmod-nfs}}} package is installed.-~

Then you can mount the remote filesystem:
{{{
mount -t nfs 192.168.1.101:/share /mnt/point -o nolock
}}}
This will mount the folder {{{/share}}} exported by the machine with the ip address {{{192.168.1.101}}} in the directory {{{/mnt/point}}} on the router. The {{{nolock}}} will disable NFS file locking. If you really need file locking, you must install the {{{portmap}}} package and start the {{{portmap}}} daemon before trying to mount an exported filesystem without the {{{nolock}}} option.


== SHFS - (Secure) SHell FileSystem ==

Shfs is a simple and easy to use Linux kernel module which allows you to mount remote filesystems using a plain shell (ssh) connection. When using shfs, you can access all remote files just like the local ones, only the access is governed through the transport security of ssh.

This is a preferred method over CIFS and NFS. They both suck when it comes to security. This matters heavily when accessing data over the internet. Also, nearly everybody in the !OpenWrt target group has a ready-to-use ssh account on his machines. Or at last, they should have. Shfs is really easy and you do not need anything except a shell and Perl on the remote side. You likely have Perl on an standard Linux box. So, you are ready to go.

Begin with installing the required packages:
{{{
ipkg install kmod-shfs shfs-utils
}}}

Then, load the shfs module into the running kernel.
{{{
insmod shfs
}}}

Now you are ready to mount your remote filesystem:
{{{
mkdir /some/local/mountpoint
shfsmount user@host:/remote/dir /some/local/mountpoint
}}}

Here are some more experienced ways of calling shfsmount (copied from the shfs user docs).

To specify another port:
{{{
shfsmount -P 2222 user@host /mnt/shfs
}}}
To specify another ssh option:
{{{
shfsmount --cmd="ssh -c blowfish %u@%h /bin/bash" user@host:/tmp /mnt/shfs/
}}}
To make mount survive temporary connection outage (reconnect mode):
{{{
shfsmount --persistent user@host /mnt/shfs
}}}
Longer transfers? Increase cache size (1MB cache per file):
{{{
shfsmount user@host /mnt/shfs -o cachesize=256
}}}
To enable symlink resolution:
{{{
shfsmount -s user@host /mnt/shfs
}}}
To preserve uid (gid) (NFS replace mode :-)):
{{{
shfsmount root@host /mnt/shfs -o preserve,rmode=755
}}}
To see what is wrong (forces kernel debug output too):
{{{
shfsmount -vvv user@host /mnt/shfs
}}}

See http://shfs.sourceforge.net/ for further details.
