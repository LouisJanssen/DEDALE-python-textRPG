# from Map import ZoneMap
from Stats import PlayerStats
from Tools import promptSlow
from Inventory import ObjectInventory
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
        DIAL1: '- Z-Zeus, c\'est bien vous ?',
        DIAL1_1: '- Bien sûr que oui, avorton ! Tu oses questionner ma royale identité ? Décidément, les héros de nos jours, c\'est plus ce que c\'était. Bon, je tenais quand même à te souhaiter bonne chance pour Dédale, tout ça. Sur ce, je dois y aller. Héra va encore me chercher des noises, sinon...',
        DIAL2: '- Zeus, Roi de l\'Olympe, savez-vous quelle est l\'origine de cette folie ?',
        DIAL2_1: '- C\'est moi-même, j\'en ai bien peur. J\'ai accordé à Dédale le statut divin, comme je le fais parfois pour les hommes exceptionnels. J\'étais loin de me douter que la folie consommait déjà le pauvre homme. Tu es notre seule chance de mettre fin cela. Je dois y aller, à présent. Je sais que tu ne me décevras pas.',
        DIALCHA: '- Tiens-donc ! Zeus, le roi des rois, m\'accorde l\'honneur de sa présence. Vous devriez plutôt être à l\'Olympe, non ? Quelqu\'un aurait vite fait de raconter à Héra que vous êtes allé vous amuser ailleurs une fois de plus. J\'ai rencontré beaucoup de dieux pendant mon périple, vous savez. Bien sûr, je suppose qu\'un petit dédommagement pour mon dur travail m\'aiderait à garder ma langue dans ma poche.',
        DIALCHA1: '- Ah non, hein ! J\'en ai assez de ses crises ! Très bien, très bien, le voilà ton dédommagement. Retiens simplement que personne ne se moque de Zeus impunément.',
        DIALSON: '- Père, enfin je vous rencontre. C\'est un honneur.',
        DIALSON1: '- (Il est de moi, celui-là aussi ?!) Ah ! Oui ! Mon enfant ! Je suis si heureux de te rencontrer enfin. Laisse-moi te donner ma bénédiction divine. À présent, tes attaques seront plus puissantes qu\'elles ne l\'ont jamais été. Je souhaite bonne chance aux monstres qui croiseront ton chemin. En revanche, évite celui d\'Héra, si possible. Adieu, mon enfant.',
        GIFT: 'not_defined',
    },
    'PoseidonDial':{
        NPCNAME: 'Poséidon',
        MINSTAT: 15,
        SENTENCE: 'Ça mord bien, aujourd\'hui.',
        DIAL1: '- Qu\'est-ce que vous faites ici, au milieu de l\'océan ?',
        DIAL1_1: '- Je te retourne la question, voyageur. Je profite du beau de temps et du calme marin. Il n\'y a que ça qui parvienne à me détendre réellement.',
        DIAL2: '- Vous êtes Poséidon, n\'est-ce pas ?',
        DIAL2_1: '- Vous êtes perspicace ! Oui, c\'est ainsi que l\'on m\'appelle. Je suis heureux de te croiser. Je te souhaite bien du courage pour ta quête. Dédale était quelqu\'un de bien, autrefois. C\'est fou ce que la jalousie et la rancoeur peuvent faire aux hommes. À présent, si tu le permets, j\'aimerais me concentrer sur ma ligne.',
        DIALCHA: '- J\'ai moi-même pêché d\'énormes poissons. Dans ma région, personne ne m\'arrivait à la cheville, dans ce domaine.',
        DIALCHA1: '- Hahaha, j\'en ai entendu parler, oui. Accepte donc ce modeste présent comme démonstration de mon admiration. Maintenant, chut, tu vas faire fuir le poisson.',
        DIALSON: '- Poséidon... J\'ai du mal à contrôler mon émotion. Je suis si heureux de vous rencontrer, père.',
        DIALSON1: '- Tiens donc ma canne à pêche un instant, mon enfant. Tu sais, la vie, c\'est comme la pêche. Tout est une question de patience. Inspire-toi de la mer à chaque instant. Aborde les épreuves avec calme et, quand le moment sera venu, déchaîne toi. Laisse-moi t\'accorder ma bénédiction avant de reprendre ton voyage. Que la vitalité de l\'océan t\'accompagne.',
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
    StartEnigma = input(' > ')
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
    print('1', NpcDial[npc][DIAL1])
    print('2', NpcDial[npc][DIAL2])
    print('3', NpcDial[npc][DIALCHA], '[ CHA :', minstat, ']')
    if npc == 'ZeusDial' and Player.father == 'Zeus' :
        print('4', NpcDial[npc][DIALSON], '[ Enfant de', NpcDial[npc][NPCNAME], ']')
    elif npc == 'PoseidonDial' and Player.father == 'Poséidon' :
        print('4', NpcDial[npc][DIALSON], '[ Enfant de', NpcDial[npc][NPCNAME], ']')
    elif npc == 'HadesDial' and Player.father == 'Hadès' :
        print('4', NpcDial[npc][DIALSON], '[ Enfant de', NpcDial[npc][NPCNAME], ']')
    print('-------------------------------------')
    DialChoice = input(' > ')
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
        ObjectInventory(NpcDial[npc][GIFT])
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

Player.Cha += 3000
Player.father = 'Poséidon'
# Dialogue('PoseidonDial')