from digi.xbee.devices import XBeeDevice
device = XBeeDevice("/dev/ttyUSB0", 9600)
device.open()

print(device.read_device_info())

protocol = device.get_protocol()
print(protocol)


print("get_64bit_addr {}".format(device.get_64bit_addr()))
print("get_16bit_addr {}".format(device.get_16bit_addr()) )



device.close()
