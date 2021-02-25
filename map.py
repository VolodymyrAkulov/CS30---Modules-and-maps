import Tiles
import random

# creates and prints out map


class Map:
    def __init__(self):
        self.position = 0
        self.map = []
        for i in range(25):
            self.map.append(random.choice(Tiles.TokenTiles))
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
            "╚═════╩═════╩═════╩═════╩═════╝   \n"
        )

    def print(self):
        print(
            self.formatted_map.format(
                *(
                    f"[{x.Token}]" if i == self.position else f' {x.Token} '
                    for i, x in enumerate(self.map)
                )
            )
        )

        tile = self.map[self.position]

        print(f"You are currently standing on {tile.name}")
        print(f"{tile.info}\n{tile.info2}")
