import time

import pyfirmata

from packages.GPIO import GPIO
from packages.Element import Element

PORT: str = '/dev/ttyACM0'
BAUDRATE: int = 921600
TIMEOUT: int = 1

if __name__ == '__main__':
    list_gpio: list = [GPIO('d:13:o')]
    element: Element = Element("cuve", list_gpio)

    board = pyfirmata.Arduino(PORT)  # Initialise la communication avec la carte
    LED_pin = board.get_pin(element.get_gpio_index())  # Initialise la broche (d => digital, 13 => N° broche, o => output)

    for i in range(10):
        LED_pin.write(True)  # Allume la led
        time.sleep(1)  # Pause de 0.5 seconde
        LED_pin.write(False)  # Eteint la led
        time.sleep(1)  #
        print("toto")
