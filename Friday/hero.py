class Hero: # Generic blueprint of a person of power
    def __init__(self):
        self.name = "Brian"
        self.attackDamage = 12
        self.health = 50
        self.mana = 50 # Every spell costs 25 mana,
        self.armor = 2
    def attackAbility(self):
        print(f"{self.name} punches the enemy in the tummy.")
        print(f"Enemy loses {self.attackDamage} health.")
    def defensiveAbility(self):
        self.armor += 2
        print(f"{self.name} crosses their arms to defend themself. Armor is now {self.armor}")
    def buffAbility(self): # Something that increases your stats.
        self.attackDamage += 2
        print(f"{self.name} gets enraged, increasing their damage. Attack damage is now {self.attackDamage}")


brian = Hero()
brian.attackAbility()

# goblin = Enemy() # Do not need this at the moment
