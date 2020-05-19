#include <stdio.h>
#include <stdlib.h>
#include <wiringPi.h>
#define SW1 7 //gpio 4 for led control
#define SW2 0 //gpio 17 for quit program
#define LED 1 //gpio 18
int switch2Control(){
	int i;
	pinMode(SW1,INPUT);
	pinMode(SW2,INPUT);
	pinMode(LED,OUTPUT);
	for(;;){
		if(digitalRead(SW2) == HIGH){
			printf("switch2 pressed... quit program.\n");
			exit(0);
		}
		if(digitalRead(SW1) == LOW){
			printf("switch1 not pressed... led on.\n");
			digitalWrite(LED,HIGH);
			delay(500);
			digitalWrite(LED,LOW);
		}
		else{
			printf("switch1 pressed... led off.\n");
			delay(500);
		}
		
		delay(10);
	}
	return 0;
}
int main (int argc, char **argv) {
	printf ("Raspberry Pi blink\n") ;
	if (wiringPiSetup () == -1)
		return 1 ;
	switch2Control();
	return 0 ;
}
