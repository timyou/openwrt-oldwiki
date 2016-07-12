'''Linksys WRT54G'''

=== Hardware versions ===

The WRT54GC is the 'Compact' version of the WRT54G. It has a built-in antenna as well as an SMA antenna connector instead of RP-TNC. 


==== WRT54GC v? ====
 * Platform:  
 * CPU:
 * Ram:
 * Radio:
 * Power: Input 3.3V DC 2.0A
 * External antenna connector: SMA

Chips (from the FCC Internal photos)
 * Marvel 88E6060 Fast Ethernet switch [http://www.marvell.com/products/switching/linkstreet/88E6060.jsp Manufacturer Product Page]
 * Etrontech EM636165TS 2MB chips (two on board) [http://www.etron.com/img/pdf/SDRAM/16Mb/Em636165(Rev%201.8).pdf Manufacturer Product Page (PDF)]
 * Macronix LV29800BTTC-70 FLASH Low Voltage 8MB Rev B Top Boot TSOP Commercial 70ns [http://www.macronix.com/QuickPlace/hq/PageLibrary48256F5500439ED0.nsf/h_CE4C9490FDF4280B48256F550043C6D8/57C05F76471CEE8F48256FCD000320A1/$File/MX29LV800CT-B-1.1.pdf?OpenElement Manufacturer Product Page (PDF)]

[https://gullfoss2.fcc.gov/prod/oet/forms/blobs/retrieve.cgi?attachment_id=507960&native_or_pdf=pdf FCC Internal photo (PDF)]

=== Manufacturer Information ===
[http://www.linksys.com/products/product.asp?grid=33&scid=35&prid=679 Linksys WRT54GC Page]

=== FCC Information ===
[https://gullfoss2.fcc.gov/prod/oet/cf/eas/reports/ViewExhibitReport.cfm?mode=Exhibits&RequestTimeout=500&calledFromFrame=N&application_id=305805&fcc_id='Q87-WRT54GC' FCCID Q87-WRT54GC]

=== Physical Disassembly ===
Having spent about seven hours trying to take the thing out of its case, here's what I found out:

 * There's a screw! On the back side with the rubber feet, towards the bottom of the bottom-left foot (next to the FCC and "Power: 3.3V 2A" sticker) is a small Philips-head screw.
 * The rest of the case is held by plastic tabs. They come apart with some force, but be gentle: the plastic feels weak.
 * Once the back cover is off, you're almost there. There's two screws that hold the PCB on, also Philips-head. The sticker on the side holds down the ethernet ports, so it must (sadly) be removed. Also, don't forget to disconnect the external antenna connector by removing the nut, and then the antenna selector switch by just pulling it out of the board.
 * Smile and be happy.

More stuff about the router:

 * The chip that's unrecognizable in the FCC photos has been identified as Macronix FLASH, 8MB. See the full PDF at [http://www.macronix.com/QuickPlace/hq/PageLibrary48256F5500439ED0.nsf/h_CE4C9490FDF4280B48256F550043C6D8/57C05F76471CEE8F48256FCD000320A1/$File/MX29LV800CT-B-1.1.pdf?OpenElement here (PDF)]. Very detailed. Thank you, Macronix. Now if only you were easier to find... P.S. Thanks to <LostFrog> for ID'ing manufacturer.
 * The power LED actually has two LEDs in one package: an orange and a green.
 * There doesn't appear to be JTAG, but there is a solderpad area. I'll test it for serial, but for now is classified as "unknown". Pin 11 seems to have some plusing output by the piezo buzzer test. I'll dig up some MAX233's and see what it says.

Pictures and more information available on my website: [http://yasha.okshtein.net/wrt54gc/ http://yasha.okshtein.net/wrt54gc/].

I really like this device: it's small and uses only 3.3v. I'd really love to get OpenWrt on it, possibly for a future version of my [http://yasha.okshtein.net/wrt54g Wifi Car]. Any takers? The router is quite cheap at $39 (i got it for $29 on Black Friday), but at that price, most users would opt for other, fully supported, routers.

Little test : 
chtitux@localhost ~/src $ nmap 192.168.2.1  -p 80 -A
Starting Nmap 4.01 ( http://www.insecure.org/nmap/ ) at 2006-06-10 19:15 CEST
Interesting ports on 192.168.2.1:
PORT   STATE SERVICE VERSION
80/tcp open  http?
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at http://www.insecure.org/cgi-bin/servicefp-submit.cgi :
SF-Port80-TCP:V=4.01%I=7%D=6/10%Time=448AFE26%P=i686-pc-linux-gnu%r(GetReq
SF:uest,8A,"HTTP/1\.0\x20401\x20Unauthorized\r\nServer:\x20IP_SHARER\x20WE
SF:B\x201\.0\r\nWWW-Authenticate:\x20Basic\x20realm=\"WRT54GC\"\r\nContent
SF:-type:\x20text/html\r\n\r\n401\x20Unauthorized");


----
CategoryModel
