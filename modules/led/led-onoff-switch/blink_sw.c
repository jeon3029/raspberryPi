#include <stdio.h>
#include <stdlib.h>
#include <wiringPi.h>
#define SW 7
#define LED 0
int switchControl(){
	int i;
	pinMode(SW,INPUT);
	pinMode(LED,OUTPUT);
	for(;;){
		if(digitalRead(SW) == LOW){
			digitalWrite(LED,HIGH);
			delay(1000);
			digitalWrite(LED,LOW);
		}
		delay(10);
	}
	return 0;
}
int main (int argc, char **argv) {
	printf ("Raspberry Pi blink\n") ;
	if (wiringPiSetup () == -1)
		return 1 ;
	//printf("gpio : %d\n",gpio);
	//pinMode (gpio, OUTPUT) ;         // aka BCM_GPIO pin 17
	switchControl();
	return 0 ;
}
