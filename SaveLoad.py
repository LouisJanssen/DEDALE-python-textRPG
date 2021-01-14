### SAUVEGARDE ###
import os.path
file_exists = os.path.isfile('loadfile.txt')

def load():
  if file_exists:
    file = open('loadfile.txt','r')
    room = file.read()
    file.close()
  else:
    room='startroom'
  roomchooser(room)

def save(s):
  file = open('loadfile.txt','w')
  file.write(s)
  file.close()

def roomchooser(room):
  if room=='startroom':
    startroom()
  elif room=='secondroom':
    secondroom()

def startroom():
  s='startroom'
  save(s)
  print('you are in the bitch\'s sources go left or right?')
  direction=input()
  if direction == 'right':
    secondroom()
  quit()

def secondroom():
  s='secondroom'
  save(s)
  print('you are in hell, left or right?')
  direction=input()
  if direction == 'right':
    startroom()
  quit()

load()