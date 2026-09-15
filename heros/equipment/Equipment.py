class Equipment:
     """
     Base class for all equipable items.
     """

     def __init__(self, name, rarity, slot):
          self.name = name
          self.rarity = rarity
          self.slot = slot

     def __str__(self):
          return f"{self.rarity.title()} {self.name}"