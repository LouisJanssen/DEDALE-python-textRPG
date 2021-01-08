

def StartQuiz():
    AnswerZeus = 0
    AnswerPoseidon = 0
    AnswerHades = 0

    # Question 1
    print('<>==============================<>')
    print('D\'où venez-vous ?')
    print('1 - D\'Olympie, à l\'ombre des platanes et des oliviers du bois sacré d\'Altis.')
    print('2 - Du Cap Sounion, bercé par les effluves iodées de la Mer Egée.')
    print('3 - De l\'Epire, dans la vallée de l\'Achéron, au bord d\'un fleuve à l\'aura étrange.')
    print('<>==============================<>')
    Answer1 = int(input())
    if Answer1 == 1 :
        AnswerZeus += 1
    elif Answer1 == 2 :
        AnswerPoseidon += 1
    elif Answer1 == 3 :
        AnswerHades += 1

    # Question 2
    print('<>==============================<>')
    print('Quel métier exerciez-vous ?')
    print('1 - Un humble pêcheur.')
    print('2 - Mineur, dans l\'obscurité quasi-constante.')
    print('3 - Un métier ? J\'étais un ROI, moi !')
    print('<>==============================<>')
    Answer2 = int(input())
    if Answer2 == 1 :
        AnswerPoseidon += 1
    elif Answer2 == 2 :
        AnswerHades += 1
    elif Answer2 == 3 :
        AnswerZeus += 1

    # Question 3
    print('<>==============================<>')
    print('Alors que vous étiez encore un jeune enfant, un événement vous a bouleversé...')
    print('1 - La nuit où un être défunt s\'est adressé à vous en rêve.')
    print('2 - La foudre vous a frappé, vous marquant à vie sans laisser aucune séquelle pour autant.')
    print('3 - La fois où vous êtes tombé d\'une trirème et avez failli vous noyer mais qu\'une vague vous a redéposé à bord.')
    print('<>==============================<>')
    Answer3 = int(input())
    if Answer3 == 1 :
        AnswerHades += 1
    elif Answer3 == 2 :
        AnswerZeus += 1
    elif Answer3 == 3 :
        AnswerPoseidon += 1

    # Question 4
    print('<>==============================<>')
    print('L\'animal qui vous correspond le plus est...')
    print('1 - L\'aigle, noble et majestueux.')
    print('2 - Le serpent, discret et rusé.')
    print('3 - Le dauphin, rapide et fédérateur.')
    print('<>==============================<>')
    Answer4 = int(input())
    if Answer4 == 1 :
        AnswerZeus += 1
    elif Answer4 == 2 :
        AnswerHades += 1
    elif Answer4 == 3 :
        AnswerPoseidon += 1

    # Question 5
    print('<>==============================<>')
    print('De tous les monstres présents dans les histoires qui vous ont été contées, le plus puissant est sans aucun doute...')
    print('1 - Cerbère, le terrible gardien des Enfers.')
    print('2 - Les cyclopes, grands, puissants et au regard de braise.')
    print('3 - Les monstres ne peuvent rien face à ma puissance.')
    print('<>==============================<>')
    Answer5 = int(input())
    if Answer5 == 1 :
        AnswerHades += 1
    elif Answer5 == 2 :
        AnswerPoseidon += 1
    elif Answer5 == 3 :
        AnswerZeus += 1
    
    # Solving equality issues
    if AnswerHades == AnswerPoseidon :
        print('<>==============================<>')
        print('Vous préférez vous baigner...')
        print('1 - Dans une rivière, profitant de l\'eau douce et de ses murmures.')
        print('2 - Dans la mer, bercé par les effluves de l\'océan tumultueux.')
        print('<>==============================<>')
        AnswerBonus1 = int(input())
        if AnswerBonus1 == 1 :
            AnswerHades += 1
        elif AnswerBonus1 == 2 :
            AnswerPoseidon += 1
    
    if AnswerPoseidon == AnswerZeus :
        print('<>==============================<>')
        print('Qu\'est-ce qui vous effraye le plus ?')
        print('1 - Le tonnerre, aussi bruyant que destructeur.')
        print('2 - Les tremblements de terre, puissants et imprévisibles.')
        print('<>==============================<>')
        AnswerBonus2 = int(input())
        if AnswerBonus2 == 1 :
            AnswerZeus += 1
        elif AnswerBonus2 == 2 :
            AnswerPoseidon += 1

    if AnswerZeus == AnswerHades :
        print('<>==============================<>')
        print('Deux chemins s\'offrent à vous alors que vous tentez de rejoindre un endroit lointain. Lequel choisissez-vous ?')
        print('1 - Un pont vertigineux, si haut que les nuages vous chatouillent la plante des pieds.')
        print('2 - Un tunnel souterrain, plongé dans l\'obscurité la plus totale.')
        print('<>==============================<>')
        AnswerBonus3 = int(input())
        if AnswerBonus3 == 1 :
            AnswerZeus += 1
        elif AnswerBonus3 == 2 :
            AnswerHades += 1

    if AnswerZeus > (AnswerPoseidon or AnswerHades) :
        print('Vous êtes le fils de Zeus')
    elif AnswerPoseidon > (AnswerZeus or AnswerHades) :
        print('Vous êtes le fils de Poséidon')
    elif AnswerHades > (AnswerZeus or AnswerPoseidon) :
        print('Vous êtes le fils d\'Hadès')
    
    print('Zeus = ', AnswerZeus)
    print('Poseidon = ', AnswerPoseidon)
    print('Hadès = ', AnswerHades)

StartQuiz()

# Ajouter moyen de résoudre les égalités