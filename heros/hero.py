import random


class Hero:

    def __init__(self, name):
        self.name = name

        self.health = random.randint(100, 150)
        self.base_attack = random.randint(10, 25)

        # Equipment slots
        self.equipment = {
            "weapon": None,
            "helmet": None,
            "chestplate": None,
            "leggings": None,
            "boots": None
        }

    @property
    def attack_power(self):
        """
        Total attack = base attack + weapon bonus
        """

        total = self.base_attack

        weapon = self.equipment["weapon"]

        if weapon:
            total += weapon.damage_bonus

        return total

    def equip(self, item):

        old_item = self.equipment[item.slot]

        if old_item:
            print(f"Unequipped {old_item}")

        self.equipment[item.slot] = item

        print(f"Equipped {item}")

    def attack(self):

        crit_roll = random.randint(1, 100)

        if crit_roll <= 10:
            print("Critical Hit!")
            return random.randint(
                self.attack_power,
                self.attack_power + 10
            )

        return random.randint(1, self.attack_power)

    def take_damage(self, damage):

        equipped_armor = [
            piece
            for slot, piece in self.equipment.items()
            if slot != "weapon" and piece
        ]

        if equipped_armor:

            damage_per_piece = damage / len(equipped_armor)

            broken = []

            for armor in equipped_armor:

                if armor.absorb_damage(damage_per_piece):
                    broken.append(armor.slot)

            for slot in broken:
                self.equipment[slot] = None

        else:
            self.health -= damage
            print(f"{self.name} takes {damage} damage.")

        print(f"Health: {self.health}")

    def is_alive(self):
        return self.health > 0

    def show_equipment(self):

        print(f"\n{self.name}'s Equipment")

        for slot, item in self.equipment.items():

            if item:
                print(f"{slot}: {item}")
            else:
                print(f"{slot}: Empty")