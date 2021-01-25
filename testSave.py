#Import of tools needed
import sys
import time
import os
import pickle

def DiceRoll() :
  import random
  D = random.randint(1,20)
  return D

def promptSlow(phrase):
  for l in phrase:
    sys.stdout.write(l)
    sys.stdout.flush()
    time.sleep(Player.textspeed)
  print('')

def Curse(Cursetype):
  if Cursetype == 'Vines':
    promptSlow('Vous subissez : HP - 1 et ATK - 1')
    Player.Hp = Player.Hp - 1
    Player.Str = Player.Atk - 1
  elif Cursetype == 'Flower':
    promptSlow('Vous subissez : CHA + 1 et HP - 2')
    Player.Cha = Player.Cha + 1
    Player.Hp = Player.Hp - 2

def Blessing(Blesstype):
  if Blesstype == 'Styx':
    promptSlow('Vous gagnez : HP + 5')
    Player.Hp = Player.Hp + 5
  elif Blesstype == 'Work':
    promptSlow('Vous gagnez : ATK + 5')
    Player.Atk = Player.Atk + 5

class PlayerStats:
  def __init__(self):
    self.name = "Bob"
    self.Hp = 10
    self.Atk = 3
    self.Cha = 5
    self.pos = 'F3'
    self.dead = False
    self.lvl = 1
    self.xp = 0
    self.father = "Zeus"
    self.textspeed = 0.02

Player = PlayerStats()

#======================================================================================
# Library monsters and stats

MOBNAME = 'MOBNAME'
HP = 'HP'
ATK = 'ATK'
XP = 'XP'

MobStats = {
  'ChickenStats':{
    MOBNAME: 'Poule',
    HP: 1,
    ATK: 0,
    XP: 10,
  },
  'SpiderStats':{
    MOBNAME: 'Arraignée mécanique',
    HP: 5,
    ATK: 3,
    XP: 20,
  },
  'BoarStats':{
    MOBNAME: 'Sanglier',
    HP: 8,
    ATK: 5,
    XP: 30,
  },
  'HydraStats':{
    MOBNAME: 'Hydre',
    HP: 15,
    ATK: 10,
    XP: 50,
  },
  'SirensStats':{
    MOBNAME: 'Sirène',
    HP: 10,
    ATK: 10,
    XP: 40,
  },
  'CyclopStats':{
    MOBNAME: 'Cyclope',
    HP: 15,
    ATK: 15,
    XP: 60,
  },
  'LestrygonStats':{
    MOBNAME: 'Lestrygon',
    HP: 10,
    ATK: 15,
    XP: 50,
  },
  'MinotaurStats':{
    MOBNAME: 'Minotaure',
    HP: 50,
    ATK: 25,
    XP: 0,
  },
}

# Test = MobStats['CyclopStats'][HP]
# print(Test)

# SAVE PLAYER STATS
class SavePlayerStats:
    def __init__(self):
        self.Hp = 10
SaveHp = Player.Hp
SavePlayer = SavePlayerStats()
SavePlayer.Hp = SaveHp

# COMBAT
PlayerTurn = True

def Combat(PlayerTurn, ennemy, playerdefense):

    PlayerDefense = playerdefense

    def useObject():
        SLOT = 'SLOT'
        QUANTITY = 'QUANTITY'
        promptSlow("Quel objet souhaitez vous utiliser ?")
        promptSlow('Entrez "retour" pour revenir au menu de combat')
        InventoryList = ['','','','','']
        for i in range(0,5):
            InventoryList[i] = Inventory[('slot' + str(i + 1))][SLOT]
        print(InventoryList)
        ask = input(' > ')
        if ask in InventoryList:
            if ask.lower() == 'ambroisie':
                promptSlow('Vous buvez l\'ambroisie')
                Player.Hp += 10
                i = 1
                while Inventory[('slot' + str(i))][SLOT] != 'ambroisie':
                    i += 1
                Inventory[('slot' + str(i))][QUANTITY] = str(int(Inventory[('slot' + str(i))][QUANTITY]) - 1)
                if Inventory[('slot' + str(i))][QUANTITY] == '0':
                    Inventory[('slot' + str(i))][SLOT] = 'empty'
            elif ask.lower() == 'feu sacré':
                promptSlow('Vous lancer le feu sacré')
                ennemy.Hp -= 10
                i = 1
                while Inventory[('slot' + str(i))][SLOT] != 'feu sacré':
                    i += 1
                Inventory[('slot' + str(i))][QUANTITY] = str(int(Inventory[('slot' + str(i))][QUANTITY]) - 1)
                if Inventory[('slot' + str(i))][QUANTITY] == '0':
                    Inventory[('slot' + str(i))][SLOT] = 'empty'
            else:
                print('Veuillez choisir un consommable : "feu sacré" ou "ambroisie"')
                useObject()
        elif ask.lower() == 'retour':
            Combat(PlayerTurn, ennemy, playerdefense)
        else:
            print('Commande inconnue')
            useObject()


    print('-----------------------------------------------------------------------')

    if (Player.Hp > 0) and (ennemy.Hp > 0) :

        if PlayerTurn == False : # TOUR DE L'ADVERSAIRE
            print('Tour de l\'adversaire')
            PlayerTurn = True
            if ennemy.Hp > 0 :
                print('L\'ennemi fait son action')
                
                # Action de l'adversaire
                # L'ennemi attaque
                MobAttack = DiceRoll()
                print('Lancer de dé ennemi :', MobAttack) # Est-ce qu'on l'affiche ?
                if MobAttack >= 10 : 
                    if PlayerDefense == False :
                        if ennemy.name == 'Minotaure' and ennemy.Hp <= 20 :
                            print('Astérion récupère une partie de l\'énergie vitale du labyrinthe pour se soigner.')
                            ennemy.Hp += 10
                        else :
                            print('L\'ennemi attaque !')
                            Player.Hp -= ennemy.Atk
                    elif PlayerDefense == True :
                        print('L\'ennemi perce légèrement votre défense !')
                        InventoryList = ['','','','','']
                        SLOT = 'SLOT'
                        for i in range(0,5):
                            InventoryList[i] = Inventory[('slot' + str(i + 1))][SLOT]
                        if 'shield' not in InventoryList:
                            Player.Hp -= (3/4)*(ennemy.Atk) # Les dégâts sont réduits de 3/4 si le joueur se défend
                else :
                    print('L\'ennemi a loupé !')

            else :
                print('L\'ennemi est K.O.')
            
            Combat(PlayerTurn, ennemy, playerdefense)

        elif PlayerTurn == True : # TOUR DU JOUEUR
            print('Joueur :', Player.name, '-', Player.Hp, 'PV')
            print('ENNEMI :', ennemy.name, '-', ennemy.Hp, 'PV')
            print(']===================================[')
            print('1 - ATTAQUER')
            print('2 - SE DÉFENDRE')
            print('3 - OBJETS')
            print(']===================================[')
            Action = input(' > ')

            if Action == '1' :
                print('Le Joueur attaque')
                PlayerDefense = False
                playerdefense = PlayerDefense
                PlayerTurn = False
                Attack = DiceRoll()
                print('Lancer de dé :', Attack)
                if Attack >= 10 : # Modifier plus tard en fonction des stats du joueur
                    ennemy.Hp -= Player.Atk # Ajouter plus tard les bonus relatifs à la STR
                else :
                    print('Loupé !')
                Combat(PlayerTurn, ennemy, playerdefense)

            elif Action == '2' :
                print('Se défendre')
                PlayerDefense = True
                playerdefense = PlayerDefense
                PlayerTurn = False
                # Se défendre : Diminue de 3/4 la prochaine attaque ennemie
                Combat(PlayerTurn, ennemy, playerdefense)

            elif Action == '3' :
                print('Objets')
                # Afficher liste des objets présents dans l'inventaire
                useObject()
                PlayerTurn = False
                Combat(PlayerTurn, ennemy, playerdefense)
            else:
                print("ERREUR : Veuillez entrer le chiffre correspondant à l\'une des questions posées.")
                Combat(PlayerTurn, ennemy, playerdefense)
    
    elif Player.Hp <= 0 :
        print('GAME OVER')
        Player.dead = True
        time.sleep(1)
        sys.exit()
    
    elif (Player.Hp > 0) and (ennemy.Hp <= 0) :
        if ennemy.name == 'Minotaure':
            print('FÉLICITATIONS : vous avez vaincu le Minotaure !')
            print('-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-')
            promptSlow('À vos pieds git le corps immense du Minotaure. Tandis que le labyrinthe s\'écroule peu à peu autour de vous, vous l\'observez longuement, partagé entre le soulagement et un sentiment étrange. Alors que vous vous apprêtez à lui tourner le dos, vous entendez un nouveau soufflement s\'échapper de ses narines. Sur votre garde, vous fixez son visage, prêt à attaquer au moindre mouvement. C\'est alors qu\'un détail qui vous a échappé jusque-là vous saute aux yeux. Vous reconnaissez la tristesse et l\'intelligence infinies qui émanent de son regard. Vous posez votre paume sur le front de la créature et, tandis qu\'une larme coule le long de votre joue, lui adressez ces ultimes mots :')
            print('')
            promptSlow('"Adieu, Dédale".')
            print('')
            print('<>===============================================================<>')
            print('Merci d\'avoir joué !')
            print('Voulez-vous retourner au menu principal ou quitter le jeu ?')
            print('<>===============================================================<>')
            ask = input(" > ")
            while not (ask.lower() == 'menu' or ask.lower() == 'quitter'):
                print('Commande inconnue, veuillez entrer "menu" ou "quitter"')
                ask = input(' > ')
            if ask.lower() == 'menu':
                PrintMainMenu()
                MainMenu()
            elif ask.lower() == 'quitter':
                print('Merci d\'avoir joué !')
                time.sleep(1)
                sys.exit()
        else:
            print('VICTOIRE')

def StartCombat(currentennemy):

    # SAVE MOB STATS
    class EnnemyStats:
        def __init__(self):
            self.name = MobStats[currentennemy][MOBNAME]
            self.Hp = MobStats[currentennemy][HP]
            self.Atk = MobStats[currentennemy][ATK]
    
    # COMBAT
    Combat(PlayerTurn, EnnemyStats(), False)

    # RESET PLAYER STATS (Mob stats reset automatically)
    Player.Hp = SavePlayer.Hp
    PlayerXP = Player.xp
    MobXP = MobStats[currentennemy][XP]
    LevelUp(PlayerXP, MobXP)

# StartCombat('MinotaurStats')
# StartCombat('ChickenStats')

#Initialisation of variables
OBJECTNAME = 'objectname'
DESCRIPTION = 'description'
EFFECT = 'effect'

# from Stats import PlayerStats
# Player = PlayerStats()

#Library for objects
Objects = {
          'ambroisie':{
            OBJECTNAME: 'Ambroisie',
            DESCRIPTION: 'la boisson des dieux',
            EFFECT: 'Rends 10 HP',
          },
          'shield':{
            OBJECTNAME: 'BOUCLIER DE PERSEE',
            DESCRIPTION: 'Un bouclier mythique ayant apartenu à Persée',
            EFFECT: 'Vous permet de bloquer l\'intégralité des combats',
          },
          'massue':{
            OBJECTNAME: 'MASSUE D\'HERACLES',
            DESCRIPTION: 'Une massue ayant appartenu à un héros mythique',
            EFFECT: 'Augmente l\'attaque de 2',
          },
          'feu sacré':{
            OBJECTNAME: 'FEU SACRE',
            DESCRIPTION: 'Vous pouvez le lancer pour infliger des dégâts',
            EFFECT: 'Inflige des dégâts à l\'ennemi.',
          },
          'ceinture':{
            OBJECTNAME: 'CEINTURE D\'APHRODITE',
            DESCRIPTION: 'Une ceinture vous permettant d\'envouter n\'importe quel mortel',
            EFFECT: 'Augmente le charisme de 5',
          },
          'empty':{
            OBJECTNAME: 'vide',
            DESCRIPTION: 'vide',
            EFFECT: '',
          },
}

