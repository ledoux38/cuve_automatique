import re


class GPIO:
    name: str
    address: int

    def __init__(self, name: str):
        values = self.__control_name(name)
        self.__type: str = values[0]
        self.__address: int = values[1]
        self.__int_out: str = values[2]

    def get_name(self) -> str:
        return "{}:{}:{}".format(self.__type, str(self.__address), self.__int_out)

    def get_address(self) -> int:
        return self.__address

    def get_type(self):
        return self.__type

    def get_io(self):
        return self.__int_out

    @staticmethod
    def __control_name(name: str) -> (str, int, str):
        regex = r"^((d|a):(\d+):(o|i))$"

        is_ok = re.search(regex, name)
        if is_ok is None:
            raise ValueError
        split = name.split(":")
        return str(split[0]), int(split[1]), str(split[2])
