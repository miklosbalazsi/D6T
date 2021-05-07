import serial
import serial.tools.list_ports
import logging

logging.basicConfig(level=logging.DEBUG)
logging.info('Started...')

""" Find E18 devices and return list of SerialPorts """
e18_devices = []
serialPortList = serial.tools.list_ports.comports()
for serialPort in serialPortList:
    logging.info("Found {}".format(serialPort.device) )
    logging.info("device : {}".format(serialPort.device))
    logging.info("name : {}".format(serialPort.name))
    logging.info("description : {}".format(serialPort.description))
    logging.info("hwid : {}".format(serialPort.hwid))
    logging.info("vid : {}".format(serialPort.vid))
    logging.info("pid : {}".format(serialPort.pid))
    logging.info("serial_number : {}".format(serialPort.serial_number))
    logging.info("location : {}".format(serialPort.location))
    logging.info("manufacturer : {}".format(serialPort.manufacturer))
    logging.info("product : {}".format(serialPort.product))
    logging.info("interface : {} \n".format(serialPort.interface))
    e18_devices.append(serialPort.device)
