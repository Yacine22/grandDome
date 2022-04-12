#!/usr/bin/env python3

import smbus
import errno
import time

def i2c_checker():
    bus_number = 1  # 1 indicates /dev/i2c-1
    bus = smbus.SMBus(bus_number)
    device_count = 0

    for device in range(3, 128):
        try:
            bus.write_byte(device, 0)
            print("Found {0}".format(hex(device)))
            device_count = device_count + 1
            
        except IOError as e:
            if e.errno != errno.EREMOTEIO:
                print("Device is not connected !")
                break
                
        except Exception as e: # exception if read_byte fails
            print("Error unk: {0} on address {1}".format(e, hex(address)))
                

    bus.close()
    bus = None
    print("Found- {0} device(s)".format(device_count))
    no_device_text = device_count
    return no_device_text


    