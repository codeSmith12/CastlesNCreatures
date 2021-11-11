from random import randint, choice
from math import ceil
'''
Ideas:

Add bleeds / dots to the game? On crit, add a dot ???



Champion types:
Warrior:
    Main Stat:
            Strength? are we doing typical shit ? I mean kids need stability
            Medium attack speed, moderate damage, high health pool, maybe shield
            least gambling type, consistent dmg


            Defensive ability: Raise Shield

Magi:
    Main Stat:
        Acuity
        heavy slow attacks, expensive can crit hard , semi gambling type
        more consistent than rogue
        Defensive ability: Spell shield, or healing magic?

Rogueish:
    Main Stat:
        Perception:
            Fast attacking, disabler, Risk vs reward type of character, gambling type
            Item dependent ? items will give chance on hit to stun, skip turn
            does a consistent dmg, or crit dmg?

        Defensive ability: Evade ?


Choice of race in beginning? Could tweak a few stats


'''
class Hero: # Generic class Hero will describe a person of greater power.
    def __init__(self):
        self.name="Default"
        self.health = 50
        self.magica = 100
        self.maxHealth = 50
        self.maxMagica = 100
        self.attackDamage = 10
        self.attackDamageRange = 4
        self.spellDamage = 10
        self.luck=1 # can help them hit better, hit harder, crit chance perhaps.
        # Luck maybe stays at 1, but can go above 1 (like 1.1) and be multiplied by other stats in increase them.
        self.dexterity = 65 # Likelyhood of hitting. fun math to do here.
        self.armor = 4
        self.equiptment = []
        self.items = []
        self.gold = 0
        self.critChance = 25

    def attackAbility(self, enemy):
        pass
    def defensiveAbility(self):
        pass
    def buffAbility(self): # Offensive buffs >?
        pass
    def useItem(self):
        while True:
            for i in range(len(self.items)):
                print(f"{i+1}: {self.items[i].name}")
            choice = input("Enter the number of the item you'd like to use. Press enter for no item.")
            if choice == "":
                return
            elif int(choice) < 1 or int(choice)> len(self.items):
                print(f"Please enter number from 1 to {len(self.items)}")
            else:
                # self.items.remove(self.items[int(choice)-1])
                return self.items[int(choice)-1]

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
        self.health = self.maxHealth
        self.attackDamageRange = 5
        self.damageBuffAmount = 0
        self.damageBuffRange = 0
        self.armor = 5

    def attackAbility(self,enemy):
        hitChance = randint(self.dexterity, 100)
        if hitChance >= enemy.dexterity:
            rollCrit = randint(0,100)
            if rollCrit > 100 - self.critChance:
                critDamage = 1.8
                print(f"{self.name} critically stabs {enemy.name}.")
            else:
                critDamage = 1
                print(f"{self.name} stabs {enemy.name}.")
            # Calculate true damage
            damage = randint(self.attackDamage + self.damageBuffAmount, self.attackDamage + self.damageBuffRange + self.attackDamageRange)
            # Calculate final damage
            damage = ceil(damage * critDamage - enemy.armor) #
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
        self.damageBuffAmount = 2
        self.attackDamageRange = 3
        print(f"{self.name}\'s attack damage increased to {self.attackDamage + self.damageBuffAmount}.")
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
        self.spellDamage = 14 # 21 - > 24?
        self.maxMagica = 150
        self.maxHealth = 100
        self.health = self.maxHealth
        self.magica = self.maxMagica
        self.attackDamageRange = 3
        self.buffActivated = False
        self.shieldActivated = False
        self.dexterity = 50
        self.armor = 2
        self.critChance = 20
    def attackAbility(self, enemy):
        rollCrit = randint(0,100)
        if rollCrit > 100 - self.critChance:
            critDamage = 1.8
            print(f"{self.name} critically strikes {enemy.name}")
        else:
            critDamage = 1
        if not self.buffActivated:
            damage = ceil(randint(self.spellDamage, self.spellDamage + self.attackDamageRange) * critDamage)
            print(f"{self.name} launches a fireball at {enemy.name} and deals {damage} damage")
            enemy.health -= self.spellDamage
        else:
            damage = randint(ceil(self.spellDamage*1.75), ceil(self.spellDamage*1.75) + self.attackDamageRange) * critDamage
            print(f"A massive fireball erupt from {self.name}, striking {enemy.name} for {damage} damage")
            enemy.health -= damage
            self.buffActivated = False

        print(f"{enemy.name}\'s health is now {enemy.health}")


    def defensiveAbility(self):
        self.magica -= 25
        print(f"{self.name} builds an icy barrier before them.")
        self.shieldActivated = True

    def buffAbility(self):
        self.magica -= 25
        print(f"Energy begins to swirl around {self.name}.")
        self.buffActivated = True

    def displayAttacks(self):
        print('''

            1) Fireball
            2) Ice Wall
            3) Unlimited Power
            4) Use Item

        ''')
        attack = input("\tEnter choice for attack here: ")
        return attack

