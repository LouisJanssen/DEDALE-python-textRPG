# IMPORTS
from DiceSystem import DiceRoll
from Stats import *
Player = PlayerStats()

# CURRENT MOB STATS

class EnnemyStats:
    def __init__(self):
        self.name = MobStats[currentname][NAME]
        self.

# COMBAT
PlayerTurn = True

def Combat(PlayerTurn, ennemy, playerdefense):

    PlayerDefense = playerdefense
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
                if MobAttack >= 10 : # Modifier plus tard en fonction des stats du joueur (AGI...)
                    if PlayerDefense == False :
                        Player.Hp -= ennemy.Atk # Ajouter plus tard les bonus relatifs à la STR
                    elif PlayerDefense == True :
                        Player.Hp -= (3/4)*(ennemy.Atk) # Les dégâts sont réduits de 3/4 si le joueur se défend
                else :
                    print('Loupé !')

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
            print('4 - FUIR')
            print(']===================================[')
            Action = int(input())

            if Action == 1 :
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

            elif Action == 2 :
                print('Se défendre')
                PlayerDefense = True
                playerdefense = PlayerDefense
                PlayerTurn = False
                # Se défendre : Diminue de 3/4 la prochaine attaque ennemie
                Combat(PlayerTurn, ennemy, playerdefense)

            elif Action == 3 :
                print('Objets')
                # Afficher liste des objets présents dans l'inventaire

            elif Action == 4 :
                print('Fuir')
                # Tentative de fuite (pourcentage de réussite dépendant des stats et objets)
    
    elif Player.Hp <= 0 :
        print('GAME OVER')
    
    elif (Player.Hp > 0) and (ennemy.Hp <= 0) :
        print('VICTOIRE')

Combat(PlayerTurn, 'EnnemyStats', False)

# SavePlayerStats = PlayerStats()
# SaveMobStats = SpiderStats()

# Player.Hp -= 5
# print(Player.Hp)
# Player = SavePlayerStats
# print(Player.Hp)

# def ResetStats():
#     # Réinitialise les stats après le combat
