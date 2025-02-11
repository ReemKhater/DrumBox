import RPi.GPIO as GPIO
import time
import os

# Liste des broches GPIO associées aux boutons
BUTTON_PINS = [12,13,14,15,16,19]  
POWER_BUTTON_PIN = 25
DEBOUNCE_TIME = 200 

def setup_gpio(callback_button, callback_power):
    # Initialisation des broches GPIO
    GPIO.setmode(GPIO.BCM)  
    
    # Configuration des boutons 
    for pin in BUTTON_PINS:
        print('Configuration du pin', pin)
        GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  
        GPIO.remove_event_detect(pin)
        GPIO.add_event_detect(pin, GPIO.RISING, callback=callback_button, bouncetime=DEBOUNCE_TIME)
        print(pin, "configured")
    
    # Configuration du power button 
    GPIO.setup(POWER_BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  
    GPIO.remove_event_detect(pin)
    GPIO.add_event_detect(POWER_BUTTON_PIN, GPIO.RISING, callback=callback_button, bouncetime=DEBOUNCE_TIME)

def cleanup_gpio():
    GPIO.cleanup()
