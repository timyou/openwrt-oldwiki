'''zt8qmwz''' (time of last update: [[DateTime(2005-10-13T17:41:52Z)]])

Hello, world! This page will contain my correspondence with
hairydairymaid (lightbulb) - I asked for his help in debricking
a TI AR7 based router. If everything goes well, hairydairymaid
will write an AR7 compatible debrick utility.

----
'''hairydairymaid'''  (time of last update: [[DateTime(2005-10-13T21:17:00Z)]])

zt8qmwz, got your link and reading over the couple things I asked
about.  The CHIP ID CODE you sent ... CHIP ID: 00000000000000000001000000001111 (0000100F)
looks really fishy to me.  That *might* be real, but it is also remotely possible the
TI AR7 chip has a broken CHIP ID (there have been some chips in the past that way);
however, I would triple check the JTAG cabling and make sure it is connected correctly
for a standard 14-pin JTAG cable pinout on the board end of the cable.  In order to
write a debricker for Non-DMA capable units the EJTAG 2.5/2.6 PrAcc method will need
to be employed.  I need to work up some MIPS assembler that will run on the debug
hosted memory in the EJTAG debugging portion of the chip in order to "run" the needed reads
and writes to memory (i.e. - for flash reads/writes).  The PrAcc routines have to "feed"
in MIPS instructions over EJTAG in order for the debugging unit to actually execute
those instructions and they have to be formed in such a way as to meaningfully run code that
will read and write the desired regions.  This is not as easy as DMA access; however, it is doable.
zt8qmwz - please triple check JTAG wiring there, especially since I am doing this blind without
any equipment in front of me.  In the meantime, I'll start on the MIPS instructions needed for
this little exercise.

----
'''zt8qmwz''' (time of last update: [[DateTime(2005-10-14T19:54:47Z)]])

hairydairymaid,

I checked the JTAG cable with a multimeter twice, and it looks like
the JTAG cable is okay. Just to confirm, here's how the JTAG cable
is wired:

{{{
Parallel Port               JTAG
-------------              -------
02 D0         <--100ohm--> 03 TDI
03 D1         <--100ohm--> 09 TCK
04 D2         <--100ohm--> 07 TMS
13 ^Select    <--100ohm--> 05 TDO

20 GND        <----+-----> 02 GND
25 GND        <----/

              /--100ohm--> 01 TRST
              \----------> 14 VIO
}}}

Are there other non-PrAcc-dependent EJTAG commands which can be used
to check the JTAG connection? For example, is it possible to learn the
amount of RAM via EJTAG? A few simple query commands should be enough
for checking the JTAG connection.

