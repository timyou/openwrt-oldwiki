[:OpenWrtDocs]
[[TableOfContents]]

== Intro ==
This HOWTO describes how to mount remote filesystems on your router, so that you can use files on remote machines as if they were stored locally.

== CIFS ==
CIFS (Common Internet File System) is a network filesystem used mainly by Windows machines.

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

Note the {{{\}}} separator in {{{unc}}} is escaped ({{{\\}}}) because it is interpreted by the shell.

== NFS ==

NFS (Network File System) is a network filesystem found on nearly all *nix systems.

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
~-'''Note:''' theese modules are automagically loaded at boot after the {{{kmod-nfs}}} package is installed.-~

Then you can mount the remote filesystem:
{{{
mount -t nfs 192.168.1.101:/share /mnt/point -o nolock
}}}
This will mount the folder {{{/share}}} exported by the machine with the ip address {{{192.168.1.101}}} in the directory {{{/mnt/point}}} on the router. The {{{nolock}}} will disable NFS file locking. If you really need file locking, you must install the {{{portmap}}} package and start the {{{portmap}}} daemon before trying to mount an exported filesystem without the {{{nolock}}} option.
