from random import randint, choice
from time import sleep
import os
from math import ceil
import pygame
import prettyBtns as pb
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


Rogueish:
    Main Stat:
        Perception:
            Fast attacking, disabler, Risk vs reward type of character, gambling type
            Item dependent ? items will give chance on hit to stun, skip turn
            does a consistent dmg, or crit dmg?

        Defensive ability: Evade ?


Choice of race in beginning? Could tweak a few stats

'''







class GameMaster():
    def __init__(self):
        # self.characterCreation()
        pygame.init()
        self.WIDTH = 600
        self.HEIGHT = 500
        self.screen = pygame.display.set_mode((self.WIDTH,self.HEIGHT))
        self.screen2 = pygame.Surface((self.WIDTH, self.HEIGHT))
        pygame.display.update()
        pygame.display.set_caption('Creatures n Castles')
        self.mainMenu()

    def mainMenu(self):
        pygame.font.init()
        myFont1 = pygame.font.SysFont('Comic Sans MS', 30)
        myFont2 = pygame.font.SysFont('Comic Sans MS', 15)
        titleLabel = myFont1.render('Creatures n Castles', False, (255,210,51))
        creditLabel = myFont2.render('by theCodeSmith', False, (255,210,51))

        gameOver = False

        startBtn = pb.button(self.screen, self.screen2, (self.WIDTH/2-40, self.HEIGHT/2-40), "Start", size=40, color = "Black", bg="Grey")

        while not gameOver:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if startBtn.collidepoint(pygame.mouse.get_pos()):
                        self.characterCreation()

            self.screen.blit(pygame.transform.scale(self.screen2, (self.WIDTH, self.HEIGHT)), (0, 0))
            self.screen.blit(titleLabel, (self.WIDTH/4, self.HEIGHT/4))
            self.screen.blit(creditLabel, (self.WIDTH/4+70, self.HEIGHT/4 + 40))

            pygame.display.update()

        pygame.quit()
        quit()

    def characterCreation(self):
        pygame.font.init()
        myFont = pygame.font.SysFont('Comic Sans MS', 30)
        textSurface = myFont.render('Choose a hero', False, (255,210,51))
        self.screen.fill((0,0,0))
        self.screen2.fill((0,0,0))

        warriorBtn = pb.button(self.screen, self.screen2, (60, self.HEIGHT/2-40), "Warrior", size=40, color = "Black", bg="Red")
        magiBtn = pb.button(self.screen, self.screen2, (220, self.HEIGHT/2-40), "Magi", size=40, color = "Black", bg="Blue")
        rogueBtn = pb.button(self.screen, self.screen2, (340, self.HEIGHT/2-40), "Rogue", size=40, color = "Black", bg="Yellow")
        gameOver = False
        while not gameOver:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if warriorBtn.collidepoint(pygame.mouse.get_pos()):
                        self.characterCreation()
                        self.hero = hero.Warrior()
                        self.GameLoop()
                    if magiBtn.collidepoint(pygame.mouse.get_pos()):
                        self.characterCreation()
                        self.hero = hero.Magi()
                        self.GameLoop()
                    if rogueBtn.collidepoint(pygame.mouse.get_pos()):
                        self.characterCreation()
                        self.hero = hero.Rogue()
                        self.GameLoop()

            self.screen.blit(pygame.transform.scale(self.screen2, (self.WIDTH, self.HEIGHT)), (0, 0))
            self.screen.blit(textSurface, (self.WIDTH/4, self.HEIGHT/4))

            pygame.display.update()
        pygame.quit()
        quit()
    def GameLoop(self):
        self.enemy = Enemy()
        self.combatLoop()
        self.lootProcess()

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




gameMaster = GameMaster()
