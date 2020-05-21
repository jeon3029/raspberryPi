# makefile
TARGET = waves_ex
CC = gcc
LDFLAGS = -lwiringPi

all : waves_ex

waves_ex : waves_ex.c
	$(CC) $(LDFLAGS) -o $@ $^

clean :
	$(RM) $(TARGET) 
