# makefile
TARGET = blink
CC = gcc
LDFLAGS = -lwiringPi

all : blink

blink : blink.c
	$(CC) $(LDFLAGS) -o $@ $^

clean :
	$(RM) $(TARGET) core
