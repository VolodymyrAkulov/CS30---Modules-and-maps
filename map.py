import Dictionary
import random

# creates and prints out map

map = []
for i in range(25):
    map.append(random.choice(Dictionary.TokenTiles))
  
class Map:
    def __init__(self):
        self.position = 0
        
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

    def print(self):
        print(
            self.formatted_map.format(
                *(
                    f"[{x.Token}]" if i == self.position else f' {x.Token} '
                    for i, x in enumerate(map)
                )
            )
        )

        tile = map[self.position]

        print(f"You are currently standing on {tile.name}")
        print(f"{tile.info}\n{tile.info2}")
