import random
from .Equipment import Equipment

class Weapon(Equipment):

    def __init__(self, weapon_type):
        self.rarity = self.generate_rarity()
        self.durability, self.damage = self.generate_rarity_weapons(self.rarity)

        super().__init__(
            name=weapon_type,
            rarity=self.rarity,
            slot="weapon"
        )

        self.damage_bonus = self.damage

        print(
            f"{self.rarity} {self.name} "
            f"created with +{self.damage_bonus} damage."
        )


