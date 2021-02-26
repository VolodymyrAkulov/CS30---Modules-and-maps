# Course: CS 30
# Period: 1
# Date created: 2/10/21
# Date last modified: 2/10/25
# Name: Volodymyr Akulov
# Description: Modules and maps

import Dictionary
import random
from GlobalVar import p

# creates and prints out map

map = []
for i in range(25):
    map.append(random.choice(Dictionary.TokenTiles))

p.position = 0
p.pos = p.position

class Map:
    def __init__(self):
        

        self.formatted_map = (
            "╔═════╦═════╦═════╦═════╦═════╗   \n"
            "║ {} ║ {} ║ {} ║ {} ║ {} ║        \n"
            "╠═════╬═════╬═════╬═════╬═════╣   \n"
            "║ {} ║ {} ║ {} ║ {} ║ {} ║        \n"
            "╠═════╬═════╬═════╬═════╬═════╣   \n"
            "║ {} ║ {} ║ {} ║ {} ║ {} ║        \n"
            "╠═════╬═════╬═════╬═════╬═════╣   \n"
            "║ {} ║ {} ║ {} ║ {} ║ {} ║        \n"
            "╠═════╬═════╬═════╬═════╬═════╣   \n"
            "║ {} ║ {} ║ {} ║ {} ║ {} ║        \n"
            "╚═════╩═════╩═════╩═════╩═════╝     "
        )
        self.tile = map[p.pos]
        
    
    def print(self):
        
        print(
            self.formatted_map.format(
                *(
                    f"[{x.Token}]" if i == p.pos else f' {x.Token} '
                    for i, x in enumerate(map)
                )
            )
        )

        print(p.pos)
        tile = map[p.pos]
        self.tile = map[p.pos]

        print(f"You are currently standing on {tile.name}")
        print(f"{tile.info}\n{tile.info2}")
        return tile

