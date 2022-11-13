#!/usr/bin/python
# -*- coding:utf-8 -*-
import board
import adafruit_shtc3

i2c = board.I2C()
sht = adafruit_shtc3.SHTC3(i2c)

class SHTC3:
    def __init__(self):
        i2c = board.I2C()
        self.sht = adafruit_shtc3.SHTC3(i2c)

    def read_temperature(self):
        return sht.temperature
    
    def read_humidity(self):
        return sht.relative_humidity

    def read_data(self):
        return {
            "temperature": self.read_temperature(),
            "humidity": self.read_humidity()
        }


if __name__ == "__main__":
    shtc3 = SHTC3()
    while True:
        data = shtc3.read_data()
        print({ 'temperature': '%6.2f°C' % data["temperature"], \
                'humidity': '%6.2f%%' % data["humidity"] \
        })