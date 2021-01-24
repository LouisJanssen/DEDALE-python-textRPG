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
        SENTENCE: 'Alors, qu\'est-ce que le grand méchant Hadès a encore fait de mal ?',
        DIAL1: '- N-n-non-non ! Pitié ne me faites pas de mal !',
        DIAL1_1: '- Eh bah dis-donc... Attends une seconde, me dis pas que c\'est toi le héros qui est censé résoudre tout ce merdier ? On est pas sortis de l\'auberge. Bon, j\'me tire, j\'vais encore avoir du boulot, moi.',
        DIAL2: '- Savez-vous qui est réellement à l\'origine de tout cela, seigneur Hadès ?',
        DIAL2_1: '- Ben oui, c\'est un secret pour personne, à l\'Olympe. J\'avais pourtant bien dit à mon crétin de frère que c\'était pas une bonne idée. J\'ai toujours dit que Dédale était complètement taré.',
        DIALCHA: '- Seigneur Hadès, sans mentir, si votre ramage se rapporte à votre plumage, Vous êtes le phénix des hôtes de ce labyrinthe.',
        DIALCHA1: '- C\'est ça, fous toi de ma gueule. Qu\'est-ce que tu veux ? J\'ai l`habitude, avec vous, les héros. Tiens, prends ça et lâche moi la grappe.',
        DIALSON: '- Il a fait un gosse avec une mortelle y\'a quelques années. Bonjour, père.',
        DIALSON1: '- Alors ça ! Je te châtierais bien pour ton insolence, mais je dois bien avouer que tu tiens ça de ton père. T\'as bien raison, te laisse pas faire. Si on se bat pas, on se fait marcher dessus. Surtout les gens comme nous. Enfin, "les gens", les dieux, pour ma part. Approche, fiston, laisse moi te donner ma bénédiction divine. Sois polyvalent, apprends à attaquer mais aussi à te défendre, ça pourrait bien te permettre de ne pas avoir à me rendre visite avant un moment. Je dois y aller, à présent. J\'ai beucoup de boulot, en ce moment !',
        GIFT: 'not_defined',
    },
    'ThanatosDial':{
        NPCNAME: 'Thanatos et Talos',
        MINSTAT: 15,
        SENTENCE: 'Tu ne devrais pas être là. Il est bien trop tôt pour que nous ne nous rencontrions. (Thanatos)',
        DIAL1: '- Excusez-moi, mais je n\'ai aucune idée de comment je suis arrivé là. Je veux bien m\'en aller, si vous me montrez la sortie. (Parler à Thanatos)',
        DIAL1_1: '- Ha ! Les humains regorgent de stratégies pour tenter de m\'échapper, mais toi, tu n\'as pas la moindre idée de ce qui t\'es arrivé. Je suis Thanatos, dieu de la mort. Rassure-toi, je vais te renvoyer de là d\'où tu viens, nous nous retrouverons tôt ou tard, de toute façon. Pour l\'heure, tu as une mission à terminer.',
        DIAL2: '- Dis-moi, jeune garçon, peux-tu me dire où on se trouve, s\'il te plaît ? (Parler à Talos)',
        DIAL2_1: '- Je sais pas trop, mais Monsieur Thanatos a été très gentil avec moi. Dites-moi, quand vous retournerez là-bas, vous pourrez dire à tonton Dédale que je sais que c\'était un accident ?',
        DIALCHA: '- Vous savez forcément ce qui a poussé Dédale à faire tout ça, j\'ai vraiment besoin qu\'on me donne des explications. Je commence à fatiguer d\'être dans le flou et de combattre sans arrêt malgré tout. (Parler à Thanatos)',
        DIALCHA1: '- Tu as raison, mortel. Comme tu le sais peut-être déjà, les dieux ont décidé d\'accorder le statut divin à Dédale, en guise de démonstration d\'admiration de la part de Zeus. Seulement, cela faisait déjà bien longtemps que Dédale avait commencé à sombrer dans la folie. Trop de démons le hantaient : Minos, Thésée, Arianne, Astérion... Talos...',
        GIFT: 'not_defined',
    },
    'DionysosDial':{
        NPCNAME: 'Dionysos',
        MINSTAT: 15,
        SENTENCE: 'C\'est quand-même meilleur que du jus de raisin !',
        DIAL1: '- Dionysos ? C\'est vous ?',
        DIAL1_1: '- Eh oui, petit ! On dirait que tu n\'as jamais vu de dieu de ta vie, héros ! Non... Me dis pas que je suis ta première fois ? Enfin, euh, on se comprend, hein. Très bien, sur ce, je dois y aller. J\'ai un groupe de satyres enivrés à retrouver. N\'oublie pas ce que je t\'ai dit concernant mon demi-frère. C\'est le roi des pièges.',
        DIAL2: '- Hé ! J\'allais juste goûter au vin, soyez sympa !',
        DIAL2_1: '- Haha, tu as bon goût, je dois dire. Tiens, attrape, je dois y retourner, de toute façon. J\'ai un groupe de satyres enivrés à retrouver.',
        DIALCHA: '- Seigneur Dionysos ! Je suis votre plus grand fan !',
        DIALCHA1: '- Oh ! J\'en connais un qui a le sens de la fête ! Malheureusement, la situation ne s\'y prête pas vraiment. Tiens, attrape ça, on fera la fête la prochaine fois qu\'on se voit. Pour l\'heure, j\'ai un groupe de satyres enivrés à retrouver.',
        GIFT: 'not_defined',
    },
    'MoiresDial':{
        NPCNAME: 'Les Moires',
        MINSTAT: 15,
        SENTENCE: 'Nous avons un visiteur, on dirait.',
        DIAL1: '- Que faites-vous ? (Parler à la plus jeune)',
        DIAL1_1: '- Je tisse, ne voyez-vous pas ?',
        DIAL2: '- Que faites-vous ? (Parler à la femme adulte)',
        DIAL2_1: '- Je déroule, ne voyez-vous pas ?',
        DIALCHA: '- Que faites-vous ?',
        DIALCHA1: '- Je coupe, ne voyez-vous pas ? Prenez ceci, cela m\'évitera peut-être de m\'occuper de votre fil trop tôt.',
        GIFT: 'not_defined',
    },
    'MinosDial':{
        NPCNAME: 'Minos',
        MINSTAT: 15,
        SENTENCE: '...',
        DIAL1: '- Je peux vous aider ?',
        DIAL1_1: '- ...',
        DIAL2: '- Qu\'est-ce qui vous est arrivé ?',
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
    print('2 - Très peu pour moi, merci.')
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
Dialogue('PoseidonDial')