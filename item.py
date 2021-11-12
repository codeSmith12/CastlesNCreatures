class Item:
    def __init__(self, name, chance, desc, stat, amt, price):
        self.name = name
        self.dropChance = chance
        self.description = desc
        self.stat = stat
        self.amount = amt
        self.sellPrice = price
