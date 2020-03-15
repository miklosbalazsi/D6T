#!/usr/bin/python

import serial
import serial.tools.list_ports

serialPortList = serial.tools.list_ports.comports()

for serialPortList in serialPort:
    print("Name : " + serialPort.name)
    print("hwid : " + serialPort.hwid)
