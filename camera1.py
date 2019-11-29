import RPi.GPIO as GPIO
import picamera
import os
import sys
import time
import datetime

def record():
	camera = picamera.PiCamera()
	camera.resolution = (1280, 720)
	now = datetime.datetime.now()
	filename = now.strftime('%Y-%m-%d %H:%M:%S')
	camera.start_recording(output = filename + '.h264')
	camera.wait_recording(50)
	camera.stop_recording()
	camera.close()
GPIOIN = 17
GPIOOUT = 27
GPIO.setmode(GPIO.BCM)
print("HC-SR501 motion detection start")
GPIO.setup(GPIOIN, GPIO.IN)
GPIO.setup(GPIOOUT, GPIO.OUT)
try:
	while True:
		state = GPIO.input(GPIOIN)
		if state == True :
			print("Motion detected")
			record()
		else :
			print("No motion")
		GPIO.output(GPIOOUT, state)
		time.sleep(0.5)

except KeyboardInterrupt:
	GPIO.cleanup()
print("Motion detection ended")
