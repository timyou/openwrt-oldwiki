This package seems to be broken. 

Portmap is not working, and nobody  to fix it yet. 
Seems that NFS on kamikaze is not going to work.


= Intro =
Here's how I was able to export a USB drive from my WRTSL54GS.

= Requirements =
Get the drive mounted (see: UsbStorageHowto)

= Installation =
Install NFS kernel module and server:

{{{
ipkg update
ipkg install kmod-nfs nfs-server
}}}

Load kernel modules (sunrpc lockd nfs):
{{{
insmod sunrpc
insmod lockd
insmod nfs
}}}
...or reboot to pick up all the kernel module deps that nfs has.


= Configuration =

 *  edit your /etc/exports appropriately (mine is just ''/mnt/disc0_2 client.ip.addr(rw,no_root_squash,async)'')

Start RPC:
{{{
/etc/init.d/S59portmap start
}}}


Start NFS:
{{{
/etc/init.d/S60nfsd start
}}}

At this point, I would try to mount the NFS drive and get "Stale NFS mount" errors. Here's what I did to get around it:

 *  I killed rpc.nfsd
 *  I restarted it like so: ''/usr/sbin/rpc.nfsd -R /mnt/disc0_2''
