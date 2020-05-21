# makefile
TARGET = motor
CC = gcc
LDFLAGS = -lwiringPi

all : motor

motor : motor.c
	$(CC) $(LDFLAGS) -o $@ $^

clean :
	$(RM) $(TARGET) 
