#!/usr/bin/python
# -*- coding:utf-8 -*-
import ctypes
import time

class SHTC3:
    def __init__(self):
        self.dll = ctypes.CDLL("./SHTC3.so")
        init = self.dll.init
        init.restype = ctypes.c_int
        init.argtypes = [ctypes.c_void_p]
        init(None)

    def SHTC3_Read_Temperature(self):
        temperature = self.dll.SHTC3_Read_TH
        temperature.restype = ctypes.c_float
        temperature.argtypes = [ctypes.c_void_p]
        return temperature(None)

    def SHTC3_Read_Humidity(self):
        humidity = self.dll.SHTC3_Read_RH
        humidity.restype = ctypes.c_float
        humidity.argtypes = [ctypes.c_void_p]
        return humidity(None)

    def readData(self):
        humidity = self.SHTC3_Read_Temperature()
        temperature = self.SHTC3_Read_Humidity()

        return {
            'temperature': temperature,
            "humidity": humidity
        }


if __name__ == "__main__":
    shtc3 = SHTC3()
    while True:
        data = shtc3.readData()
        print({'temperature': '%6.2f°C' % data.temperature, 'humidity': '%6.2f%%' % data.humidity })
        time.sleep(1)