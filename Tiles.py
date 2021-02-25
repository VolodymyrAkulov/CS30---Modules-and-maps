# descriptons for all locations, events, and enemies


# town locations and background
o = ''
LocationTiles = {
    'Mud': {
      'Accuracy': -5,
      'Damadge':  0,
      'name': 'M',
      'PreferedDamadgeType': 'Ranged'
    },
    'Dirt': {
      'Accuracy': 0,
      'Damadge':  0,
      'name': 'D',
      'PreferedDamadgeType': 'None'
    },
    'Grass': {
      'Accuracy': -5,
      'Damadge': +5,
      'name': 'G',
      'PreferedDamadgeType': 'Melee'
    },
    'Stone': {
      'Accuracy': +5,
      'Damadge':  0,
      'name': 'S',
      'PreferedDamadgeType': 'Magic'
    },
}


class Tile:
    name = "Nothing"
    info = "a blank space"


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
    info = "Hard floor difficult to stand and manourver on"
    info2 = "Conducts magic very easily."
    Token = "S"

TokenTiles = [Mud, Dirt, Grass, Stone]
