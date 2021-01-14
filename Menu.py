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
  print('Le but du jeu est d\'atteindre le boss et de le vaincre, pour ce faire vous aurez à l\'écran différents choix à faire que ce soit pour les déplacements, les choix de dialogue ou encore les combats.')
  print('Pour effectuer une action entrez simplement ce que vous souhaitez faire dans le terminal')
  print('Pour obtenir une liste des commandes en jeux entrez : aide')
  print('RETOUR')
  print('')
  print('Appuyez sur la touche correspondante')
  ChoiceMainMenu = input()
  if ChoiceMainMenu.lower() == 'retour' :
    PrintMainMenu()
    MainMenu()
  print('____________________________________________________________')

def CreditsMenu():
  print('Code : Louis Janssen & François Olona')
  print('Histoire : Louis Janssen & François Olona')
  print('Art ASCII : https://www.asciiart.eu/')
  print('Remerciements : Monsieur Loïc Janin')
  print('RETOUR')
  print('')
  print('Appuyez sur la touche correspondante')
  ChoiceMainMenu = input()
  if ChoiceMainMenu.lower() == 'retour' :
    PrintMainMenu()
    MainMenu()
  print('____________________________________________________________')

def MainMenu ():
  ChoiceMainMenu = input()
  if ChoiceMainMenu.lower() == 'jouer' :
    PlayMenu()
  elif ChoiceMainMenu.lower() == 'charger' :
    LoadMenu()
  elif ChoiceMainMenu.lower() == 'instructions' :
    InstructionsMenu()
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