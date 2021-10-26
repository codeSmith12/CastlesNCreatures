# JUST SLIGHTLY INTO THE PYGAME STUFF
# from random import randint, choice
from time import sleep
import os
from math import ceil
import hero

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
        self.characterCreation()

    def characterCreation(self):
        print("""

    Welcome to Creatures N Castles!

    Choose a class:

    1) Warrior
    2) Magi
    3) Rogue

        """)
        choice = ""
        while choice != "1" and choice != "2" and choice != "3":
            choice = input("Enter choice for class here: ")

        if choice == "1":
            print("\n\tThe warrior? A stable choice.")
            self.hero = hero.Warrior()
        elif choice == "2":
            print("\n\tThe Magi? A smart choice.")
            self.hero = hero.Magi()
        elif choice == "3":
            print("\n\tThe Rogue, eh? I see you like to take your chances.")
            self.hero = hero.Rogue()

        name = ""
        while len(name) <= 0 or not name.isalpha():
            name = input("\n\tWhat is your name hero? ")
            self.hero.name = name

        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"\n\tGreetings {name}. Good luck on your travels...")

        sleep(4)
        os.system('cls' if os.name == 'nt' else 'clear')
        self.GameLoop()
    def promptHeroAttack(self):
        choice = ""
        while choice != "1" and choice != "2" and choice != "3":
            choice = self.hero.displayAttacks()

        if choice == "1":
            os.system('cls' if os.name == 'nt' else 'clear')
            self.hero.attackAbility(self.enemy)
        elif choice == "2":
            os.system('cls' if os.name == 'nt' else 'clear')
            self.hero.defensiveAbility()
        elif choice == "3":
            os.system('cls' if os.name == 'nt' else 'clear')
            self.hero.buffAbility()

    def lootProcess(self):
        print("You find a {}")

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
        self.enemy = hero.Enemy()
        print(f"\n\tA {self.enemy.name} appears!")
        self.combatLoop()
        self.lootProcess()



gameMaster = GameMaster()
