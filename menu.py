# Course: CS 30
# Period: 1
# Date created: 21/02/10
# Date last modified: 21/02/10
# Name: Janice Cotcher
# Description: Continous gameplay

from map import Map
map = Map()

from GlobalVar import p

# Map menu
def MapMenu():
    """Function displays map menu"""
    while True:
        print("\n" + 18 * "-" + "Map" + 18 * "-")
        map.print()
        print(40 * "-")
        x = input("North\nSouth\nWest\nEast\n\nExit\n\n")
        x = x.lower()
        if x == "north" and p.pos > 4:
            p.pos = p.pos - 5 
            print(f"\nYou moved {x}")
        elif x == "south" and p.pos < 20:
            p.pos = p.pos + 5 
            print(f"\nYou moved {x}")
        elif x == "west" and p.pos != 0 and p.pos != 5 and\
            p.pos != 10 and p.pos != 15 and p.pos != 20 :
                p.pos = p.pos - 1 
                print(f"\nYou moved {x}")
        elif x == "east" and p.pos != 4 and p.pos != 9 and\
            p.pos != 14 and p.pos != 19 and p.pos != 24 :
                p.pos = p.pos + 1 
                print(f"\nYou moved {x}")
        elif x == "exit":
            print(p.pos)
            break
        else:
            print("Thats not a direction you can move in try again")


# Inventory menu
def InvMenu():
    while True:
        print(("\n" + 15 * "-" + "Inventory" + 15 * "-"))
        x = input("Armour\nHealing\nWeapons\nTraps\n\nExit\n\n")
        x = x.lower()
        if x == "armour" or x == "armor":
            print("\nDisplays Armour")
        elif x == "healing":
            print("\nDisplays Healing items")
        elif x == "traps":
            print("\nDisplays Traps")
        elif x == "weapons":
            print("\nDisplays Weapons")
        elif x == "exit":
            break
        else:
            print("\nInvalid action try again")


# Main menu
def Menu():
  while True:
      print(15*"-"+"Main Menu"+15*"-")
      x = input("Inventory\nMap\nQuit\nInteract\n\nExit\n\n")
      if x.lower() == "inventory":
          InvMenu()
      elif x.lower() == "map":
          MapMenu()
      elif x.lower() == "quit":
          break
      elif x.lower() == "interact":
          print("\nYou interacted with the environment")
      elif x.lower() == "exit":
          print(p.pos)
          break
      else:
          print("\nInvalid action try again")
