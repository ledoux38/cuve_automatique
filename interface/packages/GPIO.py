class GPIO:
    name: str
    adress: int

    def __init__(self, name: str, adress: int):
        self.adress = adress
        self.name = name

    def get_name(self):
        return self.name

    def get_adress(self):
        return self.adress
