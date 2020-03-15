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
