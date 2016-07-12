'''''Retrieve the firmware and decompress it'''''[[BR]]
{{{# mkdir /tmp/buffalo; cd /tmp/buffalo
# wget -q http://www.buffalotech.com/downloads/WZR-RS-G54_2%5B1%5D.32_1.00.zip
# unzip -q WZR-RS-G54_2\[1\].32_1.00.zip}}}

'''''Determine the correct bs value'''''[[BR]]
{{{# hexdump -C WZR-RS-G54_2\[1\].32_1.00-US_US-TZO-uclibc.00-US_US-uclibc | grep Compressed
}}}

''{{{     000c0030  00 00 00 00 00 43 6f 6d  70 72 65 73 73 65 64 20  |.....Compressed |
    000c0050  69 0e f9 84 1a 43 6f 6d  70 72 65 73 73 65 64 00  |i....Compressed.|}}}''

''{{{offset = 000c0035 (786485)
         786485 - 16 bytes = 786469
bs     = 786469}}}''

'''''Take the calculated bs value and extract the filesystem'''''[[BR]]
{{{# dd if=WZR-RS-G54_2\[1\].32_1.00-US_US-TZO-uclibc.00-US_US-uclibc of=wzr-rs-g54-fs.img skip=1 bs=786469
  5+1 records in
  5+1 records out}}}

'''''Mount the extracted filesystem'''''[[BR]]
{{{# mkdir /mnt/wzr-rs-g54
# mount -t cramfs -o loop wzr-rs-g54-fs.img /mnt/wzr-rs-g54}}}

'''''A few quick lists + sizes'''''[[BR]]
{{{# cd /mnt/wzr-rs-g54/; ls -lh
}}}

''{{{total 9.5K
drwxr-xr-x  1 root root  576 Jan  1  1970 bin
drwxr-xr-x  1 root root    0 Jan  1  1970 dev
drwxr-xr-x  1 root root  300 Jan  1  1970 etc
drwxr-xr-x  1 root root  276 Jan  1  1970 hirai
drwxr-xr-x  1 root root  244 Jan  1  1970 lib
drwxr-xr-x  1 root root  332 Jan  1  1970 message
drwxr-xr-x  1 root root    0 Jan  1  1970 mnt
drwxr-xr-x  1 root root    0 Jan  1  1970 proc
drwxr-xr-x  1 root root  416 Jan  1  1970 sbin
drwxr-xr-x  1 root root    0 Jan  1  1970 tmp
drwxr-xr-x  1 root root   64 Jan  1  1970 usr
lrwxrwxrwx  1 root root    7 Jan  1  1970 var -> tmp/var
drwxr-xr-x  1 root root 2.8K Jan  1  1970 www}}}''

{{{# du -h ./
}}}
''{{{3.8M    ./usr/sbin
4.0K    ./usr/bin
1.4M    ./usr/lib
5.1M    ./usr
2.5K    ./etc/ppp
11K     ./etc
512     ./tmp
512     ./dev
512     ./mnt
512     ./proc
320K    ./bin
299K    ./sbin
205K    ./hirai
63K     ./message/error
16K     ./message/title
20K     ./message/wireless
1.0K    ./message/lan
7.5K    ./message/dhcps
19K     ./message/wan
56K     ./message/net
9.0K    ./message/info
31K     ./message/config
18K     ./message/other
19K     ./message/wanphase
24K     ./message/sysinfo
13K     ./message/carrier
33K     ./message/cwf
7.0K    ./message/cwferror
25K     ./message/pptps
4.0K    ./message/www/bc
670K    ./message/www/advance
8.0K    ./message/www/omake
8.5K    ./message/www/version
945K    ./message/www
14K     ./message/help/attack
3.0K    ./message/help/backup
18K     ./message/help/dhcps
8.0K    ./message/help/easy
32K     ./message/help/filter
53K     ./message/help/info
6.0K    ./message/help/log
27K     ./message/help/nat
5.5K    ./message/help/packet
57K     ./message/help/pppoe
4.5K    ./message/help/rip
7.0K    ./message/help/route
6.5K    ./message/help/syslog
40K     ./message/help/wan
99K     ./message/help/wireless
62K     ./message/help/pptp
501K    ./message/help
1.8M    ./message
397K    ./www/images
10K     ./www/upnp/LAN
65K     ./www/upnp/WAN
91K     ./www/upnp
1.6M    ./www/advance
270K    ./www/help
425K    ./www/vpn/images
698K    ./www/vpn
15K     ./www/omake/images
29K     ./www/omake
6.0K    ./www/version
2.0K    ./www/bc
3.4M    ./www
33K     ./lib/modules/2.4.20/kernel/drivers/net/et
415K    ./lib/modules/2.4.20/kernel/drivers/net/wl
594K    ./lib/modules/2.4.20/kernel/drivers/net
594K    ./lib/modules/2.4.20/kernel/drivers
8.5K    ./lib/modules/2.4.20/kernel/net/ipv4/netfilter
9.0K    ./lib/modules/2.4.20/kernel/net/ipv4
9.5K    ./lib/modules/2.4.20/kernel/net
24K     ./lib/modules/2.4.20/kernel/lib/zlib_deflate
24K     ./lib/modules/2.4.20/kernel/lib
628K    ./lib/modules/2.4.20/kernel
512     ./lib/modules/2.4.20/pcmcia
630K    ./lib/modules/2.4.20
630K    ./lib/modules
917K    ./lib
12M     ./}}}''

----
CategoryModel
