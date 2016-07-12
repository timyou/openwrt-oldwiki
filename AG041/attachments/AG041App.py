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
		print "%d to go" % (length)
			
		# my firmware will only do 0x500 byte read
		lenToRead = min(0x500, length);
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
		time.sleep(0.2);
		str = comm.read(comm.inWaiting());
		
		# notice the weird line breaks
		lines = str.split('\n\r');

		# first two lines are an echo +  blank line
		# last is CONS>
		for line in lines[2:len(lines)-1]:
			strValList = re.findall(r'([\dabcdef]+)', line);
			
			# the first value is the offset, which we skip
			for strVal in strValList[1:len(strValList)]:
				for valOffs in range(6, (3-bytesToRead)*2, -2):
					a.append(int(strVal[valOffs:valOffs+2], 16));
		
		length = length - lenToRead;
		offs = offs + lenToRead;

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
	sz = ((sz[1] << 8) + sz[0]) << 10;
	return readMemory(comm, base, sz);
	



import serial;
import time;
import re;
import array;

comm = connect(0)
#testReadMemory(comm);
buff = readBinFile(comm, 0);
comm.close();

f = file("bong.bin", "w", -1);
buff.tofile(f);
f.close();
