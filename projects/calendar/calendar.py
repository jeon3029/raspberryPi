from PIL import Image, ImageDraw, ImageFont
import time
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
import RPi.GPIO as GPIO
from datetime import date
from datetime import datetime
#from datetime import time
RST,DC,SPI_PORT,SPI_DEVICE=24,25,0,0
#predefine
img = Image.new('1', (128,64),0)
draw = ImageDraw.Draw(img)
font = ImageFont.truetype("./nanum.ttf",15)
#display define
oled = Adafruit_SSD1306.SSD1306_128_64(rst=RST,dc=DC,spi=SPI.SpiDev(SPI_PORT,SPI_DEVICE,max_speed_hz=8000000))
oled.begin()
oled.clear()

#switch input
GPIO.setmode(GPIO.BCM)
SW=17
GPIO.setup(SW, GPIO.IN, pull_up_down = GPIO.PUD_UP)
flag = 0
def switchPressed(channel):
	global flag
	if flag == 0:
		flag = 1
	else:
		flag = 0
	print("switch pressed")
#bouncetime for not detect switch twice for one pressed
GPIO.add_event_detect(SW, GPIO.FALLING, callback = switchPressed, bouncetime = 200)
try:
	while True:
		img = Image.new('1', (128,64),0)
		img2 = Image.new('1', (128,64),0)
#		box = (0,0,64,64)
#region = img.crop(box)
#		region = region.transpose(Image.ROTATE_90)
#		img.paste(region,box)
		draw = ImageDraw.Draw(img)
		draw2 = ImageDraw.Draw(img2)
		font0 = ImageFont.truetype("./chelsea.ttf",13)
		font1 = ImageFont.truetype("./nanum.ttf",16)
		font2 = ImageFont.truetype("./nanum.ttf",13)
		#print calendar or time
		if flag==0:
			text ="Calendar"
			print(text)
			draw.text( (0,0),text,font=font0,fill=1)  
		else:
			text = "Time"
			print(text)
			draw.text( (0,0),text,font=font0,fill=1)  

		if flag == 0:
			date = date.today()
			text = date.strftime("%Y년")
			print(text)
			draw.text( (0,45),text,font=font1,fill=1)  
			
			text = date.strftime("%m월 %d일")
			print(text)
			draw2.text( (0,5),text,font=font2,fill=1)  
		else:
			date = datetime.now()
			ap = ""
			hour = int(date.strftime("%H"));
			if hour >= 12:
				hour -=12
				ap = "PM"
			else:
				ap = "AM"
			text = "{0} {1}시".format(ap,hour)
			print(text)
			draw.text( (0,45),text,font=font1,fill=1)  
			
			text = date.strftime("%M분 %S초")
			print(text)
			draw2.text( (0,5),text,font=font2,fill=1)  
		oled.clear()
		box = (0,0,64,64)
		region = img.crop(box)
		region = region.transpose(Image.ROTATE_90)
		img.paste(region,box)
		draw = ImageDraw.Draw(img)
		
		region2 = img2.crop(box)
		region2 = region2.transpose(Image.ROTATE_90)
		box2 = (64,0,128,64)
		img.paste(region2,box2)
		oled.image(img)
		oled.display()
#time.sleep(0.5)
except KeyboardInterrupt:
	print("interupted")
finally:
	oled.clear()
	oled.display()
	GPIO.cleanup()

	
