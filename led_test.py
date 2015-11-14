#This is a program to test an LED is working correctly.
#The user will be prompted for the GPIO number.
#Author: Rhian Fox V1.0 04/08/2015

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
Exit = 0
while Exit == 0:
	pinNum = input("Please enter GPIO number ")
	GPIO.setup(pinNum,GPIO.OUT)
	print "LED on for GPIO ",pinNum
	GPIO.output(pinNum,GPIO.HIGH)
	time.sleep(1)
	print "LED off"
	GPIO.output(pinNum,GPIO.LOW)
	Repeat = raw_input("Test again? | y | n | ")
	if Repeat == 'y':
		Exit = 0
	else: 
		Exit = 1
GPIO.cleanup()
print "Thank you for using Rhian's LED testing programme.  Bye!"
