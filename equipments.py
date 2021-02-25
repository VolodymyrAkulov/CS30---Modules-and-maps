# making a random equipment to give to the player for beating an enemy

import random

# Running the commad

level = 100

# Lists of prefixes weapons can have for game diversety

GoodModifier = ["Fine", "Murderous", "Antique", "Effective", "Massive"]
BadModifier = ["Not-quite-lethal", "Clumsy", "Strange", "Tiny"]

# List of types of damadge for a rock paper scissors style mechanic

TypesOfDamadge = [1, 2, 3]

# List of weapons for each type for game diversetye
Melee1 = ["Knife", "Axe", "Sickle", "Machete"]
Melee2 = ["Shortsword", "Longsword", "Broadsword"]

MeleeWeapons = Melee1 + Melee2

RangedWeapons = ["Longbow", "Crossbow", "Bow", "Flintlock", "Arquebus"]

MagicWeapons = ["Staff", "Spellbook", "Charm", "Scepter", "Wand", "Cards"]

# Function to make a new random equipment with an adjective, damadge type,
# weapon name, and a damadge value all randomized


def New_Offensive_Equipment(Level):

    # Defining variables

    global Adjective
    global TypeOfDamadge
    global TypeOfDamadgeName
    global Weapon
    global Damadge

    # Choosing a random weapon type
    TypeOfDamadge = random.choice(TypesOfDamadge)

    # Choosing an appropriate weapon name
    # Putting in placeholders for rock paper scisors mechanic

    if TypeOfDamadge == 1:
        TypeOfDamadgeName = "Melee"
        Weapon = random.choice(MeleeWeapons)
    elif TypeOfDamadge == 2:
        TypeOfDamadgeName = "Ranged"
        Weapon = random.choice(RangedWeapons)
    elif TypeOfDamadge == 3:
        TypeOfDamadgeName = "Magic"
        Weapon = random.choice(MagicWeapons)

    # Randomising damadge

    RandomDamadgeVariable = random.uniform(0.9, 1.1)
    Damadge = Level * RandomDamadgeVariable
    Damadge = int(Damadge)
    Damadge = str(Damadge)
    if RandomDamadgeVariable > 1.05:
        x = "☆  "
        y = " ☆"
        Adjective = random.choice(GoodModifier)
    elif RandomDamadgeVariable < 0.95:
        x = "💩  "
        y = " 💩"
        Adjective = random.choice(BadModifier)
    else:
        x = "  "
        y = "  "
        Adjective = ""
    # printing out weapon and its stats
    print("    " + x + "" + Adjective + " " + Weapon + y)
    print("\n Type of damadge: " + TypeOfDamadgeName)
    print("\n Damadge: " + Damadge)

# Executing a command
New_Offensive_Equipment(level)