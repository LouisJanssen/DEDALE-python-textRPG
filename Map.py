#Import of tools needed
import sys
import time
from Stats import PlayerStats

Player = PlayerStats()

#Creation of the MAP
ZONENAME = 'zonename'
DESCRIPTION = 'description'
NORTH = 'nord'
SOUTH = 'sud'
EAST = 'est'
WEST = 'ouest'
EVENT = 'event'

#Library for activation of map tiles
ActiveCase = {'A1': True, 'A2': True, 'A3': True,'A4': True, 'A5': True,
              'B1': True, 'B2': True, 'B3': True,'B4': True, 'B5': True,
              'C1': True, 'C2': True, 'C3': True,'C4': True, 'C5': True,
              'D1': True, 'D2': True, 'D3': True,'D4': True, 'D5': True,
              'E1': True, 'E2': True, 'E3': True,'E4': True, 'E5': True,
              'F1': True, 'F2': True, 'F3': True,'F4': True, 'F5': True
              }

#Library for the map
ZoneMap = {
  'A1': {
    ZONENAME: '',
    DESCRIPTION: '',
    NORTH: '',
    SOUTH: 'B1',
    EAST: 'A2',
    WEST: '',
    EVENT: 'object',
  },
  'B1': {
    ZONENAME: '',
    DESCRIPTION: '',
    NORTH: 'A1',
    SOUTH: 'C1',
    EAST: '',
    WEST: '',
    EVENT: 'fight',
  },
  'C1': {
    ZONENAME: '',
    DESCRIPTION: '',
    NORTH: 'B1',
    SOUTH: 'D1',
    EAST: 'C2',
    WEST: '',
    EVENT: 'npc',
  },
  'D1': {
    ZONENAME: '',
    DESCRIPTION: '',
    NORTH: 'C1',
    SOUTH: 'E1',
    EAST: 'D2',
    WEST: '',
    EVENT: 'fight',
  },
  'E1': {
    ZONENAME: '',
    DESCRIPTION: '',
    NORTH: 'D1',
    SOUTH: 'F1',
    EAST: 'E2',
    WEST: '',
    EVENT: 'object',
  },
  'F1': {
    ZONENAME: '',
    DESCRIPTION: '',
    NORTH: 'E1',
    SOUTH: '',
    EAST: 'F2',
    WEST: '',
    EVENT: 'fight',
  },
  'A2': {
    ZONENAME: '',
    DESCRIPTION: '',
    NORTH: '',
    SOUTH: '',
    EAST: 'A3',
    WEST: 'A1',
    EVENT: 'npc',
  },
  'B2': {
    ZONENAME: '',
    DESCRIPTION: '',
    NORTH: '',
    SOUTH: '',
    EAST: 'B3',
    WEST: '',
    EVENT: 'blessing',
  },
  'C2': {
    ZONENAME: '',
    DESCRIPTION: '',
    NORTH: '',
    SOUTH: 'D2',
    EAST: '',
    WEST: 'C1',
    EVENT: 'fight',
  },
  'D2': {
    ZONENAME: '',
    DESCRIPTION: '',
    NORTH: 'C2',
    SOUTH: '',
    EAST: 'D3',
    WEST: 'D1',
    EVENT: 'easter',
  },
  'E2': {
    ZONENAME: '',
    DESCRIPTION: '',
    NORTH: '',
    SOUTH: '',
    EAST: '',
    WEST: 'E1',
    EVENT: 'curse',
  },
  'F2': {
    ZONENAME: '',
    DESCRIPTION: '',
    NORTH: '',
    SOUTH: '',
    EAST: 'F3',
    WEST: 'F1',
    EVENT: 'npc',
  },
  'A3': {
    ZONENAME: '',
    DESCRIPTION: '',
    NORTH: '',
    SOUTH: 'B3',
    EAST: 'A4',
    WEST: 'A2',
    EVENT: 'BOSS',
  },
  'B3': {
    ZONENAME: '',
    DESCRIPTION: '',
    NORTH: 'A3',
    SOUTH: 'C3',
    EAST: '',
    WEST: 'B2',
    EVENT: 'npc',
  },
  'C3': {
    ZONENAME: '',
    DESCRIPTION: '',
    NORTH: 'B3',
    SOUTH: 'D3',
    EAST: '',
    WEST: '',
    EVENT: 'easter',
  },
  #### FRANCIS PART ^^^^^^^^^^^^
  'D3': {
    ZONENAME: '',
    DESCRIPTION: '',
    NORTH: 'C3',
    SOUTH: 'E3',
    EAST: 'D4',
    WEST: 'D2',
    EVENT: 'object',
  },
  'E3': {
    ZONENAME: '',
    DESCRIPTION: '',
    NORTH: 'D3',
    SOUTH: '',
    EAST: 'E4',
    WEST: '',
    EVENT: 'npc',
  },
  'F3': {
    ZONENAME: '',
    DESCRIPTION: '',
    NORTH: '',
    SOUTH: '',
    EAST: 'F4',
    WEST: 'F2',
    EVENT: 'start',
  },
  'A4': {
    ZONENAME: '',
    DESCRIPTION: '',
    NORTH: '',
    SOUTH: '',
    EAST: 'A5',
    WEST: 'A3',
    EVENT: 'npc',
  },
  'B4': {
    ZONENAME: '',
    DESCRIPTION: '',
    NORTH: '',
    SOUTH: '',
    EAST: 'B5',
    WEST: '',
    EVENT: 'curse',
  },
  'C4': {
    ZONENAME: '',
    DESCRIPTION: '',
    NORTH: '',
    SOUTH: 'D4',
    EAST: 'C5',
    WEST: '',
    EVENT: 'npc',
  },
  'D4': {
    ZONENAME: '',
    DESCRIPTION: '',
    NORTH: 'C4',
    SOUTH: '',
    EAST: 'D5',
    WEST: 'D3',
    EVENT: 'fight',
  },
  'E4': {
    ZONENAME: '',
    DESCRIPTION: '',
    NORTH: '',
    SOUTH: 'F4',
    EAST: 'E5',
    WEST: 'E3',
    EVENT: 'easter',
  },
  'F4': {
    ZONENAME: '',
    DESCRIPTION: '',
    NORTH: 'E4',
    SOUTH: '',
    EAST: '',
    WEST: 'F3',
    EVENT: 'npc',
  },
  'A5': {
    ZONENAME: '',
    DESCRIPTION: '',
    NORTH: '',
    SOUTH: 'B5',
    EAST: '',
    WEST: 'A4',
    EVENT: 'fight',
  },
  'B5': {
    ZONENAME: '',
    DESCRIPTION: '',
    NORTH: 'A5',
    SOUTH: 'C5',
    EAST: '',
    WEST: 'B4',
    EVENT: 'object',
  },
  'C5': {
    ZONENAME: '',
    DESCRIPTION: '',
    NORTH: 'B5',
    SOUTH: '',
    EAST: '',
    WEST: 'C4',
    EVENT: 'fight',
  },
  'D5': {
    ZONENAME: '',
    DESCRIPTION: '',
    NORTH: '',
    SOUTH: 'E5',
    EAST: '',
    WEST: 'D4',
    EVENT: 'object',
  },
  'E5': {
    ZONENAME: '',
    DESCRIPTION: '',
    NORTH: 'D5',
    SOUTH: 'F5',
    EAST: '',
    WEST: 'E4',
    EVENT: 'fight',
  },
  'F5': {
    ZONENAME: '',
    DESCRIPTION: '',
    NORTH: 'E5',
    SOUTH: '',
    EAST: '',
    WEST: '',
    EVENT: 'blessing',
  },
}