I couldn't completely understand what you are going to do. Is the
following correct? You are going to write a MIPS program which will
run in the router's memory (set aside for debugging). This program is
going to interpret the commands (which you'll devise, I guess) that
are sent over the JTAG cable. Then, the program will run the appropriate
code (flash read/write) and return the resulting data via the JTAG cable.
(I know, I am lost.)

-- zt8qmwz [[DateTime(2005-10-14T19:54:47Z)]]

----

'''hairydairymaid'''  (time of last update: [[DateTime(2005-10-14T20:00:00Z)]])

There are some other ways to utilize basic JTAG functions to detemine to validity of the JTAG cabling; however, in the software you have there are not really those facilities.  There are no inherent JTAG commands to view the amount of RAM or anything like that.  Things are not at a high level at all.  Think of Data and Address lines and toggling those in such a fashion as to form some valid instructions to force on the bus for the processor to execute.

You are kinda on track with the interpretation of how things might work in a PrAcc type access.  What really happens is this:  

The EJTAG block (when using NON-DMA access) can initiate on-chip peripheral transfers as a SLAVE UNIT connected to the on-chip bus. The MIPS CPU can then execute code taken from the EJTAG Probe and it can access data (via load or store) which is located on the EJTAG Probe. This occurs in a serial way through the EJTAG interface: the core can thus execute instructions e.g. debug monitor code, without occupying the user's memory.

Well, since I don't have any AR7 based unit to use for this, I am writing PrAcc routines against a WRT54Gv2.0 (instead of the DMA that I already did) just as "something" to use.  I have been able to successfully get "Word Size Reads" working as expected.  I have started the "Word Size Writes" and will follow with half-word variants (needed for flash chip routines).  Let me tell you... if you thought the debrick utility was slow using parallel JTAG and EJTAG 2.0 DMA reads/writes... grab War and Peace, take a vacation, grow older, whatever!  I successfully read out the CFE bootloader area (256K) using PrAcc routines and it took about 20-25 minutes.  With DMA it is a good deal faster.  Unfortunately, many MIPS processors only support the newer EJTAG 2.5/2.6 debug units and thus no DMA support. (at least Broadcom was good for something on the bcm47xx series chips!)

-- hairydairymaid

----

'''zt8qmwz''' (time of last update: [[DateTime(2005-10-16T12:12:25Z)]])

hairydairymaid,

I have written a simple patch for the debrick utility version 4.1.
With this patch, the EJTAG features that are implemented in the processor are printed.
You probably know about IMPCODE. (If not, it is explained in the EJTAG 2.6 specification document by MIPS.)
The bad news is that all zeroes are printed for my board.
Can you let me know what gets printed for your (Linksys) board after you apply this patch?

Here's the patch...

{{{
diff -u debrick.orig/wrt54g.c debrick/wrt54g.c
--- debrick.orig/wrt54g.c	2005-10-15 12:00:00.000000000 +0000
+++ debrick/wrt54g.c	2005-10-15 12:00:00.000000000 +0000
@@ -73,6 +73,8 @@
 
 static unsigned int ctrl_reg;
 
+static unsigned int id;
+
 int pfd;
 int instruction_length;
 int issue_reset      = 1;
@@ -584,10 +586,87 @@
     ctrl_reg &= 0x00FFFE7F&~(DLOCK|TIF|SYNC|DMAACC|DRWN|DSTRT|PRRST|PERRST|JTAGBRK);
 }
 
+void check_ejtag_features() {
+    /* Taken from the EJTAG 2.6 Specification document by MIPS
+     *
+     * All bits are read only...
+     *
+     * Bits 31:29   EJTAGver: EJTAG version
+     *              0: version 1 and 2.0
+     *              1: version 2.5
+     *              2: version 2.6
+     *              3-7: reserved
+     *
+     * Bit 28       R4k/R3k: R4k or R3k priviledged environment
+     *              0: R4k priviledged environment
+     *              1: R3k priviledged environment
+     *
+     * Bit 24       DINTsup: Support for DINT signal from the probe
+     *              0: not supported
+     *              1: supported (DINT can be used to cause a debug interrupt)
+     *
+     * Bits 22:21   ASIDsize: Size of the ASID field
+     *              0: No ASID
+     *              1: 6 bit ASID
+     *              2: 8 bit ASID
+     *              3: Reserved
+     *
+     * Bit 16       MIPS16: MIPS16 ASE support 
+     *              0: not supported
+     *              1: MIPS16 is supported
+     *
+     * Bit 14:      NoDMA: Indicates *No* EJTAG DMA support
+     *              0: reserved
+     *              1: *No* EJTAG DMA support
+     *              
+     *              (Appendix D.9 informs that an DMA-like optional
+     *              feature is considered for future EJTAG versions.)
+     *
+     * Bit 0:       MIPS32/64: whether the processor is 32bit or 64bit
+     *              0: 32bit processor
+     *              1: 64bit processor
+     *
+     * Remaining bits: ignored on write, returns 0 on read
+     */
+
+    unsigned int features, tmp;
+    
+    test_reset();
+    // instruction_length was set by the call to chip_detect()
+    set_instr(INSTR_IMPCODE);
+    features = ReadData();
+    
+    printf("\nChecking for implemented EJTAG features...\n"); 
+    printf("IMPCODE: "); 
+    ShowData(features);
+  
+    // EJTAG Version 
+    tmp = (features >> 29) & 7;
+    printf("    EJTAG Version: ");
+    if (tmp == 0)
+        printf("1 or 2.0\n");
+    else if (tmp == 1)
+        printf("2.5\n");
+    else if (tmp == 2)
+        printf("2.6\n");
+    else
+        printf("Unknown (%d is a reserved value)\n", tmp);
+
+    // EJTAG DMA Support
+    tmp = features & (1u << 14);
+    printf("    EJTAG DMA Support: ");
+    if (tmp == 0)
+        printf("Unknown (%d is a reserved value)\n", tmp);
+    else
+        printf("No\n");
+        
+    printf("\n");
+}
+
 
 void chip_detect(void)
 {
-    unsigned int id;
+    //unsigned int id;
 
     printf("\nProbing bus...\n\n");
 
@@ -638,6 +717,17 @@
         ShowData(id);  printf("*** Found a Broadcom BCM5352 Rev 1 chip ***\n\n");
         return;
     }
+    
+    // Special case for (buggy?) TI AR7 chip... 
+    test_reset();
+    instruction_length = 8;
+    set_instr(INSTR_IDCODE);
+    id = ReadData();
+    if (id == 0x0000100F)
+    {
+        ShowData(id);  printf("*** Found a TI AR7 chip ***\n\n");
+        return;
+    }
 
     ShowData(id);  printf("*** Unrecognized Chip ***\n");
 
@@ -1270,6 +1360,12 @@
 
     // Detect & Initialize
     chip_detect();
+    check_ejtag_features();
+
+    if (id == 0x0000100F) {
+        chip_shutdown();
+        exit(0);
+    }
 
     // For Good Measure
     test_reset();
diff -u debrick.orig/wrt54g.h debrick/wrt54g.h
--- debrick.orig/wrt54g.h	2005-10-15 12:00:00.000000000 +0000
+++ debrick/wrt54g.h	2005-10-15 12:00:00.000000000 +0000
@@ -76,6 +76,7 @@
 
 // --- Some BCM47XX Instructions ---
 #define INSTR_IDCODE    0x01
+#define INSTR_IMPCODE   0x03
 #define INSTR_EXTEST    0x00
 #define INSTR_SAMPLE    0x02
 #define INSTR_PRELOAD   0x02
@@ -162,6 +163,7 @@
 void WriteData(unsigned int in_data);
 void capture_dr(void);
 void capture_ir(void);
+void check_ejtag_features(void);
 void chip_detect(void);
 void chip_shutdown(void);
 void clockin(int tms, int tdi);
}}}

