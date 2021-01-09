import cmd
import textwrap
import sys
import os
import time
import random

class PlayerPos:
  def __init__(self):
    self.pos = 'D3'

PlayerPos = PlayerPos()

#### MAP ####
ZONENAME = ''
DESCRIPTION = 'description'
ACTIVECASE = True
NORTH = 'north'
SOUTH = 'south'
EAST = 'east'
WEST = 'west'

ActiveCase = {'A1': True, 'A2': True, 'A3': True,'A4': True, 'A5': True,
              'B1': True, 'B2': True, 'B3': True,'B4': True, 'B5': True,
              'C1': True, 'C2': True, 'C3': True,'C4': True, 'C5': True,
              'D1': True, 'D2': True, 'D3': True,'D4': True, 'D5': True,
              'E1': True, 'E2': True, 'E3': True,'E4': True, 'E5': True,
              'F1': True, 'F2': True, 'F3': True,'F4': True, 'F5': True
              }

ZoneMap = {
  'A1': {
    ZONENAME: 'Beach',
    DESCRIPTION: 'Bitch you are at the beach',
    ACTIVECASE: True,
    NORTH: '',
    SOUTH: 'B1',
    EAST: 'A2',
    WEST: '',
  },
  'B1': {
    ZONENAME: 'Town',
    DESCRIPTION: '',
    ACTIVECASE: True,
    NORTH: 'A1',
    SOUTH: 'C1',
    EAST: '',
    WEST: '',
  },
  'C1': {
    ZONENAME: 'Whorehouse',
    DESCRIPTION: '',
    ACTIVECASE: True,
    NORTH: 'B1',
    SOUTH: 'D1',
    EAST: 'C2',
    WEST: '',
  },
  'D1': {
    ZONENAME: '',
    DESCRIPTION: '',
    ACTIVECASE: True,
    NORTH: 'C1',
    SOUTH: 'E1',
    EAST: 'D2',
    WEST: '',
  },
  'E1': {
    ZONENAME: '',
    DESCRIPTION: '',
    ACTIVECASE: True,
    NORTH: 'D1',
    SOUTH: 'F1',
    EAST: 'E2',
    WEST: '',
  },
  'F1': {
    ZONENAME: '',
    DESCRIPTION: '',
    ACTIVECASE: True,
    NORTH: 'E1',
    SOUTH: '',
    EAST: 'F2',
    WEST: '',
  },
  'A2': {
    ZONENAME: 'Test',
    DESCRIPTION: '',
    ACTIVECASE: True,
    NORTH: '',
    SOUTH: '',
    EAST: 'A3',
    WEST: 'A1',
  },
  'B2': {
    ZONENAME: '',
    DESCRIPTION: '',
    ACTIVECASE: True,
    NORTH: '',
    SOUTH: '',
    EAST: 'B3',
    WEST: '',
  },
  'C2': {
    ZONENAME: '',
    DESCRIPTION: '',
    ACTIVECASE: True,
    NORTH: '',
    SOUTH: 'D2',
    EAST: '',
    WEST: 'C1',
  },
  'D2': {
    ZONENAME: 'dsgfs',
    DESCRIPTION: 'gfdsgf',
    ACTIVECASE: True,
    NORTH: 'C2',
    SOUTH: '',
    EAST: 'D3',
    WEST: 'D1',
  },
  'E2': {
    ZONENAME: '',
    DESCRIPTION: '',
    ACTIVECASE: True,
    NORTH: '',
    SOUTH: '',
    EAST: '',
    WEST: 'E1',
  },
  'F2': {
    ZONENAME: '',
    DESCRIPTION: '',
    ACTIVECASE: True,
    NORTH: '',
    SOUTH: '',
    EAST: 'F3',
    WEST: 'F1',
  },
  'A3': {
    ZONENAME: '',
    DESCRIPTION: '',
    ACTIVECASE: True,
    NORTH: '',
    SOUTH: 'B3',
    EAST: 'A4',
    WEST: 'A2',
  },
  'B3': {
    ZONENAME: '',
    DESCRIPTION: '',
    ACTIVECASE: True,
    NORTH: 'A3',
    SOUTH: 'C3',
    EAST: '',
    WEST: 'B2',
  },
  'C3': {
    ZONENAME: 'Hell',
    DESCRIPTION: 'dsgfdg',
    ACTIVECASE: True,
    NORTH: 'B3',
    SOUTH: 'D3',
    EAST: '',
    WEST: '',
  },
  'D3': {
    ZONENAME: 'Start',
    DESCRIPTION: 'descritohgf',
    ACTIVECASE: True,
    NORTH: 'C3',
    SOUTH: 'E3',
    EAST: 'D4',
    WEST: 'D2',
  },
  'E3': {
    ZONENAME: 'gdfdgf',
    DESCRIPTION: 'dfggdfg',
    ACTIVECASE: True,
    NORTH: 'D3',
    SOUTH: '',
    EAST: 'E4',
    WEST: '',
  },
  'F3': {
    ZONENAME: '',
    DESCRIPTION: '',
    ACTIVECASE: True,
    NORTH: '',
    SOUTH: '',
    EAST: 'F4',
    WEST: 'F2',
  },
  'A4': {
    ZONENAME: '',
    DESCRIPTION: '',
    ACTIVECASE: True,
    NORTH: '',
    SOUTH: '',
    EAST: 'A5',
    WEST: 'A3',
  },
  'B4': {
    ZONENAME: '',
    DESCRIPTION: '',
    ACTIVECASE: True,
    NORTH: '',
    SOUTH: '',
    EAST: 'B5',
    WEST: '',
  },
  'C4': {
    ZONENAME: '',
    DESCRIPTION: '',
    ACTIVECASE: True,
    NORTH: '',
    SOUTH: 'D4',
    EAST: 'C5',
    WEST: '',
  },
  'D4': {
    ZONENAME: 'ruytru',
    DESCRIPTION: 'ruhgfj',
    ACTIVECASE: True,
    NORTH: 'C4',
    SOUTH: '',
    EAST: 'D5',
    WEST: 'D3',
  },
  'E4': {
    ZONENAME: '',
    DESCRIPTION: '',
    ACTIVECASE: True,
    NORTH: '',
    SOUTH: 'F4',
    EAST: 'E5',
    WEST: 'E3',
  },
  'F4': {
    ZONENAME: '',
    DESCRIPTION: '',
    ACTIVECASE: True,
    NORTH: 'E4',
    SOUTH: '',
    EAST: '',
    WEST: 'F3',
  },
  'A5': {
    ZONENAME: '',
    DESCRIPTION: '',
    ACTIVECASE: True,
    NORTH: '',
    SOUTH: 'B5',
    EAST: '',
    WEST: 'A4',
  },
  'B5': {
    ZONENAME: '',
    DESCRIPTION: '',
    ACTIVECASE: True,
    NORTH: 'A5',
    SOUTH: 'C5',
    EAST: '',
    WEST: 'B4',
  },
  'C5': {
    ZONENAME: '',
    DESCRIPTION: '',
    ACTIVECASE: True,
    NORTH: 'B5',
    SOUTH: '',
    EAST: '',
    WEST: 'C4',
  },
  'D5': {
    ZONENAME: '',
    DESCRIPTION: '',
    ACTIVECASE: True,
    NORTH: '',
    SOUTH: 'E5',
    EAST: '',
    WEST: 'D4',
  },
  'E5': {
    ZONENAME: '',
    DESCRIPTION: '',
    ACTIVECASE: True,
    NORTH: 'D5',
    SOUTH: 'F5',
    EAST: '',
    WEST: 'E4',
  },
  'F5': {
    ZONENAME: '',
    DESCRIPTION: '',
    ACTIVECASE: True,
    NORTH: 'E5',
    SOUTH: '',
    EAST: '',
    WEST: '',
  },
}

def PrintLocation():
  print(PlayerPos.pos.upper())
  print(ZoneMap[PlayerPos.pos][DESCRIPTION])

def prompt():
  print('What to do bitch?')
  action = input('>')
  if action.lower() == 'quit':
    sys.exit()
  elif action.lower() == 'move':
    PlayerMove(action.lower())

def PlayerMove(MyAction):
  ask = "Where to go?"
  dest = input(ask + '>')
  if dest == 'east':
    destination = ZoneMap[PlayerPos.pos][EAST]
    MovementHandler(destination)
  elif dest == 'north':
    destination = ZoneMap[PlayerPos.pos][NORTH]
    MovementHandler(destination)
  elif dest == 'south':
    destination = ZoneMap[PlayerPos.pos][SOUTH]
    MovementHandler(destination)
  elif dest == 'west':
    destination = ZoneMap[PlayerPos.pos][WEST]
    MovementHandler(destination)

def MovementHandler(destination):
  print('you move to the' + destination + '.')
  PlayerPos.pos = destination
  PrintLocation()

prompt()