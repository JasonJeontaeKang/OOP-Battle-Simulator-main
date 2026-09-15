import random
from .Equipment import Equipment

class Weapon(Equipment):

    def __init__(self, weapon_type):
        rarity, damage = self.generate_rarity()

        super().__init__(
            name=weapon_type,
            rarity=rarity,
            slot="weapon"
        )

        self.damage_bonus = damage

        print(
            f"{self.rarity.title()} {self.name} "
            f"created with +{self.damage_bonus} damage."
        )

    @staticmethod
    def generate_rarity():

        roll = random.randint(1, 1000)

        if roll > 990:
            return "mythic", 50
        elif roll > 900:
            return "legendary", 35
        elif roll > 750:
            return "rare", 25
        elif roll > 300:
            return "uncommon", 15
        else:
            return "common", 5
