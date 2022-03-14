import re


class GPIO:
    name: str
    adress: int

    def __init__(self, name: str):
        i = self.__control_name(name)
        self.__type = i[0]
        self.__address = i[1]
        self.__int_out = i[2]
        self.__name = name

    def get_name(self):
        return self.__name

    def get_adress(self):
        return self.__address

    def get_type(self):
        return self.__type

    def get_int_out(self):
        return self.__int_out


    @staticmethod
    def __control_name(name: str) -> (str, int, str):
        regex = r"^((d|a):(\d+):(o|i))$"

        matches = re.finditer(regex, name, re.MULTILINE)

        type_gpio: str
        address_gpio: int
        type_int_out: str

        for matchNum, match in enumerate(matches, start=1):

            for groupNum in range(1, len(match.groups())):
                groupNum = groupNum + 1

                if groupNum == 2:
                    type_gpio = str(match.group(groupNum))

                if groupNum == 3:
                    address_gpio = int(match.group(groupNum))

                if groupNum == 4:
                    type_int_out = str(match.group(groupNum))

        return tuple(type_gpio, address_gpio, type_int_out)
