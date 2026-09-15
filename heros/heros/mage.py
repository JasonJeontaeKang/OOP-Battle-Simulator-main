from .hero import hero

class mage(hero):
    def __init__(self, name):
        super().__init__(name)
        self.health = 80
        self.attack_power = 15
        self.defense = 5

    # special_equipment = {
    #     "staff": None,
    #     "robe": None,
