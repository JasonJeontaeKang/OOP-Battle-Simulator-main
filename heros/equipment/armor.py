import random
from .Equipment import Equipment


class Armor(Equipment):

    def __init__(self, slot):
        rarity, durability = self.generate_rarity()

        super().__init__(
            name=slot,
            rarity=rarity,
            slot=slot
        )

        self.durability = durability

        print(
            f"{self.rarity.title()} {self.name} "
            f"created with {self.durability} durability."
        )

    @staticmethod
    def generate_rarity():

        roll = random.randint(1, 1000)

        if roll > 990:
            return "mythic", 1000
        elif roll > 900:
            return "legendary", 500
        elif roll > 750:
            return "rare", 250
        elif roll > 300:
            return "uncommon", 100
        else:
            return "common", 25

    def absorb_damage(self, damage):
        self.durability -= damage

        if self.durability <= 0:
            print(f"{self.name} broke!")
            return True

        print(
            f"{self.name} absorbed {damage:.1f} damage "
            f"({self.durability:.1f} durability left)"
        )

        return False