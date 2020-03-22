#!/usr/bin/python3

import serial
import serial.tools.list_ports
from . import CONST
import logging


class e18_device:
    """ E18 device driver """

    __SERIAL_CONNECTION = None
    __SERIAL_NAME = None
    __SERIAL_BAUDRATE = 115200
    __SERIAL_TIMEOUT = 5

    def __init__(self, serial_name):
        """ Constructor """
        self.__SERIAL_NAME = serial_name
        self.__SERIAL_CONNECTION = serial.Serial(self.__SERIAL_NAME)
        self.__SERIAL_CONNECTION.baudrate = self.__SERIAL_BAUDRATE
        self.__SERIAL_CONNECTION.timeout = self.__SERIAL_TIMEOUT

    def close(self):
        self.__SERIAL_CONNECTION.close()

    def get_serial_name(self):
        """ Return the name of the Serial device  eg.: /dev/tty/USB1 """
        return self.__SERIAL_CONNECTION.device

    def get_serial_hwid(self):
        """ Return the hardware ID of the serial device """
        return self.__SERIAL_CONNECTION.hwid

    def read_device_type(self):
        """ Read device type
            00 : COORDINATOR
            01 : ROUTER
            02 : TERMINAL
        """
        self.__SERIAL_CONNECTION.write(CONST.READ_DEVICE_TYPE)
        rxBytes = bytearray(self.__SERIAL_CONNECTION.read(2))
        return CONST.DEV_TYPE[rxBytes[1]]

    def read_network_state(self):
        """ Return the state of the network
            00 : NO NETWORK
            01 : NETWORK EXISTS
        """
        self.__SERIAL_CONNECTION.write(CONST.READ_NETWORK_STATE)
        rxBytes = bytearray(self.__SERIAL_CONNECTION.read(2))
        return CONST.NWK_STATE[rxBytes[1]]

    @staticmethod
    def find_e18_devices():
        """ Find E18 devices and return list of SerialPorts """
        e18_devices = []
        serialPortList = serial.tools.list_ports.comports()
        for serialPort in serialPortList:
            if serialPort.vid == CONST.DEVICE_VID and serialPort.pid == CONST.DEVICE_PID:
                logging.debug('Found ' + serialPort.device + ' as an Ebyte E18 device ')
                logging.debug("device : {}".format(serialPort.device))
                logging.debug("name : {}".format(serialPort.name))
                logging.debug("description : {}".format(serialPort.description))
                logging.debug("hwid : {}".format(serialPort.hwid))
                logging.debug("vid : {}".format(serialPort.vid))
                logging.debug("pid : {}".format(serialPort.pid))
                logging.debug("serial_number : {}".format(serialPort.serial_number))
                logging.debug("location : {}".format(serialPort.location))
                logging.debug("manufacturer : {}".format(serialPort.manufacturer))
                logging.debug("product : {}".format(serialPort.product))
                logging.debug("interface : {} \n".format(serialPort.interface))
                e18_devices.append(serialPort.device)
        return e18_devices
