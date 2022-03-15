import re


class GPIO:
    name: str
    address: int

    def __init__(self, name: str):
        values_gpio = self.__control_name(name)
        self.__type: str = values_gpio[0]
        self.__address: int = values_gpio[1]
        self.__int_out: str = values_gpio[2]

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

        matches = re.finditer(regex, name, re.MULTILINE)

        type_gpio: str = ''
        address_gpio: int = 0
        type_int_out: str = ''

        for matchNum, match in enumerate(matches, start=1):

            for groupNum in range(1, len(match.groups())):
                groupNum = groupNum + 1

                if groupNum == 2:
                    type_gpio = str(match.group(groupNum))

                if groupNum == 3:
                    address_gpio = int(match.group(groupNum))

                if groupNum == 4:
                    type_int_out = str(match.group(groupNum))

        return type_gpio, address_gpio, type_int_out
