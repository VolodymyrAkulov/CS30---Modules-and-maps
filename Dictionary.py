# descriptons for all tile types, enemies



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
    Token = "M"


class Dirt(Tile):
    name = "Dirt"
    info = "Very standard fighting ground."
    info2 = "Grants no advantage."
    Token = "D"


class Grass(Tile):
    name = "Grass"
    info = "Grassy land very easy to manouver in."
    info2 = "Recommended for hand to hand combat."
    Token = "G"


class Stone(Tile):
    name = "Stone"
    info = "Hard floor it's difficult to stand and manouver on this rough surface"
    info2 = "Conducts magic very easily."
    Token = "S"

TokenTiles = [Mud, Dirt, Grass, Stone]

# Created a class for enemies
class Enemy:
    Name  = "Enemy"
    Info = "Template"
    Hp = 0

# Creating 8 enemies 2 enemies for each of the 3 classes and 2 "Bosses"
class Peasant(Enemy):
    Name = "Peasant"
    Info = "Some random pesant whos just very slightly better than you"
    Hp = 11 

class Pillgrim(Enemy):
    Name = "Pillgrim"
    Info = "A religious man who spreads his religion to other lands"
    Hp = 15
    
class Knight(Enemy):
    Name = "Knight"
    Info = "A dapper gentlemen sure to rescue you in a time of need (or not)"
    Hp = 30
    
class Priest(Enemy):
    Name = "Priest"
    Info = "'Have you heard of our lord and saviour?''"
    Hp =  25

class Archer(Enemy):
    Name = "Archer"
    Info = "Some british lad with a bent stick and a few pointy sticks"
    Hp = 15
    
class Hero(Enemy):
    Name = "Hero"   
    Info = "'The Hero'"
    Hp = 50
    
class MainHero(Enemy):
    Name = "Main Hero"
    Info = "'You lose'"
    Hp = 300
    
class Drunkard(Enemy):
    Name = "Drunkard"
    Info =  "A drunk man who just lost his house in a rigged dice game"
    Hp = 10