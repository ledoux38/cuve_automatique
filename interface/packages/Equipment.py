from interface.packages.GPIO import GPIO


class Element:
    def __init__(self, name: str, gpio: GPIO):
        self.set_name(name)
        self.set_gpio(gpio)

    def get_name(self):
        return self.name

    def get_gpio(self):
        return self.gpio

    def set_name(self, name: str):
        self.name = name

    def set_gpio(self, new_gpio: GPIO):
        self.gpio = new_gpio

    name: property = property(get_name, set_name)
    gpio: property = property(get_gpio, set_gpio)
