= chroot to your debootstraped debian =
{{{
 /mnt/IDE1/bootstrap/bin/busybox chroot /mnt/IDE1/bootstrap/arm-sarge/ /bin/sh
 mount proc /proc -t proc
}}}
= check the version tag in /var/lib/dpkg/status =
I have a problem, to do ''dpkg -l'' if you have it to, so fix version tag of dpkg in /var/lib/dpkg/status.
{{{
 Version: 1.10.28
}}}
= install the dpkg-packages =
{{{
 dpkg --force-depends --install /var/cache/apt/archives/*
}}}
= modify your /etc/apt/sources.list =
your /etc/apt/sources.list should be similar:
{{{
deb http://security.debian.org/ stable/updates main
deb http://ftp.de.debian.org/debian/ stable main
deb-src http://ftp.de.debian.org/debian/ stable main
}}}
now you can install the packages you think you need<br/>
also install busybox-static (we need it later)
= add spezial things =
 1. leave the chroot <pre>exit</pre>
 1. copy the device for powermngt<pre>cp -a /dev/sl_pwr /mnt/IDE1/bootstrap/arm-sarge/dev/</pre>
 1. copy the sausalito-things <pre>cp -a /usr/sausalito /mnt/IDE1/bootstrap/arm-sarge/usr/</pre>
