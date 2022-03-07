# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from pyfirmata import Arduino


def board_arduino():
    # Use a breakpoint in the code line below to debug your script.
    board = Arduino('/dev/tty.usbserial-A6008rIF')
    board.digital[13].write(1)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    board_arduino()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