SLOT = 'SLOT'
QUANTITY = 'QUANTITY'

#Library for inventory
Inventory = {
            'slot1':{
              SLOT:'feu sacré',
              QUANTITY:'1',
            },
            'slot2':{
              SLOT:'ambroisie',
              QUANTITY:'1',
            },
            'slot3':{
              SLOT:'empty',
              QUANTITY:'0',
            },
            'slot4':{
              SLOT:'empty',
              QUANTITY:'0',
            },
            'slot5':{
              SLOT:'empty',
              QUANTITY:'0',
            },
}

def ObjectInventory(objectName):
  InventoryList = ['','','','','']
  for i in range(0,5):
    InventoryList[i] = Inventory[('slot' + str(i + 1))][SLOT]
  print('Ou souhaitez vous placer l\'objet ? 1, 2, 3, 4 ou 5 ?')
  print(InventoryList)
  ask = input(' > ')
  if (ask == '1' or ask =='2' or ask =='3' or ask == '4' or ask == '5'):
    if Inventory[('slot' + ask)][SLOT] == 'empty':
      Inventory[('slot' + ask)][SLOT] = objectName
      Inventory[('slot' + ask)][QUANTITY] = str(int(Inventory[('slot' + ask)][QUANTITY]) + 1)
    elif Inventory[('slot' + ask)][SLOT] == objectName:
      Inventory[('slot' + ask)][QUANTITY] = str(int(Inventory[('slot' + ask)][QUANTITY]) + 1)
    else:
      print("Voulez vous remplacer : " + Objects[Inventory[('slot' + ask)][SLOT]][OBJECTNAME])
      print("oui/non")
      ask2 = input(' > ')
      while not (ask2.lower() == 'oui' or ask2.lower() == 'non'):
        print('Veuillez entrer soit "oui" soit "non"')
        ask2 = input(' > ')
      if ask2.lower() == 'oui':
        Inventory[('slot' + ask)][SLOT] = objectName
        Inventory[('slot' + ask)][QUANTITY] = '1'
      elif ask2.lower() == 'non':
        ObjectInventory(objectName)
  else:
    print('Commande inconnue, veuillez choisir entre les emplacements : 1, 2, 3, 4 ou 5.')
    ObjectInventory(objectName)

def displayInventory():
  promptSlow('Voici votre inventaire :')
  InventoryList = ['','','','','']
  for i in range(0,5):
    InventoryList[i] = Inventory[('slot' + str(i + 1))][SLOT]
  print(InventoryList)
  promptSlow('Quel objet voulez vous examinez ?')
  promptSlow('Emplacement 1, 2, 3, 4 ou 5. Pour reveniren arrière entrez "retour"')
  ask = input(' > ')
  if ask in ['1', '2', '3', '4', '5']:
    ObjPlace = Inventory[('slot' + str(ask))][SLOT]
    ObjName = 'Objet : ' + Objects[ObjPlace][OBJECTNAME]
    ObjDesc = 'Description : ' + Objects[ObjPlace][DESCRIPTION]
    ObjEffect = 'Effet : ' + Objects[ObjPlace][EFFECT]
    promptSlow(ObjName)
    promptSlow(ObjDesc)
    promptSlow(ObjEffect)
    time.sleep(1)
  elif ask == 'retour':
    prompt()
  else:
    print('Commande inconnue essayez : "1", "2", "3", "4", "5", ou "retour"')

def passiveObject():
  InventoryList = ['','','','','']
  for i in range(0,5):
    InventoryList[i] = Inventory[('slot' + str(i + 1))][SLOT]
  if "massue" in InventoryList and massueUsed == False :
    massueUsed = True
    Player.Atk += 2
  elif "ceinture" in InventoryList and ceintureUsed == False :
    ceintureUsed = True
    Player.Cha += 5

# def useObject():
#   promptSlow("Quel objet souhaitez vous utiliser ?")
#   InventoryList = ['','','','','']
#   for i in range(0,5):
#     InventoryList[i] = Inventory[('slot' + str(i + 1))][SLOT]
#   print(InventoryList)
#   ask = input(' > ')
#   if ask in InventoryList:
#     if ask == 'ambroisie':
#       promptSlow('Vous buvez l\'ambroisie')
#       Player.Hp += 10
#     elif ask == 'feu sacré':
#       promptSlow('Vous lancer le feu sacré')

# --------------  ZONE DE TEST  ------------------
# def testInventory():
#   print(Objects)
#   print('---------------')
#   print(Inventory)
#   print('---------------')
#   i = 1
#   if Inventory[('slot' + str(i))] == 'empty':
#     Inventory[('slot' + str(i))] = 'ambroisie'
#   print(Inventory)

# def testUse(objectUsed):
#   print('avant' + str(Player.Hp))
#   if objectUsed == 'ambroisie':
#     Player.Hp += 10
#   print('après' + str(Player.Hp))


# i = 1 
# testInventory()
# testUse(Inventory[('slot' + str(i))])

# ObjectInventory('ambroisie')

# displayInventory()

# GERER LE NOM DES OBJETS
# Objects[Inventory[('slot' + str(i + 1))][SLOT]][NAME]


# function for slow prompt of prints
# def promptSlow(phrase):
#   for l in phrase:
#     sys.stdout.write(l)
#     sys.stdout.flush()
#     time.sleep(0.03)
#   print('')

# display of the menu
def PrintMainMenu():
  os.system('clear')
  print('-------------------------')
  print('DEDALE')
  print('-------------------------')
  print('')
  print('JOUER')
  # print('CHARGER')
  print('INSTRUCTIONS')
  print('OPTIONS')
  print('CREDITS')
  print('QUITTER')
  print('')
  print('____________________________________________________________')

#PLay menu
def PlayMenu():
  print('JOUER')
  print('CONTINUER')
  print('')
  ChoiceMainMenu = input(' > ')
  if ChoiceMainMenu.lower() == 'jouer' :
    Question1(0, 0, 0)
  elif ChoiceMainMenu.lower() == 'continuer' :
    if os.path.isfile("SaveFile") :
      loadGame()
    else :
      promptSlow("Aucun fichier de sauvegarde trouvé.")
      PlayMenu()
  else:
    print('Commande inconnue, essayez de rentrer une des instructions présente sur le menu.')
    PlayMenu()

#Load menu
# def LoadMenu():
#   print('SAUVEGARDE 1')
#   print('SAUVEGARDE 2')
#   print('SAUVEGARDE 3')
#   print('RETOUR')
#   print('')
#   print('____________________________________________________________')

# instructions menu
def InstructionsMenu():
  print('INSTRUCTIONS :')
  promptSlow('Le but du jeu est d\'atteindre le boss et de le vaincre, pour ce faire vous aurez à l\'écran différents choix à faire que ce soit pour les déplacements, les choix de dialogue ou encore les combats.')
  promptSlow('Pour effectuer une action entrez simplement ce que vous souhaitez faire dans le terminal')
  promptSlow('Pour obtenir une liste des commandes en jeux entrez : aide')
  print('')
  print('RETOUR')
  print('')
  ChoiceMainMenu = input(' > ')
  while ChoiceMainMenu != 'retour':
    print('Commande inconnue essayez "retour"')
    ChoiceMainMenu = input(' > ')
  if ChoiceMainMenu.lower() == 'retour' :
    PrintMainMenu()
    MainMenu()

# Options menu
def OptionsMenu():
  print('OPTIONS :')
  print('Choisissez la vitesse de défilement du texte :')
  print('1 - Vitesse 1 : rapide')
  print('2 - Vitesse 2 : moyen')
  print('3 - Vitesse 3 : lent')
  print('')
  print('RETOUR')
  print('')
  ask = input(' > ')
  while not (ask.lower() == '1' or ask.lower() == '2' or ask.lower() == '3' or ask.lower() == 'retour'):
    print('Commande inconnue veuillez rentrez "1", "2", "3", ou "retour"')
    ask = input(' > ')
  if ask.lower() == '1':
    Player.textspeed = 0
    promptSlow('Voilà une phrase exemple pour voir si la vitesse de défilement sélectionnée vous convient.')
    time.sleep(1)
    OptionsMenu()
  elif ask.lower() == '2':
    Player.textspeed = 0.02
    promptSlow('Voilà une phrase exemple pour voir si la vitesse de défilement sélectionnée vous convient.')
    time.sleep(1)
    OptionsMenu()
  elif ask.lower() == '3':
    Player.textspeed = 0.05
    promptSlow('Voilà une phrase exemple pour voir si la vitesse de défilement sélectionnée vous convient.')
    time.sleep(1)
    OptionsMenu()
  elif ask.lower() == 'retour':
    PrintMainMenu()
    MainMenu()

#credits menu
def CreditsMenu():
  promptSlow('Code : Louis Janssen & François Olona')
  promptSlow('Histoire : Louis Janssen & François Olona')
  promptSlow('Map inspirée de : https://www.youtube.com/watch?v=ERLT1iU0DVY&list=PL1-slM0ZOosXf2oQYZpTRAoeuo0TPiGpm&index=3&ab_channel=BryanTong')
  promptSlow('Ressources pédagogiques : https://courspython.com/classes-et-objets.html et https://docs.python.org/fr/3/library/index.html')
  promptSlow('Utilisation de pickle : https://www.geeksforgeeks.org/understanding-python-pickling-example/')
  promptSlow('Remerciements : Monsieur Loïc Janin')
  print('RETOUR')
  print('Appuyez sur la touche correspondante')
  ChoiceMainMenu = input()
  while ChoiceMainMenu != 'retour':
    print('Commande inconnue essayez "retour"')
    ChoiceMainMenu = input(' > ')
  if ChoiceMainMenu.lower() == 'retour' :
    PrintMainMenu()
    MainMenu()
  print('____________________________________________________________')

#main function for the main menu
def MainMenu ():
  ChoiceMainMenu = input(' > ')
  if ChoiceMainMenu.lower() == 'jouer' :
    PlayMenu()
  # elif ChoiceMainMenu.lower() == 'charger' :
  #   LoadMenu()
  elif ChoiceMainMenu.lower() == 'instructions' :
    InstructionsMenu()
  elif ChoiceMainMenu.lower() in ['options', 'option'] :
    OptionsMenu()
  elif ChoiceMainMenu.lower() in ['credits', 'crédits']:
    CreditsMenu()
  elif ChoiceMainMenu.lower() == 'quitter' :
    print('PERSONNE NE S\'ECHAPPE DU LABYRINTHE !')
    time.sleep(2)
    PrintMainMenu()
    MainMenu()
    print('____________________________________________________________')
  else :
    print('Commande inconnue, essayez de rentrer une des instructions présente sur le menu ou tapez "instructions" pour avoir plus d\'infos. ')
    MainMenu()

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

#Creation of the MAP
ZONENAME = 'zonename'
DESCRIPTION = 'description'
NORTH = 'nord'
SOUTH = 'sud'
EAST = 'est'
WEST = 'ouest'
EVENT = 'event'
SPEC = 'spec'

#Library for activation of map tiles
ActiveCase = {'A1': True, 'A2': True, 'A3': True,'A4': True, 'A5': True,
              'B1': True, 'B2': True, 'B3': True,'B4': True, 'B5': True,
              'C1': True, 'C2': True, 'C3': True,'C4': True, 'C5': True,
              'D1': True, 'D2': True, 'D3': True,'D4': True, 'D5': True,
              'E1': True, 'E2': True, 'E3': True,'E4': True, 'E5': True,
              'F1': True, 'F2': True, 'F3': False,'F4': True, 'F5': True
              }

