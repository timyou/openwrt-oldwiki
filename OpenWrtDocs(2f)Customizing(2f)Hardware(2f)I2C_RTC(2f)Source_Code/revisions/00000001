= I2C RTC Source Code =
== i2c-mips-gpio.c i2c-hw access for WRT54G/GS ==
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
