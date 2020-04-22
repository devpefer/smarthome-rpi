#!/usr/bin/python
import json
import sys
import time
import Adafruit_DHT

sensor = Adafruit_DHT.DHT11

pin = 4

try:

	while True:

                file = open("lecturaDHT11.json","w") 

		humedad, temperatura = Adafruit_DHT.read_retry(sensor, pin)

		lectura = '{0:0.1f}* {1:0.1f}%'.format(temperatura, humedad)

                lecturajson = lectura.split()
                file.write('{\"temperatura\":\"'+lecturajson[0]+'\",\"humedad\":\"'+lecturajson[1]+'\"}')

                file.close()

		time.sleep(10)

except Exception,e:

	print str(e)
