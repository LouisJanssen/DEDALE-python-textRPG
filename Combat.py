def CombatTest():
    print('Vous croisez une poule')
    print(']===================================[')
    print('1 - ATTAQUER')
    print('2 - SE DÉFENDRE')
    print('3 - OBJET')
    print('4 - FUIR')
    print(']===================================[')
    Action = int(input())
    if Action == 1 :
        # Attaquer : lancer 1d20 ?
    elif Action == 2 :
        # Se défendre : Diminue de 3/4 la prochaine attaque ennemie
    elif Action == 3 :
        # Afficher liste des objets présents dans l'inventaire
    elif Action == 4 :
        # Tentative de fuite (pourcentage de réussite dépendant des stats et objets)

