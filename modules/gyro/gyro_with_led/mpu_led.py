import RPi.GPIO as GPIO
from smbus2 import SMBus
from bitstring import Bits
import math
import time
bus = SMBus(1)
DEV_ADDR = 0x68
register_gyro_xout_h = 0x43
register_gyro_yout_h = 0x45
register_gyro_zout_h = 0x47

sensitive_gyro = 131.0

register_accel_xout_h = 0x3B
register_accel_yout_h = 0x3D
register_accel_zout_h = 0x3F

sensitive_accel = 16384.0


# led gpio channel 

channel1 = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel1,GPIO.OUT)

channel2 = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel2,GPIO.OUT)

def read_data(register):
	high = bus.read_byte_data(DEV_ADDR,register)
	low = bus.read_byte_data(DEV_ADDR,register+1)
	val = (high << 8) + low
	return val

def twocomplements(val):
	s = Bits(uint=val,length=16)
	return s.int
def gyro_dps(val):
	return twocomplements(val)/sensitive_gyro
def accel_g(val):
	return twocomplements(val)/sensitive_accel
def dist(a,b):
	return math.sqrt((a*a)+(b*b))
def get_x_rotation(x,y,z):
	radians = math.atan(x/dist(y,z))
	return radians
def get_y_rotation(x,y,z):
	radians = math.atan(y/dist(x,z))
	return radians
def get_z_rotation(x,y,z):
	radians = math.atan(z/dist(x,y))
	return radians
bus.write_byte_data(DEV_ADDR,0x6B,0b00000000)
try:
	cnt = 0
	bX=bY=bZ = 0
	while True:
		x = read_data(register_accel_xout_h)
		y = read_data(register_accel_yout_h)
		z = read_data(register_accel_zout_h)
		aX = get_x_rotation(accel_g(x),accel_g(y),accel_g(z))
		aY = get_y_rotation(accel_g(x),accel_g(y),accel_g(z))
		aZ = get_z_rotation(accel_g(x),accel_g(y),accel_g(z))
		data = str(aX) + ' , ' + str(aY) + ' , ' + str(aZ) + '$'
		print(data)
		if cnt == 0:
			cnt += 1
			bX = aX
			bY = aY
			bZ = aZ
			continue
		else:
			if abs(aX - bX) > 0.2:
				GPIO.output(channel1,GPIO.HIGH)
			else:
				GPIO.output(channel1,GPIO.LOW)
			if abs(aY - bY) > 0.2:
				GPIO.output(channel2,GPIO.HIGH)
			else:
				GPIO.output(channel2,GPIO.LOW)	
			bX = aX
			bY = aY
			bZ = aZ
			time.sleep(0.2)
		
except KeyboardInterrupt:
	print("\nInterrupted!")
except:
	print("\nClosing socket")
finally:
	bus.close()
	GPIO.cleanup()

