import re


class GPIO:
    REGEX_TYPE: str = '(d|a)'
    REGEX_ADDRESS: str = '(\d+)'
    REGEX_IO: str = '(o|i)'
    REGEX_ALL: str = '({}:{}:{})'.format(REGEX_TYPE, REGEX_ADDRESS, REGEX_IO)

    def __init__(self, value: str, label: str):
        values = self.__control(value, GPIO.REGEX_ALL).split(':')
        self.__type: str = values[0]
        self.__address: int = int(values[1])
        self.__int_out: str = values[2]
        self.__label: str = label

    def __str__(self) -> str:
        return "{}:{}:{}".format(self.__type, str(self.__address), self.__int_out)

    def get_name(self) -> str:
        return self.__str__()

    @property
    def label(self) -> str:
        return self.__label

    @property
    def address(self) -> int:
        return self.__address

    @property
    def type(self) -> str:
        return self.__type

    @property
    def io(self) -> str:
        return self.__int_out

    @address.setter
    def address(self, value: int) -> None:
        self.__address = self.__control(str(value), GPIO.REGEX_ADDRESS)

    @label.setter
    def label(self, value: str) -> None:
        self.__label = value

    @type.setter
    def type(self, value: str) -> None:
        self.__type = self.__control(value, GPIO.REGEX_TYPE)

    @io.setter
    def io(self, value: str) -> None:
        self.__int_out = self.__control(value, GPIO.REGEX_IO)

    @staticmethod
    def __control(value: str, regex: str) -> str:
        regex = r"^{}$".format(regex)

        is_ok = re.search(regex, value)
        if is_ok is None:
            raise ValueError

        return value
