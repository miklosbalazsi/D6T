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
    __SERIAL_TIMEOUT = 10

    device_type = ""
    short_addr = bytearray(2)
    mac_addr = bytearray(8)

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
        logging.debug("rxBytes count : " + str(len(rxBytes)))
        return CONST.DEV_TYPE[rxBytes[1]]

    def read_network_state(self):
        """ Return the state of the network
            00 : NO NETWORK
            01 : NETWORK EXISTS
        """
        self.__SERIAL_CONNECTION.write(CONST.READ_NETWORK_STATE)
        rxBytes = bytearray(self.__SERIAL_CONNECTION.read(2))
        logging.debug("rxBytes count : " + str(len(rxBytes)))
        return CONST.NWK_STATE[rxBytes[1]]

    def read_network_panID(self):
        """

        :return: bytearray
        """
        self.__SERIAL_CONNECTION.reset_input_buffer()
        self.__SERIAL_CONNECTION.write(CONST.READ_NETWORK_PAN_ID)
        rxBytes = bytearray(self.__SERIAL_CONNECTION.read(3))
        logging.debug("rxBytes count : " + str(len(rxBytes)))
        return ''.join(format(x, '02x') for x in rxBytes)

    def read_network_key(self):
        """
        :return: bytearray
        """
        self.__SERIAL_CONNECTION.reset_input_buffer()
        self.__SERIAL_CONNECTION.write(CONST.READ_NETWORK_KEY)
        rxBytes = bytearray(self.__SERIAL_CONNECTION.read(3))
        logging.debug("rxBytes count : " + str(len(rxBytes)))
        return ''.join(format(x, '02x') for x in rxBytes)

    def read_network_group_number(self):
        self.__SERIAL_CONNECTION.reset_input_buffer()
        self.__SERIAL_CONNECTION.write(CONST.READ_NETWORK_GROUP_NUMBER)
        rxBytes = bytearray(self.__SERIAL_CONNECTION.read(2))
        logging.debug("rxBytes count : " + str(len(rxBytes)))
        return ''.join(format(x, '02x') for x in rxBytes)

    def read_local_short_addr(self):
        self.__SERIAL_CONNECTION.reset_input_buffer()
        self.__SERIAL_CONNECTION.write(CONST.READ_LOCAL_SHORT_ADDR)
        rxBytes = bytearray(self.__SERIAL_CONNECTION.read(3))
        logging.debug("rxBytes count : " + str(len(rxBytes)))
        self.short_addr = rxBytes[1:]
        return ''.join(format(x, '02x') for x in rxBytes)

    def read_local_mac_addr(self):
        self.__SERIAL_CONNECTION.reset_input_buffer()
        self.__SERIAL_CONNECTION.write(CONST.READ_LOCAL_MAC_ADDR)
        rxBytes = bytearray(self.__SERIAL_CONNECTION.read(9))
        logging.debug("rxBytes count : " + str(len(rxBytes)))
        self.mac_addr = rxBytes[1:]
        return ''.join(format(x, '02x') for x in rxBytes)

    def read_coord_short_addr(self):
        self.__SERIAL_CONNECTION.reset_input_buffer()
        self.__SERIAL_CONNECTION.write(CONST.READ_COORD_SHORT_ADDR)
        rxBytes = bytearray(self.__SERIAL_CONNECTION.read(3))
        logging.debug("rxBytes count : " + str(len(rxBytes)))
        return ''.join(format(x, '02x') for x in rxBytes)

    def read_coord_mac_addr(self):
        self.__SERIAL_CONNECTION.reset_input_buffer()
        self.__SERIAL_CONNECTION.write(CONST.READ_COORD_MAC_ADDR)
        rxBytes = bytearray(self.__SERIAL_CONNECTION.read(9))
        logging.debug("rxBytes count : " + str(len(rxBytes)))
        return ''.join(format(x, '02x') for x in rxBytes)

    def read_gpio_state(self, short_addr, gpio_port):
        """
        Read GPIO port state : INPUT|OUTPUT

        :param short_add: E18 device short address \x00\x00
        :param gpio_port: P0_0, P0_1, P0_2, P0_3, P0_4, P0_5, P2_0, P2_1, P2_2
        :return: string
        """
        self.__SERIAL_CONNECTION.reset_input_buffer()

        print(short_addr)
        print(CONST.GPIO_PORTS[gpio_port])
        payload = CONST.READ_GPIO_STATE + short_addr + CONST.GPIO_PORTS[gpio_port] + b"\xFF"
        logging.debug("PAYLOAD : " + ''.join(format(x, '02x') for x in payload))
        self.__SERIAL_CONNECTION.write(payload)
        rxBytes = bytearray(self.__SERIAL_CONNECTION.read(5))
        logging.debug("rxBytes count : " + str(len(rxBytes)))
        return ''.join(format(x, '02x') for x in rxBytes)

    def read_gpio_value(self, short_addr, gpio_port):
        self.__SERIAL_CONNECTION.reset_input_buffer()

        payload = CONST.READ_GPIO_VALUE + short_addr + CONST.GPIO_PORTS[gpio_port] + b"\xFF"
        logging.debug("PAYLOAD : " + ''.join(format(x, '02x') for x in payload))
        self.__SERIAL_CONNECTION.write(payload)
        rxBytes = bytearray(self.__SERIAL_CONNECTION.read(5))
        logging.debug("rxBytes count : " + str(len(rxBytes)))
        return ''.join(format(x, '02x') for x in rxBytes)

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
