HeroTurn = True

def CombatTest(HeroTurn):
    if HeroTurn == False :
        print('Tour de l\'adversaire')
        HeroTurn = True
        CombatTest(HeroTurn)
    elif HeroTurn == True :
        print('Vous croisez une poule')
        print(']===================================[')
        print('1 - ATTAQUER')
        print('2 - SE DÉFENDRE')
        print('3 - OBJET')
        print('4 - FUIR')
        print(']===================================[')
        Action = int(input())
        if Action == 1 :
            print('Le Joueur attaque')
            HeroTurn = False
            print(HeroTurn)
            CombatTest(HeroTurn)
            # Attaquer : lancer 1d20 ?
        elif Action == 2 :
            print('ok')
            # Se défendre : Diminue de 3/4 la prochaine attaque ennemie
        elif Action == 3 :
            print('ok2')
            # Afficher liste des objets présents dans l'inventaire
        elif Action == 4 :
            print('ok3')
            # Tentative de fuite (pourcentage de réussite dépendant des stats et objets)

class MobChicken :
    def __init__(self, CuisseDePoulet):
        self.name = 'Poule'
        self.Hp = 1
        self.Atk = 0
        self.loot = CuisseDePoulet

CombatTest(HeroTurn)