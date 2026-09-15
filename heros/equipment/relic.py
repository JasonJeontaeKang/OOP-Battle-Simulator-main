from .Equipment import Equipment

class relic(Equipment):
    def __init__(self, name, effect):
        super().__init__(name)
        self.effect = effect

        self.name = name

        self.rarity, _ = self.generate_rarity()
        if self.name == "strength":
            self.effect = self.generate_rarity_relic(self.rarity, "strength")
        elif self.name == "defense":
            self.effect = self.generate_rarity_relic(self.rarity, "defense")   
        elif self.name == "damage":
            self.effect = self.generate_rarity_relic(self.rarity, "damage")
        elif self.name == "health":
            self.effect = self.generate_rarity_relic(self.rarity, "health")

        
