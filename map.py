# Course: CS 30
# Period: 1
# Date created: 2/10/21
# Date last modified: 2/10/25
# Name: Volodymyr Akulov
# Description: Modules and maps

import random

import Dictionary
from GlobalVar import p
from termcolor import colored

# creates and prints out map

map = []
EnemyPos = []
p.pos = 0

for i in range(25):
    map.append(random.choice(Dictionary.TokenTiles))

for i in range(random.randint(5, 10)):
    EnemyPos.append(random.randint(0, 24))


class Map:
    def __init__(self):

        self.formatted_map = (
            "╔═══════╦═══════╦═══════╦═══════╦═══════╗\n"
            "║       ║       ║       ║       ║       ║\n"
            "║ {} ║ {} ║ {} ║ {} ║ {} ║               \n"
            "║       ║       ║       ║       ║       ║\n"
            "╠═══════╬═══════╬═══════╬═══════╬═══════╣\n"
            "║       ║       ║       ║       ║       ║\n"
            "║ {} ║ {} ║ {} ║ {} ║ {} ║               \n"
            "║       ║       ║       ║       ║       ║\n"
            "╠═══════╬═══════╬═══════╬═══════╬═══════╣\n"
            "║       ║       ║       ║       ║       ║\n"
            "║ {} ║ {} ║ {} ║ {} ║ {} ║               \n"
            "║       ║       ║       ║       ║       ║\n"
            "╠═══════╬═══════╬═══════╬═══════╬═══════╣\n"
            "║       ║       ║       ║       ║       ║\n"
            "║ {} ║ {} ║ {} ║ {} ║ {} ║               \n"
            "║       ║       ║       ║       ║       ║\n"
            "╠═══════╬═══════╬═══════╬═══════╬═══════╣\n"
            "║       ║       ║       ║       ║       ║\n"
            "║ {} ║ {} ║ {} ║ {} ║ {} ║               \n"
            "║       ║       ║       ║       ║       ║\n"
            "╚═══════╩═══════╩═══════╩═══════╩═══════╝  "
        )
        self.tile = map[p.pos]

    def print(self):

        def form(i, x):
            if i in EnemyPos and i == p.pos:
                return f"[֎{x}֎]"
            elif i == p.pos:
                return f" [{x}] "
            elif i in EnemyPos:
                return f" ֎{x}֎ "
            else:
                return f"  {x}  "

        print(self.formatted_map.format(*(form(i, x.Token)
                                          for i, x in enumerate(map))))

        print(17 * "-" + "Legend" + 17 * "-")
        print(
            f"{colored('M','blue')} - Mud     \n"
            f"{colored('D','white')} - Dirt   \n"
            f"{colored('G','green')} - Grass  \n"
            f"{colored('S','red')} - Stone    \n"
            "֎ - Enemy"
        )

        print(40 * "-")
        tile = map[p.pos]
        self.tile = map[p.pos]

        print(f"You are currently standing on {tile.name}")
        print(f"{tile.info}\n{tile.info2}")
        return tile
