from interface.packages.GPIO import GPIO


class Element:
    def __init__(self, name: str, gpio: [GPIO]):
        self.name = name
        self.gpio = gpio

    def get_name(self):
        return self.name

    def get_gpio(self):
        return self.gpio
