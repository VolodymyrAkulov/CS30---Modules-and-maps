# Course: CS 30
# Period: 1
# Date created: 10/02/2021
# Date last modified: 28/02/2021
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


