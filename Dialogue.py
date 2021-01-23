# from Map import ZoneMap
from Stats import PlayerStats
from Tools import promptSlow
Player = PlayerStats()

# NpcDial['ZeusDial'][NPCNAME]

# npc = ZoneMap[Player.pos][SPEC]

# =======================================================
# NPC Dialogues Library

NPCNAME = 'NPCNAME'
MINSTAT = 'MINSTAT'
SENTENCE = 'SENTENCE'
DIAL1 = 'DIAL1'
DIAL1_1 = 'DIAL1_1'
DIAL2 = 'DIAL2'
DIAL2_1 = 'DIAL2_1'
DIALCHA = 'DIALCHA'
DIALCHA1 = 'DIALCHA1'
DIALSON = 'DIALSON'
DIALSON1 = 'DIALSON1'
GIFT = 'GIFT'

NpcDial = {
    'ZeusDial':{
        NPCNAME: 'Zeus',
        MINSTAT: 15,
        SENTENCE: '- Oui ? On me parle ?',
        DIAL1: '1 - Z-Zeus, c\'est bien vous ?',
        DIAL1_1: '- Bien sûr que oui, avorton ! Tu oses questionner ma royale identité ? Décidément, les héros de nos jours, c\'est plus ce que c\'était. Bon, je tenais quand même à te souhaiter bonne chance pour Dédale, tout ça. Sur ce, je dois y aller. Héra va encore me chercher des noises, sinon...',
        DIAL2: '2 - BlaBla',
        DIAL2_1: '- Kiki',
        DIALCHA: '3 - BliBlouBla',
        DIALCHA1: '- Kikiki',
        DIALSON: '4 - BlaBlouBli',
        DIALSON1: '- Ikikik',
        GIFT: 'not_defined',
    },
    'PoseidonDial':{
        NPCNAME: 'Poséidon',
        MINSTAT: 15,
        SENTENCE: 'Blablablablablabla',
        DIAL1: '1 - Bla',
        DIAL1_1: '- Ki',
        DIAL2: '2 - BlaBla',
        DIAL2_1: '- Kiki',
        DIALCHA: '3 - BliBlouBla',
        DIALCHA1: '- Kikiki',
        DIALSON: '4 - BlaBlouBli',
        DIALSON1: '- Ikikik',
        GIFT: 'not_defined',
    },
    'HadesDial':{
        NPCNAME: 'Hadès',
        MINSTAT: 15,
        SENTENCE: 'Blablablablablabla',
        DIAL1: '1 - Bla',
        DIAL1_1: '- Ki',
        DIAL2: '2 - BlaBla',
        DIAL2_1: '- Kiki',
        DIALCHA: '3 - BliBlouBla',
        DIALCHA1: '- Kikiki',
        DIALSON: '4 - BlaBlouBli',
        DIALSON1: '- Ikikik',
        GIFT: 'not_defined',
    },
    'ThanatosDial':{
        NPCNAME: 'Thanatos et Talos',
        MINSTAT: 15,
        SENTENCE: 'Blablablablablabla',
        DIAL1: '1 - Bla',
        DIAL1_1: '- Ki',
        DIAL2: '2 - BlaBla',
        DIAL2_1: '- Kiki',
        DIALCHA: '3 - BliBlouBla',
        DIALCHA1: '- Kikiki',
        GIFT: 'not_defined',
    },
    'DionysosDial':{
        NPCNAME: 'Dionysos',
        MINSTAT: 15,
        SENTENCE: 'Blablablablablabla',
        DIAL1: '1 - Bla',
        DIAL1_1: '- Ki',
        DIAL2: '2 - BlaBla',
        DIAL2_1: '- Kiki',
        DIALCHA: '3 - BliBlouBla',
        DIALCHA1: '- Kikiki',
        GIFT: 'not_defined',
    },
    'ParquesDial':{
        NPCNAME: 'Les Parques',
        MINSTAT: 15,
        SENTENCE: 'Blablablablablabla',
        DIAL1: '1 - Bla',
        DIAL1_1: '- Ki',
        DIAL2: '2 - BlaBla',
        DIAL2_1: '- Kiki',
        DIALCHA: '3 - BliBlouBla',
        DIALCHA1: '- Kikiki',
        GIFT: 'not_defined',
    },
    'MinosDial':{
        NPCNAME: 'Minos',
        MINSTAT: 15,
        SENTENCE: 'Blablablablablabla',
        DIAL1: '1 - Bla',
        DIAL1_1: '- Ki',
        DIAL2: '2 - BlaBla',
        DIAL2_1: '- Kiki',
        DIALCHA: '3 - BliBlouBla',
        DIALCHA1: '- Kikiki',
        GIFT: 'not_defined',
    },
    'SphinxDial':{
        NPCNAME: 'La Sphinge',
        MINSTAT: 15,
        SENTENCE: 'Blablablablablabla',
        DIAL1: '1 - Bla',
        DIAL1_1: '- Ki',
        DIAL2: '2 - BlaBla',
        DIAL2_1: '- Kiki',
        DIALCHA: '3 - BliBlouBla',
        DIALCHA1: '- Kikiki',
        GIFT: 'not_defined',
    },
}

# Énigme du Sphinx

