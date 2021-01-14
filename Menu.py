# print("\033[1;34;48m Salut je suis du bright blue\033")
import time

def PrintMainMenu():
  print('-------------------------')
  print('DEDALE')
  print('-------------------------')
  print('')
  print('JOUER')
  print('CHARGER')
  print('INSTRUCTIONS')
  print('CREDITS')
  print('QUITTER')
  print('')
  print('____________________________________________________________')

def PlayMenu():
  print('JOUER')
  print('CONTINUER')
  print('')
  print('____________________________________________________________')

def LoadMenu():
  print('SAUVEGARDE 1')
  print('SAUVEGARDE 2')
  print('SAUVEGARDE 3')
  print('RETOUR')
  print('')
  print('____________________________________________________________')

def InstructionsMenu():
  print('INSTRUCTIONS :')
  print('Le but du jeu est d\'atteindre le boss et de le vaincre, pour ce faire vous aurrez à l\'écran différents choix à faire que ce soit pour les déplacements, les choix de dialogue ou encore les combats.')
  print('Pour effectuer une action entrez simplement ce que vous souhaitez faire dans le terminal')
  print('RETOUR')
  print('')
  print('Appuyez sur la touche correspondante')
  ChoiceMainMenu = int(input())
  if ChoiceMainMenu == 1 :
    PrintMainMenu()
    MainMenu()
  print('____________________________________________________________')

def CreditsMenu():
  print('Code : Louis Janssen & François Olona')
  print('Histoire : Louis Janssen & François Olona')
  print('Art ASCII : https://www.asciiart.eu/')
  print('Remerciements : Monsieur Loïc Janin')
  print('1 - RETOUR')
  print('')
  print('Appuyez sur la touche correspondante')
  ChoiceMainMenu = int(input())
  if ChoiceMainMenu == 1 :
    PrintMainMenu()
    MainMenu()
  print('____________________________________________________________')

def MainMenu ():
  ChoiceMainMenu = int(input())
  if ChoiceMainMenu == 1 :
    PlayMenu()
  elif ChoiceMainMenu == 2 :
    LoadMenu()
  elif ChoiceMainMenu == 3 :
    InstructionsMenu()
  elif ChoiceMainMenu == 4 :
    CreditsMenu()
  elif ChoiceMainMenu == 5 :
    print('PERSONNE NE S\'ECHAPPE DU LABYRINTHE !')
    time.sleep(2)
    PrintMainMenu()
    MainMenu()
    print('____________________________________________________________')
