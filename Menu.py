# print("\033[1;34;48m Salut je suis du bright blue\033")
import time

def PrintMainMenu():
  print('-------------------------')
  print('DEDALE')
  print('-------------------------')
  print('')
  print('1 - JOUER')
  print('2 - CHARGER')
  print('3 - INSTRUCTIONS')
  print('4 - CREDITS')
  print('5 - QUITTER')
  print('')
  print('Appuyez sur la touche correspondante')
  print('____________________________________________________________')

def PlayMenu():
  print('1 - JOUER')
  print('2 - CONTINUER')
  print('')
  print('Appuyez sur la touche correspondante')
  print('____________________________________________________________')

def LoadMenu():
  print('1 - SAUVEGARDE 1')
  print('2 - SAUVEGARDE 2')
  print('3 - SAUVEGARDE 3')
  print('4 - RETOUR')
  print('')
  print('Appuyez sur la touche correspondante')
  print('____________________________________________________________')

def InstructionsMenu():
  print('INSTRUCTIONS :')
  print('Le but du jeu est d\'atteindre le boss et de le vaincre, pour ce faire vous aurrez à l\'écran différents choix à faire que ce soit pour les déplacements, les choix de dialogue ou encore les combats.')
  print('Pour choisir une action entrez le chiffre correspondant à l\'action désirée dans le terminal')
  print('1 - RETOUR')
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
