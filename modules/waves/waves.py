import RPi.GPIO as GPIO
import time

GPIO_TRIG=23
GPIO_ECHO=24
GPIO.setmode(GPIO.BCM)
print("distance meassurement in progress")

GPIO.setup(GPIO_TRIG,GPIO.OUT)
GPIO.setup(GPIO_ECHO,GPIO.IN)
GPIO.output(GPIO_TRIG,False)

print("waiting for sensor to settle")
time.sleep(2)
GPIO.output(GPIO_TRIG,True)
time.sleep(0.00001)

GPIO.output(GPIO_TRIG,False)
while True:
	while GPIO.input(GPIO_ECHO)==0:
		pulse_start=time.time()
	while GPIO.input(GPIO_ECHO)==1:
		pulse_end=time.time()
	pulse_duration = pulse_end - pulse_start
	distance=pulse_duration*17150
	distance = round(distance,2)
	print("distance : ",distance,"cm")
	time.sleep(1)
	GPIO.output(GPIO_TRIG,False)

GPIO.cleanup()
