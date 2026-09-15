import random


class Equipment:
     """
     Base class for all equipable items.
     """

     def __init__(self, name, rarity, slot):
          self.name = name
          self.rarity = rarity
          self.slot = slot

     def __str__(self):
          return f"{self.rarity} {self.name}"

     @staticmethod
     def generate_rarity():
          roll = random.randint(1, 1000)
     
          if roll > 990:
               return "mythic"
          elif roll > 900:
               return "legendary"
          elif roll > 750:
               return "rare"
          elif roll > 300:
               return "uncommon"
          else:
               return "common"
          

     @staticmethod
     def generate_rarity_weapons(rarity):

          if rarity == "mythic":
               return 1000, 250
          elif rarity == "legendary":
               return 500, 100
          elif rarity == "rare":
               return 250, 25
          elif rarity == "uncommon":
               return 100, 10
          else:
               return 25, 5
          

     @staticmethod
     def generate_rarity_armor(rarity):

          if rarity == "mythic":
               return 1000
          elif rarity == "legendary":
               return 500
          elif rarity == "rare":
               return 250
          elif rarity == "uncommon":
               return 100
          else:
               return 25

     @staticmethod
     def generate_rarity_relic(rarity, type):
          if type == "damage":
               if rarity == "mythic":
                    return 250
               elif rarity == "legendary":
                    return 100
               elif rarity == "rare":
                    return 50
               elif rarity == "uncommon":
                    return 25
               else:
                    return 10
          elif type == "health":
               if rarity == "mythic":
                    return 250
               elif rarity == "legendary":
                    return 100
               elif rarity == "rare":
                    return 50
               elif rarity == "uncommon":
                    return 25
               else:
                    return 10
          elif type == "strength":
               if rarity == "mythic":
                    return 50
               elif rarity == "legendary":
                    return 25
               elif rarity == "rare":
                    return 10
               elif rarity == "uncommon":
                    return 5
               else:
                    return 1
          elif type == "defense":
               if rarity == "mythic":
                    return 50
               elif rarity == "legendary":
                    return 25
               elif rarity == "rare":
                    return 10
               elif rarity == "uncommon":
                    return 5
               else:
                    return 1
          else:
               raise ValueError("Invalid relic type. Must be 'damage' or 'health'.")
