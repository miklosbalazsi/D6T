http://sdcc.sourceforge.net/doc/sdccman.pdf

https://readthedocs.org/projects/pyserial/downloads/pdf/latest/  
https://pyserial.readthedocs.io/en/latest/shortintro.html

``` python
miklos@raspberrypi ~ $ python3

>>> import serial
>>> usb1 = serial.serial_for_url('spy:///dev/ttyUSB1?file=usb1.txt', timeout=1)
>>> usb1.baudrate = 115200
>>> usb1.write('\xfe\x01\x01\xff')
4
>>> usb1.readline()
'\xfb\x00'
>>> 

```
E18-PCB to CC-Debugger 

![CC-Debugger PinOut](https://www.waveshare.com/img/devkit/CC-Debugger/CC-Debugger-JTAG-Header.jpg)
![E18]()

E18           CC-Debugger  
Vcc           -> 9    
GND           -> 1  
DD (P2.1)     -> 4   
DC            -> 3  
RST           -> 7  