# Library for Map in real time
MapCase = {'A1': 'o', 'A2': 'o', 'A3': 'o','A4': 'o', 'A5': 'o',
           'B1': 'o', 'B2': 'o', 'B3': 'o','B4': 'o', 'B5': 'o',
           'C1': 'o', 'C2': 'o', 'C3': 'o','C4': 'o', 'C5': 'o',
           'D1': 'o', 'D2': 'o', 'D3': 'o','D4': 'o', 'D5': 'o',
           'E1': 'o', 'E2': 'o', 'E3': 'o','E4': 'o', 'E5': 'o',
           'F1': 'o', 'F2': 'o', 'F3': 'o','F4': 'o', 'F5': 'o'
           }

#Library for the map
ZoneMap = {
  'A1': {
    ZONENAME: 'Le refuge de Prométhée',
    DESCRIPTION: 'Votre périple en mer s\'achève enfin, vous continuez donc votre aventure comme vous l\'avez commencé : à pied. Après une longue marche, vous tombez sur une maison d\'apparence commune mais aux dimensions atypiques. L\'endroit semble abandonné depuis des centaines d\'années, des milliers peut-être. Au milieu de cette demeure hors du temps, vous apercevez un foyer dépourvu de toute flamme. En y regardant de plus près, vous y décelez néanmoins un petit coffre dans lequel se trouve une fiole au contenu incandescent...',
    NORTH: '',
    SOUTH: 'B1',
    EAST: 'A2',
    WEST: '',
    EVENT: 'object',
    SPEC: 'feu sacré',
  },
  'B1': {
    ZONENAME: 'Île de l\'œil du cyclone',
    DESCRIPTION: 'Après de longs jours de plus en mer, le ciel commence à se couvrir sérieusement. Soudain, une tempête éclate avant même que vous ayez le temps de vous y préparer. Tout à coup, la foudre frappe le mat de votre navire, qui vous tombe sur la tête vous faisant tomber dans l\'inconscience. Quand Morphée vous libère enfin de son emprise, vous sentez une forte odeur. En observant autour de vous, vous réalisez que vous avez atterri dans ce qui semble être une bergerie à grande échelle avec option vue sur mer. Vous êtes d\'abord soulagé, songeant que les gens qui habitent ici accepteront peut-être de vous aider à réparer votre bateau, quand soudain, une voix gutturale retentit : "Cette odeur... C\'est pas un mouton ça, je reconnais... Mmmhh... Impossible ! PERSONNE ! JE SAIS QUE C\'EST TOI ! TU M\'ÉCHAPPERAS PAS CETTE FOIS !".',
    NORTH: 'A1',
    SOUTH: 'C1',
    EAST: '',
    WEST: '',
    EVENT: 'fight',
    SPEC: 'CyclopStats',
  },
  'C1': {
    ZONENAME: 'Le vieux pêcheur perdu en mer',
    DESCRIPTION: 'Cela va faire une semaine maintenant que vous avez pris la mer. C\'est une journée calme, et l\'absence de vent semble distordre le temps, l\'aboutissement de votre odyssée vous paraît bien loin. La monotonie de votre voyage est troublée alors que votre navire s\'enfonce dans une brume étrange. Au milieu de cette brume, vous décelez une lumière ainsi qu\'une silhouette. Piqué de curiosité, vous allez à sa rencontre. Vous croyez d\'abord halluciner quand vous découvrez un homme en train de pêcher, installé dans une barque, au beau milieu de l\'océan. Une atmosphère paisible règne. De nombreuses secondes passent sans que le vieux pêcheur ne vous adresse la parole. Finissant par perdre patience, vous vous raclez la gorge pour signaler votre présence. Après un léger froncement de sourcil, le vieil homme se tourne vers vous, l\'index collé à ses lèvres souriantes : "Chut ! Vous allez faire fuir le poisson !". Vous êtes alors frappé par le regard du vieillard, d\'un vert strictement semblable à celui de la mer, empreint à la fois de sagesse et de malice.',
    NORTH: 'B1',
    SOUTH: 'D1',
    EAST: 'C2',
    WEST: '',
    EVENT: 'npc',
    SPEC: 'PoseidonDial',
  },
  'D1': {
    ZONENAME: 'Le domaine d\'Artémis',
    DESCRIPTION: 'Vous ressentez un soulagement indescriptible lorsque vous arrivez enfin à la lisière d\'une forêt luxuriante vous offrant l\'abri parfait contre le soleil. Seulement, la chaleur laisse peu à peu place à la faim. D\'une flèche bien tirée, vous transpercez un écureuil bien portant qui passait par là. Alors que vous vous approchez de votre futur repas, vous constatez à quel point la vie semble grouiller dans les environs. Les écureuils du même acabit que votre proie sont nombreux et vous avez même croisé le regard d\'un cerf majestueux à quelques mètres de là.  Vous en profitez pour chasser un autre écureuil afin d\'en faire l\'offrande aux dieux. Soudain, un grouinement féroce se fait entendre dans votre dos. Vous vous retournez aussitôt, prêt au combat, et tombez nez à nez avec un sanglier. Cela n\'aurait pas vraiment posé problème, si celui-ci n\'avait pas fait près de deux fois votre taille.',
    NORTH: 'C1',
    SOUTH: 'E1',
    EAST: 'D2',
    WEST: '',
    EVENT: 'fight',
    SPEC: 'BoarStats',
  },
  'E1': {
    ZONENAME: 'Les yeux revolver',
    DESCRIPTION: 'Enfin, la lumière du jour ! Il faut un temps à vos yeux pour se réhabituer, mais vous réalisez que vous êtes arrivé dans ce qui semble être un temple en l\'honneur d\'Athéna. Celui-ci est décoré par des centaines de statues, dont le réalisme vous impressionne. Celui qui les avait sculptées devait être béni des dieux. En vous enfonçant un peu plus à travers ce champ de pierre, vous vous rendez compte que les scènes représentées possèdent une aura étrange. Les visages des statues reflètent une peur incontrôlable, et beaucoup d\'entre elles sont dirigées vers la direction opposée au temple. Au centre de celui-ci, vous découvrez, posé sur un autel, un bouclier orné d\'un visage monstrueux. Ce visage, celui d\'une gorgone, provoque chez vous un mouvement de recul et une frayeur que vous peinez à surmonter.',
    NORTH: 'D1',
    SOUTH: 'F1',
    EAST: 'E2',
    WEST: '',
    EVENT: 'object',
    SPEC: 'shield',
  },
  'F1': {
    ZONENAME: 'Forges d\'Héphaïstos',
    DESCRIPTION: 'Quelle idée d\'avoir décidé de passer par cette étrange caverne ! Ce ne sont pas les raisons de vous plaindre qui manquent entre cette chaleur étouffante, les cliquetis incessants qui retentissent jusqu\'à se graver dans votre crâne et cette obscurité constante interrompue uniquement par le passage peu rassurant de fines coulées de lave. Vous perdez presque espoir avant d\'enfin apercevoir la lumière du jour, loin devant vous. Soulagé, vous hurlez de joie et vous précipitez dans cette direction. C\'est alors qu\'une masse lourde tombe pile devant vous. À y regarder de plus près, il semblerait qu\'il s\'agisse d\'une boule, faite entièrement de métal... Tout à coup, celle-ci se met à grincer, déployant ses membres jusqu\'à former une araignée vous arrivant facilement à la taille.',
    NORTH: 'E1',
    SOUTH: '',
    EAST: 'F2',
    WEST: '',
    EVENT: 'fight',
    SPEC: 'SpiderStats',
  },
  'A2': {
    ZONENAME: 'Le secret de Thanatos',
    DESCRIPTION: 'Les terres que vous foulez sont de plus en plus mornes et il devient difficile de trouver de quoi vous sustenter. Vous envisagez un instant de tenter d\'attraper l\'un des nombreux corbeaux qui parcourent le ciel gris au-dessus de vous, mais qui sait de quelle funeste maladie Apollon a bien pu les affubler. Durant votre voyage, vous passez par bien des villages, tous rasés par l\'arc du dieu musicien. Vous avez soif. Et faim. Si faim... Vous finissez par perdre conscience au milieu de l\'un de ces villages, comme l\'ont fait les centaines de familles qui avaient du vivre ici autrefois. Lorsque vous rouvrez les yeux, vous vous trouvez au milieu d\'une pièce sombre et très étendue, dépourvue de tout meuble à l\'exception d\'un bureau et d\'une chaise en son centre. Assis à ce bureau, un jeune garçon est penché sur une feuille de papier, compas à la main. Debout à côté de lui se trouve une silhouette ailée, la main posée sur l\'épaule du garçon. Vous décelez ce qui ressemble à de la tristesse dans son regard à première vue sinistre.',
    NORTH: '',
    SOUTH: '',
    EAST: 'A3',
    WEST: 'A1',
    EVENT: 'npc',
    SPEC: 'ThanatosDial',
  },
  'B2': {
    ZONENAME: 'Le treizième travail',
    DESCRIPTION: 'Enfin, vous arrivez dans ce qui semble être en tout point un havre de paix au beau milieu d\'une clairière. Une cascade se déverse dans une source d\'eau douce dont le toucher tempéré vous invite à vous détendre - et à vous décrasser - pour la première fois depuis bien longtemps. Seulement, un cri retentissant vient troubler votre quiétude, faisant fuir toutes les créatures alentour : "TOI ! Je savais bien que je finirais par te trouver ! Papa m\'a donné un boulot, il veut que je fasse de toi un guerrier à ma hauteur. J\'ai bien essayé de lui faire comprendre que c\'était impossible, hein, mais il est du type assez borné... Moi c\'est Héraclès, au fait. Sors de l\'eau, on a du pain sur la planche. Et enfile quelque chose !".',
    NORTH: '',
    SOUTH: '',
    EAST: 'B3',
    WEST: '',
    EVENT: 'blessing',
    SPEC: 'Work',
  },
  'C2': {
    ZONENAME: 'Chant funeste',
    DESCRIPTION: 'Il faut être particulièrement prudent quand on prend la mer, on vous l\'a assez répété quand vous étiez jeune. Vous voguez donc sur les mers, prenant garde à ne pas fracasser votre embarcation sur le premier rocher venu. Vous êtes impressionné par vos talents de navigateur, bien que l\'idée de potentiellement tomber sur Charybde et Scylla vous terrifie. Mais bon, personne n\'est tombé sur ces monstres depuis le grand Ulysse, alors... Vous vous rendez soudain compte que vous avez légèrement dévié de cap. Alors que vous vous apprêtez à rectifier la trajectoire, une douce mélodie parvient à vos oreilles. Si douce que vous avez du mal à vous en détourner... Désormais, trouver la source de ce chant est devenu votre priorité. Malheureusement pour vous, c\'est face à une sorte d\'oiseau à taille humaine et au visage de femme que vous vous retrouvez. Aucun doute, il s\'agit d\'une sirène.',
    NORTH: '',
    SOUTH: 'D2',
    EAST: '',
    WEST: 'C1',
    EVENT: 'fight',
    SPEC: 'SirensStats',
  },
  'D2': {
    ZONENAME: 'Le trésor de Midas',
    DESCRIPTION: 'Cela fait déjà un moment que cette idée vous trotte en tête, mais c\'est désormais une certitude. Le labyrinthe de Dédale semble avoir pioché différents lieux aux quatre coins du monde pour les réunir au même endroit. Aucun doute : cette rivière, dont le sable est fait d\'or, c\'est forcément le Pactole. Sur l\'autre rive, vous voyez un coffre massif, contenant probablement d\'incroyables richesses. Vous parvenez non sans mal à l\'atteindre et constatez la présence d\'une étrange serrure...',
    NORTH: 'C2',
    SOUTH: '',
    EAST: 'D3',
    WEST: 'D1',
    EVENT: 'easter',
    SPEC: '',
  },
  'E2': {
    ZONENAME: 'La fleur au bord de l\'eau',
    DESCRIPTION: 'Après tous ces jours de marche, vous avez désespérément besoin de reprendre des forces. Vous finissez par trouver une petite grotte, dont les parois vous accorderont un formidable abri contre le vent cette nuit. Seulement, chaque bruit que vous faites à l\'intérieur de celle-ci est répété par un écho incessant. Las et sur les nerfs, vous décidez de sortir de la grotte pour récupérer de l\'eau d\'une source située non loin de là. C\'est au bord de celle-ci que vous apercevez une fleur, dont la beauté dépasse tout ce que vous avez pu voir jusque-là. Vous êtes prêt à tout pour qu\'elle vous appartienne. Alors que vous l\'extirpez du sol précautionneusement, l\'écho de la grotte que vous avez quittée répète : "Hélas ! Hélas !".',
    NORTH: '',
    SOUTH: '',
    EAST: '',
    WEST: 'E1',
    EVENT: 'curse',
    SPEC: 'Flower',
  },
  'F2': {
    ZONENAME: 'L\'heure n\'est pas à la fête',
    DESCRIPTION: 'Cette sortie semble déboucher sur une sorte de caverne, ornementée çà et là par des éléments à l\'aspect mécanique et des coulées de lave. Au milieu de cette étrange entrée se trouve une table, un canthare posé en son milieu. L\'odeur de vin s\'échappant du vase orné vous attire inéluctablement et vous pousse à vous installer un instant pour y goûter. Vous portez le canthare à votre bouche, mais quelqu\'un vous le retire des mains avant même que son contenu n\'en frôle vos papilles. "Vous êtes certain de vouloir vous aventurer dans cette direction ? Mon demi-frère peut se montrer grincheux quand on farfouille dans ses affaires... Délicieux, ce vin."',
    NORTH: '',
    SOUTH: '',
    EAST: 'F3',
    WEST: 'F1',
    EVENT: 'npc',
    SPEC: 'DionysosDial',
  },
  'A3': {
    ZONENAME: 'LA DÉTRESSE D\'ASTÉRION',
    DESCRIPTION: 'Vous entendez le cœur du labyrinthe battre la chamade un peu plus vite à chaque pas que vous faites. Vous ressentez toute la colère, la haine, la puissance, mais aussi la tristesse qui plane dans l\'atmosphère. D\'immenses blocs de terre se dressent autour de vous, bloquant toute issue alors qu\'une masse gigantesque s\'extirpe de l\'ombre. Face à vous se tient, hurlant, le Minotaure. Celui-là même que Thésée avait vaincu il y a bien longtemps, de retour du royaume d\'Hadès. Son corps, recouvert partiellement de bronze, semble avoir subi des modifications visant à le rendre plus redoutable qu\'il ne l\'a jamais été. D\'une voix sombre, il s\'adresse à vous : "Approche, héros, cela fait bien trop longtemps que je n\'ai pas tué quiconque."',
    NORTH: '',
    SOUTH: 'B3',
    EAST: 'A4',
    WEST: 'A2',
    EVENT: 'BOSS',
    SPEC: '',
  },
  'B3': {
    ZONENAME: 'Une responsabilité royale',
    DESCRIPTION: 'La fin du chemin approche, vous le sentez. Vous vous sentez fatigué, mais aussi plus fort que jamais. Comme si vous n\'en aviez pas assez bavé comme ça, le ciel commence à se couvrir et la pluie à tomber. Vous vous enfoncez de plus en plus dans le sol boueux, chaque pas étant plus difficile que le précédent. Exténué, vous glissez et tombez face contre terre. À bout de nerf, vous ne pouvez vous empêcher de pester : "Nom de Zeus !". C\'est alors que la foudre tombe juste devant vous, laissant place à une silhouette altière :',
    NORTH: 'A3',
    SOUTH: 'C3',
    EAST: '',
    WEST: 'B2',
    EVENT: 'npc',
    SPEC: 'ZeusDial',
  },
  'C3': {
    ZONENAME: 'Les vestiges de la guerre',
    DESCRIPTION: 'Vous avez marché toute la nuit, avec votre torche comme seule source de lumière. Vous espérez atteindre plus vite votre destination grâce à ce gain de temps, mais la fatigue se fait tout doucement ressentir malgré votre métabolisme héroïque. La lumière du soleil levant vous brûle la rétine. C\'est avec stupeur que vous découvrez le paysage alentour, révélé par l\'aube. Tout ici n\'est que destruction, le paysage est rasé à des milliers de pieds à la ronde, jonché d\'armes et armures rouillées, accompagné parfois par les restes d\'un guerrier malchanceux. Quelque chose vous perturbe dans cet endroit : c\'est comme s\'il appartenait à un autre temps. Ci et là, des bannières rouges et bleues se tiennent encore fièrement malgré les bris du temps. Vous ne tenez pas particulièrement à vous attarder ici. En chemin, une lance magnifique, bien que rendue inutilisable par la rouille, attire votre attention. Plantée dans le sol, un casque pilos trône en son sommet. Aucun doute, Arès aurait aimé cet endroit.',
    NORTH: 'B3',
    SOUTH: 'D3',
    EAST: '',
    WEST: '',
    EVENT: 'easter',
    SPEC: '',
  },
  'D3': {
    ZONENAME: 'Un lien irrésistible',
    DESCRIPTION: 'Les vestiges d\'un temple se trouvent devant vous. Vous entreprenez des les visiter afin de découvrir de quelle divinité ce lieu de culte était il autrefois le sanctuaire. Vous parvenez à reconnaitre des fresques encore très colorés montrant des hommes et des femmes contrôlés par une déesse des plus ravissante. Nul doute c\'était un temple à gloire d\'Aphrodite. En parcourant les débris vous tombez sur un petit coffret et décidez de l\'ouvrir. A l\'intérieur se trouve une ceinture magnifique et l\'essayez sur vous immédiatement. Elle vous va à ravir.',
    NORTH: 'C3',
    SOUTH: 'E3',
    EAST: 'D4',
    WEST: 'D2',
    EVENT: 'object',
    SPEC: 'ceinture',
  },
  'E3': {
    ZONENAME: 'Le mal-aimé',
    DESCRIPTION: 'C\'est difficile, mais vous parvenez petit à petit à prendre vos marques dans ce labyrinthe infernal. Pris par la fatigue, vous vous laissez glisser au pied d\'un arbre mort, séduit par l\'idée d\'une petite sieste. Vous levez la tête et observez les branches nues de l\'olivier qui vous protège du soleil. Vous vous rendez compte que vous allez vite finir comme lui si vous ne buvez pas rapidement. "Ce serait bête de mourir de soif quand on peut l\'être en étant cruellement déchiqueté par une bête des Enfers..." vous marmonnez-vous à vous-même en portant votre outre à votre bouche jusqu\'à ce qu\'une voix derrière vous vous en fasse recracher tout le contenu : "Allez ! ça va encore être de ma faute ! Le vilain dieu des Enfers a donné des pouvoirs à Dédale pour qu\'il réduise le monde entier à néant ! Bien sûr, j\'ai que ça à faire !". Abasourdi, vous vous retournez pour faire face à un homme aux cheveux de jais et au teint plus pâle que du lait de chèvre.',
    NORTH: 'D3',
    SOUTH: '',
    EAST: 'E4',
    WEST: '',
    EVENT: 'npc',
    SPEC: 'HadesDial',
  },
  'F3': {
    ZONENAME: 'La folie de Dédale',
    DESCRIPTION: '"Héros ! Tu m\'entends ? Hé ho ! Par Athéna, écoute-moi !" Perdu, vous parvenez difficilement à ouvrir les yeux. Vous vous trouvez dans une salle carrée vide, dont trois murs sont ouverts par une brèche. En face de vous, un homme vous fixe d\'un regard inquiet et intelligent : "Ah, tu as repris connaissance, c\'est bien. Doucement, doucement."',
    NORTH: '',
    SOUTH: '',
    EAST: 'F4',
    WEST: 'F2',
    EVENT: 'start',
    SPEC: '',
  },
  'A4': {
    ZONENAME: 'Les sœurs filandières',
    DESCRIPTION: 'Une atmosphère étrangement calme plane sur les lieux et quelque chose vous dit que celui-ci précède certainement la tempête. Sur votre route, vous tombez sur une petite maison. De la lumière s\'échappe des fenêtres et la perspective de passer une nuit dans un foyer chaleureux est un luxe que vous ne pouvez pas vous permettre de refuser. Vous constatez que la porte est déjà ouverte et vous permettez de passer la tête à l\'intérieur. Trois femmes d\'âges très différents détournent alors leur regard de leur tricot pour le poser sur vous. La plus âgée d\'entre elles tient une paire de ciseaux dans sa main parcheminée.',
    NORTH: '',
    SOUTH: '',
    EAST: 'A5',
    WEST: 'A3',
    EVENT: 'npc',
    SPEC: 'MoiresDial',
  },
  'B4': {
    ZONENAME: 'Vignes trompeuses',
    DESCRIPTION: 'Vous arrivez dans un énorme vignoble aux raisins gorgés de soleil s\'étendant à perte de vue. Vous ignorez qui entretient cet endroit et ne voyez aucune demeure dans les environs, mais vous avez cessé de chercher la moindre logique dans ce labyrinthe, de toute manière. Alors que le sommeil commence à se coucher, une musique entraînante attire votre attention, comme un appel à la fête. En vous approchante de sa source, vous découvrez, éberlué, un groupe de satyres, jouant de la flûte de pan et dansant, distribuant du vin à tour de bras. Après un court moment d\'hésitation, vous vous décidez à rejoindre la petite troupe le temps d\'une nuit. Ou peut-être plusieurs...',
    NORTH: '',
    SOUTH: '',
    EAST: 'B5',
    WEST: '',
    EVENT: 'curse',
    SPEC: 'Vines',
  },
  'C4': {
    ZONENAME: 'Juge et Roi',
    DESCRIPTION: 'Le bâtiment qui se dresse devant vous est pour le moins singulier. Haut de plusieurs dizaines de mètres, il ne possède pas la moindre fenêtre, seulement une porte aux barreaux de fer, déjà ouverte. Une fois à l\'intérieur, vous allumez une torche pour tenter d\'y voir quelque chose. Vous mettez un moment à vous rendre compte du spectacle qui a lieu sous vos yeux. Dans un coin du bâtiment, un homme vous surplombe par son imposante taille, même assis. Il ne semble pas avoir remarqué votre présence. Son regard vide et son corps décharnés vous laissent d\'abord penser que la vie a quitté cette enveloppe immense, pourtant un râle constant vous prouve le contraire. Vous vous approchez et tentez d\'attirer son attention : "Bonjour ?". Un léger mouvement de pupille vous laisse penser qu\'il s\'agit d\'une invitation à la discussion.',
    NORTH: '',
    SOUTH: 'D4',
    EAST: 'C5',
    WEST: '',
    EVENT: 'npc',
    SPEC: 'MinosDial',
  },
  'D4': {
    ZONENAME: 'Lernie, l\'hydre vorace',
    DESCRIPTION: 'La brume se lève, l\'air devient plus frais, et une aura menaçante plane sur ce lieu où la végétation ne pousse plus. Vous entendez des cris terrifiant venant d\'une caverne par laquelle vous êtes obligé de passer si vous voulez continuer votre périple. Alors que vous approchez de l\'entrée une tête hideuse sort de la caverne, puis une deuxième et une troisième. Vous en êtes sûr maintenant vous avez affaire à une Hydre.',
    NORTH: 'C4',
    SOUTH: '',
    EAST: 'D5',
    WEST: 'D3',
    EVENT: 'fight',
    SPEC: 'HydraStats',
  },
  'E4': {
    ZONENAME: 'Un labyrinthe des plus particuliers',
    DESCRIPTION: 'D\'immenses colonnes peintes en bleu et jaune se dressent devant vous. En continuant votre route vous entendez du bruit et décidez de vous cacher pour ne pas vous faire repérer et ainsi évaluer au mieux la menace. Passe alors deux hommes proche de vous, et vous arrivez à entendre leur conversation. " Tu as vu les nouveaux Gnedby ? J\'aime beaucoup la couleur mais je t\'avoue que pour la forme les Lerberg sont bien mieux! Vivement les nouveaux arrivages pour le rayon meuble ! " Quel étrange discussion... Mais si c\'était une menace vous l\'avez évitée, quel labyrinthe des plus mystérieux.',
    NORTH: '',
    SOUTH: 'F4',
    EAST: 'E5',
    WEST: 'E3',
    EVENT: 'easter',
    SPEC: '',
  },
  'F4': {
    ZONENAME: 'Questions pour un Héros',
    DESCRIPTION: 'Vous commencez votre route, sans vraiment savoir où vous allez ni ce que vous allez trouver en chemin. Vous marchez presque automatiquement, la tête encore dans le brouillard. Tout à coup, vous vous retrouvez face à un bâtiment de marbre blanc duquel s\'échappent des lumières multicolores. Ne pouvant résister à la curiosité, vous décidez d\'aller voir ce qui s\'y passe. À peine mettez-vous un pied à l\'intérieur qu\'une nouvelle lumière éclaire soudain une créature mi-femme, mi-lion disposant, pour couronner le tout, d\'une paire d\'ailes. Une chose est sûre, elle a l\'air de s\'amuser.',
    NORTH: 'E4',
    SOUTH: '',
    EAST: '',
    WEST: 'F3',
    EVENT: 'npc',
    SPEC: 'SphinxDial',
  },
  'A5': {
    ZONENAME: 'Un adversaire surprenant',
    DESCRIPTION: 'Vous arrivez dans un tunnel éclairé par de simples torches accrochées aux murs, et alors que vous le traversez, vous sentez une présence des plus perturbantes. Et c\'est là que vous l\'apercevez. Une créature effroyable vous bloque le chemin. Deux pattes aux serres acérés, un corps démesuré d\'où sortent deux grandes ailes, une tête des plus affreuses vous menaçant d\'un regard féroce et orné d\'une crête écarlate ainsi que d\'un bec des plus terrifiant. Vous voilà face à un redoutable poulet.',
    NORTH: '',
    SOUTH: 'B5',
    EAST: '',
    WEST: 'A4',
    EVENT: 'fight',
    SPEC: 'ChickenStats',
  },
  'B5': {
    ZONENAME: 'De zéro à héros',
    DESCRIPTION: 'Alors que vous continuez votre route vous vous retrouvez face à un énorme autel d\'où trône une massue, encastrée dans celui-ci. L\'autel est orné de plusieurs fresques démontrant le courage d\'un héros oublié. Vous arrivez à en compter 12 en tout. Après avoir gravit les quelques marches menant au haut de l\'autel vous y récupérer l\'arme avec énormément de difficulté car celle ci était encastré dans la pierre de l\'altar. En la tenant dans vos mais vous ressentez toute la force de son ancien propriétaire.',
    NORTH: 'A5',
    SOUTH: 'C5',
    EAST: '',
    WEST: 'B4',
    EVENT: 'object',
    SPEC: 'massue',
  },
  'C5': {
    ZONENAME: 'Un adversaire de taille',
    DESCRIPTION: 'Quel spectacle d\'horreur. Le sol devant vous est jonché d\'ossements. En examinant de plus près vous confirmez la présence d\'ossements humains et non animaux. Puis le sol se mit à trembler. Une ombre gigantesque s\'avance vers vous. Ni une ni deux vous vous préparez au combat et c\'est là que vous l\'apercevez. Il ressemble à un homme mais ce n\'en est pas. Il est beaucoup trop grand, beaucoup trop massif pour être un simple homme. Non ce ne peut être qu\'un Lestrygon, une abomination anthropophage. Et celui là n\'a l\'air de souhaiter qu\'une chose: vous dévorer.',
    NORTH: 'B5',
    SOUTH: '',
    EAST: '',
    WEST: 'C4',
    EVENT: 'fight',
    SPEC: 'LestrygonStats',
  },
  'D5': {
    ZONENAME: 'La boisson des dieux',
    DESCRIPTION: 'En continuant sur la route vous croisez les restes d\'un voyageur égaré. Le pauvre avait dû se faire attaquer par une quelconque créature et son combat résultat d\'un dessein funeste. Cependant bien qu\'il ne lui reste presque plus de chair sur les os, il peut peut être y avoir quelques objets qui pourrait vous être utile pour votre voyage. En cherchant dans les affaires du mort, vous y trouver une boite avec une flacon contenant un liquide doré. Une petite étiquette pendouille accrochée au bouchon indiquant : " Ambroisie ! La boisson des dieux qui vous revigorera immédiatement ! " ainsi que diverses mentions légales au dos de l\'étiquette sur une possibles présence d\'effets secondaires sur les mortels.',
    NORTH: '',
    SOUTH: 'E5',
    EAST: '',
    WEST: 'D4',
    EVENT: 'object',
    SPEC: 'ambroisie',
  },
  'E5': {
    ZONENAME: 'Beaucoup trop de pattes à mon goût',
    DESCRIPTION: 'La nuit tombe mais vous décidez de continuer votre chemin pour aller le plus loin possible et trouver un abri pour passer la nuit sereinement. Enfin vous trouvez une petite cave toute en pierre à même la paroi d\'un des murs du labyrinthe. Vous y serez au chaud ! Mais alors que vous commencez à vous installer vous entendez des petits cliquetis sur la roche non loin de vous. Vous levez votre torche pour éclairer et vous la voyez. Toutes ces pattes... vous voilà face à une araignée d\'Héphaïstos.',
    NORTH: 'D5',
    SOUTH: 'F5',
    EAST: '',
    WEST: 'E4',
    EVENT: 'fight',
    SPEC: 'SpiderStats',
  },
  'F5': {
    ZONENAME: 'Une trempette vivifiante',
    DESCRIPTION: 'C\'est avec un grand soulagement que vous trouvez un fleuve, dont la fraîcheur est plus que bienvenue. Seulement, en vous approchant, vous réalisez que c\'est plutôt une profonde froideur qui en ressort. Stupéfié, vous constatez la présence d\'une femme, en train d\'y tremper son enfant, peut-être pour faire sa toilette. Soudain, vous vous rendez compte de la scène à laquelle vous assistez. Ulysse vous avait prévenu, dans le labyrinthe, l\'espace et le temps sont distordus. Cette femme et son enfant, ce sont Thétis et son fils, Achille, le héros légendaire de la Guerre de Troie. Une idée vous traverse alors l\'esprit. Une idée risquée, certes, mais payante. Prenant garde de vous accrocher à un rocher pour ne pas vous faire emporter, vous vous baignez dans le Styx.',
    NORTH: 'E5',
    SOUTH: '',
    EAST: '',
    WEST: '',
    EVENT: 'blessing',
    SPEC: 'Styx',
  },
}

