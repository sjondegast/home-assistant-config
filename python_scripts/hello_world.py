#!/usr/bin/python

# Declare Imports
# import os
# import time
#import threading
import RPi.GPIO as GPIO


print("Starting the script........")

# ingore any warnings
GPIO.setwarnings(False)

# Declare variables
GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.OUT, pull_up_down=GPIO.PUD.UP)

name = data.get("name", "world")
logger.info("Hello %s", name)
hass.bus.fire(name, {"wow": "from a Python script!"})