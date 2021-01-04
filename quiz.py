

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
        AnswerZeus = AnswerZeus + 1
    elif Answer1 == 2 :
        AnswerPoseidon = AnswerPoseidon + 1
    elif Answer1 == 3 :
        AnswerHades = AnswerHades + 1

    # Question 2
    print('<>==============================<>')
    print('Quel métier exerciez-vous ?')
    print('1 - Un humble pêcheur.')
    print('2 - Mineur, dans l\'obscurité quasi-constante.')
    print('3 - Un métier ? J\'étais un ROI, moi !')
    print('<>==============================<>')
    Answer2 = int(input())
    if Answer2 == 1 :
        AnswerPoseidon = AnswerPoseidon + 1
    elif Answer2 == 2 :
        AnswerHades = AnswerHades + 1
    elif Answer2 == 3 :
        AnswerZeus = AnswerZeus + 1

    # Question 3
    print('<>==============================<>')
    print('Alors que vous étiez encore un jeune enfant, un événement vous a bouleversé...')
    print('1 - La nuit où un être défunt s\'est adressé à vous en rêve.')
    print('2 - La foudre vous a frappé, vous marquant à vie sans laisser aucune séquelle pour autant.')
    print('3 - La fois où vous êtes tombé d\'une trirème et avez failli vous noyer mais qu\'une vague vous a redéposé à bord.')
    print('<>==============================<>')
    Answer3 = int(input())
    if Answer3 == 1 :
        AnswerHades = AnswerHades + 1
    elif Answer3 == 2 :
        AnswerZeus = AnswerZeus + 1
    elif Answer3 == 3 :
        AnswerPoseidon = AnswerPoseidon + 1

    # Question 4
    print('<>==============================<>')
    print('L\'animal qui vous correspond le plus est...')
    print('1 - L\'aigle, noble et majestueux.')
    print('2 - Le serpent, discret et rusé.')
    print('3 - Le dauphin, rapide et fédérateur.')
    print('<>==============================<>')
    Answer4 = int(input())
    if Answer4 == 1 :
        AnswerZeus = AnswerZeus + 1
    elif Answer4 == 2 :
        AnswerHades = AnswerHades + 1
    elif Answer4 == 3 :
        AnswerPoseidon = AnswerPoseidon + 1

    # Question 5
    print('<>==============================<>')
    print('De tous les monstres présents dans les histoires qui vous ont été contées, le plus puissant est sans aucun doute...')
    print('1 - Cerbère, le terrible gardien des Enfers.')
    print('2 - Les cyclopes, grands, puissants et au regard de braise.')
    print('3 - Les monstres ne peuvent rien face à ma puissance.')
    print('<>==============================<>')
    Answer5 = int(input())
    if Answer5 == 1 :
        AnswerHades = AnswerHades + 1
    elif Answer5 == 2 :
        AnswerPoseidon = AnswerPoseidon + 1
    elif Answer5 == 3 :
        AnswerZeus = AnswerZeus + 1

    if AnswerZeus > (AnswerPoseidon and AnswerHades) :
        print('Vous êtes le fils de Zeus')
    elif AnswerPoseidon > (AnswerZeus and AnswerHades) :
        print('Vous êtes le fils de Poséidon')
    elif AnswerHades > (AnswerZeus and AnswerPoseidon) :
        print('Vous êtes le fils d\'Hadès')

StartQuiz()

# Ajouter moyen de résoudre les égalités