# Function for display real time map
def MapDisplay():
  for i in ActiveCase:
    if ActiveCase[i] == False:
      MapCase[i] = '-'
  MapCase[Player.pos] = 'x'

  print("   1  2  3  4  5 ")
  print("A [" + MapCase['A1'] + "][" + MapCase['A2'] + "][" + MapCase['A3'] + "][" + MapCase['A4'] + "][" + MapCase['A5'] + "]")
  print("B [" + MapCase['B1'] + "][" + MapCase['B2'] + "][" + MapCase['B3'] + "][" + MapCase['B4'] + "][" + MapCase['B5'] + "]")
  print("C [" + MapCase['C1'] + "][" + MapCase['C2'] + "][" + MapCase['C3'] + "][" + MapCase['C4'] + "][" + MapCase['C5'] + "]")
  print("D [" + MapCase['D1'] + "][" + MapCase['D2'] + "][" + MapCase['D3'] + "][" + MapCase['D4'] + "][" + MapCase['D5'] + "]")
  print("E [" + MapCase['E1'] + "][" + MapCase['E2'] + "][" + MapCase['E3'] + "][" + MapCase['E4'] + "][" + MapCase['E5'] + "]")
  print("F [" + MapCase['F1'] + "][" + MapCase['F2'] + "][" + MapCase['F3'] + "][" + MapCase['F4'] + "][" + MapCase['F5'] + "]")
  print('Lieux non visités : o')
  print('Lieux visités : -')
  print('Position du joueur : x')

