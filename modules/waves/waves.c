#include<unistd.h>
#include<time.h>
#include<sys/time.h>
#include<stdio.h>
#include<stdlib.h>
#include<stdint.h>
#include<sys/resource.h>
#include<wiringPi.h>

#define GPIO_TRIG 4
#define GPIO_ECHO 5

int main(void){
	unsigned int start,stop;
	int loop=0,count;
	float f;

	printf("starting hc-sr04 test \n");
	int status=wiringPiSetup();
	if(status!=0){
		printf("fail to wiringpi setup\n");
		return 0;
	}
	pinMode(GPIO_TRIG,OUTPUT);
	pinMode(GPIO_ECHO,INPUT);

	digitalWrite(GPIO_TRIG,LOW);
	delay(500);
	printf("st loop\n");
	while(1){
		printf("measure distance... once per 2 seconds\n");
		delay(2000);
		digitalWrite(GPIO_TRIG,HIGH);
		delayMicroseconds(10);
		digitalWrite(GPIO_TRIG,LOW);
		while(digitalRead(GPIO_ECHO) == LOW){
			//printf("loop1\n");
		}
		start=micros();
		while(digitalRead(GPIO_ECHO) == HIGH){
			//printf("loop2\n");
		}
		stop=micros();
		double dis = 34209*(stop-start)/2000000.0;
		printf("dis : %fcm\n",dis);
		//if(loop++ == 100)break;
	}
	return 0;
}
