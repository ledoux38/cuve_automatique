import time

from packages.Element import Element
from packages.IO import IO
from tkinter import *

PORT: str = '/dev/ttyACM0'
BAUDRATE: int = 921600
TIMEOUT: int = 1

if __name__ == '__main__':
    window = Tk()
    window['bg'] = 'white'

    Button(window, text='L1-C1', borderwidth=1).grid(row=1, column=1)
    Button(window, text='L1-C2', borderwidth=1).grid(row=1, column=2)
    Button(window, text='L2-C3', borderwidth=1).grid(row=2, column=3)
    Button(window, text='L2-C4', borderwidth=1).grid(row=2, column=4)
    Button(window, text='L3-C3', borderwidth=1).grid(row=3, column=3)
    window.mainloop()

    # element: Element = Element("carte", [IO('d:13:o', 'led')], PORT)
    # LED_pin = element.io('led')  # Initialise la broche (d => digital, 13 => N° broche, o => output)
    #
    # for i in range(10):
    #     element.io('led').write(True)  # Allume la led
    #     time.sleep(1)  # Pause de 0.5 seconde
    #     element.io('led').write(False)  # Eteint la led
    #     time.sleep(1)  #
    #     print("toto")
