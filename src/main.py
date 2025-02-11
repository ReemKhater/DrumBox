from gpioHandler import setup_gpio, cleanup_gpio
from soundPlayer import play_sound, play_wave_file
from volumeHandler import setup_adc, set_volume, cleanup_adc
from SpeakerHandler import setup_speaker, cleanup_speaker
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
        setup_adc()
        setup_speaker()
        print("Système pret. Appuyer sur un bouton")
        while True:
            set_volume(channel=0)
            time.sleep(0.1)
    except KeyboardInterrupt :
        print("\nArret du programme.")
    finally :
        cleanup_adc() 
        cleanup_gpio()
        cleanup_speaker()

if __name__ == "__main__":
    main()
