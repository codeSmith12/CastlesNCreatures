# JUST SLIGHTLY INTO THE PYGAME STUFF
# from random import randint, choice
from time import sleep
import os
from math import ceil
import hero
from random import randint, choice
from item import Item
'''
Dynamics:
Begin game by choosing a class. Shows inheritence...
At the beginning of every round you choose from 3 random items to help build around your classes strengths
(If item chose it is removed from list, some may repeat?)
IF you win the round, you get to choose a +5 to a stat from a list I've created... (stats change per hero? or no..)

**Keep amt of classes small so we can build items around each class**


Could ROLL on stats at characterCreation, health = randint(45-55)
                                          dexterity = randint(55-65)
                Rolls have different ranges depending on class chosen!!!



round system:

3 random enemies,
shop, big shop
boss,
shop,? limited shop
repeat with + level difficulty

'''


class GameMaster():
    def __init__(self):
        self.createLootTable()
        self.characterCreation()

    def createLootTable(self):
        self.weaponLootTable = [
            # Item name: (drop chance/100, "description", "stat", buffAmount )
            Item("Fire Sword", 25, "A legendary sword engulfed in flames. Adds 5 to attack damage.", "attackDamage", 5),
            Item("Ice Staff", 25, "A legendary staff made of enchanted ice. Adds 5 to spell damage.", "spellDamage", 5)
        ]
        self.consumableLootTable = [
            Item("Health Potion", 75, "A potion that can be used in battle to restore health points. Obviously.", "health", 50),
            Item("Mana Potion", 75, "A potion that can be used in battle to restore health points. Obviously.", "magica", 50),
        ]

    def characterCreation(self):
        print("""

    Welcome to Creatures N Castles!

    Choose a class:

    1) Warrior
    2) Magi
    3) Ranger

        """)
        choice = ""
        while choice != "1" and choice != "2" and choice != "3":
            choice = input("Enter choice for class here: ")

        if choice == "1":
            print("\n\tThe warrior? A strong choice.")
            self.hero = hero.Warrior()
        elif choice == "2":
            print("\n\tThe Magi? A smart choice.")
            self.hero = hero.Magi()
        elif choice == "3":
            print("\n\tThe Ranger, eh? Practicing social distancing I see..")
            self.hero = hero.Ranger()

        name = ""
        while len(name) <= 0 or not name.isalpha():
            name = input("\n\tWhat is your name hero? ")
            self.hero.name = name

        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"\n\tGreetings {name}. Good luck on your travels...")

        sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        self.GameLoop()

    def promptHeroAttack(self):
        choice = ""
        insufficientMana = False
        while choice != "1" and choice != "2" and choice != "3" and choice != "4":
            choice = self.hero.displayAttacks()

            if choice == "1":
                os.system('cls' if os.name == 'nt' else 'clear')
                self.hero.attackAbility(self.enemy)
                return
            elif choice == "2":
                if self.hero.magica < 25:
                    print("Insufficient mana. Choose another attack.")
                    choice = ""
                else:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    self.hero.defensiveAbility()
                    print(f"{self.hero.name}'s magica is now at {self.hero.magica}")
                    return
            elif choice == "3":
                if self.hero.magica < 25:
                    print("Insufficient mana. Choose another attack.")
                    choice = ""
                else:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    self.hero.buffAbility()
                    print(f"{self.hero.name}'s magica is now at {self.hero.magica}")
                    return
            elif choice == "4":
                    # os.system('cls' if os.name == 'nt' else 'clear')
                    self.useChosenItem()
                    return

    # TODO: Move this function into the hero class
    def useChosenItem(self):
        item = self.hero.useItem()
        if not item:
            print("No item was chosen. Back to the fight!")
        else:
            stat = getattr(self.hero, item.stat) # Grab the stat the item is increasing
            self.hero.items.remove(item)
            if item.stat == "health":
                self.hero.health += item.amount# Increase the stat by that amount.
                print(f"{self.hero.name} is now at {self.hero.health} health.")
            elif item.stat == "magica":
                self.hero.magica += item.amount# Increase the stat by that amount.
                print(f"{self.hero.name} is now at {self.hero.magica} magica.")
        sleep(2)


    def lootProcess(self):
        # Drop random gold.
        gold = randint(3, 25)
        print(f"You gather {gold} gold.")

        # Roll weapon item slot, system needs work
        weaponItem = choice(self.weaponLootTable)
        itemRoll = randint(weaponItem.dropChance, 100)
        if itemRoll > 100 - weaponItem.dropChance/2: # added /2 for fun.. IDK

            print(f"{self.hero.name} receives weapon: {weaponItem.name}")
            self.hero.equiptment.append(weaponItem)

        useableItem = choice(self.consumableLootTable)
        itemRoll = randint(useableItem.dropChance, 100)
        if itemRoll > 100 - useableItem.dropChance/2:
            print(f"{self.hero.name} receives consumable: {useableItem.name}")
            self.hero.items.append(useableItem)




    def combatLoop(self):
        heroStats = self.hero # Must save hero stats at beginning of fight
        print("\n\tEntering combat\n")

        while self.hero.health > 0 and self.enemy.health > 0:
            self.promptHeroAttack()
            if self.enemy.health > 0:
                self.enemy.attack(self.hero)
            else:
                print(f"{self.enemy.name} has been defeated.")
        print("\n\tExiting combat\n")
        self.hero = heroStats # Set the hero stats back to normal after fight.

    def GameLoop(self):
        for i in range(4):
            self.enemy = hero.Enemy()
            print(f"\n\tA {self.enemy.name} appears!")
            self.combatLoop()
            self.lootProcess()
            del self.enemy




gameMaster = GameMaster()
