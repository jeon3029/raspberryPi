# makefile
TARGET = light
CC = gcc
LDFLAGS = -lwiringPi

all : light

light : light.c
	$(CC) $(LDFLAGS) -o $@ $^

clean :
	$(RM) $(TARGET) 
