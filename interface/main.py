from datetime import time


from pyfirmata import Arduino

from interface.packages.GPIO import GPIO

PORT: str = '/dev/ttyACM0'
BAUDRATE: int = 921600
TIMEOUT: int = 1

if __name__ == '__main__':
    gpio: GPIO = GPIO('d:13:o', 13)
    carte = Arduino(PORT)
    while True:
        carte.digital[13].write(0)
        time.sleep(2.4)
        print("toto")
