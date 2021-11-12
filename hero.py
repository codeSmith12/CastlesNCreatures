from random import randint, choice
from math import ceil
from time import sleep
from item import Item
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
        self.curWeapon = Item("Basic weapon", 0, "Basic weapon", "Hero", 0, 0, False)

    def attackAbility(self, enemy):
        pass
    def defensiveAbility(self):
        pass
    def buffAbility(self): # Offensive buffs >?
        pass

 # Display all items, and their prices. Sell price should be contained in class.


    # Function that allows us to change weapons, called outside of combat
    def changeEquiptment(self):
        # While input isn't "", list each item
        while True:
            print(f"Currently equipt: {self.curWeapon.name} - {self.curWeapon.description}")
            for i in range(len(self.equiptment)):
                print(f"{i+1}: {self.equiptment[i].name} - {self.equiptment[i].description}\n")
            choice = input("Enter the number of the item you'd like to equipt. Press enter for no item.\n")
            if choice == "":
                return
                # Error check the numbers to avoid out of indexing
            elif int(choice) < 1 or int(choice)> len(self.equiptment):
                print(f"Please enter number from 1 to {len(self.equiptment)}")
            else:
                # Convert choice to the true choice
                choice = int(choice) - 1
                # Check if the equiptment item they chose is usable by their class
                if self.__class__.__name__ == self.equiptment[choice].stat:
                    # Increase the correct stat depending on the class,
                    # reduce damage from the unequipt weapon
                    if self.__class__.__name__ == "Warrior":
                        self.attackDamage -= self.curWeapon.amount
                        self.attackDamage += self.equiptment[choice].amount
                        print(f"\n{self.name} equipts {self.equiptment[choice].name}. Their attack damage is now {self.attackDamage}")
                    elif self.__class__.__name__ == "Magi":
                        self.spellDamage -= self.curWeapon.amount
                        self.spellDamage += self.equiptment[choice].amount
                        print(f"\n{self.name} equipts {self.equiptment[choice].name}. Their attack damage is now {self.spellDamage}")
                    elif self.__class__.__name__ == "Ranger":
                        self.attackDamage -= self.curWeapon.amount
                        self.attackDamage += self.equiptment[choice].amount
                        print(f"\n{self.name} equipts {self.equiptment[choice].name}. Their attack damage is now {self.attackDamage}")
                    # Place weapon in weapon slot
                    self.equiptment.append(self.curWeapon)
                    self.curWeapon = self.equiptment[choice]
                    self.equiptment.remove(self.equiptment[choice])
                    return
                else: # Print message if they chose an item that isn't part of their class
                    print(f"\nThis weapon is meant for a {self.equiptment[choice].stat}.")

    def displayAttacks(self):
        pass

    def useItem(self): # Should combine with other item function
        while True:
            for i in range(len(self.items)):
                print(f"{i+1}: {self.items[i].name} - {self.items[i].description}\n")
            choice = input("Enter the number of the item you'd like to use. Press enter for no item. ")
            if choice == "":
                return
            elif int(choice) < 1 or int(choice)> len(self.items):
                print(f"Please enter number from 1 to {len(self.items)} ")
            else:
                return self.items[int(choice)-1]

    def useChosenItem(self):
        item = self.useItem()
        if not item:
            print("No item was chosen. Back to the fight!")
            return
        else:
            stat = getattr(self, item.stat) # Grab the stat the item is increasing
            if item.stat == "health":
                self.health += item.amount# Increase the stat by that amount.
                if self.health > self.maxHealth:
                    self.health = self.maxHealth
                elif self.health == self.maxHealth:
                    print(f"{self.name} is already at full health.")
                    return
                print(f"{self.name} is now at {self.health} health.")
            elif item.stat == "magica":
                self.magica += item.amount# Increase the stat by that amount.
                if self.magica > self.maxMagica:
                    self.magica = self.maxMagica
                elif self.magica == self.maxMagica:
                    print(f"{self.name} is already at full magica.")
                    return
                print(f"{self.name} is now at {self.magica} magica.")
            elif item.stat == "dexterity":
                self.dexterity += item.amount
                if self.dexterity > 100:
                    self.dexterity = 99
                print(f"{self.name} quickens their pace. Their dexterity is now {self.dexterity}.")
            elif item.stat == "maxHealth":
                self.maxHealth += item.amount
                self.health += item.amount
                print(f"{self.name}'s vitality increases. Their health is now {self.health} out of {self.maxHealth}.")
            elif item.stat == "maxMagica":
                self.maxMagica += item.amount
                self.magica += item.amount
                print(f"{self.name}'s magical prowess increases. Their magica is now {self.magica} out of {self.maxMagica}.")
            elif item.stat == "critChance":
                self.critChance += item.amount
                if self.critChance > 100:
                    self.critChance = 99
                print(f"{self.name}'s keen eye sharpens. Their chance to critical strike is now {self.critChance}.")
            elif item.stat == "armor":
                self.armor += item.amount
                if self.armor > 100:
                    self.armor = 99
                print(f"{self.name}'s skin thickens. Their armor is now {self.armor}.")

        self.items.remove(item)
        sleep(2)

