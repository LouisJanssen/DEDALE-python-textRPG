# IMPORTS
import sys
import time
from Main import *
from DiceSystem import DiceRoll
from Level import LevelUp
from Stats import *
from Inventory import Objects, Inventory
from Tools import promptSlow
Player = PlayerStats()

# SAVE PLAYER STATS
class SavePlayerStats:
    def __init__(self):
        self.Hp = 10
SaveHp = Player.Hp
SavePlayer = SavePlayerStats()
SavePlayer.Hp = SaveHp

# COMBAT
PlayerTurn = True

def Combat(PlayerTurn, ennemy, playerdefense):

    PlayerDefense = playerdefense

    def useObject():
        SLOT = 'SLOT'
        QUANTITY = 'QUANTITY'
        promptSlow("Quel objet souhaitez vous utiliser ?")
        promptSlow('Entrez "retour" pour revenir au menu de combat')
        InventoryList = ['','','','','']
        for i in range(0,5):
            InventoryList[i] = Inventory[('slot' + str(i + 1))][SLOT]
        print(InventoryList)
        ask = input(' > ')
        if ask in InventoryList:
            if ask.lower() == 'ambrosia':
                promptSlow('Vous buvez l\'ambroisie')
                Player.Hp += 10
                i = 1
                while Inventory[('slot' + str(i))][SLOT] != 'ambrosia':
                    i += 1
                Inventory[('slot' + str(i))][QUANTITY] = str(int(Inventory[('slot' + str(i))][QUANTITY]) - 1)
                if Inventory[('slot' + str(i))][QUANTITY] == '0':
                    Inventory[('slot' + str(i))][SLOT] = 'empty'
            elif ask.lower() == 'fire':
                promptSlow('Vous lancer le feu sacré')
                ennemy.Hp -= 10
                i = 1
                while Inventory[('slot' + str(i))][SLOT] != 'fire':
                    i += 1
                Inventory[('slot' + str(i))][QUANTITY] = str(int(Inventory[('slot' + str(i))][QUANTITY]) - 1)
                if Inventory[('slot' + str(i))][QUANTITY] == '0':
                    Inventory[('slot' + str(i))][SLOT] = 'empty'
            else:
                print('Veuillez choisir un consommable')
                useObject()
        elif ask.lower() == 'retour':
            Combat(PlayerTurn, ennemy, playerdefense)
        else:
            print('Commande inconnue')
            useObject()


    print('-----------------------------------------------------------------------')

    if (Player.Hp > 0) and (ennemy.Hp > 0) :

        if PlayerTurn == False : # TOUR DE L'ADVERSAIRE
            print('Tour de l\'adversaire')
            PlayerTurn = True
            if ennemy.Hp > 0 :
                print('L\'ennemi fait son action')
                
                # Action de l'adversaire
                # L'ennemi attaque
                MobAttack = DiceRoll()
                print('Lancer de dé ennemi :', MobAttack) # Est-ce qu'on l'affiche ?
                if MobAttack >= 10 : 
                    if PlayerDefense == False :
                        if ennemy.name == 'Minotaure' and ennemy.Hp <= 20 :
                            print('Astérion récupère une partie de l\'énergie vitale du labyrinthe pour se soigner.')
                            ennemy.Hp += 10
                        else :
                            print('L\'ennemi attaque !')
                            Player.Hp -= ennemy.Atk
                    elif PlayerDefense == True :
                        print('L\'ennemi perce légèrement votre défense !')
                        InventoryList = ['','','','','']
                        SLOT = 'SLOT'
                        for i in range(0,5):
                            InventoryList[i] = Inventory[('slot' + str(i + 1))][SLOT]
                        if 'shield' not in InventoryList:
                            Player.Hp -= (3/4)*(ennemy.Atk) # Les dégâts sont réduits de 3/4 si le joueur se défend
                else :
                    print('L\'ennemi a loupé !')

            else :
                print('L\'ennemi est K.O.')
            
            Combat(PlayerTurn, ennemy, playerdefense)

        elif PlayerTurn == True : # TOUR DU JOUEUR
            print('Joueur :', Player.name, '-', Player.Hp, 'PV')
            print('ENNEMI :', ennemy.name, '-', ennemy.Hp, 'PV')
            print(']===================================[')
            print('1 - ATTAQUER')
            print('2 - SE DÉFENDRE')
            print('3 - OBJETS')
            print(']===================================[')
            Action = input(' > ')

            if Action == '1' :
                print('Le Joueur attaque')
                PlayerDefense = False
                playerdefense = PlayerDefense
                PlayerTurn = False
                Attack = DiceRoll()
                print('Lancer de dé :', Attack)
                if Attack >= 10 : # Modifier plus tard en fonction des stats du joueur
                    ennemy.Hp -= Player.Atk # Ajouter plus tard les bonus relatifs à la STR
                else :
                    print('Loupé !')
                Combat(PlayerTurn, ennemy, playerdefense)

            elif Action == '2' :
                print('Se défendre')
                PlayerDefense = True
                playerdefense = PlayerDefense
                PlayerTurn = False
                # Se défendre : Diminue de 3/4 la prochaine attaque ennemie
                Combat(PlayerTurn, ennemy, playerdefense)

            elif Action == '3' :
                print('Objets')
                # Afficher liste des objets présents dans l'inventaire
                useObject()
                PlayerTurn = False
                Combat(PlayerTurn, ennemy, playerdefense)
            else:
                print("ERREUR : Veuillez entrer le chiffre correspondant à l\'une des questions posées.")
                Combat(PlayerTurn, ennemy, playerdefense)
    
    elif Player.Hp <= 0 :
        print('GAME OVER')
        Player.dead = True
        time.sleep(1)
        sys.exit()
    
    elif (Player.Hp > 0) and (ennemy.Hp <= 0) :
        if ennemy.name == 'Minotaure':
            print('Victoire vous avez vaincu le Minotaure !')
            print('Voulez-vous retourner au menu principal ou quitter le jeu?')
            ask = input(" > ")
            while not (ask.lower() == 'menu' or ask.lower() == 'quitter'):
                print('Commande inconnue, veuillez entrer "menu" ou "quitter"')
                ask = input(' > ')
            if ask.lower() == 'menu':
                PrintMainMenu()
                MainMenu()
            elif ask.lower() == 'quitter':
                print('Merci d\'avoir joué !')
                time.sleep(1)
                sys.exit()
        else:
            print('VICTOIRE')

def StartCombat(currentennemy):

    # SAVE MOB STATS
    class EnnemyStats:
        def __init__(self):
            self.name = MobStats[currentennemy][MOBNAME]
            self.Hp = MobStats[currentennemy][HP]
            self.Atk = MobStats[currentennemy][ATK]
    
    # COMBAT
    Combat(PlayerTurn, EnnemyStats(), False)

    # RESET PLAYER STATS (Mob stats reset automatically)
    Player.Hp = SavePlayer.Hp
    PlayerXP = Player.xp
    MobXP = MobStats[currentennemy][XP]
    LevelUp(PlayerXP, MobXP)

# StartCombat('MinotaurStats')
# StartCombat('ChickenStats')