def SphinxEnigma() :
    print('>-------------------------------------------------<')
    promptSlow('- Une dernière chose, {}. J\'ai une proposition à te faire, si tu te sens à la hauteur.'.format(Player.name))
    promptSlow('- De quoi s\'agit-il ?')
    promptSlow('- Une énigme.')
    promptSlow('- Ben tiens, étonnant, ça... Et qu\'est-ce que j\'y gagne ?')
    promptSlow('- De la force vitale...')
    promptSlow('- Et l\'entourloupe, elle est où ?')
    promptSlow('- Tu devras parier une partie de ta force vitale actuelle pour en gagner le double. Alors, qu\'en dis-tu ? Attention, tu n\'auras qu\'une seule chance.')
    print('1 - Je prends le risque, envoie ton énigme.')
    print('2 - Très peu pour moi, merci')
    print('>-------------------------------------------------<')
    StartEnigma = input()
    if StartEnigma == '1' :
        Player.Hp -= 5
        promptSlow('- Même en marchant vers lui, vous ne pouvez l\'atteindre.')
        promptSlow('Alors, {}, une idée ?'.format(Player.name))
        AnswerEnigma = input(' > ')
        if AnswerEnigma.lower() == 'l\'horizon' or AnswerEnigma.lower() == 'horizon' :
            promptSlow('- Alors là... Je dois admettre que je suis impressionnée. Tu es quelqu\'un de culture, {}. Laisse-moi augmenter tes points de v-... Euh, ta force vitale !'.format(Player.name))
            Player.Hp += 15
        else :
            promptSlow('Loupé, héhéhé ! La réponse était l\'horizon. Ne t\'en fais pas, va, tu t\'en sortiras très bien même si tu es un peu, disons, affaibli. Bon voyage, {}'.format(Player.name))

    elif StartEnigma == '2' :
        promptSlow('- C\'est facheux, tant pis. Je te pensais plus malin que ça, {}. Adieu, dans ce cas.'.format(Player.name))
    else :
        print('ERREUR : Veuillez entrer le chiffre correspondant au dialogue voulu.')
        SphinxEnigma()

def Dialogue(npc):
    minstat = NpcDial[npc][MINSTAT]
    print(')(=================================================)(')
    print(NpcDial[npc][NPCNAME], ':')
    print(NpcDial[npc][SENTENCE])
    print('-------------------------------------')
    print(NpcDial[npc][DIAL1])
    print(NpcDial[npc][DIAL2])
    print(NpcDial[npc][DIALCHA], '[ CHA :', minstat, ']')
    if npc == 'ZeusDial' and Player.father == 'Zeus' :
        print(NpcDial[npc][DIALSON], '[ Enfant de', NpcDial[npc][NPCNAME], ']')
    elif npc == 'PoseidonDial' and Player.father == 'Poséidon' :
        print(NpcDial[npc][DIALSON], '[ Enfant de', NpcDial[npc][NPCNAME], ']')
    elif npc == 'HadesDial' and Player.father == 'Hadès' :
        print(NpcDial[npc][DIALSON], '[ Enfant de', NpcDial[npc][NPCNAME], ']')
    print('-------------------------------------')
    DialChoice = input()
    print(')(=================================================)(')
    if DialChoice == '1' :
        promptSlow(NpcDial[npc][DIAL1])
        promptSlow(NpcDial[npc][DIAL1_1])
    elif DialChoice == '2' :
        promptSlow(NpcDial[npc][DIAL2])
        promptSlow(NpcDial[npc][DIAL2_1])
    elif (DialChoice == '3') and (Player.Cha >= minstat) :
        promptSlow(NpcDial[npc][DIALCHA])
        promptSlow(NpcDial[npc][DIALCHA1])
        # Le joueur recoit l'objet GIFT dans son inventaire
    elif (DialChoice == '3') and (Player.Cha < minstat) :
        promptSlow('Vous n\'avez pas le charisme nécessaire. Choisissez une autre option.')
        Dialogue(npc)
    elif (DialChoice == '4') and (npc == 'ZeusDial') and (Player.father == 'Zeus') :
        promptSlow(NpcDial[npc][DIALSON])
        promptSlow(NpcDial[npc][DIALSON1])
        Player.Atk += 10
        # Le joueur gagne un bonus d'attaque de la part de son père.
    elif (DialChoice == '4') and (npc == 'PoseidonDial') and (Player.father == 'Poséidon') :
        promptSlow(NpcDial[npc][DIALSON])
        promptSlow(NpcDial[npc][DIALSON1])
        Player.Hp += 10
        # Le joueur gagne un bonus de vie de la part de son père.
    elif (DialChoice == '4') and (npc == 'HadesDial') and (Player.father == 'Hadès') :
        promptSlow(NpcDial[npc][DIALSON])
        promptSlow(NpcDial[npc][DIALSON1])
        Player.Atk += 5
        Player.Hp += 5
        # Le joueur gagne un bonus d'attaque et de vie de la part de son père.
    else :
        print('ERREUR : Veuillez entrer le chiffre correspondant au dialogue voulu.')
        Dialogue(npc)
    if npc == 'SphinxDial' :
        SphinxEnigma()

# Dialogue('SphinxDial')