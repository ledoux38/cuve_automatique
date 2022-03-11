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

    def set_name(self, new_name: str):
        self.name = new_name

    def set_adress(self, new_address: int):
        self.adress = new_address

    name: property = property(get_name, set_name)
    gpio: property = property(get_adress, get_adress)
