from interface.packages.GPIO import GPIO


class Element:
    def __init__(self, name: str, gpio: [GPIO]):
        self.name = name
        self.gpio: [GPIO] = gpio

    def get_name(self):
        return self.name

    def get_gpio_all(self) -> [GPIO]:
        return self.gpio

    def get_gpio_index(self, index: int) -> GPIO:
        return self.gpio[index]
