import random
import Dictionary
from termcolor import colored
from map import Map
from GlobalVar import p
map = Map()


Dmg = 100
Hp = 100
S = ''
YType = 'MGC'


class Encounter:
    def __init__(self):
        self.position = p.pos
        self.formatted_encounter = (
            "       ╔═════╦═════╦═════╦═════╗                     \n"
            "       ║{q}  ║  {one} ║ {two} ║ {w}║                 \n"
            "       ║{DL}{DMG} ║{L}{HP} ║{EL}{EHP} ║{EDL}{EDMG} ║ \n"
            "       ╠═════╬═════╩═════╬═════╣                     \n"
            "       ║{e} ║ {S} {ADV}   ║ {r}║                     \n"
            "       ║ {T} ║           ║ {ET} ║                    \n"
            "       ╚═════╝ {D} {TER}   ╚═════╝                   \n"
            "                                                     \n"
        )
    
    def SetupFight():
        global HpLength, EHpLength, Enemy, DmgLength
        global EDmgLength, Dmg, Hp, YType, ADV, S, TER, D

        Enemy = random.choice(Dictionary.EnemyList)

        HpLength = ((4-len(str(Hp)))*" ")
        DmgLength = ((4-len(str(Dmg)))*" ")

        EHpLength = ((4-len(str(Enemy.Hp)))*" ")
        EDmgLength = ((4-len(str(Enemy.Dmg)))*" ")

        if YType == 'MGC' and Enemy.TypeDmg == 'MEL' or\
                YType == 'RGD' and Enemy.TypeDmg == 'MGC' or\
                    YType == 'MEL' and Enemy.TypeDmg == 'RGD':
            ADV = colored('ADV', 'green')
            S = '   '
        elif YType == Enemy.TypeDmg:
            ADV = 'None'
            S = '  '
        else:
            ADV = colored('DisADV', 'red')

        if map.tile.name == 'Mud' and YType == 'RGD':
            Dmg = 2 * Dmg
            TER = colored('ADV', 'green')
            D = '   '
        elif map.tile.name == 'Stone' and YType == 'MGC':
            Dmg = 2*Dmg
            TER = colored('ADV', 'green')
            D = '   '
        elif map.tile.name == 'Grass' and YType == 'MEL':
            Dmg = 2*Dmg
            TER = colored('ADV', 'green')
            D = '   '
        else:
            TER = ''
            D = 6 * ' '

    def print(self):
        print(16 * "-" + Enemy.Name + 16 * "-")
        print(
            self.formatted_encounter.format(
                L=HpLength,
                HP=Hp,

                DMG=Dmg,
                DL=DmgLength,

                EHP=Enemy.Hp,
                EL=EHpLength,

                EDMG=Enemy.Dmg,
                EDL=EDmgLength,

                T=YType,
                ET=Enemy.TypeDmg,


                ADV=ADV,
                r=colored('Type', 'red'),
                two=colored('EHP', 'red'),
                w=colored('EDMG', 'red'),
                one=colored('HP', 'green'),
                q=colored('DMG', 'green'),
                e=colored('Type', 'green'),
                S=S,
                TER=TER,
                D=D

            )
        )
