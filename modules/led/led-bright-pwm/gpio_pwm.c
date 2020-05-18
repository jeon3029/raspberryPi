#include <stdio.h>
#include <stdlib.h>
#include <wiringPi.h>
#define SW 7
#define LED 0
#define LED2 1
int pwmControl(){
	int i;
	pinMode(LED2,PWM_OUTPUT);
	digitalWrite(LED2,LOW);
	for(;;){
		int bright;
		for(bright = 0;bright<1024;++bright){
			pwmWrite(LED2,bright);
			delay(5);
		}
		for(bright = 1023;bright>=0;--bright){
			pwmWrite(LED2,bright);
			delay(5);
		}
		
	}
	return 0;
}
int main (int argc, char **argv) {
	printf ("Raspberry Pi blink\n") ;
	if (wiringPiSetup () == -1)
		return 1 ;
	pwmControl();
	return 0 ;
}
