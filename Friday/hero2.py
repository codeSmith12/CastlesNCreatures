class Hero:
    def __init__(self, name):
        self.name = name
class Enemy:
    def __init__(self):
        self.name = "Goblin"
        self.Health = 45
        self.physicalDamage = 5
        self.dexterity = 50
    def attackAbility():
        print(f"{self.name} slashes at {Person.name}")

class Fighter:
    def  __init___(self):
        self.maxHp = 50
        self.atkDmg = 15
        self.atkDmgRange = 5
        self.mana = 50
        self.maxMana = 50
        self.atkTact = "Slash"
        self.dex = 50
        self.armor = 10
        self.manaRegen = 10
    def attackAbility(self, enemy):
        print(f"{self.name} strikes the enemy")
    def defensiveAbility(self):
        print(f"{self.name} raises the shield {self.name} owns")
    def buffAbility(self):
        print(f"{self.name} calls upon the powerfuls Chicken")

goblin = Enemy()
fighter = Fighter()
fighter.attackAbility(goblin)
goblin.attackAbility(fighter)

# class Mage:
#     def  __init___(Person):
#         self.maxHp = 35
#         self.atkDmg = 5
#         self.atskDmgRange = 5
#         self.mana = 100
#         self.maxMana = 100
#         self.atkTact = "SpellCast"
#         self.dex = 30
#         self.armor = 5
#         self.manaRegen = 25
#     def attackAbility():
#         print(f"{self.name} utters the ultimate spell's words: POOPIOSA!!")
#     def defensiveAbility():
#         print(f"{self.name} casts the spell of Chicken-Nugget-Shaped-MagicShield")
#     def buffAbility():
#         print(f"{self.name} calls upon the power of calls upon the power!!!!!!!!!!!!!!")
#
#     mage = Mage()
#     mage.attackAbility
#     mage.defensiveAbility
#     mage.buffAbility
#
# class Rouge:
#     def  __init___(Person):
#         self.maxHp = 45
#         self.atkDmg = 10
#         self.atkDmgRange = 5
#         self.mana = 45
#         self.maxMana = 45
#         self.atkTact = "Slash"
#         self.dex = 60
#         self.armor = 7
#     def attackAbility():
#         print(f"{self.name} stabs the enemy")
#     def defensiveAbility():
#         print(f"{self.name} doesn't know any effect defensive things to do and the enemy knows how clueless {self.name} is and finds it boring to attack an enemy who won't fight back so the enemy doesn't attack {self.name}")
#     def buffAbility():
#         print(f"{self.name} cals ape on the power ov mis speling")
#
#     rouge= Rouge()
#     rouge.attackAbility
#     rouge.defensiveAbility
#     rouge.buffAbility
#
# class Archer:
#     def  __init___(Person):
# self.maxHp = 40
# self.ememyDist = rand(0-200)
# self.atkDmg = 10 + atkDmgDist
# self.atkDmgDist = -5 if enemyDist is 0 to 10, 0 if enemyDist is 11 to 20, 5 if enemyDist is 21 to 30, 10 if enemyDist is 31 to 40, 15 if enemyDist is 41 to 50, -10 if enemyDist is > 51 or = 51
# self.mana = 30
# self.maxMana = 30
# self.atkTact = "Shoot"
# self.dex = 40
# self.armor = 10
#     def attackAbility():
#         print(f"{self.name} Shoots da enemy with the arrow of mis speling")
#     def defensiveAbility():
#         print(f"{self.name} Uses the bow like a sword to block")
#     def buffAbility():
#         print(f"{self.name} calls upon the spell of temporary bigger bow to shoot more arrows")
#
#     archer = Archer()
#     archer.attackAbility
#     archer.defensiveAbility
#     archer.buffAbility
#
#
# class Barbarian:
#     def __init___(Person):
# self.maxHp = 60
# self.atkDmg = 35
# self.atkDmgRange = 3
# self.mana = 10
# self.maxMana = 10
# self.atkTact = "SMASH"
# self.dex = 10
# self.armor = 15
#     def attackAbility():
#         print(f"{self.name} SMASH!!!!!")
#     def defensiveAbility():
#         print(f"{self.name} BLOCK!!!")
#     def buffAbility():
#         print(f"{self.name} uses proper grammar in this sentence for once, and now {self.name} is proud.")
#
#     barbarian = Barbarian()
#     barbarian.attackAbility
#     barbarian.defensiveAbility
#     barbarian.buffAbility
#
#
#
#
# class Druid:
# def  __init__(Person):
# self.maxHp = 35
# self.atkDmg = 10
# self.atkDmgRange = 7
# self.mana = 80
# self.maxMana = 80
# self.atkTact = "SpellCast"
# self.dex = 45
# self.armor = 10
#     def attackAbility():
#         print(f"{self.name} used vine whip! It's super effective. Enemy fainted! Or not. Maybe yes!!!!")
#     def defensiveAbility():
#         print(f"{self.name} used protect!")
#     def buffAbility():
#         print(f"{self.name} used howl! {self.name}'s attack rose!")
#
#     druid = Druid()
#     druid.attackAbility
#     druid.defensiveAbility
#     druid.buffAbility
#
# class Tank:
# def  __init__(Person):
# self.maxHp = 90
# self.atkDmg = 3
# self.atkDmgRange = 5
# self.mana = 55
# self.maxMana = 55
# self.atkTact = "Shiled-Bash"
# self.dex = 20
# self.armor = 45
#     def attackAbility():
#         print(f"{self.name} basheded!")
#     def defensiveAbility():
#         print(f"{self.name} shielded!")
#     def buffAbility():
#         print(f"{self.name} screameded")
#
#     tank = Tank()
#     tank.attackAbility
#     tank.defensiveAbility
#     tank.buffAbility
