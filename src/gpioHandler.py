import RPi.GPIO as GPIO
import time

# Liste des broches GPIO associées aux boutons
BUTTON_PINS = [17, 18, 27, 22, 23, 24]  # À adapter selon ton câblage

def setup_gpio():
    """Initialise les broches GPIO."""
    GPIO.setmode(GPIO.BCM)  # Mode BCM pour numéroter les broches
    for pin in BUTTON_PINS:
        GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # Résistance de pull-down

def wait_for_button_press():
    """Attend qu'un des boutons soit pressé et retourne le numéro de broche."""
    while True:
        for pin in BUTTON_PINS:
            if GPIO.input(pin) == GPIO.HIGH:  # Bouton pressé
                return pin
        time.sleep(0.01)  # Petit délai pour éviter une boucle trop rapide
