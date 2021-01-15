# import of tools needed
import time
import sys

# function for slow prompt of prints
def promptSlow(phrase):
  for l in phrase:
    sys.stdout.write(l)
    sys.stdout.flush()
    time.sleep(0.05)
  print('')

# display of the menu
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

#PLay menu
def PlayMenu():
  print('JOUER')
  print('CONTINUER')
  print('')
  print('____________________________________________________________')

#Load menu
def LoadMenu():
  print('SAUVEGARDE 1')
  print('SAUVEGARDE 2')
  print('SAUVEGARDE 3')
  print('RETOUR')
  print('')
  print('____________________________________________________________')

# instructions menu
def InstructionsMenu():
  print('INSTRUCTIONS :')
  promptSlow('Le but du jeu est d\'atteindre le boss et de le vaincre, pour ce faire vous aurez à l\'écran différents choix à faire que ce soit pour les déplacements, les choix de dialogue ou encore les combats.')
  promptSlow('Pour effectuer une action entrez simplement ce que vous souhaitez faire dans le terminal')
  promptSlow('Pour obtenir une liste des commandes en jeux entrez : aide')
  print('')
  print('RETOUR')
  print('')
  ChoiceMainMenu = input(' > ')
  if ChoiceMainMenu.lower() == 'retour' :
    PrintMainMenu()
    MainMenu()

#credits menu
def CreditsMenu():
  promptSlow('Code : Louis Janssen & François Olona')
  promptSlow('Histoire : Louis Janssen & François Olona')
  promptSlow('Art ASCII : https://www.asciiart.eu/')
  promptSlow('Map inspirée de : https://www.youtube.com/watch?v=ERLT1iU0DVY&list=PL1-slM0ZOosXf2oQYZpTRAoeuo0TPiGpm&index=3&ab_channel=BryanTong')
  promptSlow('Ressources pédagogiques : https://courspython.com/classes-et-objets.html et https://docs.python.org/fr/3/library/index.html')
  promptSlow('Remerciements : Monsieur Loïc Janin')
  print('RETOUR')
  print('Appuyez sur la touche correspondante')
  ChoiceMainMenu = input()
  if ChoiceMainMenu.lower() == 'retour' :
    PrintMainMenu()
    MainMenu()
  print('____________________________________________________________')

#main function for the main menu
def MainMenu ():
  ChoiceMainMenu = input(' > ')
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
    promptSlow('Commande inconnue, essayez de rentrer une des instructions présente sur le menu ou tapez "instructions" pour avoir plus d\'infos. ')