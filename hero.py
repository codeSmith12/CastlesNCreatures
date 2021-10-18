class Enemy:
    def __init__(self):
        self.name = "Goblin"
        self.health = 25
        self.attackDamage = 10
        self.attackDamageRange = 4
        self.spellDamage = 5
        self.dexterity = 55
        self.attackType = "slashes at"
        self.armor = 1

    def attack(self, hero):
        print(f"{self.name} {self.attackType} {hero.name}.")
        hitChance = randint(self.dexterity, 100)

        if  hasattr(hero, "shieldActivated") and hero.shieldActivated == True:
             print(f"{self.name}\'s attack was absorbed by {hero.name}\'s ice shield.")
             hero.shieldActivated = False
        elif hitChance >= hero.dexterity:
            damage = randint(self.attackDamage, self.attackDamage + self.attackDamageRange) - hero.armor
            if damage <=0:
                print(f"\n{hero.name} blocked the attack.")
            else:
                print(f"\n{self.name} strikes {hero.name} for {damage}")
                hero.health -= damage
                print(f"\n{hero.name} is at {hero.health} health.")
        else:
            print(f"\n{self.name}\'s attack missed.")


class Hero: # Generic class Hero will describe a person of greater power.
    def __init__(self):
        self.name="Default"
        self.health = 50
        self.magica = 100 # Even needed?
        self.maxHealth = 50
        self.maxMagica = 100
        self.attackDamage = 10
        self.attackDamageRange = 4
        self.spellDamage = 10
        self.luck=1 # can help them hit better, hit harder, crit chance perhaps.
        # Luck maybe stays at 1, but can go above 1 (like 1.1) and be multiplied by other stats in increase them.
        self.dexterity = 65 # Likelyhood of hitting. fun math to do here.
        self.armor = 9
        self.equiptment = []
        self.items = []

    def attackAbility(self, enemy):
        pass
    def defensiveAbility(self):
        pass
    def buffAbility(self): # Offensive buffs >?
        pass
    def useItem(self):
        pass
    def displayAttacks(self):
        pass


'''
Warrior class:

Notes:


'''

class Warrior(Hero):
    def __init__(self):
        super().__init__()
        self.dexterity = 60
        self.magica = 50
        self.maxMagica = 50
        self.maxHealth = 150
        self.attackDamageRange = 5

    def attackAbility(self,enemy):
        print(f"{self.name} stabs {enemy.name}.")
        hitChance = randint(self.dexterity, 100)
        if hitChance >= enemy.dexterity:
            damage = randint(self.attackDamage, self.attackDamage + self.attackDamageRange) - enemy.armor
            if damage <=0:
                print(f"{enemy.name} blocked the attack.")
            else:
                print(f"{self.name} strikes {enemy.name} for {damage}")
                enemy.health -= damage
                print(f"{enemy.name} is at {enemy.health} health")
        else:
            print(f"{self.name}\'s attack missed.")

    def defensiveAbility(self):
        self.magica -= 25
        print(f"{self.name} blesses their shield with an ancient chant.")
        self.armor += 2
        print(f"Armor has increased to {self.armor}")
        print(f"Magica: {self.magica}")

    def buffAbility(self):
        print(f"{self.name} beats on their chest in a rhythm while shouting vigorously.")
        self.magica -= 25
        self.attackDamage += 2
        self.attackDamageRange += 3
        print(f"{self.name}\'s attack damage increased to {self.attackDamage}.")
        print(f"Magica: {self.magica}")

    def useItem(self):
        pass

    def displayAttacks(self):
        print('''

            1) Stab
            2) Blessed Shield
            3) Bloodrage
            4) Use Item

        ''')
        attack = input("\tEnter choice for attack here: ")
        return attack



'''
Magi Class:

Notes:


'''
class Magi(Hero):
    def __init__(self):
        super().__init__()
        self.spellDamage = 12 # 21 - > 24?
        self.magica = 150
        self.maxMagica = 150
        self.attackDamageRange = 3
        self.buffActivated = False
        self.shieldActivated = False
        self.dexterity = 50

    def attackAbility(self, enemy):
        print(self.shieldActivated)
        if not self.buffActivated:
            damage = randint(self.spellDamage, self.spellDamage + self.attackDamageRange)
            print(f"{self.name} launches a fireball at {enemy.name} and deals {damage} damage")
            enemy.health -= self.spellDamage
        else:
            damage = randint(ceil(self.spellDamage*1.75), ceil(self.spellDamage*1.75) + self.attackDamageRange)
            print(f"A massive fireball erupt from {self.name}, striking {enemy.name} for {damage} damage")
            enemy.health -= damage
            self.buffActivated = False

        print(f"{enemy.name}\'s health is now {enemy.health}")


    def defensiveAbility(self):
        self.magica -= 25
        print(f"{self.name} builds an icy barrier before them.")
        print(f"Magica: {self.magica}")
        self.shieldActivated = True

    def buffAbility(self):
        self.magica -= 25
        print(f"Energy begins to swirl around {self.name}.")
        print(f"Magica: {self.magica}")
        self.buffActivated = True

    def useItem(self):
        pass

    def displayAttacks(self):
        print('''

            1) Fireball
            2) Ice Wall
            3) Unlimited Power
            4) Use Item

        ''')
        attack = input("\tEnter choice for attack here: ")
        return attack

class Rogue(Hero):
    def __init__(self):
        super().__init__()
        self.dexterity = 70
        self.magica = 125 # Energy instead for Rogue?? regain after every basic attack
        self.attackDamageRange = 8
