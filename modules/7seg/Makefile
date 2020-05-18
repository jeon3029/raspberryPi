# makefile
TARGET = fnd
CC = gcc
LDFLAGS = -lwiringPi

all : fnd

fnd : wiringfnd.c
	$(CC) $(LDFLAGS) -o $@ $^

clean :
	$(RM) $(TARGET) 
