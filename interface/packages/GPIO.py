import re


class GPIO:
    REGEX_TYPE: str = '(d|a)'
    REGEX_ADDRESS: str = '(\d+)'
    REGEX_IO: str = '(o|i)'
    REGEX_ALL: str = r"({}:{}:{})".format(REGEX_TYPE, REGEX_ADDRESS, REGEX_IO)

    def __init__(self, name: str):
        values = self.__control(name)
        self.__type: str = values[0]
        self.__address: int = values[1]
        self.__int_out: str = values[2]

    def get_name(self) -> str:
        return "{}:{}:{}".format(self.__type, str(self.__address), self.__int_out)

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
        self.__address = value

    @type.setter
    def type(self, value: str) -> None:
        self.__type = value

    @io.setter
    def io(self, value: str) -> None:
        self.__int_out = value

    @staticmethod
    def __control(name: str) -> (str, int, str):
        regex = r"^({}:{}:{})$".format(GPIO.REGEX_TYPE, GPIO.REGEX_ADDRESS, GPIO.REGEX_IO)

        is_ok = re.search(regex, name)
        if is_ok is None:
            raise ValueError
        split = name.split(":")
        return str(split[0]), int(split[1]), str(split[2])
