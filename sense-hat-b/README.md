# Waveshare Sense Hat (B)
https://www.waveshare.com/sense-hat-b.htm

## wiki
https://www.waveshare.com/wiki/Sense_HAT_(B)

### enable I2C Interface
```
sudo raspi-config 
Interfacing Options -> I2C -> yes
sudo reboot
```

## python3
### install python3
```
sudo apt-get install python-pip3 
sudo pip3 install RPi.GPIO
sudo pip3 install spidev
sudo apt-get install python3-smbus
```

### original demo
```
sudo apt-get install p7zip-full
wget https://www.waveshare.com/w/upload/6/6c/Sense-HAT-B-Demo.7z
7z x Sense-HAT-B-Demo.7z -O./Sense-HAT-B-Demo
cd Sense-HAT-B-Demo
```

```
cd ICM-20948/Raspberry\ Pi/python/
sudo python3 ICM20948.py

cd LPS22HBTR/Raspberry\ Pi/python/
sudo python3 LPS22HB.py

cd SHTC3/Raspberry\ Pi/python/
sudo python3 SHTC3.py

cd TCS34725/RaspberryPi/python3/
sudo python3 main.py

cd ADS1015/Raspberry\ Pi/python/
sudo python3 AD.py
```