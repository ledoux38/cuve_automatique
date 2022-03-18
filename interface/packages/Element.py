from pyfirmata import Arduino

from interface.packages.GPIO import GPIO


class Element(Arduino):
    def __init__(self, name: str, gpio: [GPIO], *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__name = name
        self.__gpios: [GPIO] = gpio

    @property
    def name(self):
        return self.__name

    @property
    def gpios(self) -> [GPIO]:
        return self.__gpios

    def get_gpio_index(self, index: int) -> GPIO:
        return self.__gpios[index]

    def search_gpio(self, search_label: str) -> GPIO | None:
        for x in self.__gpios:
            if x.label == search_label:
                return x
        return None

    def init_pin(self, pin: str) -> any:
        return self.get_pin(self.search_gpio(pin).get_name())

    def action(self, pin: str, value: bool):
        self.get_pin(self.search_gpio(pin).get_name())

    @name.setter
    def name(self, value: str) -> None:
        self.__name = value
