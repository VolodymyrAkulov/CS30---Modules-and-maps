# Course: CS 30
# Period: 1
# Date created: 2/10/21
# Date last modified: 2/10/25
# Name: Volodymyr Akulov
# Description: RPG Game


HP = 20

from Enemy import Encounter
from map import Map
from menu import Menu


map = Map()
Menu()

encounter = Encounter()
encounter.print()


