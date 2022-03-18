from pyfirmata import Arduino, Pin

from interface.packages.IO import IO


class Element(Arduino):
    def __init__(self, label: str, ios: [IO], test: bool, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__label = label
        self.__io: dict = {}
        for io in ios:
            if test:
                self.__io[io.label] = self.get_pin(io.io)

    def label(self):
        return self.__label

    def io(self, label: str) -> Pin:
        return self.__io[label]