#display the location of the player
def PrintLocation():
  if(ActiveCase[Player.pos] == True):
    promptSlow(ZoneMap[Player.pos][ZONENAME].upper())
    promptSlow(ZoneMap[Player.pos][DESCRIPTION])
  else:
    promptSlow('Vous êtes déjà passé par ici, il ne reste plus rien d\'intéressant')
  

#main display with actions of the player
def prompt():
  if (ZoneMap[Player.pos][EVENT] == 'fight' and ActiveCase[Player.pos] == True):
    testlecombat()
  elif (ZoneMap[Player.pos][EVENT] == 'npc' and ActiveCase[Player.pos] == True):
    testnpc()
  elif (ZoneMap[Player.pos][EVENT] == 'object' and ActiveCase[Player.pos] == True):
    testobject()
  elif (ZoneMap[Player.pos][EVENT] == 'curse' and ActiveCase[Player.pos] == True):
    testcurse()
  elif (ZoneMap[Player.pos][EVENT] == 'blessing' and ActiveCase[Player.pos] == True):
    testblessing()
  elif (ZoneMap[Player.pos][EVENT] == 'easter' and ActiveCase[Player.pos] == True):
    testeaster()
  else:
    promptSlow('Que souhaitez vous faire ?')
    action = input('\n > ')
    if action.lower() == 'quitter':
      sys.exit()
    elif action.lower() == 'voyager':
      PlayerMove(action.lower())
    elif action.lower() == 'aide':
      promptSlow('Liste des commandes: ')
      promptSlow('voyager        -       vous permets de vous déplacer')
      promptSlow('inventaire     -       vous permets d\'accéder à votre inventaire')
      promptSlow('stats          -       vous permets d\'accéder à vos stats')
      promptSlow('carte          -       vous permets d\'accéder à votre carte')
      promptSlow('sauvegarder    -       vous permets de sauvegarder votre partie')
      promptSlow('aide           -       vous permets d\'avoir une liste des commandes')
      promptSlow('quitter        -       vous permet de quitter le jeu')
    elif action.lower() == 'inventaire':
      displayInventory()
    elif action.lower() == 'stats':
      displayStats()
    elif action.lower() == 'carte':
      MapDisplay()
    elif action.lower() == 'sauvegarder':
      promptSlow('Vous avez bien sauvegardé votre partie !')
      saveGame()
    else:
      print("Commande invalide, essayez 'aide' pour avoir la liste des commandes.\n")

