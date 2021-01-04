# print("\033[1;34;48m Salut je suis du bright blue\033")
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
  print('CECI EST LES INSTRUCTIONS')
  print('1 - RETOUR')
  print('')
  print('Appuyez sur la touche correspondante')
  print('____________________________________________________________')

def CreditsMenu():
  print('Code : Louis Janssen & François Olona')
  print('1 - RETOUR')
  print('')
  print('Appuyez sur la touche correspondante')
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
    print('Merci d\'avoir joué !')
    print('____________________________________________________________')
