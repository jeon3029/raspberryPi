# makefile
TARGET = blink_sw
CC = gcc
LDFLAGS = -lwiringPi

all : blink_sw

blink : blink_sw.c
	$(CC) $(LDFLAGS) -o $@ $^

clean :
	$(RM) $(TARGET) core
