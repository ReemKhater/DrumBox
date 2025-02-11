import RPi.GPIO as GPIO
import time

def setup_speaker(pin):
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(pin, GPIO.OUT)
	pwm = GPIO.PWM(440)
	return pwm
	
def cleanup_speaker():
	GPIO.cleanup()
