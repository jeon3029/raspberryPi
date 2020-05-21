import serial
port= serial.Serial('/dev/ttyS0',115200)

while True:
	str = "\r\nHello Serial:"
	port.write(bytes(str.encode()))
	rcv = port.read(10)
	port.write("\r\nReceived:"+repr(rcv))

