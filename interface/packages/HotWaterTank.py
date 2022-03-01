class hot_water_tank:
    def __init__(self):
        self.qte_water: int = 20
        self.temperature: double = 20
        self.activation: bool = False

    def set_qte_water(self, water):
        self.qte_water = water

    def set_temperature(self, new_temperature):
        self.temperature = new_temperature

    def set_activation(self, activation):
        self.activation = activation
