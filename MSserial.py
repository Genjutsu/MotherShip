#!/usr/bin/python
#Serial Intreface For Radar
import serial
import time
ser = serial.Serial('/dev/tty.usbmodem1411',230500,timeout=1)
def readSerial():
	 return ser.readline()
counter = 0
start_time = time.time()
while True:
	counter+=1
	print readSerial()
	#print counter
		

