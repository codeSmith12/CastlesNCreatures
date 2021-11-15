# JUST SLIGHTLY INTO THE PYGAME STUFF
# from random import randint, choice
from copy import copy, deepcopy
from time import sleep
import os
from math import ceil
import hero
from random import randint, choice
from item import Item
from playsound import playsound
# from pydub import AudioSegment
# from pydub.playback import play
playsound('./assets/sounds/coin.wav')
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


class Shop():
    def __init__(self, weaponTable, consumables):
        self.weaponTable = weaponTable
        self.consumables = consumables
        self.gold = randint(350, 1000)
        self.itemsToSell = []
        self.populateItems()

    def populateItems(self):
        for i in range(3):
            self.itemsToSell.append(choice(self.weaponTable))
            self.itemsToSell.append(choice(self.consumables))
        self.itemsToSell.sort(key=self.sortByName)

    def buyMenu(self,hero):
        while True:
            print(f"\nShop gold: {self.gold}")
            print(f"\nGold: {hero.gold}\n")
            for i in range(len(self.itemsToSell)):
                print(f"{i+1}) {self.itemsToSell[i].name} - {self.itemsToSell[i].sellPrice*15} gold")
            choice = input("Enter the number of the item you'd like to buy, hit enter to leave: ")
            if choice == "":
                return
            elif int(choice) < 1 or int(choice) > len(self.itemsToSell):
                print("Please enter a valid number")
            elif hero.gold >= self.itemsToSell[int(choice)-1].sellPrice*15: # They'd like to purchase a valid item
                item = self.itemsToSell[int(choice)-1]
                price = item.sellPrice*15
                hero.gold -= price
                self.gold += price
                print(f"{item.isConsumable=}")
                if hero.gold >= price:
                    if item.isConsumable == True:
                        hero.items.append(item)
                        self.itemsToSell.remove(item)
                    elif not item.isConsumable:
                        hero.equiptment.append(item)
                        self.itemsToSell.remove(item)
            else:
                print(f"{hero.name} doesn't have enough gold.")
    def sellMenu(self,hero):
        while True:
            # Gather every item the user has for selling.
            totalItems = []
            for item in hero.equiptment:
                totalItems.append(item)
            for item in hero.items:
                totalItems.append(item)

            totalItems.sort(key=self.sortByName)

            print(f"\nGold: {hero.gold}")

            for i in range(len(totalItems)):
                print(f"{i+1}) {totalItems[i].name} - {totalItems[i].sellPrice} gold")
            choice = input("Enter the number of the item you'd like to sell, hit enter to leave: ")
            if choice == "":
                return
            elif int(choice) < 1 or int(choice) > len(totalItems):
                print("Please enter a valid number")
            elif self.gold >= totalItems[int(choice)-1].sellPrice: # They'd like to sell a valid item
                playsound("/assets/sounds/coin.wav")
                item = totalItems[int(choice)-1] # Store item
                hero.gold += item.sellPrice # Either way hero gold is increased
                self.gold -= item.sellPrice # Either way store gold is reduced
                print(f"\nShop is now gold: {self.gold}\n")
                self.itemsToSell.append(item) # We must add the sold item back to the store
                if item.isConsumable == True: # Depending on what kind of item it is
                    hero.items.remove(item) # remove it from the specific list.
                elif not item.isConsumable:
                    hero.equiptment.remove(item) # remove it from the specific list.
            else:
                print("The merchant doesn't have enough gold for that.")

    def shopMenu(self, hero):
        print(f"{hero.name} enters the shop.")
        while True:
            choice = input(" 1) Buy\n 2) Sell\n 3) Exit\n")
            if choice == "3" or choice == "":
                return
            elif choice == "1":
                self.buyMenu(hero)
            elif choice == "2":
                self.sellMenu(hero)


    def sortByName(self, x):
        return x.name


