#!/usr/bin/python3

# E18 c2530 chip serial port
# Bus 001 Device 004: ID 1a86:7523 QinHeng Electronics HL-340 USB-Serial adapter
# Bus 001 Device 003: ID 1a86:7523 QinHeng Electronics HL-340 USB-Serial adapter
#       idVendor           0x1a86 QinHeng Electronics
#       idProduct          0x7523 HL-340 USB-Serial adapter


import serial
import serial.tools.list_ports

BAUDRATE = 115200
VID = 0x1a86  # 6790
PID = 0x7523  # 29987
VENDOR = "QinHeng Electronics"
PRODUCT = "HL-340 USB-Serial adapter"

e18_devices = []

serialPortList = serial.tools.list_ports.comports()
for serialPort in serialPortList:
    if (serialPort.vid == VID & & serialPort.pid == PID):
        print(f'Found : {serialPort.location} as a Ebyte E18 device ')
        e18_devices.append(serialPort)

        print("device : " + serialPort.device)
        print("name : " + serialPort.name)
        print("description : " + serialPort.description)
        print("hwid : " + serialPort.hwid)
        print("vid : " + str(hex(serialPort.vid)))
        print("pid : " + str(serialPort.pid))
        print("serial_number : " + serialPort.serial_number)
        print("location : " + serialPort.location)
        print("manufacturer : " + serialPort.manufacturer)
        print("product : " + serialPort.product)
        print("interface : " + serialPort.interface)
        print("\n")
