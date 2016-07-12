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

== i2cdump.c ==
{{{

/*
    i2cdump.c - Part of i2cdump, a user-space program to dump I2C registers
    Copyright (c) 2002  Frodo Looijaard <frodol@dds.nl>, and
    Mark D. Studebaker <mdsxyz123@yahoo.com>

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
    Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.

    17-Apr-2004 Modified version for I2C project by NekMech.
*/

#include <errno.h>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>
#include <linux/i2c-dev.h>

/*
   We don't use this #define but it was put into i2c.h at the same time as
   i2c_smbus_read_i2c_block_data() was implemented (i2c 2.6.3),
   so we use it as a version check.
*/
#ifdef I2C_FUNC_SMBUS_READ_I2C_BLOCK_2 
#define USE_I2C_BLOCK 1
#else
#define USE_I2C_BLOCK 0
#endif

#ifdef I2C_FUNC_SMBUS_BLOCK_DATA_PEC
#define HAVE_PEC 1
#endif

void help(void)
{
  FILE *fptr;
  char s[100];

  fprintf(stderr,"Syntax: i2cdump I2CBUS ADDRESS [MODE] [BANK [BANKREG]]\n");
  fprintf(stderr,"  MODE is 'b[yte]', 'w[ord]', 's[mbusblock], or 'i[2cblock]' (default b)\n");
  fprintf(stderr,"  Append MODE with 'p' for PEC checking\n");
  fprintf(stderr,"  I2CBUS is an integer\n");
  fprintf(stderr,"  ADDRESS is an integer 0x00 - 0x7f\n");
  fprintf(stderr,"  BANK and BANKREG are for byte and word accesses (default bank 0, reg 0x4e)\n");
  fprintf(stderr,"  BANK is the command for smbusblock accesses (default 0)\n");
  if((fptr = fopen("/proc/bus/i2c", "r"))) {
    fprintf(stderr,"  Installed I2C busses:\n");
    while(fgets(s, 100, fptr))
      fprintf(stderr, "    %s", s);	
    fclose(fptr);
  }
}

int main(int argc, char *argv[])
{
  char *end;
  int i,j,i2cbus,address,size,file;
  int e1, e2, e3;
  int res = 0;
  int bank = 0, bankreg = 0x4E;
  char filename1[20];
  char filename2[20];
  char filename3[20];
  char *filename;
  long funcs;
  unsigned char cblock[256];  
  int block[256];  
  int pec = 0;

  if (argc < 2) {
    fprintf(stderr,"Error: No i2c-bus specified!\n");
    help();
    exit(1);
  }

  i2cbus = strtol(argv[1],&end,0);
  if (*end) {
    fprintf(stderr,"Error: First argument not a number!\n");
    help();
    exit(1);
  }
  if ((i2cbus < 0) || (i2cbus > 0xff)) {
    fprintf(stderr,"Error: I2CBUS argument out of range!\n");
    help();
  }

  if (argc < 3) {
    fprintf(stderr,"Error: No address specified!\n");
    help();
    exit(1);
  }
  address = strtol(argv[2],&end,0);
  if (*end) {
    fprintf(stderr,"Error: Second argument not a number!\n");
    help();
    exit(1);
  }
  if ((address < 0) || (address > 0x7f)) {
    fprintf(stderr,"Error: Address out of range!\n");
    help();
  }

  if (argc < 4) {
    fprintf(stderr,"No size specified (using byte-data access)\n");
    size = I2C_SMBUS_BYTE_DATA;
  } else if (!strncmp(argv[3],"b",1)) {
    size = I2C_SMBUS_BYTE_DATA;
    pec = argv[3][1] == 'p';
  } else if (!strncmp(argv[3],"w",1)) {
    size = I2C_SMBUS_WORD_DATA;
    pec = argv[3][1] == 'p';
  } else if (!strncmp(argv[3],"s",1)) {
    size = I2C_SMBUS_BLOCK_DATA;
    pec = argv[3][1] == 'p';
  } else if (!strcmp(argv[3],"i"))
    size = I2C_SMBUS_I2C_BLOCK_DATA;
  else {
    fprintf(stderr,"Error: Invalid mode!\n");
    help();
    exit(1);
  }

  if(argc > 4) {
    bank = strtol(argv[4],&end,0);
    if (*end || size == I2C_SMBUS_I2C_BLOCK_DATA) {
      fprintf(stderr,"Error: Invalid bank number!\n");
      help();
      exit(1);
    }
    if (((size == I2C_SMBUS_BYTE_DATA) || (size == I2C_SMBUS_WORD_DATA)) &&
        ((bank < 0) || (bank > 15))) {
      fprintf(stderr,"Error: bank out of range!\n");
      help();
      exit(1);
    }
    if (((size == I2C_SMBUS_BLOCK_DATA)) &&
        ((bank < 0) || (bank > 0xff))) {
      fprintf(stderr,"Error: block command out of range!\n");
      help();
      exit(1);
    }

    if(argc > 5) {
      bankreg = strtol(argv[5],&end,0);
      if (*end || size == I2C_SMBUS_BLOCK_DATA) {
        fprintf(stderr,"Error: Invalid bank register number!\n");
        help();
        exit(1);
      }
      if ((bankreg < 0) || (bankreg > 0xff)) {
        fprintf(stderr,"Error: bank out of range (0-0xff)!\n");
        help();
        exit(1);
      }
    }
  }

/*
 * Try all three variants and give the correct error message
 * upon failure
 */

  sprintf(filename1,"/dev/i2c-%d",i2cbus);
  sprintf(filename2,"/dev/i2c%d",i2cbus);
  sprintf(filename3,"/dev/i2c/%d",i2cbus);
  if ((file = open(filename1,O_RDWR)) < 0) {
    e1 = errno;
    if ((file = open(filename2,O_RDWR)) < 0) {
      e2 = errno;
      if ((file = open(filename3,O_RDWR)) < 0) {
        e3 = errno;
        if(e1 == ENOENT && e2 == ENOENT && e3 == ENOENT) {
          fprintf(stderr,"Error: Could not open file `%s', `%s', or `%s': %s\n",
                     filename1,filename2,filename3,strerror(ENOENT));
        }
        if (e1 != ENOENT) {
          fprintf(stderr,"Error: Could not open file `%s' : %s\n",
                     filename1,strerror(e1));
          if(e1 == EACCES)
            fprintf(stderr,"Run as root?\n");
        }
        if (e2 != ENOENT) {
          fprintf(stderr,"Error: Could not open file `%s' : %s\n",
                     filename2,strerror(e2));
          if(e2 == EACCES)
            fprintf(stderr,"Run as root?\n");
        }
        if (e3 != ENOENT) {
          fprintf(stderr,"Error: Could not open file `%s' : %s\n",
                     filename3,strerror(e3));
          if(e3 == EACCES)
            fprintf(stderr,"Run as root?\n");
        }
        exit(1);
      } else {
         filename = filename3;
      }
    } else {
       filename = filename2;
    }
  } else {
    filename = filename1;
  }
  
  /* check adapter functionality */
  if (ioctl(file,I2C_FUNCS,&funcs) < 0) {
    fprintf(stderr,
            "Error: Could not get the adapter functionality matrix: %s\n",
            strerror(errno));
    exit(1);
  }

  switch(size) {
     case I2C_SMBUS_BYTE_DATA:
#ifdef HAVE_PEC
	if(pec) {
	  if (! (funcs & I2C_FUNC_SMBUS_READ_BYTE_DATA_PEC)) {
	     fprintf(stderr, "Error: Adapter for i2c bus %d", i2cbus);
	     fprintf(stderr, " does not have byte read w/ PEC capability\n");
	     exit(1);
	  }       
	} else
#endif
	{
	  if (! (funcs & I2C_FUNC_SMBUS_READ_BYTE_DATA)) {
	     fprintf(stderr, "Error: Adapter for i2c bus %d", i2cbus);
	     fprintf(stderr, " does not have byte read capability\n");
	     exit(1);
	  }       
	}
	break;

     case I2C_SMBUS_WORD_DATA:
#ifdef HAVE_PEC
	if(pec) {
	  if (! (funcs & I2C_FUNC_SMBUS_READ_WORD_DATA_PEC)) {
	     fprintf(stderr, "Error: Adapter for i2c bus %d", i2cbus);
	     fprintf(stderr, " does not have word read w/ PEC capability\n");
	     exit(1);
	  }       
	} else
#endif
	{
	  if (! (funcs & I2C_FUNC_SMBUS_READ_WORD_DATA)) {
	     fprintf(stderr, "Error: Adapter for i2c bus %d", i2cbus);
	     fprintf(stderr, " does not have word read capability\n");
	     exit(1);
	  }       
	}
	break;

     case I2C_SMBUS_BLOCK_DATA:
#ifdef HAVE_PEC
	if(pec) {
	  if (! (funcs & I2C_FUNC_SMBUS_READ_BLOCK_DATA_PEC)) {
	     fprintf(stderr, "Error: Adapter for i2c bus %d", i2cbus);
	     fprintf(stderr, " does not have smbus block read capability\n");
	     exit(1);
	  }       
	} else
#endif
	{
	  if (! (funcs & I2C_FUNC_SMBUS_READ_BLOCK_DATA)) {
	     fprintf(stderr, "Error: Adapter for i2c bus %d", i2cbus);
	     fprintf(stderr, " does not have smbus block read w/ PEC capability\n");
	     exit(1);
	  }       
	}
	break;

     case I2C_SMBUS_I2C_BLOCK_DATA:
	if (! (funcs & I2C_FUNC_SMBUS_READ_I2C_BLOCK)) {
	   fprintf(stderr, "Error: Adapter for i2c bus %d", i2cbus);
	   fprintf(stderr, " does not have i2c block read capability\n");
	   exit(1);
	}       
	break;

  }
  /* use FORCE so that we can look at registers even when
     a driver is also running */
  if (ioctl(file,I2C_SLAVE_FORCE,address) < 0) {
    fprintf(stderr,"Error: Could not set address to %d: %s\n",address,
            strerror(errno));
    exit(1);
  }
 
  if(pec) {
#ifdef HAVE_PEC
    if (ioctl(file,I2C_PEC, 1) < 0) {
      fprintf(stderr,"Error: Could not set PEC: %s\n", strerror(errno));
      exit(1);
    }
#else
    fprintf(stderr,"Error: PEC not supported in your kernel\n");
    exit(1);
#endif
  }

  fprintf(stderr,"  WARNING! This program can confuse your I2C bus, "
          "cause data loss and worse!\n");
  fprintf(stderr,"  I will probe file %s, address 0x%x, mode %s\n",
          filename,address,size == I2C_SMBUS_BLOCK_DATA ? "smbus block" :
                           size == I2C_SMBUS_I2C_BLOCK_DATA ? "i2c block" :
                           size == I2C_SMBUS_BYTE_DATA ? "byte" : "word");
  if(pec)
    fprintf(stderr,"  with PEC checking.\n");
  if(bank) { 	
    if(size == I2C_SMBUS_BLOCK_DATA)
      fprintf(stderr,"  Using command 0x%02x.\n", bank);
    else
      fprintf(stderr,"  Probing bank %d using bank register 0x%02x.\n",
              bank, bankreg);
  }
  fprintf(stderr,"  You have five seconds to reconsider and press CTRL-C!\n\n");
  sleep(5);

  /* See Winbond w83781d data sheet for bank details */
  if(bank && size != I2C_SMBUS_BLOCK_DATA) {
    i2c_smbus_write_byte_data(file,bankreg,bank | 0x80);
  }

  /* handle all but word data */
  if (size != I2C_SMBUS_WORD_DATA) {

    /* do the block transaction */
    if(size == I2C_SMBUS_BLOCK_DATA || size == I2C_SMBUS_I2C_BLOCK_DATA) {
      if(size == I2C_SMBUS_BLOCK_DATA) {
        res = i2c_smbus_read_block_data(file, bank, cblock);
      } else if(size == I2C_SMBUS_I2C_BLOCK_DATA) {
#if USE_I2C_BLOCK
        res = 0;
        for (i = 0; i < 256; i+=32) {
          res2 = i2c_smbus_read_i2c_block_data(file, i, cblock+i);
          if(res2 <= 0)
            break;
          res += res2;
        }
#else
        fprintf(stderr, "Error: I2C block read unsupported in i2c-core\n");
        exit(1);
#endif
      }
      if(res <= 0) {
        fprintf(stderr, "Error: Block read failed, return code %d\n", res);
        exit(1);
      }
      if(res >= 256)
        res = 256;
      for (i = 0; i < res; i++)
        block[i] = cblock[i];
      for (i = res; i < 256; i++)
        block[i] = -1;
    }

    printf("     0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f    0123456789abcdef\n");
    for (i = 0; i < 256; i+=16) {
      printf("%02x: ",i);
      for(j = 0; j < 16; j++) {
        if(size == I2C_SMBUS_BYTE_DATA) {
          res = i2c_smbus_read_byte_data(file,i+j);
          block[i+j] = res;
        } else
          res = block[i+j];
        if (res < 0)
          printf("XX ");
        else
          printf("%02x ",res & 0xff);
      }
      printf("   ");
      for(j = 0; j < 16; j++) {
        res = block[i+j];
        if (res < 0)
          printf("X");
        else if (((res & 0xff) == 0x00) || ((res & 0xff) == 0xff))
          printf(".");
        else if (((res & 0xff) < 32) || ((res & 0xff) >= 127))
          printf("?");
        else
          printf("%c",res & 0xff);
      }
      printf("\n");
    if(size == I2C_SMBUS_BLOCK_DATA && i == 16)
      break;		
    }
  } else {
    printf("     0,8  1,9  2,a  3,b  4,c  5,d  6,e  7,f\n");
    for (i = 0; i < 256; i+=8) {
      printf("%02x: ",i);
      for(j = 0; j < 8; j++) {
        res = i2c_smbus_read_word_data(file,i+j);
        if (res < 0)
          printf("XXXX ");
        else
          printf("%04x ",res & 0xffff);
      }
      printf("\n");
    }
  }
  if(bank && size != I2C_SMBUS_BLOCK_DATA) {
    i2c_smbus_write_byte_data(file,bankreg,0x80);
  }
  exit(0);
}

}}}
== i2cread.c ==
{{{
/*
    i2cset.c - A user-space program to write an I2C register.
    Copyright (c) 2001  Frodo Looijaard <frodol@dds.nl>, and
    Mark D. Studebaker <mdsxyz123@yahoo.com>

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
    Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.

    17-Apr-2004 Modified version for I2C project by NekMech.
*/

#include <errno.h>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>
#include <linux/i2c.h>
#include <linux/i2c-dev.h>

void help(void)
{
  FILE *fptr;
  char s[100];

  printf("Syntax: i2cread I2CBUS CHIP-ADDRESS COUNT\n");
  printf("  I2CBUS is an integer\n");
  if((fptr = fopen("/proc/bus/i2c", "r"))) {
    printf("  Installed I2C busses:\n");
    while(fgets(s, 100, fptr))
      printf("    %s", s);	
    fclose(fptr);
  }
  exit(1);
}

int main(int argc, char *argv[])
{
  char *end;
  int i2cbus,address,count,file;
  int loop;
  int e1, e2, e3;
  char filename1[20];
  char filename2[20];
  char filename3[20];
  char *filename;
  char buf[10];

  if (argc < 3)
    help();


  i2cbus = strtol(argv[1],&end,0);
  if (*end || (i2cbus < 0) || (i2cbus > 0x3f)) {
    printf("Error: I2CBUS argument invalid!\n");
    help();
  }

  address = strtol(argv[2],&end,0);
  if (*end || (address < 0) || (address > 0x7f)) {
    printf("Error: Chip address invalid!\n");
    help();
  }

  count = 1;
  if (argc > 3) {
     count = strtol(argv[3],&end,0);
     if (*end || (count < 1) || (count > 10)) {
       printf("Error: count is invalid! Must be in range 1 to 10\n");
       help();
     }
  }

/*
 * Try all three variants and give the correct error message
 * upon failure
 */

  sprintf(filename1,"/dev/i2c-%d",i2cbus);
  sprintf(filename2,"/dev/i2c%d",i2cbus);
  sprintf(filename3,"/dev/i2c/%d",i2cbus);
  if ((file = open(filename1,O_RDWR)) < 0) {
    e1 = errno;
    if ((file = open(filename2,O_RDWR)) < 0) {
      e2 = errno;
      if ((file = open(filename3,O_RDWR)) < 0) {
        e3 = errno;
        if(e1 == ENOENT && e2 == ENOENT && e3 == ENOENT) {
          printf("Error: Could not open file `%s', `%s', or `%s': %s\n",
                     filename1,filename2,filename3,strerror(ENOENT));
        }
        if (e1 != ENOENT) {
          printf("Error: Could not open file `%s' : %s\n",
                     filename1,strerror(e1));
          if(e1 == EACCES)
            printf("Run as root?\n");
        }
        if (e2 != ENOENT) {
          printf("Error: Could not open file `%s' : %s\n",
                     filename2,strerror(e2));
          if(e2 == EACCES)
            printf("Run as root?\n");
        }
        if (e3 != ENOENT) {
          printf("Error: Could not open file `%s' : %s\n",
                     filename3,strerror(e3));
          if(e3 == EACCES)
            printf("Run as root?\n");
        }
        exit(1);
      } else {
         filename = filename3;
      }
    } else {
       filename = filename2;
    }
  } else {
    filename = filename1;
  }
  
  if (ioctl(file,I2C_SLAVE,address) < 0) {
    /* ERROR HANDLING; you can check errno to see what went wrong */
    printf("Error: Could not set address to %d: %s\n",address,
            strerror(errno));
    exit(1);
  }

  /* Using I2C Read bytes */
  if (read(file,buf,count) != count) {
    /* ERROR HANDLING: i2c transaction failed */
    printf ("Failed to read bytes\n");
    exit(1);
  } else {
    /* buf array contains the read byte */
    printf ("Returned bytes:");
    for (loop = 0; loop < count; ++loop)
       printf (" %i",buf[loop]);
    printf ("\n");
  }
  close(file);
  exit(0);
}

}}}