#function for the movement of the player
def PlayerMove(MyAction):
  ask = "Où souhaitez-vous aller ?"
  dest = input(ask + '\n > ')

  if dest == 'est':
    if ZoneMap[Player.pos][EAST] == '':
      promptSlow('Impossible d\'aller dans cette direction, un mur vous bloque la route.')
      PlayerMove(MyAction)
    elif (ZoneMap[ZoneMap[Player.pos][EAST]][EVENT] == 'BOSS'):
      promptSlow('Vous êtes face au combat ultime, vous ne pourrez plus revenir en arrière, êtes vous sûr de vouloir continuer ?')
      print('Oui / Non')
      ask = input('>' ).lower()
      if (ask == 'oui'):
        destination = ZoneMap[Player.pos][EAST]
        MovementHandler(destination)
      elif (ask == 'non'):
        ActiveCase[Player.pos] = True
        prompt()
    else :
      destination = ZoneMap[Player.pos][EAST]
      MovementHandler(destination)

  elif dest == 'nord':
    if ZoneMap[Player.pos][NORTH] == '':
      promptSlow('Impossible d\'aller dans cette direction, un mur vous bloque la route.')
      PlayerMove(MyAction)
    elif (ZoneMap[ZoneMap[Player.pos][NORTH]][EVENT] == 'BOSS'):
      promptSlow('Vous êtes face au combat ultime, vous ne pourrez plus revenir en arrière, êtes vous sûr de vouloir continuer ?')
      print('Oui / Non')
      ask = input('>' ).lower()
      if (ask == 'oui'):
        destination = ZoneMap[Player.pos][NORTH]
        MovementHandler(destination)
      elif (ask == 'non'):
        ActiveCase[Player.pos] = True
        prompt()
    else :
      destination = ZoneMap[Player.pos][NORTH]
      MovementHandler(destination)

  elif dest == 'sud':
    if ZoneMap[Player.pos][SOUTH] == '':
      promptSlow('Impossible d\'aller dans cette direction, un mur vous bloque la route.')
      PlayerMove(MyAction)
    elif (ZoneMap[ZoneMap[Player.pos][SOUTH]][EVENT] == 'BOSS'):
      promptSlow('Vous êtes face au combat ultime, vous ne pourrez plus revenir en arrière, êtes vous sûr de vouloir continuer ?')
      print('Oui / Non')
      ask = input('>' ).lower()
      if (ask == 'oui'):
        destination = ZoneMap[Player.pos][SOUTH]
        MovementHandler(destination)
      elif (ask == 'non'):
        ActiveCase[Player.pos] = True
        prompt()
    else :
      destination = ZoneMap[Player.pos][SOUTH]
      MovementHandler(destination)

  elif dest == 'ouest':
    if ZoneMap[Player.pos][WEST] == '':
      promptSlow('Impossible d\'aller dans cette direction, un mur vous bloque la route.')
      PlayerMove(MyAction)
    elif (ZoneMap[ZoneMap[Player.pos][WEST]][EVENT] == 'BOSS'):
      promptSlow('Vous êtes face au combat ultime, vous ne pourrez plus revenir en arrière, êtes vous sûr de vouloir continuer ?')
      print('Oui / Non')
      ask = input('>' ).lower()
      if (ask == 'oui'):
        destination = ZoneMap[Player.pos][WEST]
        MovementHandler(destination)
      elif (ask == 'non'):
        ActiveCase[Player.pos] = True
        prompt()
    else :
      destination = ZoneMap[Player.pos][WEST]
      MovementHandler(destination)
  else :
    print("Commande invalide, essayez avec nord, sud, est ou ouest.\n")
    PlayerMove(MyAction)

#Movement of the player
def MovementHandler(destination):
  Player.pos = destination
  PrintLocation()

def displayStats():
  print("Joueur : " + Player.name + " fils de " + Player.father)
  print("Niveau : " + str(Player.lvl) + " Expérience : " + str(Player.xp))
  print("HP : " + str(Player.Hp) + " | CHA : " + str(Player.Cha) + " |  ATK : " + str(Player.Atk))
  print("")

#Main game loop function
def main_game_loop():
  while Player.dead is False:
    passiveObject()
    prompt()

########## ZONE DE TESTS ##########
#test 001
def testlecombat():
  StartCombat(ZoneMap[Player.pos][SPEC])
  ActiveCase[Player.pos] = False
  time.sleep(0.5)
  prompt()

def testeaster():
  print('easter')
  ActiveCase[Player.pos] = False
  time.sleep(0.5)
  prompt()

def testblessing():
  Blessing(ZoneMap[Player.pos][SPEC])
  ActiveCase[Player.pos] = False
  time.sleep(0.5)
  prompt()

def testcurse():
  Curse(ZoneMap[Player.pos][SPEC])
  ActiveCase[Player.pos] = False
  time.sleep(0.5)
  prompt()

def testobject():
  ObjectInventory(ZoneMap[Player.pos][SPEC])
  ActiveCase[Player.pos] = False
  time.sleep(0.5)
  prompt()

def testnpc():
  Dialogue(ZoneMap[Player.pos][SPEC])
  ActiveCase[Player.pos] = False
  time.sleep(0.5)
  prompt()

# main_game_loop()



# from Map import ZoneMap

# NpcDial['ZeusDial'][NPCNAME]

# npc = ZoneMap[Player.pos][SPEC]

# =======================================================
# NPC Dialogues Library

NPCNAME = 'NPCNAME'
MINSTAT = 'MINSTAT'
SENTENCE = 'SENTENCE'
DIAL1 = 'DIAL1'
DIAL1_1 = 'DIAL1_1'
DIAL2 = 'DIAL2'
DIAL2_1 = 'DIAL2_1'
DIALCHA = 'DIALCHA'
DIALCHA1 = 'DIALCHA1'
DIALSON = 'DIALSON'
DIALSON1 = 'DIALSON1'
GIFT = 'GIFT'

NpcDial = {
    'ZeusDial':{
        NPCNAME: 'Zeus',
        MINSTAT: 15,
        SENTENCE: '- Oui ? On me parle ?',
        DIAL1: '- Z-Zeus, c\'est bien vous ?',
        DIAL1_1: '- Bien sûr que oui, avorton ! Tu oses questionner ma royale identité ? Décidément, les héros de nos jours, c\'est plus ce que c\'était. Bon, je tenais quand même à te souhaiter bonne chance pour Dédale, tout ça. Sur ce, je dois y aller. Héra va encore me chercher des noises, sinon...',
        DIAL2: '- Zeus, Roi de l\'Olympe, savez-vous quelle est l\'origine de cette folie ?',
        DIAL2_1: '- C\'est moi-même, j\'en ai bien peur. J\'ai accordé à Dédale le statut divin, comme je le fais parfois pour les hommes exceptionnels. J\'étais loin de me douter que la folie consommait déjà le pauvre homme. Tu es notre seule chance de mettre fin cela. Je dois y aller, à présent. Je sais que tu ne me décevras pas.',
        DIALCHA: '- Tiens-donc ! Zeus, le roi des rois, m\'accorde l\'honneur de sa présence. Vous devriez plutôt être à l\'Olympe, non ? Quelqu\'un aurait vite fait de raconter à Héra que vous êtes allé vous amuser ailleurs une fois de plus. J\'ai rencontré beaucoup de dieux pendant mon périple, vous savez. Bien sûr, je suppose qu\'un petit dédommagement pour mon dur travail m\'aiderait à garder ma langue dans ma poche.',
        DIALCHA1: '- Ah non, hein ! J\'en ai assez de ses crises ! Très bien, très bien, le voilà ton dédommagement. Retiens simplement que personne ne se moque de Zeus impunément.',
        DIALSON: '- Père, enfin je vous rencontre. C\'est un honneur.',
        DIALSON1: '- (Il est de moi, celui-là aussi ?!) Ah ! Oui ! Mon enfant ! Je suis si heureux de te rencontrer enfin. Laisse-moi te donner ma bénédiction divine. À présent, tes attaques seront plus puissantes qu\'elles ne l\'ont jamais été. Je souhaite bonne chance aux monstres qui croiseront ton chemin. En revanche, évite celui d\'Héra, si possible. Adieu, mon enfant.',
        GIFT: 'feu sacré',
    },
    'PoseidonDial':{
        NPCNAME: 'Poséidon',
        MINSTAT: 15,
        SENTENCE: 'Ça mord bien, aujourd\'hui.',
        DIAL1: '- Qu\'est-ce que vous faites ici, au milieu de l\'océan ?',
        DIAL1_1: '- Je te retourne la question, voyageur. Je profite du beau de temps et du calme marin. Il n\'y a que ça qui parvienne à me détendre réellement.',
        DIAL2: '- Vous êtes Poséidon, n\'est-ce pas ?',
        DIAL2_1: '- Vous êtes perspicace ! Oui, c\'est ainsi que l\'on m\'appelle. Je suis heureux de te croiser. Je te souhaite bien du courage pour ta quête. Dédale était quelqu\'un de bien, autrefois. C\'est fou ce que la jalousie et la rancoeur peuvent faire aux hommes. À présent, si tu le permets, j\'aimerais me concentrer sur ma ligne.',
        DIALCHA: '- J\'ai moi-même pêché d\'énormes poissons. Dans ma région, personne ne m\'arrivait à la cheville, dans ce domaine.',
        DIALCHA1: '- Hahaha, j\'en ai entendu parler, oui. Accepte donc ce modeste présent comme démonstration de mon admiration. Maintenant, chut, tu vas faire fuir le poisson.',
        DIALSON: '- Poséidon... J\'ai du mal à contrôler mon émotion. Je suis si heureux de vous rencontrer, père.',
        DIALSON1: '- Tiens donc ma canne à pêche un instant, mon enfant. Tu sais, la vie, c\'est comme la pêche. Tout est une question de patience. Inspire-toi de la mer à chaque instant. Aborde les épreuves avec calme et, quand le moment sera venu, déchaîne toi. Laisse-moi t\'accorder ma bénédiction avant de reprendre ton voyage. Que la vitalité de l\'océan t\'accompagne.',
        GIFT: 'feu sacré',
    },
    'HadesDial':{
        NPCNAME: 'Hadès',
        MINSTAT: 15,
        SENTENCE: 'Alors, qu\'est-ce que le grand méchant Hadès a encore fait de mal ?',
        DIAL1: '- N-n-non-non ! Pitié ne me faites pas de mal !',
        DIAL1_1: '- Eh bah dis-donc... Attends une seconde, me dis pas que c\'est toi le héros qui est censé résoudre tout ce merdier ? On est pas sortis de l\'auberge. Bon, j\'me tire, j\'vais encore avoir du boulot, moi.',
        DIAL2: '- Savez-vous qui est réellement à l\'origine de tout cela, seigneur Hadès ?',
        DIAL2_1: '- Ben oui, c\'est un secret pour personne, à l\'Olympe. J\'avais pourtant bien dit à mon crétin de frère que c\'était pas une bonne idée. J\'ai toujours dit que Dédale était complètement taré.',
        DIALCHA: '- Seigneur Hadès, sans mentir, si votre ramage se rapporte à votre plumage, Vous êtes le phénix des hôtes de ce labyrinthe.',
        DIALCHA1: '- C\'est ça, fous toi de ma gueule. Qu\'est-ce que tu veux ? J\'ai l`habitude, avec vous, les héros. Tiens, prends ça et lâche moi la grappe.',
        DIALSON: '- Il a fait un gosse avec une mortelle y\'a quelques années. Bonjour, père.',
        DIALSON1: '- Alors ça ! Je te châtierais bien pour ton insolence, mais je dois bien avouer que tu tiens ça de ton père. T\'as bien raison, te laisse pas faire. Si on se bat pas, on se fait marcher dessus. Surtout les gens comme nous. Enfin, "les gens", les dieux, pour ma part. Approche, fiston, laisse moi te donner ma bénédiction divine. Sois polyvalent, apprends à attaquer mais aussi à te défendre, ça pourrait bien te permettre de ne pas avoir à me rendre visite avant un moment. Je dois y aller, à présent. J\'ai beucoup de boulot, en ce moment !',
        GIFT: 'feu sacré',
    },
    'ThanatosDial':{
        NPCNAME: 'Thanatos et Talos',
        MINSTAT: 15,
        SENTENCE: 'Tu ne devrais pas être là. Il est bien trop tôt pour que nous ne nous rencontrions. (Thanatos)',
        DIAL1: '- Excusez-moi, mais je n\'ai aucune idée de comment je suis arrivé là. Je veux bien m\'en aller, si vous me montrez la sortie. (Parler à Thanatos)',
        DIAL1_1: '- Ha ! Les humains regorgent de stratégies pour tenter de m\'échapper, mais toi, tu n\'as pas la moindre idée de ce qui t\'es arrivé. Je suis Thanatos, dieu de la mort. Rassure-toi, je vais te renvoyer de là d\'où tu viens, nous nous retrouverons tôt ou tard, de toute façon. Pour l\'heure, tu as une mission à terminer.',
        DIAL2: '- Dis-moi, jeune garçon, peux-tu me dire où on se trouve, s\'il te plaît ? (Parler à Talos)',
        DIAL2_1: '- Je sais pas trop, mais Monsieur Thanatos a été très gentil avec moi. Dites-moi, quand vous retournerez là-bas, vous pourrez dire à tonton Dédale que je sais que c\'était un accident ?',
        DIALCHA: '- Vous savez forcément ce qui a poussé Dédale à faire tout ça, j\'ai vraiment besoin qu\'on me donne des explications. Je commence à fatiguer d\'être dans le flou et de combattre sans arrêt malgré tout. (Parler à Thanatos)',
        DIALCHA1: '- Tu as raison, mortel. Comme tu le sais peut-être déjà, les dieux ont décidé d\'accorder le statut divin à Dédale, en guise de démonstration d\'admiration de la part de Zeus. Seulement, cela faisait déjà bien longtemps que Dédale avait commencé à sombrer dans la folie. Trop de démons le hantaient : Minos, Thésée, Arianne, Astérion... Talos...',
        GIFT: 'ambroisie',
    },
    'DionysosDial':{
        NPCNAME: 'Dionysos',
        MINSTAT: 15,
        SENTENCE: 'C\'est quand-même meilleur que du jus de raisin !',
        DIAL1: '- Dionysos ? C\'est vous ?',
        DIAL1_1: '- Eh oui, petit ! On dirait que tu n\'as jamais vu de dieu de ta vie, héros ! Non... Me dis pas que je suis ta première fois ? Enfin, euh, on se comprend, hein. Très bien, sur ce, je dois y aller. J\'ai un groupe de satyres enivrés à retrouver. N\'oublie pas ce que je t\'ai dit concernant mon demi-frère. C\'est le roi des pièges.',
        DIAL2: '- Hé ! J\'allais juste goûter au vin, soyez sympa !',
        DIAL2_1: '- Haha, tu as bon goût, je dois dire. Tiens, attrape, je dois y retourner, de toute façon. J\'ai un groupe de satyres enivrés à retrouver.',
        DIALCHA: '- Seigneur Dionysos ! Je suis votre plus grand fan !',
        DIALCHA1: '- Oh ! J\'en connais un qui a le sens de la fête ! Malheureusement, la situation ne s\'y prête pas vraiment. Tiens, attrape ça, on fera la fête la prochaine fois qu\'on se voit. Pour l\'heure, j\'ai un groupe de satyres enivrés à retrouver.',
        GIFT: 'ambroisie',
    },
    'MoiresDial':{
        NPCNAME: 'Les Moires',
        MINSTAT: 15,
        SENTENCE: 'Nous avons un visiteur, on dirait.',
        DIAL1: '- Que faites-vous ? (Parler à la plus jeune)',
        DIAL1_1: '- Je tisse, ne voyez-vous pas ?',
        DIAL2: '- Que faites-vous ? (Parler à la femme adulte)',
        DIAL2_1: '- Je déroule, ne voyez-vous pas ?',
        DIALCHA: '- Que faites-vous ?',
        DIALCHA1: '- Je coupe, ne voyez-vous pas ? Prenez ceci, cela m\'évitera peut-être de m\'occuper de votre fil trop tôt.',
        GIFT: 'ambroisie',
    },
    'MinosDial':{
        NPCNAME: 'Minos',
        MINSTAT: 15,
        SENTENCE: '...',
        DIAL1: '- Je peux vous aider ?',
        DIAL1_1: '- ...',
        DIAL2: '- Qu\'est-ce qui vous est arrivé ?',
        DIAL2_1: '- ... Fou... Vengeance...',
        DIALCHA: '- C\'est Dédale qui vous a fait ça ?',
        DIALCHA1: '- ... Pitié... ... Partez... ... ... Prenez... et... ... ... partez...',
        GIFT: 'feu sacré',
    },
    'SphinxDial':{
        NPCNAME: 'La Sphinge',
        MINSTAT: 15,
        SENTENCE: 'C\'est l\'heure du shoooooooooooow !',
        DIAL1: '- Le Show ?',
        DIAL1_1: '- Je suis une sphinge, tu t\'attendais à quoi ? Évidemment, qu\'il va y avoir du show.',
        DIAL2: '- Le Sphinx ! Celui qui a rencontré Oedipe ?!',
        DIAL2_1: '- LA SPHINGE ! Ça se voit quand même, non ? L\'impolitesse des gens, je m\'y ferai jamais. t\'as de la chance que j\'ai commencé un régime sans humain.',
        DIALCHA: '- Laissez-moi deviner, c\'est l\'heure de la devinette, c\'est ça ?',
        DIALCHA1: '- Hihihi, tu es un malin, toi. Tiens, je t\'offre une petite friandise, tu me plais bien.',
        GIFT: 'ambroisie',
    },
}

