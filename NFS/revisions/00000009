Here's how I was able to export a USB drive from my WRTSL54GS:

 *  get the drive mounted (see: UsbStorageHowto)

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

At this point, I would try to mount the NFS drive and get "Stale NFS mount" errors. Here's what I did to get around it:

 *  I killed rpc.nfsd
 *  I restarted it like so: ''/usr/sbin/rpc.nfsd -R /mnt/disc0_2''
