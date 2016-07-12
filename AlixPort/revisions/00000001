== Building firmware for the alix 2c2: ==

http://www.netgate.com/product_info.php?cPath=60&products_id=509

 * config buildroot with the following options:
  * Target System: x86
  * Subtarget: Generic
  * Target Profile: PCEngines Alix
  * Target Options: 
   * jffs2, squashfs, ext2
   * serial baud rate: 38400
   * Kernel partition size: 12
   * root partition: /dev/hda2
   * Filsystem part size: 96MB
   * Maximum number of inodes: 1500


On a linux box with a cf reader:
 * Make sure the card isn't mounted, often its mounted by default
 * use dd to write the image to the disk:
{{{
 dd if=openwrt-x86-squashfs.image of=/dev/sda
}}}
 * After booting linux, it took a long time for the jffs partition to init.
 * After jffs init, run firstboot manually (causes oops?)


To upgrade from within openwrt:
 * use dd to write the image to the disk:
{{{
 dd if=openwrt-x86-squashfs.image of=/dev/hda
}}}
 * reboot
 * make sure the root_data partition was regenerated automatically


Using the LEDs on the alix: 
{{{
You should get three LED devices under /sys/class/leds/ 
- alix:1, alix:2 and alix:3

This should turn on one led:
  echo 1 > /sys/class/leds/alix:1/brightness

And off:
  echo 0 > /sys/class/leds/alix:1/brightness

And this should make it blink:
  echo timer > /sys/class/leds/alix:1/trigger
  echo 1000 > /sys/class/leds/alix:1/delay_off
  echo 100 > /sys/class/leds/alix:1/delay_on
}}}

After rebooting, you will have to add the wan interface to /etc/config/network


Entering failsafe:
 * The button does not seem to work
 * Attach serial cable, speed is 38400
 * Press Esc during the memory check
 * Choose 'safe mode' in the grub menu
