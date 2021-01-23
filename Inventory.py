from Stats import PlayerStats
from Tools import promptSlow

Player = PlayerStats()
#Initialisation of variables
NAME = 'name'
DESCRIPTION = 'description'
EFFECT = 'effect'

# from Stats import PlayerStats
# Player = PlayerStats()

#Library for objects
Objects = {
          'ambrosia':{
            NAME: 'Ambroisie',
            DESCRIPTION: 'la boisson des dieux',
            EFFECT: 'Rends 10 HP',
          },
          'shield':{
            NAME: 'BOUCLIER DE PERSEE',
            DESCRIPTION: 'Un bouclier mythique ayant apartenu à Persée',
            EFFECT: 'Vous permet de bloquer l\'intégralité des combats',
          },
          'club':{
            NAME: 'MASSUE D\'HERACLES',
            DESCRIPTION: 'Une massue ayant appartenu à un héros mythique',
            EFFECT: 'Augmente l\'attaque de 2',
          },
          'fire':{
            NAME: 'FEU SACRE',
            DESCRIPTION: 'Vous pouvez le lancer pour infliger des dégâts',
            EFFECT: 'Inflige des dégâts à l\'ennemi.',
          },
          'belt':{
            NAME: 'CEINTURE D\'APHRODITE',
            DESCRIPTION: 'Une ceinture vous permettant d\'envouter n\'importe quel mortel',
            EFFECT: 'Augmente le charisme de 5',
          },
          'empty':{
            NAME: 'vide',
            DESCRIPTION: 'vide',
            EFFECT: '',
          },
}

SLOT = 'SLOT'
QUANTITY = 'QUANTITY'

#Library for inventory
Inventory = {
            'slot1':{
              SLOT:'fire',
              QUANTITY:'1',
            },
            'slot2':{
              SLOT:'ambrosia',
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
  print('Ou souhaitez vous placer l\'objet ?')
  print(InventoryList)
  ask = input(' > ')
  if ask == '1':
    if Inventory[('slot' + ask)][SLOT] == 'empty':
      Inventory[('slot' + ask)][SLOT] = objectName
      Inventory[('slot' + ask)][QUANTITY] = str(int(Inventory[('slot' + ask)][QUANTITY]) + 1)
    elif Inventory[('slot' + ask)][SLOT] == objectName:
      Inventory[('slot' + ask)][QUANTITY] = str(int(Inventory[('slot' + ask)][QUANTITY]) + 1)
    else:
      print("Voulez vous remplacer : " + Objects[Inventory[('slot' + ask)][SLOT]][NAME])
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

def displayInventory():
  promptSlow('Voici votre inventaire :')
  InventoryList = ['','','','','']
  for i in range(0,5):
    InventoryList[i] = Inventory[('slot' + str(i + 1))][SLOT]
  print(InventoryList)

def passiveObject():
  InventoryList = ['','','','','']
  for i in range(0,5):
    InventoryList[i] = Inventory[('slot' + str(i + 1))][SLOT]
  if "club" in InventoryList and clubUsed == False :
    clubUsed = True
    Player.Atk += 2
  elif "belt" in InventoryList and beltUsed == False :
    beltUsed = True
    Player.Cha += 5

# def useObject():
#   promptSlow("Quel objet souhaitez vous utiliser ?")
#   InventoryList = ['','','','','']
#   for i in range(0,5):
#     InventoryList[i] = Inventory[('slot' + str(i + 1))][SLOT]
#   print(InventoryList)
#   ask = input(' > ')
#   if ask in InventoryList:
#     if ask == 'ambrosia':
#       promptSlow('Vous buvez l\'ambroisie')
#       Player.Hp += 10
#     elif ask == 'Fire':
#       promptSlow('Vous lancer le feu sacré')

# --------------  ZONE DE TEST  ------------------
# def testInventory():
#   print(Objects)
#   print('---------------')
#   print(Inventory)
#   print('---------------')
#   i = 1
#   if Inventory[('slot' + str(i))] == 'empty':
#     Inventory[('slot' + str(i))] = 'ambrosia'
#   print(Inventory)

# def testUse(objectUsed):
#   print('avant' + str(Player.Hp))
#   if objectUsed == 'ambrosia':
#     Player.Hp += 10
#   print('après' + str(Player.Hp))


# i = 1 
# testInventory()
# testUse(Inventory[('slot' + str(i))])

# ObjectInventory('ambrosia')
# displayInventory()

# GERER LE NOM DES OBJETS
# Objects[Inventory[('slot' + str(i + 1))][SLOT]][NAME]