Oh, and by the way, (as I mentioned in the patch,) it looks like DMA is coming back
as an optional feature in future EJTAG versions. And regarding the difference of
speed between PrAcc and DMA methods, my guess is that most people would probably
prefer *some* (even slow) way of recovering bricked routers (based on recent MIPS
processors) rather than dumping them in the garbage. No matter how slow PrAcc routines
are, it is nice to hear good news from your side.

Regards,

-- ["zt8qmwz"] [[DateTime(2005-10-16T12:12:25Z)]]

----

'''hairydairymaid'''  (time of last update: [[DateTime(2005-10-16T11:39:00Z)]])

It sure appears your JTAG cabling needs a little adjustment somewhere.  I suspected the ID CODE of 0x100f looked very fishy.  It seems at the moment that is not talking properly.  I'll look at the mappings for you in a bit.

On another note... the code you provided is close and I did cut and paste into my program here for comparison.  The only thing I changed was the part below:

{{{
    // EJTAG DMA Support
    tmp = features & (1u << 14);
    printf("    EJTAG DMA Support: ");
    if (tmp == 0)
        //printf("Unknown (%d is a reserved value)\n", tmp);
        printf("Yes\n", tmp);
    else
        printf("No\n");
}}}

Since bit 14 of the IMPLEMENTATION register denoted DMA support (0 = yes)(1 = no).  In the 2.5 and 2.6 standards they just call it "reserved" (since they don't implement DMA in those versions).  I have a much more detailed routine that does that which is helpful, but not needed when things are really working.  Now that PrAcc routines might be in there - I'll use the "DMA Support" bit as the driver.

Here are the results I get against a Linksys WRT54Gv2.0 board:

{{{
====================================
WRT54G/GS EJTAG DeBrick Utility v4.3
====================================


Probing bus...

CHIP ID: 00010100011100010010000101111111 (1471217F)
*** Found a Broadcom BCM4712 Rev 1 CPU chip ***


Checking for implemented EJTAG features...
IMPCODE: 00000000100000000000100100000100 (00800904)
    EJTAG Version: 1 or 2.0
    EJTAG DMA Support: Yes

Issuing Processor / Peripheral Reset...
Done

Enabling Memory Writes...
Clearing Watchdog...
Halting Processor...
Probing Flash...
}}}

As you can see it does indeed get the proper data... which is another indicator we need to get your JTAG cabling correct.  It may be some needed pullups or pulldowns be in place or removed.  Or it could be just crossed lines. Or it could be solder not making good contact.  That is what we need to focus on at the moment.

I have added all the PrAcc rotuines for word and half word reads and writes.  I can fully read and write to Intel flash chips here using PrAcc routines.  I still need to add a little code for the AMD and SST style flash chips.  This is needed since the DMA effectively use byte lanes when the sending the flash commands and PrAcc routines need to be ever so slightly different.  Also need to do some code cleanup.  I have hand tweaked some of the MIPS assembly instructions to reduce the number needed to be sent to a minimum and that has helped speedwise of the PrAcc routines; however they are still slower than DMA routines (to be expected).

If you can focus on getting your JTAG cable working and reading what looks like a valid CHIP ID CODE that will be a big help.  In trying - try adjusting the instruction_length variable from say a length 3 up thru 10 (valid ranges are really 5 to 8 if I recall), and recompile and try each value checking the CHIP ID CODE for something useful.

-- hairydairymaid

----

'''zt8qmwz''' (time of last update: [[DateTime(2005-10-17T08:13:08Z)]])

hairydairymaid,

I have good news! I followed your advice and tried instruction lengths other 
than 8 bits. And guess what, this router (or TI AR7, rather) uses an 
instruction length of 5! I have no idea why the chip ID reads succeeded before...
It was probably because of the detection code for BCM4702 Chip which also uses an 
instruction length of 5.

Here is the output of the hacked wrt54g:
(Edit: I mean the debrick program, not the router!)

{{{
====================================
WRT54G/GS EJTAG DeBrick Utility v4.1
====================================


Probing bus...

Instruction length: 5
CHIP ID: 00000000000000000001000000001111 (0000100F)

Checking for implemented EJTAG features...
IMPCODE: 01000001010000000100000000000000 (41404000)
    EJTAG Version: 2.6
    EJTAG DMA Support: No
}}}


I feel happy now!

Regards,

-- ["zt8qmwz"] [[DateTime(2005-10-17T08:13:08Z)]]

Note: This should also confirm the chip ID of TI AR7.

----
'''AlecV''' (time of last update: [[DateTime(2005-10-22T04:39:00Z)]])

Hi, All!

Try this links: [http://www.dlinkpedia.net/index.php/Jtag_su_30xT JTAG for D-Link DSL-30xT], [http://www.dlinkpedia.net/index.php/Interfaccia_JTAG JTAGInterface] (Italian, but I hope you cold understand at least some words).

The '''OCD Debugger''' works ans '''OCD Flash''' works too. BUT! You need a full WIGGLER cable, instead of your favorite "Xilix DLC parallel cable III" mage with 5 resistors... ;)

I've tested it with ADM5120 CPU (another MIPS with EJTAG 2.6) and found it working, even single Step debug works. My expiriments are descibed there: http://www.norocketscience.com/forum/topic.asp?TOPIC_ID=67
You could find my WIGGLER schematic variant there too.

I hope it helps. I have an AR7 router too and will test it ASAP.

----

'''hairydairymaid'''  (time of last update: [[DateTime(2005-11-05T12:00:00Z)]])

The PrAcc programing for the debrick utility has been done for a while and is working as expected.  All operations are working as expected on the test boards I have here... which, unfortunately, none are TI AR7 based boards... so we'll need some testing done elsewhere.

zt8qmwz, I have sent you a version to test out for me and we'll see how that goes.  If all goes well then I'll probably be set to go ahead release a new version of the debrick utility very shortly.

Cheers,
-hairydairymaid

----
CategoryHomepage
