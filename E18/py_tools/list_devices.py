#!/usr/bin/python

import serial
import serial.tools.list_ports

serialPortList = serial.tools.list_ports.comports()

for serialPort in serialPortList:
    print("device : " + serialPort.device)
    print("name : " + serialPort.name)
    print("description : " + serialPort.description)
    print("hwid : " + serialPort.hwid)
    print("vid : " + serialPort.vid)
    print("pid : " + serialPort.pid)
    print("serial_number : " + serialPort.serial_number)
    print("location : " + serialPort.location)
    print("manufacturer : " + serialPort.manufacturer)
    print("product : " + serialPort.product)
    print("interface : " + serialPort.interface)
    print("\n")