== i2cset.c ==
{{{
/*
    i2cset.c - A user-space program to write an I2C register.
    Copyright (c) 2001  Frodo Looijaard <frodol@dds.nl>, and
    Mark D. Studebaker <mdsxyz123@yahoo.com>

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
    Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.

    17-Apr-2004 Modified version for I2C project by NekMech.
*/

#include <errno.h>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>
#include <linux/i2c.h>
#include <linux/i2c-dev.h>

void help(void)
{
  FILE *fptr;
  char s[100];

  printf("Syntax: i2cset I2CBUS CHIP-ADDRESS VALUES\n");
  printf("  I2CBUS is an integer\n");
  if((fptr = fopen("/proc/bus/i2c", "r"))) {
    printf("  Installed I2C busses:\n");
    while(fgets(s, 100, fptr))
      printf("    %s", s);	
    fclose(fptr);
  }
  exit(1);
}

int main(int argc, char *argv[])
{
  char *end;
  int i2cbus,address,file;
  int value, count, loop;
  int e1, e2, e3;
  char filename1[20];
  char filename2[20];
  char filename3[20];
  char *filename;
  char buf[10];

  if (argc < 4)
    help();

  count = argc - 3;

  i2cbus = strtol(argv[1],&end,0);
  if (*end || (i2cbus < 0) || (i2cbus > 0x3f)) {
    printf("Error: I2CBUS argument invalid!\n");
    help();
  }

  address = strtol(argv[2],&end,0);
  if (*end || (address < 0) || (address > 0x7f)) {
    printf("Error: Chip address invalid!\n");
    help();
  }

  value = strtol(argv[3],&end,0);
  if (*end) {
    printf("Error: Data value invalid!\n");
    help();
  }

  // Build up transmit buffer 
  for (loop = 0; loop < count; ++loop) {
     value = strtol(argv[3 + loop],&end,0);
     buf[loop] = value;
  }

/*
 * Try all three variants and give the correct error message
 * upon failure
 */

  sprintf(filename1,"/dev/i2c-%d",i2cbus);
  sprintf(filename2,"/dev/i2c%d",i2cbus);
  sprintf(filename3,"/dev/i2c/%d",i2cbus);
  if ((file = open(filename1,O_RDWR)) < 0) {
    e1 = errno;
    if ((file = open(filename2,O_RDWR)) < 0) {
      e2 = errno;
      if ((file = open(filename3,O_RDWR)) < 0) {
        e3 = errno;
        if(e1 == ENOENT && e2 == ENOENT && e3 == ENOENT) {
          printf("Error: Could not open file `%s', `%s', or `%s': %s\n",
                     filename1,filename2,filename3,strerror(ENOENT));
        }
        if (e1 != ENOENT) {
          printf("Error: Could not open file `%s' : %s\n",
                     filename1,strerror(e1));
          if(e1 == EACCES)
            printf("Run as root?\n");
        }
        if (e2 != ENOENT) {
          printf("Error: Could not open file `%s' : %s\n",
                     filename2,strerror(e2));
          if(e2 == EACCES)
            printf("Run as root?\n");
        }
        if (e3 != ENOENT) {
          printf("Error: Could not open file `%s' : %s\n",
                     filename3,strerror(e3));
          if(e3 == EACCES)
            printf("Run as root?\n");
        }
        exit(1);
      } else {
         filename = filename3;
      }
    } else {
       filename = filename2;
    }
  } else {
    filename = filename1;
  }
  
  if (ioctl(file,I2C_SLAVE,address) < 0) {
    /* ERROR HANDLING; you can check errno to see what went wrong */
    printf("Error: Could not set address to %d: %s\n",address,
            strerror(errno));
    exit(1);
  }


  // Perform the buffer transmit
  if ( write(file, buf, count) != count) {
    printf( "Warning - write failed\n");
    exit(1);
  }

  close(file);
  exit(0);
}

}}}

