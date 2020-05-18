# makefile
TARGET = gpio_pwm
CC = gcc
LDFLAGS = -lwiringPi

all : gpio_pwm

gpio_pwm : gpio_pwm.c
	$(CC) $(LDFLAGS) -o $@ $^

clean :
	$(RM) $(TARGET) 
