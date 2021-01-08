# IMPORTS
from DiceSystem import DiceRoll
from Stats import PlayerStats
Player = PlayerStats()
from Stats import ChickenStats
from Stats import SpiderStats

# MOBS
Chicken = ChickenStats()
Spider = SpiderStats()

# COMBAT
HeroTurn = True

def Combat(HeroTurn, ennemy):

    if HeroTurn == False : # TOUR DE L'ADVERSAIRE
        print('Tour de l\'adversaire')
        HeroTurn = True
        if ennemy.Hp > 0 :
            print(ennemy.Hp)
            print('L\'ennemi fait son action')
        else :
            print('L\'ennemi est K.O.')
        # Combat(HeroTurn, ennemy)

    elif HeroTurn == True : # TOUR DU JOUEUR
        print('Vous croisez un [NAME]')
        print(']===================================[')
        print('1 - ATTAQUER')
        print('2 - SE DÉFENDRE')
        print('3 - OBJETS')
        print('4 - FUIR')
        print(']===================================[')
        Action = int(input())

        if Action == 1 :
            print('Le Joueur attaque')
            HeroTurn = False
            print(HeroTurn)
            Attack = DiceRoll()
            print('Lancer de dé :', Attack)
            if Attack >= 10 : # Modifier plus tard en fonction des stats du joueur
                ennemy.Hp -= Player.Atk # Ajouter plus tard les bonus relatifs à la STR
            Combat(HeroTurn, ennemy)

        elif Action == 2 :
            print('Se défendre')
            # Se défendre : Diminue de 3/4 la prochaine attaque ennemie

        elif Action == 3 :
            print('Objets')
            # Afficher liste des objets présents dans l'inventaire

        elif Action == 4 :
            print('Fuir')
            # Tentative de fuite (pourcentage de réussite dépendant des stats et objets)

Combat(HeroTurn, Spider)