#display the location of the player
def PrintLocation():
  print(ZoneMap[Player.pos][ZONENAME].upper())
  if(ActiveCase[Player.pos] == True):
    print(ZoneMap[Player.pos][DESCRIPTION])
  else:
    print('Vous êtes déjà passé par ici, il ne reste plus rien d\'intéressant')
  

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
    print('Que souhaitez vous faire ?')
    action = input('\n > ')
    if action.lower() == 'quitter':
      sys.exit()
    elif action.lower() == 'voyager':
      PlayerMove(action.lower())
    elif action.lower() == 'aide':
      print('Liste des commandes: ')
      print('voyager        -       vous permets de vous déplacer')
      print('inventaire     -       vous permets d\'accéder à votre inventaire')
      print('carte          -       vous permets d\'accéder à votre carte')
      print('journal        -       vous permets d\'accéder à votre journal de quête')
      print('aide           -       vous permet d\'avoir une liste des commandes')
      print('quitter        -       vous permet de quitter le jeu')

#function for the movement of the player
def PlayerMove(MyAction):
  ask = "Où souhaitez-vous aller ?"
  dest = input(ask + '\n > ')

  if dest == 'est':
    if ZoneMap[Player.pos][EAST] == '':
      print('Impossible d\'aller dans cette direction, un mur vous bloque la route.')
      PlayerMove(MyAction)
    elif (ZoneMap[ZoneMap[Player.pos][EAST]][EVENT] == 'BOSS'):
      print('Vous êtes face au combat ultime, vous ne pourrez plus revenir en arrière, êtes vous sûr de vouloir continuer ?')
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
      print('Impossible d\'aller dans cette direction, un mur vous bloque la route.')
      PlayerMove(MyAction)
    elif (ZoneMap[ZoneMap[Player.pos][NORTH]][EVENT] == 'BOSS'):
      print('Vous êtes face au combat ultime, vous ne pourrez plus revenir en arrière, êtes vous sûr de vouloir continuer ?')
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
      print('Impossible d\'aller dans cette direction, un mur vous bloque la route.')
      PlayerMove(MyAction)
    elif (ZoneMap[ZoneMap[Player.pos][SOUTH]][EVENT] == 'BOSS'):
      print('Vous êtes face au combat ultime, vous ne pourrez plus revenir en arrière, êtes vous sûr de vouloir continuer ?')
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
      print('Impossible d\'aller dans cette direction, un mur vous bloque la route.')
      PlayerMove(MyAction)
    elif (ZoneMap[ZoneMap[Player.pos][WEST]][EVENT] == 'BOSS'):
      print('Vous êtes face au combat ultime, vous ne pourrez plus revenir en arrière, êtes vous sûr de vouloir continuer ?')
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
  print('Vous quittez ' + ZoneMap[Player.pos][ZONENAME])
  Player.pos = destination
  PrintLocation()

#Main game loop function
def main_game_loop():
  while Player.won is False:
    prompt()

########## ZONE DE TESTS ##########
#test 001
def testlecombat():
  print('boum boum')
  ActiveCase[Player.pos] = False
  time.sleep(2)
  prompt()

def testeaster():
  print('easter')
  ActiveCase[Player.pos] = False
  time.sleep(2)
  prompt()
def testblessing():
  print('blessing')
  ActiveCase[Player.pos] = False
  time.sleep(2)
  prompt()

def testcurse():
  print('curse')
  ActiveCase[Player.pos] = False
  time.sleep(2)
  prompt()

def testobject():
  print('object')
  ActiveCase[Player.pos] = False
  time.sleep(2)
  prompt()

def testnpc():
  print('npc')
  ActiveCase[Player.pos] = False
  time.sleep(2)
  prompt()

main_game_loop()

