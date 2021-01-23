import time
from Map import main_game_loop
from Tools import promptSlow
from Stats import PlayerStats
Player = PlayerStats()

def QuestionBonus1(zeus, poseidon, hades) :
    AnswerZeus = zeus
    AnswerPoseidon = poseidon
    AnswerHades = hades
    print('<>==============================<>')
    promptSlow('Vous préférez vous baigner...')
    print('1 - Dans une rivière, profitant de l\'eau douce et de ses murmures.')
    time.sleep(0.3)
    print('2 - Dans la mer, bercé par les effluves de l\'océan tumultueux.')
    print('<>==============================<>')
    AnswerBonus1 = int(input(' > '))
    if AnswerBonus1 == 1 :
        promptSlow('Vous êtes l\'enfant d\'Hadès')
        # AJOUTER modification stats (à déterminer)
    elif AnswerBonus1 == 2 :
        promptSlow('Vous êtes l\'enfant de Poséidon')
        # AJOUTER modification stats (à déterminer)
    else :
        print('ERREUR : Veuillez entrer le chiffre correspondant à l\'une des questions posées.')
        QuestionBonus1(zeus, poseidon, hades)

def QuestionBonus2(zeus, poseidon, hades) :
    AnswerZeus = zeus
    AnswerPoseidon = poseidon
    AnswerHades = hades
    print('<>==============================<>')
    promptSlow('Qu\'est-ce qui vous impressionne le plus ?')
    print('1 - Le tonnerre, aussi bruyant que destructeur.')
    time.sleep(0.3)
    print('2 - Les tremblements de terre, puissants et imprévisibles.')
    print('<>==============================<>')
    AnswerBonus2 = int(input(' > '))
    if AnswerBonus2 == 1 :
        promptSlow('Vous êtes l\'enfant de Zeus')
        # AJOUTER modification stats (à déterminer)
    elif AnswerBonus2 == 2 :
        promptSlow('Vous êtes l\'enfant de Poséidon')
        # AJOUTER modification stats (à déterminer)
    else :
        print('ERREUR : Veuillez entrer le chiffre correspondant à l\'une des questions posées.')
        QuestionBonus2(zeus, poseidon, hades)

def QuestionBonus3(zeus, poseidon, hades) :
    AnswerZeus = zeus
    AnswerPoseidon = poseidon
    AnswerHades = hades
    print('<>==============================<>')
    promptSlow('Deux chemins s\'offrent à vous alors que vous tentez de rejoindre un endroit lointain. Lequel choisissez-vous ?')
    print('1 - Un pont vertigineux, si haut que les nuages vous chatouillent la plante des pieds.')
    time.sleep(0.3)
    print('2 - Un tunnel souterrain, plongé dans l\'obscurité la plus totale.')
    print('<>==============================<>')
    AnswerBonus3 = int(input(' > '))
    if AnswerBonus3 == 1 :
        promptSlow('Vous êtes l\'enfant de Zeus')
        # AJOUTER modification stats (à déterminer)
    elif AnswerBonus3 == 2 :
        promptSlow('Vous êtes l\'enfant d\'Hadès')
        # AJOUTER modification stats (à déterminer)
    else :
        print('ERREUR : Veuillez entrer le chiffre correspondant à l\'une des questions posées.')
        QuestionBonus3(zeus, poseidon, hades)

def Question1(zeus, poseidon, hades) :
    AnswerZeus = zeus
    AnswerPoseidon = poseidon
    AnswerHades = hades
    print('<>==============================<>')
    promptSlow('D\'où venez-vous ?')
    print('1 - D\'Olympie, à l\'ombre des platanes et des oliviers du bois sacré d\'Altis.')
    time.sleep(0.3)
    print('2 - Du Cap Sounion, bercé par les effluves iodées de la Mer Egée.')
    time.sleep(0.3)
    print('3 - De l\'Epire, dans la vallée de l\'Achéron, au bord d\'un fleuve à l\'aura étrange.')
    print('<>==============================<>')
    Answer1 = int(input(' > '))
    if Answer1 == 1 :
        AnswerZeus += 1
        zeus = AnswerZeus
    elif Answer1 == 2 :
        AnswerPoseidon += 1
        poseidon = AnswerPoseidon
    elif Answer1 == 3 :
        AnswerHades += 1
        hades = AnswerHades
    else :
        print('ERREUR : Veuillez entrer le chiffre correspondant à l\'une des questions posées.')
        Question1(zeus, poseidon, hades)
    Question2(zeus, poseidon, hades)

