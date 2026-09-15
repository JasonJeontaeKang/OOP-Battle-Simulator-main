import random

class Hero:

    def __init__(self,name):
        self.name = name
        self.health = random.randint(100,150)
        self.attack_power = random.randint(10,25)

    def attack(self):
        crit_chance = 10
        hit_chance = random.randint(0,100)

        if hit_chance > crit_chance:
            return random.randint(1,self.attack_power)
        else:
            print("Critical Hit!")
            return randon,randint(self.attack_power, self.attack_power + 10)

    def take_damage(self, damage):
        self.health -= damage
        print(f"{self.name} takes {damage} damage. Health: {self.health}")

    def is_alive(self):
        if self.health > 0:
            return True
        elif self.health < 0:
            return False
        
