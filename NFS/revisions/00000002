Here's how I was able to export a USB drive from my WRTSL54GS:

 *  get the drive mounted (this is documented elsewhere)
 *  install kmod-nfs and nfs-server
 *  edit your /etc/exports appropriately
 * reboot to pick up all the kernel module deps that nfs has
At this point, I would try to mount the NFS drive and get "Stale NFS mount" errors. Here's what I did to get around it:

 *  I killed rpc.nfsd
 * I restarted it like so: /usr/sbin/rpc.nfsd -R /mnt/disc0_2
