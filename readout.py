#!/usr/bin/python
from max6675 import MAX6675, MAX6675Error
import time
import os

cs_pin = 8 
clock_pin = 11
data_pin = 9 
units = "c"
thermocouple = MAX6675(cs_pin, clock_pin, data_pin, units)
running = True
while(running):
    try:
        try:
            tc = thermocouple.get()
            os.system("/opt/fhem/fhem.pl 7072 'set BRT tc'")
            print("tc: {}".format(tc))
        except MAX6675Error as e:
            tc = "Error: "+ e.value
            running = False
            print("tc: {}".format(tc))
        time.sleep(1)
    except KeyboardInterrupt:
        running = False
thermocouple.cleanup()
