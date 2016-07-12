== create dir ==
{{{
 mkdir -p /mnt/IDE1/bootstrap/
 cd /mnt/IDE1/bootstrap/
}}}
== copy the necessary files ==
you will need the content from this files on /mnt/IDE1/bootstrap/:
 * [ftp://ftp.de.debian.org/pub/debian/pool/main/d/debootstrap/debootstrap-udeb_0.2.45-0.2_arm.udeb debootstrap-udeb_0.2.45-0.2_arm.udeb]
 * the symbolic links from [ftp://ftp.de.debian.org/pub/debian/pool/main/b/busybox/busybox_1.1.3-3_arm.deb busybox_1.1.3-3_arm.deb]
 * the static busybox [ftp://ftp.de.debian.org/pub/debian/pool/main/b/busybox/busybox-static_1.1.3-3_arm.deb busybox-static_1.1.3-3_arm.deb]
 * [ftp://ftp.de.debian.org/pub/debian/pool/main/g/glibc/libc6_2.3.2.ds1-22sarge4_arm.deb libc6_2.3.2.ds1-22sarge4_arm.deb]
 * the contet of /etc <pre>cp -a /etc /mnt/IDE1/bootstrap/</pre>
== chroot to /mnt/IDE1/bootstrap ==
{{{ /mnt/IDE1/bootstrap/bin/busybox chroot /mnt/IDE1/bootstrap /bin/sh}}}
== mount proc ==
{{{
 mkdir /proc
 mount proc /proc -t proc
}}}
== debootstrap ==
{{[ debootstrap sarge /arm-sarge }}}
== things afer debootstrap ==
 * exit the chroot <pre>exit</pre>
 * umount proc <pre>umount /mnt/IDE1/bootstrap/proc
