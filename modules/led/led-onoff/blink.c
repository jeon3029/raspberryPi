#include <stdio.h>
#include <stdlib.h>
#include <wiringPi.h>
int main (int argc, char **argv) {
	printf ("Raspberry Pi blink\n") ;
	if (wiringPiSetup () == -1)
		return 1 ;
	int gpio = atoi(argv[1]);
	printf("gpio : %d\n",gpio);
	pinMode (gpio, OUTPUT) ;         // aka BCM_GPIO pin 17
	int i;
	for (i=0;i<10;i++) {
		digitalWrite (gpio, HIGH) ; delay (500) ;           
		digitalWrite (gpio, LOW) ; delay (500) ;
	}
	return 0 ;
}
