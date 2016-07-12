The WL-HDD and WL-700gE both integrate a Real Time Clock using a Ricoh RV5C386A chip over the I2C bus.  This chip is not supported out of the box by OpenWRT, but Asus's source code includes a driver for it, as well as freely available documentation from Ricoh.

You can download a package, to placed in the `../openwrt/package` when building OpenWRT.

{{{bzr clone http://www.iro.umontreal.ca/~monnier/bzr/rtc-rv5c386a}}}

This will add a standard /dev/rtc device which you can use with the usual `hwclock` utility.
There is a Trac [https://dev.openwrt.org/ticket/1873 ticket] to try and get this included in OpenWRT, which includes some older versions of this package.
There is also an older Trac [https://dev.openwrt.org/ticket/1749 ticket] with even older code for it.
