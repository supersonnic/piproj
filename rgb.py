# Shervin Oloumi
# This package can be used to control a correctly wired RGB LED

import time, sys
import RPi.GPIO as GPIO

redPin = 11   #Set to appropriate GPIO
greenPin = 15 #Should be set in the 
bluePin = 13  #GPIO.BOARD format

def turnOn(pin):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.HIGH)
    
def turnOff(pin):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

def redOn():
    turnOn(redPin)

def redOff():
    turnOff(redPin)

def greenOn():
    turnOn(greenPin)

def greenOff():
    turnOff(greenPin)

def blueOn():
    turnOn(bluePin)

def blueOff():
    turnOff(bluePin)

def yellowOn():
    turnOn(redPin)
    turnOn(greenPin)

def yellowOff():
    turnOff(redPin)
    turnOff(greenPin)

def cyanOn():
    turnOn(greenPin)
    turnOn(bluePin)

def cyanOff():
    turnOff(greenPin)
    turnOff(bluePin)

def magentaOn():
    turnOn(redPin)
    turnOn(bluePin)

def magentaOff():
    turnOff(redPin)
    turnOff(bluePin)

def whiteOn():
    turnOn(redPin)
    turnOn(greenPin)
    turnOn(bluePin)

def whiteOff():
    turnOff(redPin)
    turnOff(greenPin)
    turnOff(bluePin)