# Énigme du Sphinx

def SphinxEnigma() :
    print('>-------------------------------------------------<')
    promptSlow('- Une dernière chose, {}. J\'ai une proposition à te faire, si tu te sens à la hauteur.'.format(Player.name))
    promptSlow('- De quoi s\'agit-il ?')
    promptSlow('- Une énigme.')
    promptSlow('- Ben tiens, étonnant, ça... Et qu\'est-ce que j\'y gagne ?')
    promptSlow('- De la force vitale...')
    promptSlow('- Et l\'entourloupe, elle est où ?')
    promptSlow('- Tu devras parier une partie de ta force vitale actuelle pour en gagner le double. Alors, qu\'en dis-tu ? Attention, tu n\'auras qu\'une seule chance.')
    print('1 - Je prends le risque, envoie ton énigme.')
    print('2 - Très peu pour moi, merci.')
    print('>-------------------------------------------------<')
    StartEnigma = input(' > ')
    if StartEnigma == '1' :
        Player.Hp -= 5
        promptSlow('- Même en marchant vers lui, vous ne pouvez l\'atteindre.')
        promptSlow('Alors, {}, une idée ?'.format(Player.name))
        AnswerEnigma = input(' > ')
        if AnswerEnigma.lower() == 'l\'horizon' or AnswerEnigma.lower() == 'horizon' :
            promptSlow('- Alors là... Je dois admettre que je suis impressionnée. Tu es quelqu\'un de culture, {}. Laisse-moi augmenter tes points de v-... Euh, ta force vitale !'.format(Player.name))
            Player.Hp += 15
        else :
            promptSlow('Loupé, héhéhé ! La réponse était l\'horizon. Ne t\'en fais pas, va, tu t\'en sortiras très bien même si tu es un peu, disons, affaibli. Bon voyage, {}'.format(Player.name))

    elif StartEnigma == '2' :
        promptSlow('- C\'est facheux, tant pis. Je te pensais plus malin que ça, {}. Adieu, dans ce cas.'.format(Player.name))
    else :
        print('ERREUR : Veuillez entrer le chiffre correspondant au dialogue voulu.')
        SphinxEnigma()

def Dialogue(npc):
    minstat = NpcDial[npc][MINSTAT]
    print(')(=================================================)(')
    print(NpcDial[npc][NPCNAME], ':')
    print(NpcDial[npc][SENTENCE])
    print('-------------------------------------')
    print('1', NpcDial[npc][DIAL1])
    print('2', NpcDial[npc][DIAL2])
    print('3', NpcDial[npc][DIALCHA], '[ CHA :', minstat, ']')
    if npc == 'ZeusDial' and Player.father == 'Zeus' :
        print('4', NpcDial[npc][DIALSON], '[ Enfant de', NpcDial[npc][NPCNAME], ']')
    elif npc == 'PoseidonDial' and Player.father == 'Poséidon' :
        print('4', NpcDial[npc][DIALSON], '[ Enfant de', NpcDial[npc][NPCNAME], ']')
    elif npc == 'HadesDial' and Player.father == 'Hadès' :
        print('4', NpcDial[npc][DIALSON], '[ Enfant de', NpcDial[npc][NPCNAME], ']')
    print('-------------------------------------')
    DialChoice = input(' > ')
    print(')(=================================================)(')
    if DialChoice == '1' :
        promptSlow(NpcDial[npc][DIAL1])
        promptSlow(NpcDial[npc][DIAL1_1])
    elif DialChoice == '2' :
        promptSlow(NpcDial[npc][DIAL2])
        promptSlow(NpcDial[npc][DIAL2_1])
    elif (DialChoice == '3') and (Player.Cha >= minstat) :
        promptSlow(NpcDial[npc][DIALCHA])
        promptSlow(NpcDial[npc][DIALCHA1])
        ObjectInventory(NpcDial[npc][GIFT])
    elif (DialChoice == '3') and (Player.Cha < minstat) :
        promptSlow('Vous n\'avez pas le charisme nécessaire. Choisissez une autre option.')
        Dialogue(npc)
    elif (DialChoice == '4') and (npc == 'ZeusDial') and (Player.father == 'Zeus') :
        promptSlow(NpcDial[npc][DIALSON])
        promptSlow(NpcDial[npc][DIALSON1])
        Player.Atk += 10
        # Le joueur gagne un bonus d'attaque de la part de son père.
    elif (DialChoice == '4') and (npc == 'PoseidonDial') and (Player.father == 'Poséidon') :
        promptSlow(NpcDial[npc][DIALSON])
        promptSlow(NpcDial[npc][DIALSON1])
        Player.Hp += 10
        # Le joueur gagne un bonus de vie de la part de son père.
    elif (DialChoice == '4') and (npc == 'HadesDial') and (Player.father == 'Hadès') :
        promptSlow(NpcDial[npc][DIALSON])
        promptSlow(NpcDial[npc][DIALSON1])
        Player.Atk += 5
        Player.Hp += 5
        # Le joueur gagne un bonus d'attaque et de vie de la part de son père.
    else :
        print('ERREUR : Veuillez entrer le chiffre correspondant au dialogue voulu.')
        Dialogue(npc)
    if npc == 'SphinxDial' :
        SphinxEnigma()

# Dialogue('SphinxDial')

# Player.Cha += 3000
# Player.father = 'Poséidon'
# Dialogue('PoseidonDial')

def QuestionBonus1(zeus, poseidon, hades) :
    print('<>==============================<>')
    promptSlow('Vous préférez vous baigner...')
    print('1 - Dans une rivière, profitant de l\'eau douce et de ses murmures.')
    time.sleep(0.3)
    print('2 - Dans la mer, bercé par les effluves de l\'océan tumultueux.')
    print('<>==============================<>')
    AnswerBonus1 = input(' > ')
    if AnswerBonus1 == '1' :
        promptSlow('Vous êtes l\'enfant d\'Hadès')
        Player.father = 'Hadès'
        # AJOUTER modification stats (à déterminer)
    elif AnswerBonus1 == '2' :
        promptSlow('Vous êtes l\'enfant de Poséidon')
        Player.father = 'Poséidon'
        # AJOUTER modification stats (à déterminer)
    else :
        print('ERREUR : Veuillez entrer le chiffre correspondant à l\'une des questions posées.')
        QuestionBonus1(zeus, poseidon, hades)

def QuestionBonus2(zeus, poseidon, hades) :
    print('<>==============================<>')
    promptSlow('Qu\'est-ce qui vous impressionne le plus ?')
    print('1 - Le tonnerre, aussi bruyant que destructeur.')
    time.sleep(0.3)
    print('2 - Les tremblements de terre, puissants et imprévisibles.')
    print('<>==============================<>')
    AnswerBonus2 = input(' > ')
    if AnswerBonus2 == '1' :
        promptSlow('Vous êtes l\'enfant de Zeus')
        Player.father = 'Zeus'
        # AJOUTER modification stats (à déterminer)
    elif AnswerBonus2 == '2' :
        promptSlow('Vous êtes l\'enfant de Poséidon')
        Player.father = 'Poséidon'
        # AJOUTER modification stats (à déterminer)
    else :
        print('ERREUR : Veuillez entrer le chiffre correspondant à l\'une des questions posées.')
        QuestionBonus2(zeus, poseidon, hades)