class Ranger(Hero):
    def __init__(self):
        super().__init__()
        self.maxMagica = 75
        self.maxHealth = 90
        self.health = self.maxHealth
        self.magica = self.maxMagica
        self.dexterity = 70
        self.attackDamage = 8
        self.attackDamageRange = 8
        self.evasionCharges = 0
        self.damageBuffAmount = 0
        self.damageBuffRange = 0
        self.armor = 3

    def attackAbility(self, enemy): #
        hitChance = randint(self.dexterity, 100)
        if hitChance >= enemy.dexterity:
            rollCrit = randint(0, 100)
            if rollCrit > 100 - self.critChance:
                critDamage = 1.8
                print(f"{self.name} critically hits {enemy.name}.")
            else:
                critDamage = 1
                print(f"{self.name} hits {enemy.name}.")
            # Calculate true damage
            damage = randint(self.attackDamage + self.damageBuffAmount, self.attackDamage + self.damageBuffRange + self.attackDamageRange)
            # Calculate final damage
            damage = ceil(damage * critDamage - enemy.armor) #
            if damage <=0:
                print(f"{enemy.name} blocked the attack.")
            else:
                print(f"{self.name}'s arrow hits {enemy.name} for {damage}")
                enemy.health -= damage
                print(f"{enemy.name} is at {enemy.health} health")
        else:
            print(f"{self.name}\'s arrow misses by an inch.")

    def defensiveAbility(self):
        print(f"{self.name} throws a smoke screen onto the battle field.")
        print(f"For 2 turns, enemy loses 20 dexterity while attacking.")
        self.magica -= 25
        self.evasionCharges += 2


    def buffAbility(self):
        print(f"{self.name} sharpens their arrows.")
        self.critChance += 13
        self.magica -= 25
        print(f"{self.name}'s chance to crit has increased to {self.critChance}.")

    def displayAttacks(self):
        print('''

            1) Shoot Arrow
            2) Evasion
            3) Piercing Arrows
            4) Use Item

        ''')
        attack = input("\tEnter choice for attack here: ")
        return attack

class Enemy:
    def __init__(self):
        self.name = "Goblin"
        self.health = 25
        self.attackDamage = 12
        self.attackDamageRange = 3
        self.spellDamage = 4
        self.dexterity = 55
        self.attackType = "slashes at"
        self.armor = 0

    def attack(self, hero):
        print(f"{self.name} {self.attackType} {hero.name}.")
        if  hasattr(hero, "evasionCharges") and hero.evasionCharges>0:
            hitChance = randint(self.dexterity-20, 80)
            hero.evasionCharges -= 1
            print(f"{hero.name} has {hero.evasionCharges} evasion charges left.")
        else:
            hitChance = randint(self.dexterity, 100)

        # If hero is Warrior and has used Shield Buff, attack is absorbed by shield, buff is toggled off
        if  hasattr(hero, "shieldActivated") and hero.shieldActivated == True:
             print(f"{self.name}\'s attack was absorbed by {hero.name}\'s ice shield.")
             hero.shieldActivated = False
        elif hitChance >= hero.dexterity:
            damage = randint(self.attackDamage, self.attackDamage + self.attackDamageRange) - hero.armor
            if damage <=-1:
                print(f"\n{hero.name} blocked the attack.")
            else:
                print(f"\n{self.name} strikes {hero.name} for {damage}")
                hero.health -= damage
                print(f"\n{hero.name} is at {hero.health} health.")
        else:
            print(f"\n{self.name}\'s attack missed.")
