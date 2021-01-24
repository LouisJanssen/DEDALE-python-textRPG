from Stats import PlayerStats
Player = PlayerStats()

def ChooseUpgrade(PlayerLevel):
    print('-======================================-')
    print('Bravo ! Vous venez de passer niveau', PlayerLevel, '.')
    print('Choisissez quelle statistique vous souhaitez augmenter :')
    print('[HP]', Player.Hp)
    print('[ATK]', Player.Atk)
    print('[CHA]', Player.Cha)
    Choice = input()
    if Choice.lower() == 'hp' :
        Player.Hp += 3
    elif Choice.lower() == 'atk' :
        Player.Atk += 3
    elif Choice.lower() == 'cha' :
        Player.Cha += 1
    else :
        print('[ERREUR] Veuillez entrer un choix valide.')
        ChooseUpgrade(PlayerLevel)
    Player.lvl = PlayerLevel
    print('-======================================-')

def LevelUp(XP, amount):
    XP += amount
    Player.xp += XP
    if Player.xp >= 25 :
        PlayerLevel = 2
        ChooseUpgrade(PlayerLevel)
    elif Player.xp >= 75 :
        PlayerLevel = 3
        ChooseUpgrade(PlayerLevel)
    elif Player.xp >= 150 :
        PlayerLevel = 4
        ChooseUpgrade(PlayerLevel)
    elif Player.xp >= 300 :
        PlayerLevel = 5
        ChooseUpgrade(PlayerLevel)

# LevelUp(XP, 25)