'''
Warrior class:

Notes:


'''

class Warrior(Hero):
    def __init__(self):
        super().__init__()
        self.dexterity = 50
        self.magica = 50
        self.maxMagica = 50
        self.maxHealth = 150
        self.health = self.maxHealth
        self.attackDamageRange = 5
        self.damageBuffAmount = 0
        self.damageBuffRange = 0
        self.armor = 4
        self.critChance = 20
        self.dexterity = 45

    def attackAbility(self,enemy):
        hitChance = randint(self.dexterity, 100)
        if hitChance >= enemy.dexterity:
            rollCrit = randint(0,100)
            if rollCrit > 100 - self.critChance:
                critDamage = 1.8
                print(f"{self.name} critically stabs {enemy.name}")
            else:
                critDamage = 1
                print(f"{self.name} stabs {enemy.name}")
            # Calculate true damage
            damage = randint(self.attackDamage + self.damageBuffAmount, self.attackDamage + self.damageBuffRange + self.attackDamageRange)
            # Calculate final damage
            damage = ceil(damage * critDamage - enemy.armor) #
            if damage <=0:
                print(f"{enemy.name} blocked the attack\n")
            else:
                print(f"{self.name} strikes {enemy.name} for {damage}\n")
                enemy.health -= damage
                print(f"{enemy.name} is at {enemy.health} health\n")
        else:
            print(f"{self.name}\'s attack missed\n")

    def defensiveAbility(self):
        self.magica -= 25
        print(f"{self.name} blesses their shield with an ancient chant")
        self.armor += 3
        print(f"Armor has increased to {self.armor}")

    def buffAbility(self):
        print(f"{self.name} beats on their chest in a rhythm while shouting vigorously")
        self.magica -= 25
        self.damageBuffAmount += 2
        self.attackDamageRange += 2
        print(f"{self.name}\'s attack damage increased to {self.attackDamage + self.damageBuffAmount}")


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
 Currently no scaling...

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
        self.shieldCharges = 0
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
            enemy.health -= damage
        else:
            damage = randint(ceil(self.spellDamage*1.75), ceil(self.spellDamage*1.75) + self.attackDamageRange) * critDamage
            print(f"A massive fireball erupts from {self.name}, striking {enemy.name} for {damage} damage")
            enemy.health -= damage
            self.buffActivated = False

        print(f"{enemy.name}\'s health is now {enemy.health}")


    def defensiveAbility(self):
        self.magica -= 25
        print(f"{self.name} builds an icy barrier before them.")
        self.shieldCharges = 2

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
        self.critChance = 20

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
        print(f"For 3 turns, enemy loses 20 dexterity while attacking.")
        self.magica -= 25
        self.evasionCharges += 3


    def buffAbility(self):
        print(f"{self.name} sharpens their arrows.")
        self.critChance += 8
        self.magica -= 25
        if self.critChance > 100:
            self.critChance = 99
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

        # Need to make an enemy that has ability to ignore armor ?
class Enemy:
    def __init__(self, name, health, attack, range, spellDmg, dex, attackType, arm, dropRate, spawn):
        self.name = name
        self.health = health
        self.attackDamage = attack
        self.attackDamageRange = range
        self.spellDamage = spellDmg
        self.dexterity = dex
        self.attackType = attackType
        self.armor = arm
        self.increasedDropRate = dropRate
        self.spawnChance = spawn

    def attack(self, hero):
        print(f"{self.name} {self.attackType} {hero.name}.")
        if  hasattr(hero, "evasionCharges") and hero.evasionCharges>0:
            hitChance = randint(self.dexterity-20, 80)
            hero.evasionCharges -= 1
            print(f"{hero.name} has {hero.evasionCharges} evasion charges left.")
        else:
            hitChance = randint(self.dexterity, 100)

        # If hero is Warrior and has used Shield Buff, attack is absorbed by shield, buff is toggled off
        if  hasattr(hero, "shieldCharges") and hero.shieldCharges > 0:
             print(f"{self.name}\'s attack was absorbed by {hero.name}\'s ice shield.")
             hero.shieldCharges -= 1
        elif hitChance >= hero.dexterity:
            damage = randint(self.attackDamage, self.attackDamage + self.attackDamageRange) - hero.armor
            if damage <=0:
                print(f"\n{hero.name} blocked the attack.")
            else:
                print(f"\n{self.name} strikes {hero.name} for {damage}")
                hero.health -= damage
                print(f"{hero.name} is at {hero.health} health.")
        else:
            print(f"\n{self.name}\'s attack missed.")
