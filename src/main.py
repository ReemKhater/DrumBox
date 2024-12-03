from gpioHandler import setup_gpio, wait_for_button_press
from soundPlayer import play_sound

def handle_button_press(button):
    print(f"Bouton {button} pressé !")
    play_sound(button)

def main():
    print("Initialisation de la boîte à rythmes...")
    setup_gpio()
    print("Appuyez sur un bouton pour jouer un son.")
    wait_for_button_press(handle_button_press)

if __name__ == "__main__":
    main()
