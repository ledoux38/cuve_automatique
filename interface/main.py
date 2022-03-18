import time

from packages.Element import Element
from packages.IO import IO

PORT: str = '/dev/ttyACM0'
BAUDRATE: int = 921600
TIMEOUT: int = 1

if __name__ == '__main__':
    element: Element = Element("carte", [IO('d:13:o', 'led')], PORT)
    LED_pin = element.io('led')  # Initialise la broche (d => digital, 13 => N° broche, o => output)

    for i in range(10):
        element.io('led').write(True)  # Allume la led
        time.sleep(1)  # Pause de 0.5 seconde
        element.io('led').write(False)  # Eteint la led
        time.sleep(1)  #
        print("toto")
