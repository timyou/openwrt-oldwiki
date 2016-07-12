= Introduction =
This gives an overview for running I2C on your router. There are a few other openwrt I2C projects out there and they really helped me getting this up and running. In contrast to the other projects this one just

 * uses 2 GPIOs of the router,
 * does not need any external circuit,
 * it works with the 2.4 kernel (for broadcom),
 * uses kamikaze 7.09 and
If you have questions or any other kind of feedback feel free to send me an e-mail. See http://wiki.openwrt.org/schobi for details.

= Hardware =
I2C is bi-directional and needs pull-up resistors on both lines (10k is recommended). As the router uses its GPIOs for LEDs they act as some uncontrolled pullup or down. For this reason I disconnected the LEDs from those GPIOs (by removing the resistors).

First of all I put a 8 pinconnector on the bach side and connected all GPIOs in the right order. (I left out the reset GPIO  4).  http://www.ratnet.stw.uni-erlangen.de/~simischo/openwrt/overview.jpg 


Apart from the pull-ups my modification does not need any circuit except the I2C device you want to connect.

I used GPIOs 5 and 6. They need to be set in the bit-level driver (see below).

= Software =
Most of the software is already there - we'll just need to compile it. We will need

 * the low-level kernel module i2c-mips-gpio
 * ready made i2c kernel modules from the standard kernel (i2c-core, i2c-dev, i2c-algo-bit)
 * the userspace i2c-tools from lm-sensors
