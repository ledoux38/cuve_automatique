import time

from pyfirmata import Arduino, util


def blink(carte_target: Arduino, set_value: bool):
    carte_target.digital[13].write(set_value)


if __name__ == '__main__':
    carte = Arduino('/dev/ttyACM0')
    print(carte.get_pin("d:13:o"))
    # carte.digital[13].write(1)
