import RPi.GPIO as GPIO
import time

# Liste des broches GPIO associées aux boutons
BUTTON_PINS = [7,8,9,12,13,14]  
DEBOUNCE_TIME = 0.2 #delai apres la detection d'une pression pour ignorer les signaux de rebond

def setup_gpio():
    # Initialisation des broches GPIO.
    GPIO.setmode(GPIO.BCM)  # Mode BCM pour numéroter les broches
    for pin in BUTTON_PINS:
        GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # Résistance pull-down

def wait_for_button_press():
    # Attend qu'un des boutons soit pressé et retourne le numéro de broche
    while True:
        for pin in BUTTON_PINS:
            if GPIO.input(pin) == GPIO.HIGH:  # Bouton pressé
                time.sleep(DEBOUNCE_TIME) # anti-rebond
                if GPIO.input(pin) == GPIO.HIGH: # verification apres stabilisation
                    return pin
        time.sleep(0.01)  # délai pour éviter une boucle trop rapide
