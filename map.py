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


class Yes:
    YN = "E"


class No:
    YN = " "


YN = [Yes, No]

for i in range(25):
    map.append(random.choice(Dictionary.TokenTiles))
    EnemyPos.append(random.choice(YN))

p.position = 0
p.pos = p.position


class Map:
    def __init__(self):

        self.formatted_map = (
            "╔═══════╦═══════╦═══════╦═══════╦═══════╗            \n"
            "║       ║       ║       ║       ║       ║            \n"
            "║ {} ║ {} ║ {} ║ {} ║ {} ║                           \n"
            "║       ║       ║       ║       ║       ║            \n"
            "╠═══════╬═══════╬═══════╬═══════╬═══════╣            \n"
            "║       ║       ║       ║       ║       ║            \n"
            "║ {} ║ {} ║ {} ║ {} ║ {} ║                           \n"
            "║       ║       ║       ║       ║       ║            \n"
            "╠═══════╬═══════╬═══════╬═══════╬═══════╣            \n"
            "║       ║       ║       ║       ║       ║            \n"
            "║ {} ║ {} ║ {} ║ {} ║ {} ║                           \n"
            "║       ║       ║       ║       ║       ║            \n"
            "╠═══════╬═══════╬═══════╬═══════╬═══════╣            \n"
            "║       ║       ║       ║       ║       ║            \n"
            "║ {} ║ {} ║ {} ║ {} ║ {} ║                           \n"
            "║       ║       ║       ║       ║       ║            \n"
            "╠═══════╬═══════╬═══════╬═══════╬═══════╣            \n"
            "║       ║       ║       ║       ║       ║            \n"
            "║ {} ║ {} ║ {} ║ {} ║ {} ║                           \n"
            "║       ║       ║       ║       ║       ║            \n"
            "╚═══════╩═══════╩═══════╩═══════╩═══════╝              "
        )
        self.tile = map[p.pos]

    def print(self):

        Aformat = self.formatted_map.format(
            *(
                f"[֎{x.Token}֎]"
                if "E" == EnemyPos[i].YN and i == p.pos
                else "{}"
                for i, x in enumerate(map)
            )
        )

        Bformat = Aformat.format(
            *(
                f" [{x.Token}] " if i == p.pos else "{}"
                for i, x in enumerate(map)
            )
        )

        Cformat = Bformat.format(
            *(
                f" ֎{x.Token}֎ "
                if "E" == EnemyPos[i].YN and i != p.pos
                else "{}"
                for i, x in enumerate(map)
            )
        )

        print(
            Cformat.format(
                *(
                    f"  {x.Token}  "
                    if i != EnemyPos[i].YN and i != p.pos
                    else "{}"
                    for i, x in enumerate(map)
                )
            )
        )
        print(17 * "-" + "Legend" + 17 * "-")
        print(
            f"{colored('M','blue')} - Mud     \n"
            f"{colored('D','white')} - Dirt   \n"
            f"{colored('G','green')} - Grass  \n"
            f"{colored('S','red')} - Stone      "
        )

        print(40 * "-")
        tile = map[p.pos]
        self.tile = map[p.pos]

        print(f"You are currently standing on {tile.name}")
        print(f"{tile.info}\n{tile.info2}")
        return tile
