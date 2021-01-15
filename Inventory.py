#Initialisation of variables
NAME = 'name'
DESCRIPTION = 'description'
EFFECT = 'effect'
from Stats import PlayerStats

Player = PlayerStats()

#Library for objects
Objects = {
          'ambroisie':{
            NAME: 'AMBROISIE',
            DESCRIPTION: 'la boisson des dieux',
            EFFECT: '+ 10 HP',
          },
          'bouclier':{
            NAME: 'BOUCLIER',
            DESCRIPTION: '',
            EFFECT: '',
          },
          'épée':{
            NAME: 'EPEE',
            DESCRIPTION: '',
            EFFECT: '',
          },
          'casque':{
            NAME: 'CASQUE',
            DESCRIPTION: '',
            EFFECT: '',
          },
          'armure':{
            NAME: 'ARMURE',
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