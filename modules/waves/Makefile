# makefile
TARGET = waves
CC = gcc
LDFLAGS = -lwiringPi

all : waves

waves : waves.c
	$(CC) $(LDFLAGS) -o $@ $^

clean :
	$(RM) $(TARGET) 