def Question2(zeus, poseidon, hades) :
    AnswerZeus = zeus
    AnswerPoseidon = poseidon
    AnswerHades = hades
    print('<>==============================<>')
    promptSlow('Quel métier exerciez-vous ?')
    print('1 - Un humble pêcheur.')
    time.sleep(0.3)
    print('2 - Mineur, dans l\'obscurité quasi-constante.')
    time.sleep(0.3)
    print('3 - Un métier ? J\'étais un ROI, moi !')
    print('<>==============================<>')
    Answer2 = int(input(' > '))
    if Answer2 == 1 :
        AnswerPoseidon += 1
        poseidon = AnswerPoseidon
    elif Answer2 == 2 :
        AnswerHades += 1
        hades = AnswerHades
    elif Answer2 == 3 :
        AnswerZeus += 1
        zeus = AnswerZeus
    else :
        print('ERREUR : Veuillez entrer le chiffre correspondant à l\'une des questions posées.')
        Question2(zeus, poseidon, hades)
    Question3(zeus, poseidon, hades)

def Question3(zeus, poseidon, hades) :
    AnswerZeus = zeus
    AnswerPoseidon = poseidon
    AnswerHades = hades
    print('<>==============================<>')
    promptSlow('Alors que vous étiez encore un jeune enfant, un événement vous a bouleversé...')
    print('1 - La nuit où un être défunt s\'est adressé à vous en rêve.')
    time.sleep(0.3)
    print('2 - La foudre vous a frappé, vous marquant à vie sans laisser aucune séquelle pour autant.')
    time.sleep(0.3)
    print('3 - La fois où vous êtes tombé d\'une trirème et avez failli vous noyer mais qu\'une vague vous a redéposé à bord.')
    print('<>==============================<>')
    Answer3 = int(input(' > '))
    if Answer3 == 1 :
        AnswerHades += 1
        hades = AnswerHades
    elif Answer3 == 2 :
        AnswerZeus += 1
        zeus = AnswerZeus
    elif Answer3 == 3 :
        AnswerPoseidon += 1
        poseidon = AnswerPoseidon
    else :
        print('ERREUR : Veuillez entrer le chiffre correspondant à l\'une des questions posées.')
        Question3(zeus, poseidon, hades)
    Question4(zeus, poseidon, hades)

def Question4(zeus, poseidon, hades) :
    AnswerZeus = zeus
    AnswerPoseidon = poseidon
    AnswerHades = hades
    print('<>==============================<>')
    promptSlow('L\'animal qui vous correspond le plus est...')
    print('1 - L\'aigle, noble et majestueux.')
    time.sleep(0.3)
    print('2 - Le serpent, discret et rusé.')
    time.sleep(0.3)
    print('3 - Le dauphin, rapide et fédérateur.')
    print('<>==============================<>')
    Answer4 = int(input(' > '))
    if Answer4 == 1 :
        AnswerZeus += 1
        zeus = AnswerZeus
    elif Answer4 == 2 :
        AnswerHades += 1
        hades = AnswerHades
    elif Answer4 == 3 :
        AnswerPoseidon += 1
        poseidon = AnswerPoseidon
    else :
        print('ERREUR : Veuillez entrer le chiffre correspondant à l\'une des questions posées.')
        Question4(zeus, poseidon, hades)
    Question5(zeus, poseidon, hades)

def Question5(zeus, poseidon, hades) :
    AnswerZeus = zeus
    AnswerPoseidon = poseidon
    AnswerHades = hades
    print('<>==============================<>')
    promptSlow('De tous les monstres présents dans les histoires qui vous ont été contées, le plus puissant est sans aucun doute...')
    print('1 - Cerbère, le terrible gardien des Enfers.')
    time.sleep(0.3)
    print('2 - Les cyclopes, grands, puissants et au regard de braise.')
    time.sleep(0.3)
    print('3 - Les monstres ne peuvent rien face à ma puissance.')
    print('<>==============================<>')
    Answer5 = int(input(' > '))
    if Answer5 == 1 :
        AnswerHades += 1
        hades = AnswerHades
    elif Answer5 == 2 :
        AnswerPoseidon += 1
        poseidon = AnswerPoseidon
    elif Answer5 == 3 :
        AnswerZeus += 1
        zeus = AnswerZeus
    else :
        print('ERREUR : Veuillez entrer le chiffre correspondant à l\'une des questions posées.')
        Question5(zeus, poseidon, hades)

    # Solving equality issues

    if AnswerHades == AnswerPoseidon :
        QuestionBonus1(zeus, poseidon, hades)
    elif AnswerPoseidon == AnswerZeus :
        QuestionBonus2(zeus, poseidon, hades)
    elif AnswerZeus == AnswerHades :
        QuestionBonus3(zeus, poseidon, hades)
    else :
        if AnswerZeus > (AnswerPoseidon or AnswerHades) :
            promptSlow('Vous êtes l\'enfant de Zeus')
            # AJOUTER modification stats (à déterminer)
        elif AnswerPoseidon > (AnswerZeus or AnswerHades) :
            promptSlow('Vous êtes l\'enfant de Poséidon')
            # AJOUTER modification stats (à déterminer)
        elif AnswerHades > (AnswerZeus or AnswerPoseidon) :
            promptSlow('Vous êtes l\'enfant d\'Hadès')
            # AJOUTER modification stats (à déterminer)

