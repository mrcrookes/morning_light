#!/usr/bin/python

from gpiozero import PWMLED
from time import sleep
from datetime import datetime
from threading import Timer

light = PWMLED(17)

def wakeup():
    for i in range(11):
        
        power = .1 * i
        light.value = .2 * (6**power - 1)       
        sleep(120)      
        print(i)

def off():
    
    light.value = 0  
    print("off")

today = datetime.today()
start = today.replace(day = today.day + 1, hour = 6, minute = 40, second = 0, microsecond = 0)
stop = today.replace(day = today.day + 1, hour = 7, minute = 30, second = 0, microsecond = 0)

start_diff = start - today
stop_diff = stop - today

on_secs = start_diff.seconds + 1
off_secs = stop_diff.seconds + 1

on = Timer(on_secs, wakeup)
off = Timer(off_secs, off)

on.start()
off.start()
