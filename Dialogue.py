# from Map import ZoneMap
from Stats import PlayerStats
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
        DIAL1: '1 - Z-Zeus, c\'est bien vous ?,
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

SonOfZeus = False
SonOfPoseidon = False
SonOfHades = False

def Dialogue(npc):
    minstat = NpcDial[npc][MINSTAT]
    print(')(=================================================)(')
    print(NpcDial[npc][NPCNAME], ':')
    print(NpcDial[npc][SENTENCE])
    print('-------------------------------------')
    print(NpcDial[npc][DIAL1])
    print(NpcDial[npc][DIAL2])
    print(NpcDial[npc][DIALCHA], '[ CHA :', minstat, ']')
    if npc == 'ZeusDial' and SonOfZeus == True :
        print(NpcDial[npc][DIALSON], '[ Enfant de', NpcDial[npc][NPCNAME], ']')
    elif npc == 'PoseidonDial' and SonOfPoseidon == True :
        print(NpcDial[npc][DIALSON], '[ Enfant de', NpcDial[npc][NPCNAME], ']')
    elif npc == 'HadesDial' and SonOfHades == True :
        print(NpcDial[npc][DIALSON], '[ Enfant de', NpcDial[npc][NPCNAME], ']')
    print('-------------------------------------')
    DialChoice = int(input())
    print(')(=================================================)(')
    if DialChoice == 1 :
        promptSlow(NpcDial[npc][DIAL1])
        promptSlow(NpcDial[npc][DIAL1_1])
    elif DialChoice == 2 :
        promptSlow(NpcDial[npc][DIAL2])
        promptSlow(NpcDial[npc][DIAL2_1])
    elif (DialChoice == 3) and (Player.Cha >= minstat) :
        promptSlow(NpcDial[npc][DIALCHA])
        promptSlow(NpcDial[npc][DIALCHA1])
    elif (DialChoice == 3) and (Player.Cha < minstat) :
        promptSlow('Vous n\'avez pas le charisme nécessaire. Choisissez une autre option.')
        Dialogue(npc)
    elif (DialChoice == 4) and (npc == 'ZeusDial') and (SonOfZeus == True) :
        promptSlow(NpcDial[npc][DIALSON])
        promptSlow(NpcDial[npc][DIALSON1])
    elif (DialChoice == 4) and (npc == 'PoseidonDial') and (SonOfPoseidon == True) :
        promptSlow(NpcDial[npc][DIALSON])
        promptSlow(NpcDial[npc][DIALSON1])
    elif (DialChoice == 4) and (npc == 'HadesDial') and (SonOfHades == True) :
        promptSlow(NpcDial[npc][DIALSON])
        promptSlow(NpcDial[npc][DIALSON1])
    else :
        print('ERREUR : Veuillez entrer le chiffre correspondant au dialogue voulu.')
        Dialogue(npc)

# Dialogue('ZeusDial')