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
            f"{self.rarity} {self.name} "
            f"created with {self.durability} durability."
        )

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