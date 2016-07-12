Installing spca5xx


Install dependencies.

ipkg install kmod-videodev libpthread libgcc 

use the following if you want spca5xx 
wget http://pmeerw.net/openwrt/kmod-spca5xx_2.4.30+20060501-brcm-1_mipsel.ipk
ipkg install kmod-spca5xx_2.4.30\+20060501-brcm-1_mipsel.ipk


use this for the light edition.

The needed files are:
To download you need to register first.

Kernel Module - LE version: http://www.macsat.com/macsat/component/option,com_docman/task,doc_details/gid,11/Itemid,63/
Kernel Module - Full version: http://www.macsat.com/macsat/component/option,com_docman/task,doc_details/gid,10/Itemid,63/
Software to retrive images: http://www.macsat.com/macsat/component/option,com_docman/task,doc_details/gid,12/Itemid,63/


Download and gunzip the files locally and copied it via scp:

scp spca5xx_lite.o root@openwrt:/lib/modules/2.4.30
scp spcacat root@openwrt:/usr/bin
chmod +x /usr/bin/spcacat

Now it is time to add the module, so that it is loaded at statup. The kernel module is dependent of the kmod-videodev, so this will be installed first, and then the spca4xx_lite module is set to be loaded at startup.

echo "videodev" >> /etc/modules
echo "spca5xx_lite" >> /etc/modules

In order to test if this works, either reboot your router or run something like this:

insmod videodev
insmod spca5xx_lite

Try running dmesg to see if you get something like this occurs at the end:

Linux video capture interface: v1.00
usb.c: registered new driver spca5xx
spca_core.c: spca5xx driver 00.57.06LE registered

Now connect your web cam, for my cam - a Creative NX Pro - I get this in  my syslog (dmesg): 

hub.c: new USB device 01:02.0-1, assigned address 5
spca_core.c: USB SPCA5XX camera found. Type Creative NX Pro Zc301+hv7131b

This creates a device called /dev/v4l/video0
For some reason, the version of spcacat we have here, dosnt support using this device, but if you create a symlink to it, it will works just fine:

ln -s /dev/v4l/video0 /dev/video0 

 
Using spcacat

The spcacat binary has the following possible switches:
spcacat [-h -d -g -f -s -p -N -P -o]
     -h show this usage message.
     -d  device ask the driver to use specified video output device (/dev/video1)
     -o outputfile  causes the program to output avi  with image data received from the video device to the specified file.
     -g grab with READ method instead of default MMAP
     -f video format  nothing YUV420P  fourcc I420
        jpg JPEG         fourcc MJPG
        yuv YUV420P   fourcc I420
    r16 RGB565 16bits fourcc RGB2
    r24 RGB 24bits  fourcc RGB3
    r32 RGB 32bits  fourcc RGB4
    -v RAW data  fourcc RAWD
     -s widthxheight ask the driver for input size
     -p X take a picture every X seconds
     -p X && -o getPicture every X seconds and record in SpcaPict.jpg (spcacat)
     -N take N pictures and stop
     -P parport device (spcacat, spcaserv)

I have made a small bash script that will retrieve an image every 10 seconds, and save it as SpcaPict.jpg.

My script is called imagesnap.sh and looks like:
#/bin/sh
spcacat -d /dev/video0 -g -f jpg -p 10000 -o > /opt/var/log/spcacat.log

As you can see, I write my log on the /opt location, meaning that I write it on an external storage device. It is NOT recommended to write the output log in the falsh, as it will wear out with all the writing. If you do not have an external storage device attached, I recommend that you write the log (the > /opt/var/log/spcacat.log statement) and the image itselves, to /tmp

To make the script run at startup, you can place it in /opt/www and make a S97webcam like:
cp imagesnap.sh /opt/www
chmod +x /opt/www/imagesnap.sh
echo "/opt/www/imagesnap.sh &" > /etc/init.d/S97webcam
chmod +x /etc/init.d/S97webcam

Now at boot time you will have your webcam create the image /opt/www/SpcaPict.jpg every 10 seconds.
To access the file, I have made a small html page (/opt/www/webcam.html) :

<html><head>
<script language="JavaScript">
<!--
function refreshIt() {
   if (!document.images) return;
      document.images['SpcaPic'].src = 'SpcaPict.jpg?' + Math.random();
      setTimeout('refreshIt()',10000); // refresh every timeout/1000 secs
 }
//-->
</script>
</head>
<body onLoad=" setTimeout('refreshIt()',5000)">
<br><br><br>
<center>
<img src="SpcaPict.jpg" name="SpcaPic">
<br>
Images refreshed every 10 seconds.
</center>
</body></html>
