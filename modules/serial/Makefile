# makefile
TARGET = serial
CC = gcc
LDFLAGS = -lwiringPi

all : serial

serial : serial.c
	$(CC) $(LDFLAGS) -o $@ $^

clean :
	$(RM) $(TARGET) 
