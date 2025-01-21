from gpioHandler import setup_gpio, wait_for_button_press
from soundPlayer import play_sound
import time
import os

def handle_button_press(pin):
    play_sound(pin)
    
def handle_power_button(pin):
    time.sleep(2) # Verifier si le boutton est maintenu 2 secondes 
    if GPIO.input(pin) == GPIO.HIGH:
        os.system('sudo shutdown now') # arret du raspberry

def main():
    try : 
        setup_gpio(handle_button_press, handle_power_button)
        while True:
            pass 
    except KeyboardInterrupt :
        print("\nArret du programme.")
    finally : 
        cleanup_gpio()

if __name__ == "__main__":
    main()
