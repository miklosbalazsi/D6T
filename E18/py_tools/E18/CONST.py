#!/usr/bin/python3

# Define Device constants
DEVICE_VID = 0x1a86  # 6790
DEVICE_PID = 0x7523  # 29987
DEVICE_VENDOR = "QinHeng Electronics"
DEVICE_PRODUCT = "HL-340 USB-Serial adapter"

# Device types
DEV_TYPE = {0: "COORDINATOR",
            1: "ROUTER",
            2: "TERMINAL"
            }

# Network states
NWK_STATE = {0: "NO NETWORK",
             1: "NETWORK EXISTS"
             }
# Power
TX_POWER = {0: -3,
            1: -1.5,
            2: 0,
            3: 2.5,
            4: 4.5
            }

# Define Read commands
READ_DEVICE_TYPE = b"\xFE\x01\x01\xFF"
READ_NETWORK_STATE = b"\xFE\x01\x02\xFF"
READ_NETWORK_PAN_ID = b"\xFE\x01\x03\xFF"
READ_NETWORK_KEY = b"\xFE\x01\x04\xFF"
READ_LOCAL_SHORT_ADDR = b"\xFE\x01\x05\xFF"
READ_LOCAL_MAC_ADDR = b"\xFE\x01\x06\xFF"
READ_COORD_SHORT_ADDR = b"\xFE\x01\x07\xFF"
READ_COORD_MAC_ADDR = b"\xFE\x01\x08\xFF",
READ_NETWORK_GROUP_NUMBER = b"\xFE\x01\x09\xFF"

# Define Config commands