Question1(0, 0, 0)

# print('Zeus = ', AnswerZeus)
# print('Poseidon = ', AnswerPoseidon)
# print('Hadès = ', AnswerHades)
print ('<>==============================<>')
print('')
print(')(=================================================)(')
print('Mystérieux inconnu :')
promptSlow('"Héros ! Tu m\'entends ? Hé ho ! Par Athéna, écoute-moi !" Perdu, vous parvenez difficilement à ouvrir les yeux. Vous vous trouvez dans une salle carrée vide. En face de vous, un homme vous fixe d\'un regard inquiet et intelligent : "Ah, tu as repris connaissance, c\'est bien. Doucement, doucement.')
promptSlow('"Quel est ton nom ?"')
HeroName = str(input('NOM : > '))
Player.name = HeroName
print(Player.name)
def OdysseusDialogue() :
    print('-------------------------------------')
    print('1 - Où sommes-nous ?')
    print('2 - Qui êtes-vous ?')
    print('3 - Et maintenant ?')
    print('4 - Je vais trouver le moyen de mettre fin à ce chaos. (Passer)')
    print('-------------------------------------')
    OdysseusAnswer = int(input())
    if OdysseusAnswer == 1 :
        promptSlow('- Où sommes-nous ?')
        promptSlow('- Alors là, j\'ai bien peur de ne pas pouvoir te répondre, {}. Il semblerait que l\'espace et le temps s\'entremêlent en ce lieu. Par les dieux, comment Dédale a-t-il pu acquérir pareils pouvoirs ?!'.format(Player.name))
        OdysseusDialogue()
    elif OdysseusAnswer == 2 :
        promptSlow('- Qui êtes-vous ?')
        promptSlow('- Je suis Ulysse, Roi d\'Ithaque. Et toi, tu dois être le héros choisi par ceux qui règnent sur l\'Olympe et sur le monde des hommes. J\'espère que c\'était le bon choix, l\'enjeux est crucial...')
        OdysseusDialogue()
    elif OdysseusAnswer == 3 :
        promptSlow('- Et maintenant ?')
        promptSlow('- J\'ai bien peur que tu n\'aies pas d\'autre solution que de mettre fin à cette folie.')
        promptSlow('- Vous n\'allez pas m\'aider ?')
        promptSlow('- Crois-moi, je le ferais, si je le pouvais. Seulement, ma présence ici est temporaire. Zeus est parvenu à convaincre Morphée de me laisser te contacter. Il sait se montrer persuasif... Seulement, tu ne vas pas tarder à te réveiller, alors je dois faire vite, le temps presse. Tu dois trouver la source vitale du labyrinthe ! Dédale a beau avoir l\'intelligence d\'un dieu, il n\'en est pas un pour autant, et il est bien trop faible pour créer cet endroit à partir de sa seule psyché. Une fois que tu feras face à cette source, tu devras la détruire pour que tout revienne dans l\'ordre. C\'est le seul moyen d\'en finir avec cette folie.')
        OdysseusDialogue()
    elif OdysseusAnswer == 4 :
        promptSlow('- Je vais trouver le moyen de mettre fin à ce chaos.')
        promptSlow('- Prudence, {}.'.format(Player.name))
        print(')(=================================================)(')
        print('')
        promptSlow('Vous vous réveillez dans la même salle que celle de votre rêve, à la différence près qu\'Ulysse n\'est plus là pour vous aider. Soudain, les murs Est et Ouest de la salle s\'effondrent, vous laissant le choix entre deux chemins.')
        main_game_loop()
    else :
        print('ERREUR : Veuillez entrer le chiffre correspondant au dialogue voulu.')
        OdysseusDialogue()
OdysseusDialogue()

#     main_game_loop()
