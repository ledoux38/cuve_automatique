import time

import pyfirmata

from interface.packages.Element import Element
from interface.packages.GPIO import GPIO

PORT: str = '/dev/ttyACM0'
BAUDRATE: int = 921600
TIMEOUT: int = 1

if __name__ == '__main__':
    i: Element = Element("resistance_cuve", GPIO('d:13:o', 13))

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
