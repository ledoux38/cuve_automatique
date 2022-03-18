from interface.packages.GPIO import GPIO


class Element:
    def __init__(self, name: str, gpio: [GPIO]):
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
                return self.__gpios
        return None

    @name.setter
    def name(self, value: str) -> None:
        self.__name = value
