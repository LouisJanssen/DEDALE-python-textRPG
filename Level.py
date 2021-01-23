from Stats import *
Player = PlayerStats()
PlayerLevel = 1

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
    if Choice.lower() == 'hp' :
        Player.Hp += 3
    elif Choice.lower() == 'atk' :
        Player.Atk += 3
    elif Choice.lower() == 'str' :
        Player.Str += 1
    elif Choice.lower() == 'agi' :
        Player.Agi += 1
    elif Choice.lower() == 'int' :
        Player.Int += 1
    elif Choice.lower() == 'cha' :
        Player.Cha += 1
    else :
        print('[ERREUR] Veuillez entrer un choix valide.')
        ChooseUpgrade()
    print('-======================================-')

def LevelUp(XP, amount):
    print(XP)
    print(amount)
    XP += amount
    Player.xp += XP
    if Player.xp >= 25 :
        PlayerLevel = 2
        ChooseUpgrade()
    elif Player.xp >= 75 :
        PlayerLevel = 3
        ChooseUpgrade()
    elif Player.xp >= 150 :
        PlayerLevel = 4
        ChooseUpgrade()
    elif Player.xp >= 300 :
        PlayerLevel = 5
        ChooseUpgrade()

# LevelUp(XP, 25)