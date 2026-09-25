from enemy import Enemy


class Boss(Enemy):
    """A stronger enemy with a powered-up attack."""

    def __init__(self, name):
        super().__init__(name, health=250, attack_power=30)

    def attack(self):
        damage = super().attack()
        bonus_damage = 5
        print(f"{self.name} unleashes a crushing blow!")
        return damage + bonus_damage
    def introduce(self):
        print(f"I am the mighty {self.name}! Prepare to face my wrath!")