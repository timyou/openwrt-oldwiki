#format wiki

Building [http://accel-pptp.sourceforge.net/ Accel-PPTP]

1. checkout OpenWRT trunk and build the toolchain
{{{
svn co http...
}}}

2. Configure kernel to include pppoe or pppoa, this will give the required pppox.ko module.

3. Untar accel-pptp 0.8.2

4. Go to accel-pptp-0.8.2/pppd_plugin

5. Patch configure:
{{{
--- pppd_plugin/configure.old	2009-01-28 10:26:02.000000000 +0200
+++ pppd_plugin/configure	2009-03-10 09:02:35.000000000 +0200
@@ -19482,7 +19482,8 @@
 echo "$as_me: error: Could not find pppd" >&2;}
    { (exit 1); exit 1; }; }
 fi
-pppd_ver=`${pppd} --version 2>&1 | grep version | sed 's/pppd version //'`
+#pppd_ver=`${pppd} --version 2>&1 | grep version | sed 's/pppd version //'`
+pppd_ver="2.4.3"
 { echo "$as_me:$LINENO: result: $pppd ($pppd_ver)" >&5
 echo "${ECHO_T}$pppd ($pppd_ver)" >&6; }
 cat >>confdefs.h <<_ACEOF
}}}
We don't need host pppd version in cross-compiled module. OpenWRT trunk contains pppd 2.4.3 so far.

6. Set paths for crosscompiling.
{{{
TODO
}}}

7. Build pppd plugin
{{{
./configure
make
}}}

8. Get the resulting pptp.so.0.0.0 from pppd_plugin/src/.libs/

9. Upload pptp.so.0.0.0 to OpenWRT box as  /usr/lib/pppd/2.4.3/pptp.so

10. Build kernel module
{{{
TODO
}}}

11. Upload resulting pptp.ko to /lib/modules/`uname -r`

12. insmod pppox and pptp, observe the following line in dmesg
{{{
PPTP driver version 0.8.2
}}}

13. Test the connection
{{{
TODO
}}}

Live example: http://myrtg.blogspot.com/2009/03/openwrt-pptp-client-part-2.html
