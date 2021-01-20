from Stats import *
Player = PlayerStats()
PlayerLevel = 1
XP = 0

def ChooseUpgrade():
    print('-======================================-')
    print('Bravo ! Vous venez de passer niveau', PlayerLevel, '.')
    print('Choisissez quelle statistique vous souhaitez augmenter :')
    print('[HP]', Player.Hp)
    print('[ATK]', Player.Atk)
    print('[STR]', Player.Str)
    print('[AGI]', Player.Agi)
    print('[INT]', Player.Int)
    print('[CHA]', Player.Cha)
    Choice = input()
    if Choice == 'HP' or Choice == 'hp' or Choice == 'Hp' :
        Player.Hp += 3
    elif Choice == 'ATK' or Choice == 'atk' or Choice == 'Atk' :
        Player.Atk += 3
    elif Choice == 'STR' or Choice == 'str' or Choice == 'Str' :
        Player.Str += 1
    elif Choice == 'AGI' or Choice == 'agi' or Choice == 'Agi' :
        Player.Agi += 1
    elif Choice == 'INT' or Choice == 'int' or Choice == 'Int' :
        Player.Int += 1
    elif Choice == 'CHA' or Choice == 'cha' or Choice == 'Cha' :
        Player.Cha += 1
    else :
        print('[ERREUR] Veuillez entrer un choix valide.')
        ChooseUpgrade()
    print('-======================================-')

def LevelUp(XP, amount):
    XP += amount
    if XP >= 25 :
        PlayerLevel = 2
        ChooseUpgrade()
    elif XP >= 75 :
        PlayerLevel = 3
        ChooseUpgrade()
    elif XP >= 150 :
        PlayerLevel = 4
        ChooseUpgrade()
    elif XP >= 300 :
        PlayerLevel = 5
        ChooseUpgrade()

LevelUp(XP, 25)