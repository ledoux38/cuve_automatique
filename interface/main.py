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

    # frame 1
    Frame1 = Frame(window, relief=GROOVE)
    Frame1.pack(side=LEFT)

    # frame 2
    Frame2 = Frame(window, relief=GROOVE)
    Frame2.pack(side=LEFT)

    # frame 3 dans frame 2
    Frame3 = Frame(Frame2, bg="white", relief=GROOVE)
    Frame3.pack(side=RIGHT)

    # Ajout de labels

    canvas = Canvas(Frame1, width=150, height=120, background='yellow')
    canvas.pack(padx=10, pady=10)
    ligne1 = canvas.create_line(75, 0, 75, 120)
    ligne2 = canvas.create_line(0, 60, 150, 60)
    txt = canvas.create_text(75, 60, text="Cible", font="Arial 16 italic", fill="blue")


    Label(Frame2, text="Frame 2").pack(padx=10, pady=10)
    Label(Frame3, text="Frame 3", bg="white").pack(padx=10, pady=10)
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
