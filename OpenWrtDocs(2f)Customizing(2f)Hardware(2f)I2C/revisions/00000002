= Introduction =

This gives an overview for running i2c on your router. 

There are a few other openwrt i2c projects out there and they really helped me getting this up and running. In contrast to the other projects this one just 
  * uses 2 GPIOs of the router, 
  * does not need any external circuit,
  * it works with the 2.4 kernel (for broadcom), 
  * uses kamikaze 7.09 and 
  * there are just two custom files.


= Hardware =

I2C is bi-directional and needs pull-up resistors on both lines (10k is recommended). As the router uses its GPIOs for LEDs they act as some uncontrolled pullup or down. For this reason I removed the LEDs from those GPIOs.

Apart from the pull-ups my modification does not need any circuit except the I2C device you want to connect.

I used GPIOs 5 and 6. They need to be set in the bit-level driver (see below).

= Software =

Most of the software is already there - we'll just need to compile it. We will need

  * the low-level kernel module i2c-mips-gpio
  * ready made i2c kernel modules from the standard kernel (i2c-core, i2c-dev, i2c-algo-bit)
  * the userspace i2c-tools from lm-sensors

The next steps will describe how to compile all that. For this I set up a [http://forum.openwrt.org/viewtopic.php?id=7879 vmware compile environment] and downloaded the most recent kamikaze 7.09 sources.


== i2c-mips-gpio ==

This is a kernel module that handles the lowest part of the I2C stack. It just turns on/off the line drivers and reads the line state. This file is based on many previous mods. For properly working with the i2c bus with just 2 wires I needed to make some adjustments.

To create a kernel module package I just created a new directory within my /package containing these files:

{{{
/package/broadcom-i2c/Makefile
/package/broadcom-i2c/src/Makefile
/package/broadcom-i2c/src/i2c-mips-gpio.c
}}}

For integrating this package I need to call

{{{
make menuconfig 
}}}

and select the package from Kernel modules > I2C Bus > kmod-broadcom-i2c. 
If you just want to build the package and package index you can call:

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

For setting a line to low, we need to actively drive the line to a low state. Any device can do that as well!
For getting a line to a high state we need to release the line and let it float. The pullup will then get it to a high state. We must not drive it to high permanently. The short output-high helps with signal quality though.

For reading a line we just need to read its state. We must not explicitly switch to input. If we drive it to low, then we will read a low signal. If we would release the line, then it could change its state just by reading it back.




== make kernel_menuconfig ==
