
= Introduction =

This gives an overview for running i2c on your router. 

There are a few other openwrt i2c projects out there and they really helped me getting this up and running. In contrast to the other projects this one just uses 2 GPIOs of the router, it works with the 2.4 kernel and kamikaze and there are just two custom files for the driver.


= Hardware =

I2C is bi-directional and needs pull-up resistors on both lines (10k is recommended). As the router uses its GPIOs for LEDs they act as some uncontrolled pullup or down. For this reason I removed the LEDs from those GPIOs.

Apart from the pull-ups my modification does not need any circuit except the i2c device you want to connect.

I used GPIOs 5 and 6. They need to be set in the bit-level driver (see below).

= Software =

Most of the software is already there. We will need

- the low-level kernel module i2c-mips-gpio
- ready made i2c kernel modules from the standard kernel (i2c-core, i2c-dev, i2c-algo-bit)
- the userspace i2c-tools from lm-sensors

The next steps will describe how I built them. For this I set up a vmware compile environment and downloaded the most recent kamikaze 7.09 sources.


== i2c-mips-gpio ==

This file is based on many previous mods. For properly working with the i2c bus with just 2 wires I needed to make some adjustments.

=== Controlling scl and sda ===

Remember: both signal lines have a pullup.

For setting a line to low, we need to actively drive the line to a low state. Any device can do that as well!
For getting a line to a high state we need to release the line and let it float. The pullup will then get it to a high state. We must not drive it to high permanently. The short output-high helps with signal quality though.

For reading a line we just need to read its state. We must not explicitly switch to input. If we drive it to low, then we will read a low signal. If we would release the line, then it could change its state just by reading it back.

=== creating a kernel module package ===

I just created a new directory within my packages

{{{
mkdir broadcom-i2c
cd broadcom-i2c

}}}




== make kernel_menuconfig ==
