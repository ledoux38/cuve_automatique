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

    canvasFrame = Frame(window)
    canvasFrame.pack(side=LEFT)

    buttonFrame = Frame(window)
    buttonFrame.pack(side=RIGHT)

    # canvas
    canvas = Canvas(canvasFrame, width=150, height=120, background='yellow')
    ligne1 = canvas.create_line(75, 0, 75, 120)
    ligne2 = canvas.create_line(0, 60, 150, 60)
    txt = canvas.create_text(75, 60, text="Cible", font="Arial 16 italic", fill="blue")
    canvas.pack()


    Button(buttonFrame, text='L1-C1', borderwidth=1).grid(row=1, column=1)
    Button(buttonFrame, text='L1-C2', borderwidth=1).grid(row=1, column=2)
    Button(buttonFrame, text='L2-C3', borderwidth=1).grid(row=2, column=3)
    Button(buttonFrame, text='L2-C4', borderwidth=1).grid(row=2, column=4)
    Button(buttonFrame, text='L3-C3', borderwidth=1).grid(row=3, column=3)
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