def QuestionBonus3(zeus, poseidon, hades) :
    print('<>==============================<>')
    promptSlow('Deux chemins s\'offrent à vous alors que vous tentez de rejoindre un endroit lointain. Lequel choisissez-vous ?')
    print('1 - Un pont vertigineux, si haut que les nuages vous chatouillent la plante des pieds.')
    time.sleep(0.3)
    print('2 - Un tunnel souterrain, plongé dans l\'obscurité la plus totale.')
    print('<>==============================<>')
    AnswerBonus3 = input(' > ')
    if AnswerBonus3 == '1' :
        promptSlow('Vous êtes l\'enfant de Zeus')
        Player.father = 'Zeus'
        # AJOUTER modification stats (à déterminer)
    elif AnswerBonus3 == '2' :
        promptSlow('Vous êtes l\'enfant d\'Hadès')
        Player.father = 'Hadès'
        # AJOUTER modification stats (à déterminer)
    else :
        print('ERREUR : Veuillez entrer le chiffre correspondant à l\'une des questions posées.')
        QuestionBonus3(zeus, poseidon, hades)

def Question1(zeus, poseidon, hades) :
    print('<>==============================<>')
    promptSlow('D\'où venez-vous ?')
    print('1 - D\'Olympie, à l\'ombre des platanes et des oliviers du bois sacré d\'Altis.')
    time.sleep(0.3)
    print('2 - Du Cap Sounion, bercé par les effluves iodées de la Mer Egée.')
    time.sleep(0.3)
    print('3 - De l\'Epire, dans la vallée de l\'Achéron, au bord d\'un fleuve à l\'aura étrange.')
    print('<>==============================<>')
    Answer1 = input(' > ')
    if Answer1 == '1' :
        zeus += 1
    elif Answer1 == '2' :
        poseidon += 1
    elif Answer1 == '3' :
        hades += 1
    else :
        print('ERREUR : Veuillez entrer le chiffre correspondant à l\'une des questions posées.')
        Question1(zeus, poseidon, hades)
    Question2(zeus, poseidon, hades)

def Question2(zeus, poseidon, hades) :
    print('<>==============================<>')
    promptSlow('Quel métier exerciez-vous ?')
    print('1 - Un humble pêcheur.')
    time.sleep(0.3)
    print('2 - Mineur, dans l\'obscurité quasi-constante.')
    time.sleep(0.3)
    print('3 - Un métier ? J\'étais un ROI, moi !')
    print('<>==============================<>')
    Answer2 = input(' > ')
    if Answer2 == '1' :
        zeus += 1
    elif Answer2 == '2' :
        poseidon += 1
    elif Answer2 == '3' :
        hades += 1
    else :
        print('ERREUR : Veuillez entrer le chiffre correspondant à l\'une des questions posées.')
        Question2(zeus, poseidon, hades)
    Question3(zeus, poseidon, hades)

def Question3(zeus, poseidon, hades) :
    print('<>==============================<>')
    promptSlow('Alors que vous étiez encore un jeune enfant, un événement vous a bouleversé...')
    print('1 - La nuit où un être défunt s\'est adressé à vous en rêve.')
    time.sleep(0.3)
    print('2 - La foudre vous a frappé, vous marquant à vie sans laisser aucune séquelle pour autant.')
    time.sleep(0.3)
    print('3 - La fois où vous êtes tombé d\'une trirème et avez failli vous noyer mais qu\'une vague vous a redéposé à bord.')
    print('<>==============================<>')
    Answer3 = input(' > ')
    if Answer3 == '1' :
        zeus += 1
    elif Answer3 == '2' :
        poseidon += 1
    elif Answer3 == '3' :
        hades += 1
    else :
        print('ERREUR : Veuillez entrer le chiffre correspondant à l\'une des questions posées.')
        Question3(zeus, poseidon, hades)
    Question4(zeus, poseidon, hades)

def Question4(zeus, poseidon, hades) :
    print('<>==============================<>')
    promptSlow('L\'animal qui vous correspond le plus est...')
    print('1 - L\'aigle, noble et majestueux.')
    time.sleep(0.3)
    print('2 - Le serpent, discret et rusé.')
    time.sleep(0.3)
    print('3 - Le dauphin, rapide et fédérateur.')
    print('<>==============================<>')
    Answer4 = input(' > ')
    if Answer4 == '1' :
        zeus += 1
    elif Answer4 == '2' :
        poseidon += 1
    elif Answer4 == '3' :
        hades += 1
    else :
        print('ERREUR : Veuillez entrer le chiffre correspondant à l\'une des questions posées.')
        Question4(zeus, poseidon, hades)
    Question5(zeus, poseidon, hades)

def Question5(zeus, poseidon, hades) :
    print('<>==============================<>')
    promptSlow('De tous les monstres présents dans les histoires qui vous ont été contées, le plus puissant est sans aucun doute...')
    print('1 - Cerbère, le terrible gardien des Enfers.')
    time.sleep(0.3)
    print('2 - Les cyclopes, grands, puissants et au regard de braise.')
    time.sleep(0.3)
    print('3 - Les monstres ne peuvent rien face à ma puissance.')
    print('<>==============================<>')
    Answer5 = input(' > ')
    if Answer5 == '1' :
        zeus += 1
    elif Answer5 == '2' :
        poseidon += 1
    elif Answer5 == '3' :
        hades += 1
    else :
        print('ERREUR : Veuillez entrer le chiffre correspondant à l\'une des questions posées.')
        Question5(zeus, poseidon, hades)

    # Solving equality issues

    if hades == poseidon :
        QuestionBonus1(zeus, poseidon, hades)
    elif poseidon == zeus :
        QuestionBonus2(zeus, poseidon, hades)
    elif zeus == hades :
        QuestionBonus3(zeus, poseidon, hades)
    else :
        if zeus > (poseidon and hades) :
            promptSlow('Vous êtes l\'enfant de Zeus')
            Player.father = 'Zeus'
            # AJOUTER modification stats (à déterminer)
        elif poseidon > (zeus and hades) :
            promptSlow('Vous êtes l\'enfant de Poséidon')
            Player.father = 'Poséidon'
            # AJOUTER modification stats (à déterminer)
        elif hades > (zeus and poseidon) :
            promptSlow('Vous êtes l\'enfant d\'Hadès')
            Player.father = 'Hadès'
            # AJOUTER modification stats (à déterminer)
    StartDial()


# print('Zeus = ', AnswerZeus)
# print('Poseidon = ', AnswerPoseidon)
# print('Hadès = ', AnswerHades)
def StartDial():
    print ('<>==============================<>')
    print('')
    print(')(=================================================)(')
    print('Mystérieux inconnu :')
    promptSlow('"Héros ! Tu m\'entends ? Hé ho ! Par Athéna, écoute-moi !" Perdu, vous parvenez difficilement à ouvrir les yeux. Vous vous trouvez dans une salle carrée vide. En face de vous, un homme vous fixe d\'un regard inquiet et intelligent : "Ah, tu as repris connaissance, c\'est bien. Doucement, doucement.')
    promptSlow('"Quel est ton nom ?"')
    HeroName = input('NOM : > ')
    Player.name = HeroName
    print(Player.name)
    OdysseusDialogue()

def OdysseusDialogue() :
    print('-------------------------------------')
    print('1 - Où sommes-nous ?')
    print('2 - Qui êtes-vous ?')
    print('3 - Et maintenant ?')
    print('4 - Je vais trouver le moyen de mettre fin à ce chaos. (Passer)')
    print('-------------------------------------')
    OdysseusAnswer = input(' > ')
    if OdysseusAnswer == '1' :
        promptSlow('- Où sommes-nous ?')
        promptSlow('- Alors là, j\'ai bien peur de ne pas pouvoir te répondre, {}. Il semblerait que l\'espace et le temps s\'entremêlent en ce lieu. Par les dieux, comment Dédale a-t-il pu acquérir pareils pouvoirs ?!'.format(Player.name))
        OdysseusDialogue()
    elif OdysseusAnswer == '2' :
        promptSlow('- Qui êtes-vous ?')
        promptSlow('- Je suis Ulysse, Roi d\'Ithaque. Et toi, tu dois être le héros choisi par ceux qui règnent sur l\'Olympe et sur le monde des hommes. J\'espère que c\'était le bon choix, l\'enjeux est crucial...')
        OdysseusDialogue()
    elif OdysseusAnswer == '3' :
        promptSlow('- Et maintenant ?')
        promptSlow('- J\'ai bien peur que tu n\'aies pas d\'autre solution que de mettre fin à cette folie.')
        promptSlow('- Vous n\'allez pas m\'aider ?')
        promptSlow('- Crois-moi, je le ferais, si je le pouvais. Seulement, ma présence ici est temporaire. Zeus est parvenu à convaincre Morphée de me laisser te contacter. Il sait se montrer persuasif... Seulement, tu ne vas pas tarder à te réveiller, alors je dois faire vite, le temps presse. Tu dois trouver la source vitale du labyrinthe ! Dédale a dû choisir une créature assez puissante pour le supporter. Probablement une créature liée à son passé, je le crains... Seulement, il faudrait une créature ayant à la fois une force physique et mentale hors du commun. Mais qui ? Quoi ? C\'est à toi de le découvrir, je suppose. Une fois que tu feras face à cette source, tu devras la détruire pour que tout revienne dans l\'ordre. C\'est le seul moyen d\'en finir avec cette folie.')
        OdysseusDialogue()
    elif OdysseusAnswer == '4' :
        promptSlow('- Je vais trouver le moyen de mettre fin à ce chaos.')
        promptSlow('- Prudence, {}.'.format(Player.name))
        print(')(=================================================)(')
        print('')
        promptSlow('Vous vous réveillez dans la même salle que celle de votre rêve, à la différence près qu\'Ulysse n\'est plus là pour vous aider. Soudain, les murs Est et Ouest de la salle s\'effondrent, vous laissant le choix entre deux chemins.')
        main_game_loop()
    else :
        print('ERREUR : Veuillez entrer le chiffre correspondant au dialogue voulu.')
        OdysseusDialogue()
  
def saveGame(): 
    # database 
    db = {} 
    db['PlayerName'] = Player.name
    db['PlayerHp'] = Player.Hp
    db['PlayerAtk'] = Player.Atk
    db['PlayerCha'] = Player.Cha
    db['Playerpos'] = Player.pos
    db['Playerlvl'] = Player.lvl
    db['Playerxp'] = Player.xp
    db['Playerfather'] = Player.father
    db['Playertextspeed'] = Player.textspeed
    db['ActiveCase'] = ActiveCase
    db['Inventory'] = Inventory
      
    # Création ou update du fichier
    dbfile = open('SaveFile', 'wb') 
      
    # source, destination 
    pickle.dump(db, dbfile)                      
    dbfile.close() 
  
def loadGame(): 
    dbfile = open('SaveFile', 'rb')      
    db = pickle.load(dbfile) 
    Player.name = db['PlayerName']
    Player.Hp = db['PlayerHp']
    Player.Atk = db['PlayerAtk']
    Player.Cha = db['PlayerCha']
    Player.pos = db['Playerpos']
    Player.lvl = db['Playerlvl']
    Player.xp = db['Playerxp']
    Player.father = db['Playerfather']
    Player.textspeed = db['Playertextspeed']
    LoadedActiveCase = db['ActiveCase']
    LoadedInventory = db['Inventory']
    dbfile.close()
    ActiveCase.clear()
    ActiveCase.update(LoadedActiveCase)
    Inventory.clear()
    Inventory.update(LoadedInventory)
    promptSlow('Chargement effectué ! Bon jeu !')
    main_game_loop()

PrintMainMenu()
MainMenu()