The next steps will describe how to compile all that. For this I set up a [http://forum.openwrt.org/viewtopic.php?id=7879 vmware compile environment] and [http://forum.openwrt.org/viewtopic.php?id=8410 check out] the most recent kamikaze 7.09 sources.

== i2c-mips-gpio ==
This is a kernel module that handles the lowest part of the I2C stack. It just turns on/off the line drivers and reads the line state. This file is based on many previous mods. For properly working with the i2c bus with just 2 wires I needed to make some adjustments.

To create a kernel module package I just created a new directory within my /package containing these files:

{{{
/package/broadcom-i2c/Makefile
/package/broadcom-i2c/src/Makefile
/package/broadcom-i2c/src/i2c-mips-gpio.c
}}}
If you want to adjust your pinout, this needs to be done in i2c-mips-gpio.c. For integrating this package I need to call

{{{
make menuconfig
}}}
and select the package from Kernel modules > I2C Bus > kmod-broadcom-i2c.  If you just want to build the package and package index you can call:

{{{
package/broadcom-i2c-compile
package/broadcom-i2c-install
package/index
}}}
Your new kernel module package can be found in

{{{
bin/packages/kmod-broadcom-i2c_xxxxxxxxxxx.ipk
}}}
=== Controlling scl and sda ===
Remember: both signal lines have a pullup.

For setting a line to low, we need to actively drive the line to a low state. Any device can do that as well! For getting a line to a high state we need to release the line and let it float. The pullup will then get it to a high state. We must not drive it to high permanently. The short output-high helps with signal quality though.

For reading a line we just need to read its state. We must not explicitly switch to input. If we drive it to low, then we will read a low signal. If we would release the line, then it could change its state just by reading it back.

== building i2c-core, i2c-dev, i2c-algo-bit ==
These modules can be used from the standard kernel that is used from the openwrt build environment. For enabling them we need to get to the basic kernel configuration with

{{{
make kernel_menuconfig
}}}
After some waiting we need to go to Character Devices > I2C support and enable

{{{
<M> I2C support
<M> I2Cbit-banging interfaces
<M> I2C device interface
<M> I2C /proc interface
}}}
Then you can build all of that with

{{{
make menuconfig
make world
}}}
Your new kernel module packages can be found in

{{{
bin/packages/kmod-i2c-algos_xxxxxxxxxxx.ipk
bin/packages/kmod-i2c-core_xxxxxxxxxxx.ipk
}}}
=== problems with make world ===
In my case something broke during make world. Some script wanted to copy the newly generated i2c*.o module files from

{{{
build_mipsel/linux-2.4-brcm/linux-2.4.34/drivers/i2c/algos/*.o
}}}
to somewhere else. In my case these files were generated in

{{{
build_mipsel/linux-2.4-brcm/linux-2.4.34/drivers/i2c/i2c-algo-bit.o
build_mipsel/linux-2.4-brcm/linux-2.4.34/drivers/i2c/i2c-core.o
build_mipsel/linux-2.4-brcm/linux-2.4.34/drivers/i2c/i2c-dev.o
build_mipsel/linux-2.4-brcm/linux-2.4.34/drivers/i2c/i2c-proc.o
}}}
As a workaround I could just

{{{
mkdir build_mipsel/linux-2.4-brcm/linux-2.4.34/drivers/i2c/algos/
cp build_mipsel/linux-2.4-brcm/linux-2.4.34/drivers/i2c/*.o build_mipsel/linux-2.4-brcm/linux-2.4.34/drivers/i2c/algos/
make world
}}}
I guess someone should have a look at that problem!

== I2C-tools from lm-sensors ==
For using our I2C bus we can use the official [http://www.lm-sensors.org/wiki/I2CTools I2C tools package] from lm-sensors. These tools are most useful:

 * i2cdetect: scans the bus and lists device adresses
 * i2cdump: scans a device and displays its data
 * i2cget: gets a sigle data byte/word from a device
 * i2cset: sets a value to a device
Again we need to build a package. Luckily there is a Makefile in the openwrt repository [https://dev.openwrt.org/browser/packages/utils/i2c-tools/Makefile Makefile] which needs to be placed in.

{{{
package/i2c-tools/Makefile
}}}
As the lm-sensors tools are valid for 2.4 and 2.6 kernel versions we need to edit this Makefile and remove the line

{{{
DEPENDS:=@LINUX_2_6
}}}
Then we can

{{{
make menuconfig
}}}
and select the package Utilities > I2C-tools. This package can be compiled with

{{{
package/i2c-tools-compile
package/i2c-tools-install
package/index
}}}
Your new kernel module package can be found in

{{{
bin/packages/i2c-tools_xxxxxxxxxxx.ipk
}}}
== Testing ==
Now you can install and test these packages. First you have to point your /etc/ikg.conf to your repository. Then you can call:

{{{
ipkg update
ipkg install kmod-i2c-algos
ipkg install kmod-i2c-core
ipkg install kmod-broadcom-i2c
ipkg install i2c-tools
}}}
If everything went right, you should find your modules:

{{{
root@OpenWrt:~# lsmod
Module                  Size  Used by    Tainted: P
i2c-mips-gpio           1132   0
i2c-algo-bit            8860   1 [i2c-mips-gpio]
i2c-dev                 4252   0
i2c-core               16000   0 [i2c-algo-bit i2c-dev]
[...]
}}}
There is a special i2c-algo-bit testmode where you can find out if any of your lines is stuck. This can be done by

{{{
rmmod i2c-mips-gpio
rmmod i2c-algo-bit
insmod i2c-algo-bit bit_test=1
insmod i2c-mips-gpio
}}}
Your dmesg should show something like this. The scl and sda numbers may vary depending on your GPIOs:

{{{
i2c-algo-bit.o: i2c bit algorithm module
i2c-mpis-gpio.o: i2c WRT54G GPIO module version 2.6.1 (20010830)
i2c-algo-bit.o: Adapter: WRT54G GPIO scl: 32  sda: 64 -- testing...
i2c-algo-bit.o:1 scl: 32  sda: 0
i2c-algo-bit.o:2 scl: 32  sda: 64
i2c-algo-bit.o:3 scl: 0  sda: 64
i2c-algo-bit.o:4 scl: 32  sda: 64
i2c-algo-bit.o: WRT54G GPIO passed test.
i2c-dev.o: Registered 'WRT54G GPIO' as minor 0
i2c-core.o: adapter WRT54G GPIO registered as adapter 0.
}}}
For further testing you can use i2cdetect, i2cdump, i2cget and i2cset.

= links to other projects =
 * I2C for 2.6 kernels: http://openwrt.pbwiki.com/I2C
 * 4 wire interface http://wiki.openwrt.org/OpenWrtDocs/Customizing/Hardware/I2C_RTC
 * another i2c module: http://forum.openwrt.org/viewtopic.php?id=7949
 * http://forum.openwrt.org/viewtopic.php?pid=60106
 * http://forum.openwrt.org/viewtopic.php?pid=59975
 * i2c for fonera http://www.lefinnois.net/wpen/index.php/2007/05/13/i2c-bus-for-la-fonera/
