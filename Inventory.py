#Initialisation of variables
NAME = 'name'
DESCRIPTION = 'description'
EFFECT = 'effect'
from Stats import PlayerStats

Player = PlayerStats()

#Library for objects
Objects = {
          'ambrosia':{
            NAME: 'Ambroisie',
            DESCRIPTION: 'la boisson des dieux',
            EFFECT: '+ 10 HP',
          },
          'shield':{
            NAME: 'BOUCLIER DE PERSEE',
            DESCRIPTION: '',
            EFFECT: '',
          },
          'club':{
            NAME: 'MASSUE D\'HERCULE',
            DESCRIPTION: '',
            EFFECT: '',
          },
          'fire':{
            NAME: 'FEU SACRE',
            DESCRIPTION: '',
            EFFECT: '',
          },
          'belt':{
            NAME: 'CEINTURE D\'APHRODITE',
            DESCRIPTION: '',
            EFFECT: '',
          },
}

#Library for inventory
Inventory = {'slot1':'empty','slot2':'empty','slot3':'empty','slot4':'empty','slot5':'empty',}




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