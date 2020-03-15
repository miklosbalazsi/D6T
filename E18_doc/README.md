``` python
miklos@raspberrypi ~ $ python
Python 2.7.13 (default, Sep 26 2018, 18:42:22) 
[GCC 6.3.0 20170516] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> import serial
>>> ser = serial.Serials('/dev/ttyUSB0')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'module' object has no attribute 'Serials'
>>> ser = serial.Serial('/dev/ttyUSB0')
>>> ser.name
'/dev/ttyUSB0'
>>> ser.baudrate = 115200
>>> ser.get_settings()
{'parity': 'N', 'baudrate': 115200, 'bytesize': 8, 'xonxoff': False, 'rtscts': False, 'timeout': None, 'inter_byte_timeout': None, 'stopbits': 1, 'dsrdtr': False, 'write_timeout': None}
>>> ser.write('alma')
4
>>> ser.readline()


^CTraceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/lib/python2.7/dist-packages/serial/serialposix.py", line 472, in read
    ready, _, _ = select.select([self.fd, self.pipe_abort_read_r], [], [], timeout.time_left())
KeyboardInterrupt
>>> ser.timeout= 1 
>>> ser.readline()
''
>>> ser.write("FE0101FF")
8
>>> ser.readline()
'\xf7\xff'
>>> 
>>> 
>>> 
>>> 
>>> 
>>> s = serial.serial_for_url('spy:///dev/ttyUSB1?file=test.txt', timeout=1)
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> usb1 = serial.serial_for_url('spy:///dev/ttyUSB1?file=usb1.txt', timeout=1)
>>> usb1.baudrate = 115200
>>> usb1.write("FE0101FF")
8
>>> usb1.readline()
'\xf7\xff'
>>> 
```