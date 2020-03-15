#!/usr/bin/python3

# E18 c2530 chip serial port
# Bus 001 Device 004: ID 1a86:7523 QinHeng Electronics HL-340 USB-Serial adapter
# Bus 001 Device 003: ID 1a86:7523 QinHeng Electronics HL-340 USB-Serial adapter
#       idVendor           0x1a86 QinHeng Electronics
#       idProduct          0x7523 HL-340 USB-Serial adapter


import serial
import serial.tools.list_ports

BAUDRATE = 115200
TIMEOUT = 1
VID = 0x1a86  # 6790
PID = 0x7523  # 29987
VENDOR = "QinHeng Electronics"
PRODUCT = "HL-340 USB-Serial adapter"

e18_devices = []

serialPortList = serial.tools.list_ports.comports()
for serialPort in serialPortList:
    if serialPort.vid == VID and serialPort.pid == PID:
        print('Found ' + serialPort.device + ' as an Ebyte E18 device ')
        print("device : {}".format(serialPort.device))
        print("name : {}".format(serialPort.name))
        print("description : {}".format(serialPort.description))
        print("hwid : {}".format(serialPort.hwid))
        print("vid : {}".format(serialPort.vid))
        print("pid : {}".format(serialPort.pid))
        print("serial_number : {}".format(serialPort.serial_number))
        print("location : {}".format(serialPort.location))
        print("manufacturer : {}".format(serialPort.manufacturer))
        print("product : {}".format(serialPort.product))
        print("interface : {} \n".format(serialPort.interface))
        e18_devices.append(serialPort)

for dev in e18_devices:
    print("Open Serial connection to : {}\n".format(dev.device))
    ser = serial.Serial(dev.device)
    ser.baudrate = BAUDRATE
    ser.timeout = TIMEOUT
    txBytes = b"\xfe\x01\x01\xff"
    print("Tx : {}\n".format(txBytes))
    ser.write(txBytes)
    rxBytes = ser.read(2)
    print("TR : {}\n".format(rxBytes))
    print("Close Serial connection to : {}\n".format(dev.device))
    ser.close()