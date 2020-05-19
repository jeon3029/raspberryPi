import RPi.GPIO as GPIO
import time

LED,SW = 17,4
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED,GPIO.OUT)
GPIO.setup(SW,GPIO.IN)

print("press the button")
for i in range (30):
	if GPIO.input(SW) == GPIO.HIGH:
		print("button pressed")
		GPIO.output(LED,True)
		time.sleep(1)
		print("press the button(c-c to exit)")
	else:
		print("button not pressed")
		GPIO.output(LED,False)
		time.sleep(1)
GPIO.cleanup()
