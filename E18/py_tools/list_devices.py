#!/usr/bin/python3

# E18 c2530 chip serial port
# Bus 001 Device 004: ID 1a86:7523 QinHeng Electronics HL-340 USB-Serial adapter
# Bus 001 Device 003: ID 1a86:7523 QinHeng Electronics HL-340 USB-Serial adapter
#       idVendor           0x1a86 QinHeng Electronics
#       idProduct          0x7523 HL-340 USB-Serial adapter

import logging
import E18.driver


def main():
    logging.basicConfig(level=logging.INFO)
    logging.info('Started...')
    e18_devices = []
    e18_devices = E18.driver.e18_device.find_e18_devices()
    if len(e18_devices) == 0: raise Exception("No E18 device found...exiting")

    logging.info('Found {} E18 device(s)'.format(len(e18_devices)))

    for port in e18_devices:
        e18_dev = E18.driver.e18_device(port)
        print(e18_dev.get_device_type())
        e18_dev.close()


if __name__ == '__main__':
    main()
