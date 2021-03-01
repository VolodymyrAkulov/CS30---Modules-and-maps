# descriptons for all tile types, enemies
from termcolor import colored


# Created a class for tiles
class Tile:
    name = "Nothing"
    info = "a blank space"
    info2 = "No advantage"
    Token = " "

#Creating 4 categories of tiles to enhance combat strategy
class Mud(Tile):
    name = "Mud"
    info = "Muddy ground is difficult to traverse."
    info2 = "Optimal terrain for picking enemies off at a distance."
    Token = colored('M','blue')


class Dirt(Tile):
    name = "Dirt"
    info = "Very standard fighting ground."
    info2 = "Grants no advantage."
    Token = colored('D','white')


class Grass(Tile):
    name = "Grass"
    info = "Grassy land very easy to manouver in."
    info2 = "Recommended for hand to hand combat."
    Token = colored('G','green')


class Stone(Tile):
    name = "Stone"
    info = "Hard floor it's difficult to stand and manouver on this rough surface"
    info2 = "Conducts magic very easily."
    Token = colored('S','red')

TokenTiles = [Mud, Dirt, Grass, Stone]

# Created a class for enemies
class Enemy:
    Name  = "Enemy"
    Info = "Template"
    Hp = 0
    Weapon = "None"
    Armour = "None"
    Healing = "None"
    Dmg = 0
    TypeDmg = 'None'

# Creating 8 enemies 2 enemies for each of the 3 classes and 2 "Bosses"
class Peasant(Enemy):
    Name = "Peasant"
    Info = "Some random pesant whos just very slightly better than you"
    Hp = 11 
    Weapon = 'Stick'
    Armour = 'Leather Cap'
    Healing = 'Potato'
    Dmg = 3
    TypeDmg = 'MEL'

class Pillgrim(Enemy):
    Name = "Pillgrim"
    Info = "A religious man who spreads his religion to other lands"
    Hp = 15
    Weapon = 'Staff'
    Armour = 'Leather Cap'
    Healing = 'Bread'
    Dmg = 7
    TypeDmg = 'MGC'
    
    
class Knight(Enemy):
    Name = "Knight"
    Info = "A dapper gentlemen sure to rescue you in a time of need (or not)"
    Hp = 30
    Weapon = 'Sword'
    Armour = 'Steel Breastplate'
    Healing ='Health Potion'
    Dmg = 15
    TypeDmg = 'MEL'
    
class Priest(Enemy):
    Name = "Priest"
    Info = "'Have you heard of our lord and saviour?''"
    Hp =  25
    Weapon = 'God'
    Armour = 'Faith', 'Drapes'
    Healing = 'Holy water'
    Dmg = 10
    TypeDmg = 'MGC'

class Archer(Enemy):
    Name = "Archer"
    Info = "Some british lad with a bent stick and a few pointy sticks"
    Hp = 15
    Weapon = 'Bow'
    Armour = 'Hardened leather'
    Healing = 'Potato'
    Dmg = 15
    TypeDmg = 'RGD'
    
class Hero(Enemy):
    Name = "Hero"   
    Info = "'The Hero'"
    Hp = 20
    Weapon = 'The hammer of god'
    Armour = 'Full plate armour'
    Healing = 'Health potion'
    Dmg = 20
    TypeDmg = 'TRU'
    
class MainHero(Enemy):
    Name = "Main Hero"
    Info = "'You lose'"
    Hp = 300
    Weapon = 'Friendship'
    Armour = 'Plot armour'
    Healing = 'Determination'
    Dmg = 30
    TypeDmg = 'TRU'
    
class Drunkard(Enemy):
    Name = "Drunkard"
    Info =  "A drunk man who just lost his house in a rigged dice game"
    Hp = 10
    Weapon = 'projectile vomit'
    Armour = 'none'
    Healing ='Beer'
    Dmg = 5
    TypeDmg = 'RGD'

EnemyList = [Peasant, Pillgrim, Knight, Priest, Archer, Drunkard]