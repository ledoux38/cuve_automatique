import time

import pyfirmata

from packages.GPIO import GPIO
from packages.Element import Element



PORT: str = '/dev/ttyACM0'
BAUDRATE: int = 921600
TIMEOUT: int = 1

if __name__ == '__main__':
    list_gpio: list = [GPIO('d:13:o'), GPIO('d:12:o'), GPIO('d:11:o')]
    i: Element = Element("cuve", list_gpio)

    # HIGH = True  # Crée un état haut qui correspond à la led allumée
    # LOW = False  # Crée un état bas qui correspond à la led éteinte
    # board = pyfirmata.Arduino(PORT)  # Initialise la communication avec la carte
    # LED_pin = board.get_pin('d:13:o')  # Initialise la broche (d => digital, 13 => N° broche, o => output)
    #
    # for i in range(10):
    #     LED_pin.write(HIGH)  # Allume la led
    #     time.sleep(1)  # Pause de 0.5 seconde
    #     LED_pin.write(LOW)  # Eteint la led
    #     time.sleep(1)  #
    #     print("toto")