class GameMaster():
    def __init__(self):
        self.createLootTable()
        self.characterCreation()

    def createLootTable(self):
        self.weaponLootTable = [
            # TODO: Add an item that can only be found in shop with random chance, VERY expensive, but VERY good ? Maybe a potion of perma +stat or something?
            # Or another weapon that anyone can use ?? idk...
            # Item name, (drop chance/100, "description", "stat", buffAmount, sell price )
            Item("Fire Sword", 35, "A magic sword engulfed in flames. Adds 5 to attack damage.", "Warrior", 5, 20, False),
            Item("Chaos Sword", 20, "An epic sword that ensues chaos around the weilder. Adds 12 to attack damage.", "Warrior", 12, 45, False),
            Item("Master Sword", 10, "A legendary sword that only a combat master can weild. Adds 20 to attack damage.", "Warrior", 20, 60, False),
            Item("Ice Staff", 35, "A magic staff made of enchanted ice. Adds 5 to spell damage.", "Magi", 5, 20, False),
            Item("Vortex Staff", 20, "An epic staff made of swirling energy. Adds 12 to spell damage.", "Magi", 12, 45, False),
            Item("Master Staff", 10, "A legendary staff crafted by the gods. Adds 20 to spell damage.", "Magi", 20, 60, False),
            Item("Lightning Bow", 35, "A magic bow that enchants each arrow it shoots with lightning. Adds 5 to attack damage.", "Ranger", 5, 20, False),
            Item("Holy Bow", 20, "An epic bow that shoots bolts of holy light. Adds 12 to attack damage.", "Ranger", 12, 45, False),
            Item("Master Bow", 10, "A legendary bow that was crafted by the gods. Adds 20 to attack damage.", "Ranger", 20, 60, False),
        ]

        # FULL MANA POT OR GREATER MANA POT !!!
        self.consumableLootTable = [
            Item("Health Potion", 75, "A potion that can be used in battle to restore 50 health. Obviously.", "health", 50, 5, True),
            Item("Magica Potion", 75, "A potion that can be used in battle to restore 50 magica.", "magica", 50, 5, True),
            Item("Greater Health Potion", 33, "A potion that can be used in battle to restore 100 health.", "health", 100, 10, True),
            Item("Greater Magica Potion", 33, "A potion that can be used in battle to restore 100 magica.", "magica", 100, 10, True),
            Item("Evasion Talisman", 25, "Permanently increases Dexterity by 10.", "dexterity", 10, 10, True),
            Item("Armor Talisman", 25, "Permanently increases armor by 4.", "armor", 4, 10, True),
            Item("Max Health Talisman", 25, "Permanently increases Max Health by 15.", "maxHealth", 15, 10, True),
            Item("Max Mana Talisman", 25, "Permanently increases Max Mana by 25.", "maxMagica", 25, 10, True),
            Item("Lucky Talisman", 10, "Permanently increases critical strike chance by 10.", "critChance", 15, 30, True),
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
                    print("Insufficient magica. Choose another attack.")
                    choice = ""
                else:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    self.hero.defensiveAbility()
                    print(f"{self.hero.name}'s magica is now at {self.hero.magica}")
                    return
            elif choice == "3":
                if self.hero.magica < 25:
                    print("Insufficient magica. Choose another attack.")
                    choice = ""
                else:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    self.hero.buffAbility()
                    print(f"{self.hero.name}'s magica is now at {self.hero.magica}")
                    return
            elif choice == "4":
                    # os.system('cls' if os.name == 'nt' else 'clear')
                    self.hero.useChosenItem()
                    return

    def lootProcess(self):
        # Drop random gold.
        gold = randint(3, 25) + self.enemy.increasedDropRate #Add some small amount to the gold they find depending on the enemy type
        self.hero.gold += gold
        print(f"{self.hero.name} gathers {gold} gold. They now have {self.hero.gold} gold.")

        # Choose item from loot table, check to see if they won the item
        weaponItem = choice(self.weaponLootTable)
        itemRoll = randint(0, 100)
        if itemRoll > 100 - weaponItem.dropChance - self.enemy.increasedDropRate:
            print(f"{self.hero.name} receives weapon: {weaponItem.name}")
            self.hero.equiptment.append(weaponItem)
        else: # Rolls a second time if the first roll fails..
            weaponItem = choice(self.weaponLootTable)
            itemRoll = randint(0, 100)
            if itemRoll > 100 - weaponItem.dropChance - self.enemy.increasedDropRate:
                print(f"{self.hero.name} receives weapon: {weaponItem.name}")
                self.hero.equiptment.append(weaponItem)

        # Choose item from loot table, check to see if they won the item
        useableItem = choice(self.consumableLootTable)
        itemRoll = randint(0, 100)
        if itemRoll > 100 - useableItem.dropChance:
            print(f"{self.hero.name} receives consumable: {useableItem.name}")
            self.hero.items.append(useableItem)

    def combatLoop(self):
        heroStats = self.hero # Must save hero stats at beginning of fight
        print("\n\tEntering combat\n")

        while self.hero.health > 0 and self.enemy.health > 0:
            self.promptHeroAttack()
            print("\n")
            if self.enemy.health > 0:
                self.enemy.attack(self.hero)
            else:
                print(f"{self.enemy.name} has been defeated.")
        print("\n\tExiting combat\n")
        self.hero = heroStats # Set the hero stats back to normal after fight.

    def outOfCombatMenu(self):
        # Every time we leave combat, we generate a new shop.
        self.shop = Shop(self.weaponLootTable, self.consumableLootTable)
        while True:
            choice = input("\n1) Continue\n2) Change equiptment\n3) Use item \n4) Shop\n")
            if choice == "" or choice == "1":
                del self.shop # Delete old shop to avoid memory leak
                return
            elif choice == "2":
                self.hero.changeEquiptment()
            elif choice == "3":
                self.hero.useChosenItem()
            elif choice == "4":
                self.shop.shopMenu(self.hero)

    def GameLoop(self):
        # TODO: Level 1 enemy list, pull from level 2 after X amount of fights or something.
        # Sometimes you get lucky with progression and even the Wyvern doesn't do much.

        while self.hero.health > 0:
            self.enemyList = [
                        #  name    ,   health   ,    attackDamage,     range     , spellDmg,  dex,    attack type,   armor, dropRate,  spawn chance
                hero.Enemy("Goblin", randint(25,30), randint(12,14), randint(2,4), 0, randint(50,60), "slashes at", randint(0,2), 0, 90),
                hero.Enemy("Goblin Archer", randint(15,22), randint(10,11), randint(6,8), 0, randint(45,75), "shoots at", randint(0,1),5, 90),
                hero.Enemy("Wyvern", randint(55,65), randint(14,20), randint(4,7), 0, randint(35,70), "breathes fire at", randint(6,7),35, 15),
                hero.Enemy("Skeleton Warrior", randint(35,40), randint(15,15), randint(3,4), 0, randint(50,75), "stabs", randint(2,4),15, 50),
                hero.Enemy("Skeleton Archer", randint(30,35), randint(20,22), randint(1,2), 0, randint(55,80), "shoots at", randint(0,2),17, 50),
                hero.Enemy("Dragon", randint(80,100), randint(20,26), randint(5,8), 0, randint(55,85), "breathes fire at", randint(8,10),65, 15),
            ]

            # Allows enemies to have different spawn chances.
            # Don't want bosses to have same chance as goblin..
            enemySpawned = False
            while not enemySpawned:
                rollSpawn = randint(0,100)
                self.enemy = choice(self.enemyList)
                print(f"Rolled {rollSpawn} against enemy type: {self.enemy.name}")
                if rollSpawn > 100 - self.enemy.spawnChance:
                    enemySpawned = True
            print(f"\n\tA {self.enemy.name} appears!")
            self.combatLoop()
            if self.hero.health <= 0:
                break
            self.lootProcess()
            del self.enemy
            if self.hero.health > 0:
                # Change equiptment, use items and visit shop
                self.outOfCombatMenu()
                os.system('cls' if os.name == 'nt' else 'clear')
            # deallocate enemy objects for a new randomized group
            for enemy in self.enemyList:
                del enemy
            del self.enemyList

        print(f"{self.hero.name} has died...")



while True:
    gameMaster = GameMaster()
    playAgain = input("Would you like to:\n1) Continue\n2) Exit\n")
    if playAgain == "1":
        os.system('cls' if os.name == 'nt' else 'clear')
        del gameMaster
    else:
        exit()