== gethwclock.pl ==
{{{
#!/usr/bin/microperl
#######################################################################
# Author:  (NekMech)
# Date:    9 Apr 2007
# Version: 1.0
#
# Perl script to read and set the DS1307 clock chip, convert to 
# real-time or set system clock
#
# Layout of chip registers:
# ADDR| 7       6       5       4       3       2       1       0
#------------------------------------------------------------------
# 0x00| CH  |      10 seconds        |         seconds            |
# 0x01|  0  |      10 minutes        |         minutes            |
# 0x02|  0  | 12/24 |10h/AM-PM| 10h  |          hours             |
# 0x03|  0  |   0   |   0   |   0    |  0   |     day of week     |
# 0x04|  0  |   0   |    10 date     |          date              |
# 0x05|  0  |   0   |   0   |   10m  |          month             |
# 0x06|           10 year            |          year              |
# 0x07|                     control register                      |
# 0x08 - 0x3F                 data  registers                     |
#------------------------------------------------------------------
#
# Notes:
# 1) Clock is read by setting FF in last data register causing register 
#    pointer overflow and then reading 7 bytes.
#    Avoid using last data register (0x3F) since it will be overwritten.
# 2) Since year is stored as last 2 digits only, year 2000+ is assumed
# 3) Clock init will start the counter and turn on SQW at 1Hz
########################################################################

my $help = <<EOH;

gethwclock.pl <sethw|gethw|setos|inithw>

sethw - set the hardware clock from system time
gethw - display the date stored in the hardware clock
setos - set the system time from the hardware clock
inithw - initialize hardware clock control register
         and start counter. This should be done once before
         using the clock for the first time
EOH

my @dowarray = ("","Mon","Tue","Wed","Thu","Fri","Sat","Sun");
my @montharray = ("","Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec");
my $i2cbus = "0";
my $i2caddr = "104";
my $lastregister = "63";
my $lastregvalue = "255";
my $regcount = "7";

my %hwregisters = (
   'seconds' => {
                   'register' => "0",
                   'data'     => "0"
                },
   'minutes' => {
                   'register' => "1",
                   'data'     => ""
                },
   'hours'   => {
                   'register' => "2",
                   'data'     => ""
                },
   'dow'     => {
                   'register' => "3",
                   'data'     => ""
                },
   'date'    => {
                   'register' => "4",
                   'data'     => ""
                },
   'month'   => {
                   'register' => "5",
                   'data'     => ""
                },
   'year'    => {
                   'register' => "6",
                   'data'     => ""
                },
   'control' => {
                   'register' => "7",
                   'data'     => "16"
                }
);
                                                           
my ($seconds,$minutes,$hours,$dow,$date,$month,$year);

sub showhelp {
   print $help;
}

sub get_sys_date {
   my $osdate_command = 'date +%S:%M:%H:%u:%d:%m:%y';
   my $osdate = `$osdate_command`;
   if ($?) {
      print $osdate,"\n";
      return(0);
   }
   chomp($osdate);
   # Debug: 
   # print "Got OS: $osdate\n";
   return($osdate);
}

sub convert_bcd_to_decimal {
   my $bcdvalue = shift;
   return(oct("0x".$bcdvalue));
}

sub set_hw_reg_values {
   # Load hash with OS date info
   my $OSdata = shift;
   ($hwregisters{'seconds'}->{'data'},
    $hwregisters{'minutes'}->{'data'},
    $hwregisters{'hours'}->{'data'},
    $hwregisters{'dow'}->{'data'},
    $hwregisters{'date'}->{'data'},
    $hwregisters{'month'}->{'data'},
    $hwregisters{'year'}->{'data'}) = split(/:/,$OSdata);
    
   # Convert values to correct notation and send data to hw clock.
   # Seconds should be last because of the way the clock resets the
   # internal divider when seconds are written.
   
   foreach my $reg (keys %hwregisters) {
      next if ($reg =~ /(control|seconds)/);
      $hwregisters{$reg}->{'data'} = 
         convert_bcd_to_decimal($hwregisters{$reg}->{'data'});
      set_hw_reg($hwregisters{$reg}->{'register'},
                 $hwregisters{$reg}->{'data'}) or 
                    die "clock set failed on $reg\n"; 
   }
   $hwregisters{'seconds'}->{'data'} = 
      convert_bcd_to_decimal($hwregisters{'seconds'}->{'data'});
   set_hw_reg($hwregisters{'seconds'}->{'register'},
              $hwregisters{'seconds'}->{'data'}) or 
                 die "clock set failed on seconds\n"; 
}

sub set_hw_reg {
   my ($regnum, $regvalue) = @_;
   my $i2c_command = "./i2cset $i2cbus $i2caddr $regnum $regvalue";
   my $i2cset = `$i2c_command`;
   if ($?) {
      print $i2cset,"\n";
      return(0);
   }
   return(1);
}

sub set_hw_clock {
   my $OSdata = get_sys_date();
   return (0) unless ($OSdata);
   set_hw_reg_values($OSdata);
   return(1);
}

sub get_hw_regs {
   my $i2csetstate = set_hw_reg($lastregister,$lastregvalue);
   return (0) unless ($i2csetstate);
   my $readhwclock = "./i2cread $i2cbus $i2caddr $regcount";
   my $rtcregs = `$readhwclock`;
   if ($?) {
      print $rtcregs,"\n";
      return(0);
   }
   chomp($rtcregs);
   # Debug: 
   # print "Got: $rtcregs\n";
   return ($rtcregs);
}

sub get_hw_data {
   my $rtcclockbytes = get_hw_regs() or die;
   my ($null,$null,$rtcseconds,$rtcminutes,$rtchours,$rtcday,$rtcdate,$rtcmonth,$rtcyear) =
       split(/\s+/,$rtcclockbytes);
   $date = sprintf("%02s",sprintf("%x",$rtcdate));
   $month = sprintf("%02s",sprintf("%x",$rtcmonth));
   $hours = sprintf("%02s",sprintf("%x",$rtchours));
   $minutes = sprintf("%02s",sprintf("%x",$rtcminutes));
   $seconds = sprintf("%02s",sprintf("%x",$rtcseconds));
   $year = "20".sprintf("%02s",sprintf("%x",$rtcyear));
   $dow = $rtcday;
}

sub show_hw_date {
   get_hw_data();
   printf("%s %s %s %s:%s:%s %s\n",
          $dowarray[$dow],
          $montharray[$month],
          $date, 
          $hours,
          $minutes,
          $seconds,
          $year);
}

sub set_os_date {
   get_hw_data();
   my $osdate = $month.$date.$hours.$minutes.$year.".".$seconds;
   my $res = `date -s $osdate`;
   if ($?) {
      print $res,"\n";
      return(0);
   }
   retunr(1);
}

sub init_hw_clock {
   set_hw_reg($hwregisters{'control'}->{'register'},
              $hwregisters{'control'}->{'data'}) or 
                 die "clock init failed on control register\n"; 
   set_hw_reg($hwregisters{'seconds'}->{'register'},
              $hwregisters{'seconds'}->{'data'}) or 
                 die "clock set failed on seconds register\n"; 
   return(1);
}

## Main ##

if (scalar(@ARGV)) {
   $option = shift(@ARGV);
} else {
   showhelp(); 
   exit(0);
}

if ($option eq "sethw") {
   set_hw_clock() or die "failed to set hwclock\n";
} elsif ($option eq "gethw") {
   show_hw_date();
} elsif ($option eq "setos") {
   set_os_date() or die "failed to set os clock\n";
} elsif ($option eq "inithw") {
   print "hw clock init succeeded\n" if init_hw_clock();
} else {
   showhelp();
   exit(0);
}

}}}

== i2c-load.sh ==
{{{

insmod i2c-core
insmod i2c-algo-bit
insmod i2c-proc
insmod i2c-dev
insmod i2c-mips-gpio

}}}

== S99i2c ==
{{{

#!/bin/sh
[ -d /usr/share/i2c ] || exit
cd /usr/share/i2c
./i2c-load.sh || exit
sleep 1
./gethwclock.pl setos && echo "Set clock from I2C RTC"
date

}}}
