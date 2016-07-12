= Using Go6.net for IPv6 =
This section describe how to setup IPv6 using the [[http://go6.net/ | Go6.net]] service.

 1. Sign up for a free account with Go6.
 1. Setup your router for IPv6.
  1. Install the following packages: kmod-ipv6, kmod-tun, ip, libpthread, radvd.
  1. Install the Gateway6 client v5 from here: http://www.roadrunner.cx/openwrt/gw6c_4.2.2_mipsel.ipk
 1. Configure the Gateway6 Client. The config file is located at /etc/gw6c/
  1. Change userid and passwd to your username and password.
  1. Change server to broker.freenet6.net
  1. Change host_type to one of the following:
   1. router if you want to use IPv6 on your whole network.
   1. host if you want to use IPv6 just on your router.
  1. You should not have to mess with any other settings.
 1. Start the Gateway6 Client.
  1. Start immediately with /etc/init.d/gw6c start
  1. Reboot your router
 1. Check syslog for errors.

Most of this information came from [http://forum.openwrt.org/profile.php?id=524 jake1981] at the OpenWRT forums from this post:

http://forum.openwrt.org/profile.php?id=524

----
CategoryHowTo
