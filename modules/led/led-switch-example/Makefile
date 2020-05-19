# makefile
TARGET = blink_sw2
CC = gcc
LDFLAGS = -lwiringPi

all : blink_sw2

blink : blink_sw2.c
	$(CC) $(LDFLAGS) -o $@ $^

clean :
	$(RM) $(TARGET) 
