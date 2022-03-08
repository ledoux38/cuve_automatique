from pyfirmata import Arduino

from interface.packages.GPIO import GPIO

PORT: str = '/dev/ttyACM0'
BAUDRATE: int = 921600
TIMEOUT: int = 1


if __name__ == '__main__':
    gpio: GPIO = GPIO('d:13:o', 13)
    carte = Arduino(PORT)
    carte.digital[gpio.adress].write(1)
