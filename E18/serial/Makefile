SHELL = /bin/sh
CC = sdcc

all: clean make.hex

clean:
	-rm -f *.ihx *.lk *.lst *.map *.mem *.rel *.rst *.sym *.hex *.asm

main.ihx:
	sdcc main.c

make.hex: main.ihx
	packihx main.ihx > main.hex
	
