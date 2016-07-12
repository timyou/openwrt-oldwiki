#        Pulls firmware from linksys AG041 and saves to bong.bin
#
#		written by Andrew Beck
#
#		I don't care what you do with this file since it almost certainly
#   won't work. Try not to do bad things though - it's not nice. Whatever
#   you do, you definitely agree to take full responsibility for anything
#   that happens. And don't mention my name, I never agreed to anything.
#
#   I strongly recommend that you don't use this because it will most likely
#   break something & may possibly end civilisation as we know it. I am a
#		much better blacksmith than software writer & I'm fairly new to the whole
#   python thing. 
#
#		!! This is to be used at your own risk !!
#
#   Having said that, it did manage to download the firmware from my AG041
#   via the serial console without major incident. it's quite slow though

def connect(port):
	comm = serial.Serial(port, 115200);
	comm.write("?\r");

	time.sleep(0.5);

	comm.read(2);

	sz = comm.inWaiting();
	if (sz < 1):
		print "Device (COM$port) not ready";
		comm.close();
		die; # how to do this in python?

	comm.read(sz);

	return comm;



def readMemory(comm, offs, length):
	a = array.array("B");

	while (length > 0):
		b = array.array("B");
		print "%d to go" % (length)
			
		# my firmware will only do 0x500 byte read
		lenToRead = min(0x100, length);
		if (offs % 4):
			# if not on DWORD boundary, do first operation
			# as single DWORD read & extract what we want
			lenToRead = min(lenToRead, 4 - (offs % 4));
		elif (lenToRead % 4) and (lenToRead > 4):
			# if we are reading over a DWORD boundary, truncate
			# it to the boundary & handle the remainder separately
			lenToRead = lenToRead - (lenToRead % 4);
		
		# the number of bytes to read out of this DWORD
		bytesToRead = min(4, lenToRead);
		comm.write("mread %x %x\r" % (offs, max(4, lenToRead)));
		time.sleep(.1);
		str = comm.read(comm.inWaiting());
		# strip the echo'd command
		str = str.strip("mread %x %x\r" % (offs, max(4, lenToRead)));
		
		strValList = re.findall(r'([\dabcdef]+)', str);

		# the first value is the offset, which we skip
		for valIdx in range(0, len(strValList)):
			if (valIdx % 5):
				for valOffs in range(6, (3-bytesToRead)*2, -2):
					b.append(int(strValList[valIdx][valOffs:valOffs+2], 16));

		if (len(b) == lenToRead):
			length = length - lenToRead;
			offs = offs + lenToRead;
			a.extend(b);
		else:
			print "%d of %d" % (len(b), lenToRead);	
								
			# need to flush everything & start this one again
			time.sleep(1);			
			comm.read(comm.inWaiting());
			print "Retry at offset %d" % (offs);
		
	return a;


def testReadMemory(comm):
	arrTot = readMemory(comm, 0, 32);	
	
	a = readMemory(comm, 1, 2);
	if (a != arrTot[1:3]): print "testReadMemory";	

	a = readMemory(comm, 3, 4);	
	if (a != arrTot[3:7]): print "testReadMemory";

	a = readMemory(comm, 2, 6);	
	if (a != arrTot[2:8]): print "testReadMemory";	

	a = readMemory(comm, 2, 18);	
	if (a != arrTot[2:20]): print "testReadMemory";	

	a = readMemory(comm, 4, 16);	
	if (a != arrTot[4:20]): print "testReadMemory";	

	a = readMemory(comm, 4, 13);	
	if (a != arrTot[4:17]): print "testReadMemory";	


def readBinFile(comm, base):
	sz = readMemory(comm, base + 32, 2);
	# the size in the header specifies the number
	# of kilobytes	
	sz = ((sz[1] << 8) + sz[0]) << 10;
	return readMemory(comm, base, sz);
#	return readMemory(comm, base, 10000);
	

def usage():
	print "AG041App.py [-p<port>] [-b<base>] [fileName]"
	print "\tport:\tcomm port\tdefault: 0=COMM1"
	print "\tbase:\timage base addr\tdefault: 0x0"
	print "\tfileName:\toutput file\tdefault: code.bin"

import serial;
import time;
import re;
import array;
import sys
import getopt

try:
	opts, args = getopt.getopt(sys.argv[1:], 'p:b:')
except getopt.error, msg:
	print msg
	usage();
	sys.exit(2)

port = 0
base = 0
fileName = "code.bin"

for o, a in opts:
	if o == "-p":
		port = int(a);
	if o == "-b":
		base = int(a, 0);

if (len(args) > 1):
	usage();
	sys.exit(2)
elif (len(args) == 1):
	fileName = args[0];	

f = file(fileName, "wb", -1);
	
comm = connect(port)
#testReadMemory(comm);
buff = readBinFile(comm, base);

comm.close();

buff.tofile(f);
f.close();
