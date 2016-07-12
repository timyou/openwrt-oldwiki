= Introduction =
These pages will describe building the hardware and software required to add an I2C bus and a Real-Time Clock to the Linksys WRT54GL router.
The I2C bus is very versatile and can interface with many components such as eeprom memory chips, GPS location detectors, solid-state compasses, LCD displays and of course the Real-Time clock chip described here.

Eventually more I2C projects will be documented here.

= Credits =
The information presented here was partially gathered from sources on the Internet
including the following:[[BR]][http://www.linksysinfo.org] and [http://openwrt.org]:

'''Firmware:''' `OpenWrt Whiterussian 0.9`[[BR]]
'''Kernel driver:''' i2c-mips-gpio: from [http://forum.openwrt.org/viewtopic.php?id=7949][[BR]]
Based on original i2c-mips-gpio by John Newbigin,[[BR]]
which in turn was based on i2c-philips-par.c by Simon G. Vogl.[[BR]]
Changed to sb_gpio-Interface by Torsten Landschoff.[[BR]]
4-wire logic and final version by niclas at datenritter dot de.[[BR]]
'''User space binaries''' are modified versions of utilities provided in the lm_sensors package: [http://www.lm-sensors.org][[BR]]
'''Schematics''' were created with gEDA: [http://www.geda.seul.org]

= Hardware =
=== Schematic ===

attachment:i2c_rtc.png

Basically, the circuit is comprised of 2 IC's and support components.
The 74LS05 buffer is open collector and requires pull up resistors on the outputs. All incoming and outgoing signals are buffered.
The DS1307 clock circuit is just the basic reference design specified in the data sheet and it's I2C signals are just connected to the I2C bus.
The SQW signal is just a square wave programmable as 1Hz, 4kHz, 8kHz, 32kHz or as a constant high or low output. Can be used for anything you want.[[BR]] [[BR]]
The battery backup mechanism of the clock chip ensures time is maintained also when
the router is powered off.[[BR]]
+5V power was obtained from a 7805 regulator circuit (added on a separate circuit) which is not described here.

=== GPIO pins ===
I2C GPIO signals used:[[BR]]
SDA_OUT : GPIO 4 (Cisco switch)[[BR]]
SDA_IN: GPIO 2 (White LED)[[BR]]
SCL_OUT: GPIO 7 (DMZ LED)[[BR]]
SCL_IN: GPIO 3 (Orange LED)[[BR]]

''Note:'' Because of the use of these GPIO pins which are also used by the MMC project, you won't be able to have both. Sorry.

=== Construction ===
The circuit was built on a small piece of perforated board.[[BR]][[BR]]
attachment:i2c-rtc-circuit.jpg

The upper right hand corner is for the I2C extension connector for additional I2C devices.[[BR]]
The 4 GPIO signals as you see are connected with the upper terminal block and +5V connected with the lower terminal block.

attachment:i2c-rtc-mounted.jpg

Mounted in the router together with the serial console adapter and 5v regulator.[[BR]]Although it doesn't look like it, there's about 10mm clearance above the main board.[[BR]]
Since the gpio pin for the Cisco button is used, I decided to shorten the length of the
buttons lever to avoid it getting pressed accidentally. This probably wouldn't cause any
problems but better to be safe.

attachment:shorten-cisco-button.jpg

= Software =
== Prerequisites ==
 *`OpenWrt Whiterussian 0.9` flashed to the router and running normally. Available from [http://downloads.openwrt.org/whiterussian/0.9/default/]
 *Microperl ipkg installed on the router. Available from [http://downloads.openwrt.org/backports/0.9/microperl_5.8.6-1_mipsel.ipk]
 *A Linux workstation if you plan on compiling the binaries.

== WRT54GL OS ==
Not much to be said here besides flash your router with Whiterussian 0.9 as stated in
the prerequisites. No other router or Whiterussian version has been tested although I can see no reason why it wouldn't work on other routers.

== Kernel Modules ==
These kernel modules were used:
 *i2c-core
 *i2c-algo-bit
 *i2c-proc
 *i2c-dev
 *i2c-mips-gpio (compiled separately from the regular kernel modules)

The first 4 can be obtained by rebuilding the kernel using "make menuconfig" in the kernel tree build_mipsel/linux and enabling the I2C bit-banging routines. After compilation, they can just be copied over to the router to the /lib/modules/2.4.30 directory.[[BR]]
The last kernel module needs to be compiled from the code mentioned in the credits section of this page or copied from here:
{{{

/* ------------------------------------------------------------------------- */
/* i2c-mips-gpio.c i2c-hw access for WRT54G/GS                               */
/* ------------------------------------------------------------------------- */
/*
    Based on original i2c-mips-gpio by John Newbigin,
    which in turn was based on i2c-philips-par.c by Simon G. Vogl.

    Changed to sb_gpio-Interface by Torsten Landschoff.

    4-wire logic and final version by niclas at datenritter dot de.

    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 2 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program; if not, write to the Free Software
    Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.                */
/* ------------------------------------------------------------------------- */

#include <linux/kernel.h>
#include <linux/ioport.h>
#include <linux/module.h>
#include <linux/init.h>
#include <linux/stddef.h>

#include <typedefs.h>
#include <bcmdevs.h>
#include <sbutils.h>

#include <linux/i2c.h>
#include <linux/i2c-algo-bit.h>

#include <linux/reboot.h>

#define GPIO_WHITE 2
#define GPIO_ORANGE 3
/* that's RP4 3rd pin from left on GS V1.1            */
/* on GS V4.0 there are solder points at the orange   */
/* and white LEDs.                                    */

#define GPIO_CISCO 4
/* that's RA13 on GS V1.1                             */

#define GPIO_RESET 6
#define GPIO_RA10 5
/* RA10 is left of RP4, near BCM5325 on GS V1.1       */

#define GPIO_WHITE 2
/* white LED */

#define GPIO_DMZ 7
/* DMZ LED */


#define INVERTED_OUTPUTS 1        /* default */
/* we use NPN transistors on output lines to pull     */
/* down the line and 10k pull up resistors, so the    */
/* output is inverted.                                */
/* undef for PNP transistors.                         */

static void *sbh;    /* handle for sb_* functions  */



/* WARNING: User space programms can interfere with this driver through */
/* /dev/gpio if they change control and/or enable flags!                */
/* Don't touch the flags! Also, /dev/gpio should be left alone!         */



/* ----------------- the circuit -------------------------------------- */
/*

The GPIO lines somehow didn't show nice signal levels, if they are used
as SDA and SCL directly. This might have something to do with changing 
from input to output and back all the time.

So we use four GPIO lines instead, two outputs to control NPN pull down 
transistors, two input lines to read the bus.


          (+)--------------------------------.
                        |                    |
                       .-.                  .-.
                       | |10k               | |10k
                       | |                  | |
                       '-'                  '-'
                        |                    '---o-----(I2C_SCL)
                        |                    |   |
                        '---o----------------)---)-----(I2C_SDA)
                      |/    |              |/    |
          (SDA_OUT)---|     |  (SCL_OUT)---|     |
                      |>    |              |>    |
                        |   |                |   |
          (-)-----------o---)----------------'   |
                            |                    |
                            |                    |
     (SDA_IN)---------------'                    |
                                                 |
     (SCL_IN)------------------------------------'


                                                                        */
/* -------------------------------------------------------------------- */

/* ----- module parameters -------------------------------------------- */

/* better don't use reset as input! */

static int i2c_scl_i = GPIO_ORANGE;
static int i2c_sda_i = GPIO_WHITE;
static int i2c_scl_o = GPIO_DMZ;
static int i2c_sda_o = GPIO_CISCO;
static int i2c_inverted = INVERTED_OUTPUTS;

#define GPIO_CLOCK (1 << i2c_scl_i)
#define GPIO_DATA  (1 << i2c_sda_i)
#define GPIO_CLOCK_OUT (1 << i2c_scl_o)
#define GPIO_DATA_OUT (1 << i2c_sda_o)


/* ----- local functions ---------------------------------------------- */

static void bit_gpio_set(unsigned int mask) {
#ifdef INVERTED_OUTPUTS
    sb_gpioout(sbh, mask, 0);
#else
    sb_gpioout(sbh, mask, mask);
#endif
}

static void bit_gpio_clear(unsigned int mask) {
#ifdef INVERTED_OUTPUTS
    sb_gpioout(sbh, mask, mask);
#else
    sb_gpioout(sbh, mask, 0);
#endif
}

static int bit_gpio_get(int mask) {
    return (sb_gpioin(sbh) & mask);
}

static void bit_gpio_setscl(void *data, int state) {
        if (state) {
                bit_gpio_set(GPIO_CLOCK_OUT);
        } else {
                bit_gpio_clear(GPIO_CLOCK_OUT);
        }
}

static void bit_gpio_setsda(void *data, int state) {
        if (state) {
                bit_gpio_set(GPIO_DATA_OUT);
        } else {
                bit_gpio_clear(GPIO_DATA_OUT);
        }
}

static int bit_gpio_getscl(void *data) {
        return bit_gpio_get(GPIO_CLOCK);
}

static int bit_gpio_getsda(void *data) {
        return bit_gpio_get(GPIO_DATA);
}

/*   */

static int bit_gpio_reg(struct i2c_client *client) {
        return 0;
}

static int bit_gpio_unreg(struct i2c_client *client) {
        return 0;
}

static void bit_gpio_inc_use(struct i2c_adapter *adap) {
        MOD_INC_USE_COUNT;
}

static void bit_gpio_dec_use(struct i2c_adapter *adap) {
        MOD_DEC_USE_COUNT;
}

/* ------------------------------------------------------------------------
 * Encapsulate the above functions in the correct operations structure.
 * This is only done when more than one hardware adapter is supported.
 */

static struct i2c_algo_bit_data bit_gpio_data = {
        NULL,
        bit_gpio_setsda,
        bit_gpio_setscl,
        bit_gpio_getsda,
        bit_gpio_getscl,
        80,             /* udelay, half-clock-cycle time in microsecs, i.e. clock is (500 / udelay) KHz */
        80,                /* mdelay, in millisecs, unused                                                 */
        100,            /* timeout, in jiffies                                                          */
                        /* delays are high, use 80,80,100 or less for fast transistors                  */
        };


static struct i2c_adapter bit_gpio_ops = {
        "WRT54G GPIO",
        0x00,
        NULL,
        &bit_gpio_data,
        bit_gpio_inc_use,
        bit_gpio_dec_use,
        bit_gpio_reg,
        bit_gpio_unreg,
};


/* This function will do any cleanup required on reboot or module unloading. */

static void tidyup(void){
    /* set wires back to input/output:             */

    sb_gpioouten(sbh, 1<<2, 1<<2);     /* white output  */
    sb_gpioouten(sbh, 1<<3, 1<<3);     /* orange output */
    sb_gpioouten(sbh, 1<<4, 0);     /* cisco input   */
    sb_gpioouten(sbh, 1<<5, 1<<5);     /* RA10 output   */
    sb_gpioouten(sbh, 1<<7, 1<<7);     /* DMZ output    */
    
    
    
    /* set reset high so we won't reboot into failsafe or even reset nvram:     */
    sb_gpioout(sbh, 1<<6, 1<<6);
    
    /* sb_gpiocontrol(sbh, 1<<6, 1<<6); */     /* not required */
    /* sb_gpioouten(sbh, 1<<6, 0); */     /* not required */

        /* no way to restore control flags, sbutils don't offer a way to read them. */
    /* we don't need to do that anyway, do we?                                  */
}


/*
 * This function is called when the system is halted or rebooted. 
 * At this point we have to reset the I/O lines as explained later.
 */

static int reboot_notifier_func(struct notifier_block *self, unsigned long mode, void *ignore)
{
    tidyup();
    return NOTIFY_OK;
}

static struct notifier_block reboot_notifier = {
    .notifier_call = reboot_notifier_func
};


int __init i2c_bitgpio_init(void) {
        printk(KERN_INFO "i2c-mips-gpio.o: i2c WRT54G GPIO module version 1.5 2005-12-16\n");
    sbh = sb_kattach();

    /* 
     * Register reboot notifier to make sure the I/O lines are released correctly.
     */
    register_reboot_notifier(&reboot_notifier);

    if ((i2c_sda_i == GPIO_RESET)||(i2c_scl_i==GPIO_RESET)) printk(KERN_INFO "i2c-mips-gpio.o: WARNING: GPIO line 6 (reset) used as input!\n");

        /* clear control flag for all 4 lines - still not sure what control is for... */
    sb_gpiocontrol(sbh, GPIO_CLOCK, 0);    
    sb_gpiocontrol(sbh, GPIO_DATA, 0);
    sb_gpiocontrol(sbh, GPIO_CLOCK_OUT, 0);    
    sb_gpiocontrol(sbh, GPIO_DATA_OUT, 0);

    /* set both I2C lines to high level */
    bit_gpio_set(GPIO_DATA_OUT);
    bit_gpio_set(GPIO_CLOCK_OUT);

    /* enable output for output lines   */
    sb_gpioouten(sbh, GPIO_CLOCK_OUT, GPIO_CLOCK_OUT);
    sb_gpioouten(sbh, GPIO_DATA_OUT, GPIO_DATA_OUT);

    /* disable output for input lines   */
    sb_gpioouten(sbh, GPIO_CLOCK, 0);
    sb_gpioouten(sbh, GPIO_DATA, 0);

    if(i2c_bit_add_bus(&bit_gpio_ops) < 0)
                return -ENODEV;

        return 0;
}


void __exit i2c_bitgpio_exit(void) {
    
    i2c_bit_del_bus(&bit_gpio_ops);
    tidyup();
    /* Unregister the reboot notifier or hell will break lose when the 
    / * system is rebooted after module unloading. */
    unregister_reboot_notifier(&reboot_notifier);
}


EXPORT_NO_SYMBOLS;

MODULE_PARM(i2c_scl_i,"i");
MODULE_PARM_DESC(i2c_scl_i, "Number of GPIO wire used for SCL input.");
MODULE_PARM(i2c_sda_i,"i");
MODULE_PARM_DESC(i2c_sda_i, "Number of GPIO wire used for SDA input.");
MODULE_PARM(i2c_scl_o, "i");
MODULE_PARM_DESC(i2c_scl_o, "Number of GPIO wire used for SCL output.");
MODULE_PARM(i2c_sda_o, "i");
MODULE_PARM_DESC(i2c_sda_o, "Number of GPIO wire used for SDA output.");
MODULE_PARM(i2c_inverted, "i");
MODULE_PARM_DESC(i2c_inverted, "Set this to 1 if output signals should be inverted.");

MODULE_AUTHOR("<niclas at datenritter dot de>");
MODULE_DESCRIPTION("I2C-Bus adapter routines for WRT54G GPIO");
MODULE_LICENSE("GPL");

#ifdef MODULE
int init_module(void) {
        return i2c_bitgpio_init();
}

void cleanup_module(void) {
        i2c_bitgpio_exit();
}
#endif


}}}

Note that the code shows an alternate hardware schematic for the I2C bus which differs from the schematic presented in the Hardware section of this page.[[BR]]
The schematic presented in the Hardware section provides better signal buffering to and from the I2c devices.
After compiling the last module it too needs to be copied to th router and installed under /lib/modules/2.4.30 just like the previous modules.
If you want to get all the Modules precompiled, send a PM to `NekMech` on the `OpenWrt` forum.

== User Space programs and scripts ==
There are 3 binaries: i2cset, i2cread, i2cdump[[BR]]
And 3 scripts: i2c-load.sh, gethwclock.pl, S99i2c[[BR]]

In all the examples below, the device used was the DS1307 I2C clock chip.
The clock chip is wired to I2C bus “0” (the only one), and has a device address of “104”
decimal or “68H” hex. These programs were all installed under /usr/share/i2c on the
router and are run from there besides S99i2c which is installed under /etc/init.d.

=== Binaries ===
 *i2cset – Sends any command over the i2c bus to any device.
 *i2cread – Reads any number of characters from any device on the i2c bus.
 *i2cdump – Provided as a diagnostic tool which can read all the available data from any i2c device.
=== Scripts ===
 *i2c-load.sh – bash script for loading the kernel modules in the correct order with “insmod”.
 *gethwclock.pl – microperl script which performs all the tasks of reading and writing to the clock chip. You will need the microperl ipkg installed as stated in the prerequisites.
 *S99i2c – bash script which is executed at boot to load the kernel modules, and update the system time from the hardware clock.

=== Using the scripts and binaries ===
'''i2cset''' - Used to send data/commands to an i2c device.[[BR]]
Running with no command line options displays an error message and help syntax as well as the available i2c busses.[[BR]]
{{{
Example:
root@OpenWrt:/usr/share/i2c# ./i2cset
Syntax: i2cset I2CBUS CHIP-ADDRESS VALUES
I2CBUS is an integer
Installed I2C busses:
i2c-0 i2c WRT54G GPIO Bit-shift algorithm
}}}
The gethwclock.pl script uses it to set the time, the control register and to move the
register pointer of the hardware clock to the correct position for reading the time.[[BR]]

'''i2cread''' - Used to read back data from an i2c device.[[BR]]
Running with no command line options, displays an error message and help syntax as well as the available i2c busses.
{{{
Example:
root@OpenWrt:/usr/share/i2c# ./i2cread
Syntax: i2cread I2CBUS CHIP-ADDRESS COUNT
I2CBUS is an integer
Installed I2C busses:
i2c-0 i2c WRT54G GPIO Bit-shift algorithm
}}}
The gethwclock.pl script uses it to read the hardware clock during boot (to set the
system clock) and any time requested manually.

'''i2cdump''' - Used as a general purpose diagnostic tool, it performs a dump of any i2c devices registers/memory.[[BR]]
Running with no command line options displays an error message and help syntax.
{{{
Example:
root@OpenWrt:/usr/share/i2c# ./i2cdump
Error: No i2c-bus specified!
Syntax: i2cdump I2CBUS ADDRESS [MODE] [BANK [BANKREG]]
MODE is 'b[yte]', 'w[ord]', 's[mbusblock], or 'i[2cblock]' (default b)
Append MODE with 'p' for PEC checking
I2CBUS is an integer
ADDRESS is an integer 0x00 - 0x7f
BANK and BANKREG are for byte and word accesses (default bank 0, reg 0x4e)
BANK is the command for smbusblock accesses (default 0)
Installed I2C busses:
i2c-0 i2c WRT54G GPIO Bit-shift algorithm
}}}

Running the utility with the bus number “0” and device address “104” will dump all the registers for the clock chip. Note that addresses 08H – 3FH are general purpose ram registers which can be used for anything you want. Do not use ram register 3FH since it will be overwritten when reading the date from the clock chip by the gethwclock.pl script.
{{{
Example:
root@OpenWrt:/usr/share/i2c# ./i2cdump 0 104
No size specified (using byte-data access)
WARNING! This program can confuse your I2C bus, cause data loss and worse!
I will probe file /dev/i2c/0, address 0x68, mode byte
You have five seconds to reconsider and press CTRL-C!

0 1 2 3 4 5 6 7 8 9 a b c d e f 0123456789abcdef
00: 04 48 16 01 09 04 07 10 10 10 6a 50 52 c3 4d 22 ?H????????jPR?M"
10: cb 6a 68 00 e2 7c 50 41 03 01 f9 55 12 0c 69 0c ?jh.?|PA???U??i?
20: 70 1e 02 42 a8 2c 02 2a bc 48 28 3e 80 2c b7 84 p??B?,?*?H(>?,??
30: 1f 00 68 42 c6 5e 34 d4 42 8a 20 28 c7 90 fe ff ?.hB?^4?B? (???.
40: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 ................
50: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 ................
60: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 ................
70: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 ................
80: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 ................
90: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 ................
a0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 ................
b0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 ................
c0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 ................
d0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 ................
e0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 ................
f0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 ................
}}}






Work in progress
