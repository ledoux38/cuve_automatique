import re


class IO:
    REGEX_TYPE: str = '(d|a)'
    REGEX_ADDRESS: str = '(\d+)'
    REGEX_IO: str = '(o|i)'
    REGEX_ALL: str = '({}:{}:{})'.format(REGEX_TYPE, REGEX_ADDRESS, REGEX_IO)

    def __init__(self, io: str, label: str):
        self.io: str = self.__control(io, IO.REGEX_ALL)
        self.label: str = label

    @staticmethod
    def __control(value: str, regex: str) -> str:
        regex = r"^{}$".format(regex)

        is_ok = re.search(regex, value)
        if is_ok is None:
            raise ValueError

        return value
