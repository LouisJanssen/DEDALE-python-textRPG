#Import of tools needed
import sys
import time
from Stats import PlayerStats
from Tools import promptSlow
from Dialogue import Dialogue
from Combat import StartCombat
from CursesAndBlessings import Curse,Blessing
from Inventory import displayInventory, passiveObject, ObjectInventory

Player = PlayerStats()

#Creation of the MAP
ZONENAME = 'zonename'
DESCRIPTION = 'description'
NORTH = 'nord'
SOUTH = 'sud'
EAST = 'est'
WEST = 'ouest'
EVENT = 'event'
SPEC = 'spec'

#Library for activation of map tiles
ActiveCase = {'A1': True, 'A2': True, 'A3': True,'A4': True, 'A5': True,
              'B1': True, 'B2': True, 'B3': True,'B4': True, 'B5': True,
              'C1': True, 'C2': True, 'C3': True,'C4': True, 'C5': True,
              'D1': True, 'D2': True, 'D3': True,'D4': True, 'D5': True,
              'E1': True, 'E2': True, 'E3': True,'E4': True, 'E5': True,
              'F1': True, 'F2': True, 'F3': False,'F4': True, 'F5': True
              }

#Library for the map
ZoneMap = {
  'A1': {
    ZONENAME: 'Le refuge de Prométhée',
    DESCRIPTION: 'Votre périple en mer s\'achève enfin, vous continuez donc votre aventure comme vous l\'avez commencé : à pied. Après une longue marche, vous tombez sur une maison d\'apparence commune mais aux dimensions atypiques. L\'endroit semble abandonné depuis des centaines d\'années, des milliers peut-être. Au milieu de cette demeure hors du temps, vous apercevez un foyer dépourvu de toute flamme. En y regardant de plus près, vous y décelez néanmoins un petit coffre dans lequel se trouve une fiole au contenu incandescent...',
    NORTH: '',
    SOUTH: 'B1',
    EAST: 'A2',
    WEST: '',
    EVENT: 'object',
    SPEC: 'fire',
  },
  'B1': {
    ZONENAME: 'Île de l\'œil du cyclone',
    DESCRIPTION: 'Après de longs jours de plus en mer, le ciel commence à se couvrir sérieusement. Soudain, une tempête éclate avant même que vous ayez le temps de vous y préparer. Tout à coup, la foudre frappe le mat de votre navire, qui vous tombe sur la tête vous faisant tomber dans l\'inconscience. Quand Morphée vous libère enfin de son emprise, vous sentez une forte odeur. En observant autour de vous, vous réalisez que vous avez atterri dans ce qui semble être une bergerie à grande échelle avec option vue sur mer. Vous êtes d\'abord soulagé, songeant que les gens qui habitent ici accepteront peut-être de vous aider à réparer votre bateau, quand soudain, une voix gutturale retentit : "Cette odeur... C\'est pas un mouton ça, je reconnais... Mmmhh... Impossible ! PERSONNE ! JE SAIS QUE C\'EST TOI ! TU M\'ÉCHAPPERAS PAS CETTE FOIS !".',
    NORTH: 'A1',
    SOUTH: 'C1',
    EAST: '',
    WEST: '',
    EVENT: 'fight',
    SPEC: 'CyclopStats',
  },
  'C1': {
    ZONENAME: 'Le vieux pêcheur perdu en mer',
    DESCRIPTION: 'Cela va faire une semaine maintenant que vous avez pris la mer. C\'est une journée calme, et l\'absence de vent semble distordre le temps, l\'aboutissement de votre odyssée vous paraît bien loin. La monotonie de votre voyage est troublée alors que votre navire s\'enfonce dans une brume étrange. Au milieu de cette brume, vous décelez une lumière ainsi qu\'une silhouette. Piqué de curiosité, vous allez à sa rencontre. Vous croyez d\'abord halluciner quand vous découvrez un homme en train de pêcher, installé dans une barque, au beau milieu de l\'océan. Une atmosphère paisible règne. De nombreuses secondes passent sans que le vieux pêcheur ne vous adresse la parole. Finissant par perdre patience, vous vous raclez la gorge pour signaler votre présence. Après un léger froncement de sourcil, le vieil homme se tourne vers vous, l\'index collé à ses lèvres souriantes : "Chut ! Vous allez faire fuir le poisson !". Vous êtes alors frappé par le regard du vieillard, d\'un vert strictement semblable à celui de la mer, empreint à la fois de sagesse et de malice.',
    NORTH: 'B1',
    SOUTH: 'D1',
    EAST: 'C2',
    WEST: '',
    EVENT: 'npc',
    SPEC: 'PoseidonDial',
  },
  'D1': {
    ZONENAME: 'Le domaine d\'Artémis',
    DESCRIPTION: 'Vous ressentez un soulagement indescriptible lorsque vous arrivez enfin à la lisière d\'une forêt luxuriante vous offrant l\'abri parfait contre le soleil. Seulement, la chaleur laisse peu à peu place à la faim. D\'une flèche bien tirée, vous transpercez un écureuil bien portant qui passait par là. Alors que vous vous approchez de votre futur repas, vous constatez à quel point la vie semble grouiller dans les environs. Les écureuils du même acabit que votre proie sont nombreux et vous avez même croisé le regard d\'un cerf majestueux à quelques mètres de là.  Vous en profitez pour chasser un autre écureuil afin d\'en faire l\'offrande aux dieux. Soudain, un grouinement féroce se fait entendre dans votre dos. Vous vous retournez aussitôt, prêt au combat, et tombez nez à nez avec un sanglier. Cela n\'aurait pas vraiment posé problème, si celui-ci n\'avait pas fait près de deux fois votre taille.',
    NORTH: 'C1',
    SOUTH: 'E1',
    EAST: 'D2',
    WEST: '',
    EVENT: 'fight',
    SPEC: 'BoarStats',
  },
  'E1': {
    ZONENAME: 'Les yeux revolver',
    DESCRIPTION: 'Enfin, la lumière du jour ! Il faut un temps à vos yeux pour se réhabituer, mais vous réalisez que vous êtes arrivé dans ce qui semble être un temple en l\'honneur d\'Athéna. Celui-ci est décoré par des centaines de statues, dont le réalisme vous impressionne. Celui qui les avait sculptées devait être béni des dieux. En vous enfonçant un peu plus à travers ce champ de pierre, vous vous rendez compte que les scènes représentées possèdent une aura étrange. Les visages des statues reflètent une peur incontrôlable, et beaucoup d\'entre elles sont dirigées vers la direction opposée au temple. Au centre de celui-ci, vous découvrez, posé sur un autel, un bouclier orné d\'un visage monstrueux. Ce visage, celui d\'une gorgone, provoque chez vous un mouvement de recul et une frayeur que vous peinez à surmonter.',
    NORTH: 'D1',
    SOUTH: 'F1',
    EAST: 'E2',
    WEST: '',
    EVENT: 'object',
    SPEC: 'shield',
  },
  'F1': {
    ZONENAME: 'Forges d\'Héphaïstos',
    DESCRIPTION: 'Quelle idée d\'avoir décidé de passer par cette étrange caverne ! Ce ne sont pas les raisons de vous plaindre qui manquent entre cette chaleur étouffante, les cliquetis incessants qui retentissent jusqu\'à se graver dans votre crâne et cette obscurité constante interrompue uniquement par le passage peu rassurant de fines coulées de lave. Vous perdez presque espoir avant d\'enfin apercevoir la lumière du jour, loin devant vous. Soulagé, vous hurlez de joie et vous précipitez dans cette direction. C\'est alors qu\'une masse lourde tombe pile devant vous. À y regarder de plus près, il semblerait qu\'il s\'agisse d\'une boule, faite entièrement de métal... Tout à coup, celle-ci se met à grincer, déployant ses membres jusqu\'à former une araignée vous arrivant facilement à la taille.',
    NORTH: 'E1',
    SOUTH: '',
    EAST: 'F2',
    WEST: '',
    EVENT: 'fight',
    SPEC: 'SpiderStats',
  },
  'A2': {
    ZONENAME: 'Le secret de Thanatos',
    DESCRIPTION: 'Les terres que vous foulez sont de plus en plus mornes et il devient difficile de trouver de quoi vous sustenter. Vous envisagez un instant de tenter d\'attraper l\'un des nombreux corbeaux qui parcourent le ciel gris au-dessus de vous, mais qui sait de quelle funeste maladie Apollon a bien pu les affubler. Durant votre voyage, vous passez par bien des villages, tous rasés par l\'arc du dieu musicien. Vous avez soif. Et faim. Si faim... Vous finissez par perdre conscience au milieu de l\'un de ces villages, comme l\'ont fait les centaines de familles qui avaient du vivre ici autrefois. Lorsque vous rouvrez les yeux, vous vous trouvez au milieu d\'une pièce sombre et très étendue, dépourvue de tout meuble à l\'exception d\'un bureau et d\'une chaise en son centre. Assis à ce bureau, un jeune garçon est penché sur une feuille de papier, compas à la main. Debout à côté de lui se trouve une silhouette ailée, la main posée sur l\'épaule du garçon. Vous décelez ce qui ressemble à de la tristesse dans son regard à première vue sinistre.',
    NORTH: '',
    SOUTH: '',
    EAST: 'A3',
    WEST: 'A1',
    EVENT: 'npc',
    SPEC: 'ThanatosDial',
  },
  'B2': {
    ZONENAME: 'Le treizième travail',
    DESCRIPTION: 'Enfin, vous arrivez dans ce qui semble être en tout point un havre de paix au beau milieu d\'une clairière. Une cascade se déverse dans une source d\'eau douce dont le toucher tempéré vous invite à vous détendre - et à vous décrasser - pour la première fois depuis bien longtemps. Seulement, un cri retentissant vient troubler votre quiétude, faisant fuir toutes les créatures alentour : "TOI ! Je savais bien que je finirais par te trouver ! Papa m\'a donné un boulot, il veut que je fasse de toi un guerrier à ma hauteur. J\'ai bien essayé de lui faire comprendre que c\'était impossible, hein, mais il est du type assez borné... Moi c\'est Héraclès, au fait. Sors de l\'eau, on a du pain sur la planche. Et enfile quelque chose !".',
    NORTH: '',
    SOUTH: '',
    EAST: 'B3',
    WEST: '',
    EVENT: 'blessing',
    SPEC: 'Work',
  },
  'C2': {
    ZONENAME: 'Chant funeste',
    DESCRIPTION: 'Il faut être particulièrement prudent quand on prend la mer, on vous l\'a assez répété quand vous étiez jeune. Vous voguez donc sur les mers, prenant garde à ne pas fracasser votre embarcation sur le premier rocher venu. Vous êtes impressionné par vos talents de navigateur, bien que l\'idée de potentiellement tomber sur Charybde et Scylla vous terrifie. Mais bon, personne n\'est tombé sur ces monstres depuis le grand Ulysse, alors... Vous vous rendez soudain compte que vous avez légèrement dévié de cap. Alors que vous vous apprêtez à rectifier la trajectoire, une douce mélodie parvient à vos oreilles. Si douce que vous avez du mal à vous en détourner... Désormais, trouver la source de ce chant est devenu votre priorité. Malheureusement pour vous, c\'est face à une sorte d\'oiseau à taille humaine et au visage de femme que vous vous retrouvez. Aucun doute, il s\'agit d\'une sirène.',
    NORTH: '',
    SOUTH: 'D2',
    EAST: '',
    WEST: 'C1',
    EVENT: 'fight',
    SPEC: 'SirensStats',
  },
  'D2': {
    ZONENAME: 'Le trésor de Midas',
    DESCRIPTION: 'Cela fait déjà un moment que cette idée vous trotte en tête, mais c\'est désormais une certitude. Le labyrinthe de Dédale semble avoir pioché différents lieux aux quatre coins du monde pour les réunir au même endroit. Aucun doute : cette rivière, dont le sable est fait d\'or, c\'est forcément le Pactole. Sur l\'autre rive, vous voyez un coffre massif, contenant probablement d\'incroyables richesses. Vous parvenez non sans mal à l\'atteindre et constatez la présence d\'une étrange serrure...',
    NORTH: 'C2',
    SOUTH: '',
    EAST: 'D3',
    WEST: 'D1',
    EVENT: 'easter',
    SPEC: '',
  },
  'E2': {
    ZONENAME: 'La fleur au bord de l\'eau',
    DESCRIPTION: 'Après tous ces jours de marche, vous avez désespérément besoin de reprendre des forces. Vous finissez par trouver une petite grotte, dont les parois vous accorderont un formidable abri contre le vent cette nuit. Seulement, chaque bruit que vous faites à l\'intérieur de celle-ci est répété par un écho incessant. Las et sur les nerfs, vous décidez de sortir de la grotte pour récupérer de l\'eau d\'une source située non loin de là. C\'est au bord de celle-ci que vous apercevez une fleur, dont la beauté dépasse tout ce que vous avez pu voir jusque-là. Vous êtes prêt à tout pour qu\'elle vous appartienne. Alors que vous l\'extirpez du sol précautionneusement, l\'écho de la grotte que vous avez quittée répète : "Hélas ! Hélas !".',
    NORTH: '',
    SOUTH: '',
    EAST: '',
    WEST: 'E1',
    EVENT: 'curse',
    SPEC: 'Flower',
  },
  'F2': {
    ZONENAME: 'L\'heure n\'est pas à la fête',
    DESCRIPTION: 'Cette sortie semble déboucher sur une sorte de caverne, ornementée çà et là par des éléments à l\'aspect mécanique et des coulées de lave. Au milieu de cette étrange entrée se trouve une table, un canthare posé en son milieu. L\'odeur de vin s\'échappant du vase orné vous attire inéluctablement et vous pousse à vous installer un instant pour y goûter. Vous portez le canthare à votre bouche, mais quelqu\'un vous le retire des mains avant même que son contenu n\'en frôle vos papilles. "Vous êtes certain de vouloir vous aventurer dans cette direction ? Mon demi-frère peut se montrer grincheux quand on farfouille dans ses affaires... Délicieux, ce vin."',
    NORTH: '',
    SOUTH: '',
    EAST: 'F3',
    WEST: 'F1',
    EVENT: 'npc',
    SPEC: 'DionysosDial',
  },
  'A3': {
    ZONENAME: 'LA DÉTRESSE D\'ASTÉRION',
    DESCRIPTION: 'Vous entendez le cœur du labyrinthe battre la chamade un peu plus vite à chaque pas que vous faites. Vous ressentez toute la colère, la haine, la puissance, mais aussi la tristesse qui plane dans l\'atmosphère. D\'immenses blocs de terre se dressent autour de vous, bloquant toute issue alors qu\'une masse gigantesque s\'extirpe de l\'ombre. Face à vous se tient, hurlant, le Minotaure. Celui-là même que Thésée avait vaincu il y a bien longtemps, de retour du royaume d\'Hadès. Son corps, recouvert partiellement de bronze, semble avoir subi des modifications visant à le rendre plus redoutable qu\'il ne l\'a jamais été. D\'une voix sombre, il s\'adresse à vous : "Approche, héros, cela fait bien trop longtemps que je n\'ai pas tué quiconque."',
    NORTH: '',
    SOUTH: 'B3',
    EAST: 'A4',
    WEST: 'A2',
    EVENT: 'BOSS',
    SPEC: '',
  },
  'B3': {
    ZONENAME: 'Une responsabilité royale',
    DESCRIPTION: 'La fin du chemin approche, vous le sentez. Vous vous sentez fatigué, mais aussi plus fort que jamais. Comme si vous n\'en aviez pas assez bavé comme ça, le ciel commence à se couvrir et la pluie à tomber. Vous vous enfoncez de plus en plus dans le sol boueux, chaque pas étant plus difficile que le précédent. Exténué, vous glissez et tombez face contre terre. À bout de nerf, vous ne pouvez vous empêcher de pester : "Nom de Zeus !". C\'est alors que la foudre tombe juste devant vous, laissant place à une silhouette altière :',
    NORTH: 'A3',
    SOUTH: 'C3',
    EAST: '',
    WEST: 'B2',
    EVENT: 'npc',
    SPEC: 'ZeusDial',
  },
  'C3': {
    ZONENAME: 'Les vestiges de la guerre',
    DESCRIPTION: 'Vous avez marché toute la nuit, avec votre torche comme seule source de lumière. Vous espérez atteindre plus vite votre destination grâce à ce gain de temps, mais la fatigue se fait tout doucement ressentir malgré votre métabolisme héroïque. La lumière du soleil levant vous brûle la rétine. C\'est avec stupeur que vous découvrez le paysage alentour, révélé par l\'aube. Tout ici n\'est que destruction, le paysage est rasé à des milliers de pieds à la ronde, jonché d\'armes et armures rouillées, accompagné parfois par les restes d\'un guerrier malchanceux. Quelque chose vous perturbe dans cet endroit : c\'est comme s\'il appartenait à un autre temps. Ci et là, des bannières rouges et bleues se tiennent encore fièrement malgré les bris du temps. Vous ne tenez pas particulièrement à vous attarder ici. En chemin, une lance magnifique, bien que rendue inutilisable par la rouille, attire votre attention. Plantée dans le sol, un casque pilos trône en son sommet. Aucun doute, Arès aurait aimé cet endroit.',
    NORTH: 'B3',
    SOUTH: 'D3',
    EAST: '',
    WEST: '',
    EVENT: 'easter',
    SPEC: '',
  },
  'D3': {
    ZONENAME: 'Un lien irrésistible',
    DESCRIPTION: 'Les vestiges d\'un temple se trouvent devant vous. Vous entreprenez des les visiter afin de découvrir de quelle divinité ce lieu de culte était il autrefois le sanctuaire. Vous parvenez à reconnaitre des fresques encore très colorés montrant des hommes et des femmes contrôlés par une déesse des plus ravissante. Nul doute c\'était un temple à gloire d\'Aphrodite. En parcourant les débris vous tombez sur un petit coffret et décidez de l\'ouvrir. A l\'intérieur se trouve une ceinture magnifique et l\'essayez sur vous immédiatement. Elle vous va à ravir.',
    NORTH: 'C3',
    SOUTH: 'E3',
    EAST: 'D4',
    WEST: 'D2',
    EVENT: 'object',
    SPEC: 'belt',
  },
  'E3': {
    ZONENAME: 'Le mal-aimé',
    DESCRIPTION: 'C\'est difficile, mais vous parvenez petit à petit à prendre vos marques dans ce labyrinthe infernal. Pris par la fatigue, vous vous laissez glisser au pied d\'un arbre mort, séduit par l\'idée d\'une petite sieste. Vous levez la tête et observez les branches nues de l\'olivier qui vous protège du soleil. Vous vous rendez compte que vous allez vite finir comme lui si vous ne buvez pas rapidement. "Ce serait bête de mourir de soif quand on peut l\'être en étant cruellement déchiqueté par une bête des Enfers..." vous marmonnez-vous à vous-même en portant votre outre à votre bouche jusqu\'à ce qu\'une voix derrière vous vous en fasse recracher tout le contenu : "Allez ! ça va encore être de ma faute ! Le vilain dieu des Enfers a donné des pouvoirs à Dédale pour qu\'il réduise le monde entier à néant ! Bien sûr, j\'ai que ça à faire !". Abasourdi, vous vous retournez pour faire face à un homme aux cheveux de jais et au teint plus pâle que du lait de chèvre.',
    NORTH: 'D3',
    SOUTH: '',
    EAST: 'E4',
    WEST: '',
    EVENT: 'npc',
    SPEC: 'HadesDial',
  },
  'F3': {
    ZONENAME: 'La folie de Dédale',
    DESCRIPTION: '"Héros ! Tu m\'entends ? Hé ho ! Par Athéna, écoute-moi !" Perdu, vous parvenez difficilement à ouvrir les yeux. Vous vous trouvez dans une salle carrée vide, dont trois murs sont ouverts par une brèche. En face de vous, un homme vous fixe d\'un regard inquiet et intelligent : "Ah, tu as repris connaissance, c\'est bien. Doucement, doucement."',
    NORTH: '',
    SOUTH: '',
    EAST: 'F4',
    WEST: 'F2',
    EVENT: 'start',
    SPEC: '',
  },
  'A4': {
    ZONENAME: 'Les sœurs filandières',
    DESCRIPTION: 'Une atmosphère étrangement calme plane sur les lieux et quelque chose vous dit que celui-ci précède certainement la tempête. Sur votre route, vous tombez sur une petite maison. De la lumière s\'échappe des fenêtres et la perspective de passer une nuit dans un foyer chaleureux est un luxe que vous ne pouvez pas vous permettre de refuser. Vous constatez que la porte est déjà ouverte et vous permettez de passer la tête à l\'intérieur. Trois femmes d\'âges très différents détournent alors leur regard de leur tricot pour le poser sur vous. La plus âgée d\'entre elles tient une paire de ciseaux dans sa main parcheminée.',
    NORTH: '',
    SOUTH: '',
    EAST: 'A5',
    WEST: 'A3',
    EVENT: 'npc',
    SPEC: 'MoiresDial',
  },
  'B4': {
    ZONENAME: 'Vignes trompeuses',
    DESCRIPTION: 'Vous arrivez dans un énorme vignoble aux raisins gorgés de soleil s\'étendant à perte de vue. Vous ignorez qui entretient cet endroit et ne voyez aucune demeure dans les environs, mais vous avez cessé de chercher la moindre logique dans ce labyrinthe, de toute manière. Alors que le sommeil commence à se coucher, une musique entraînante attire votre attention, comme un appel à la fête. En vous approchante de sa source, vous découvrez, éberlué, un groupe de satyres, jouant de la flûte de pan et dansant, distribuant du vin à tour de bras. Après un court moment d\'hésitation, vous vous décidez à rejoindre la petite troupe le temps d\'une nuit. Ou peut-être plusieurs...',
    NORTH: '',
    SOUTH: '',
    EAST: 'B5',
    WEST: '',
    EVENT: 'curse',
    SPEC: 'Vines',
  },
  'C4': {
    ZONENAME: 'Juge et Roi',
    DESCRIPTION: 'Le bâtiment qui se dresse devant vous est pour le moins singulier. Haut de plusieurs dizaines de mètres, il ne possède pas la moindre fenêtre, seulement une porte aux barreaux de fer, déjà ouverte. Une fois à l\'intérieur, vous allumez une torche pour tenter d\'y voir quelque chose. Vous mettez un moment à vous rendre compte du spectacle qui a lieu sous vos yeux. Dans un coin du bâtiment, un homme vous surplombe par son imposante taille, même assis. Il ne semble pas avoir remarqué votre présence. Son regard vide et son corps décharnés vous laissent d\'abord penser que la vie a quitté cette enveloppe immense, pourtant un râle constant vous prouve le contraire. Vous vous approchez et tentez d\'attirer son attention : "Bonjour ?". Un léger mouvement de pupille vous laisse penser qu\'il s\'agit d\'une invitation à la discussion.',
    NORTH: '',
    SOUTH: 'D4',
    EAST: 'C5',
    WEST: '',
    EVENT: 'npc',
    SPEC: 'MinosDial',
  },
  'D4': {
    ZONENAME: 'Lernie, l\'hydre vorace',
    DESCRIPTION: 'La brume se lève, l\'air devient plus frais, et une aura menaçante plane sur ce lieu où la végétation ne pousse plus. Vous entendez des cris terrifiant venant d\'une caverne par laquelle vous êtes obligé de passer si vous voulez continuer votre périple. Alors que vous approchez de l\'entrée une tête hideuse sort de la caverne, puis une deuxième et une troisième. Vous en êtes sûr maintenant vous avez affaire à une Hydre.',
    NORTH: 'C4',
    SOUTH: '',
    EAST: 'D5',
    WEST: 'D3',
    EVENT: 'fight',
    SPEC: 'HydraStats',
  },
  'E4': {
    ZONENAME: 'Un labyrinthe des plus particuliers',
    DESCRIPTION: 'D\'immenses colonnes peintes en bleu et jaune se dressent devant vous. En continuant votre route vous entendez du bruit et décidez de vous cacher pour ne pas vous faire repérer et ainsi évaluer au mieux la menace. Passe alors deux hommes proche de vous, et vous arrivez à entendre leur conversation. " Tu as vu les nouveaux Gnedby ? J\'aime beaucoup la couleur mais je t\'avoue que pour la forme les Lerberg sont bien mieux! Vivement les nouveaux arrivages pour le rayon meuble ! " Quel étrange discussion... Mais si c\'était une menace vous l\'avez évitée, quel labyrinthe des plus mystérieux.',
    NORTH: '',
    SOUTH: 'F4',
    EAST: 'E5',
    WEST: 'E3',
    EVENT: 'easter',
    SPEC: '',
  },
  'F4': {
    ZONENAME: 'Un message de dernière minute',
    DESCRIPTION: 'Vous commencez votre route, sans vraiment savoir où vous allez ni ce que vous allez trouver en chemin. Vous marchez presque automatiquement, la tête encore dans le brouillard. Tout à coup, un souffle puissant vous fait presque perdre l\'équilibre. Sorti de nulle part, un homme se tient devant vous. Son accoutrement et son arrivée fulgurante laissent peu de doute quant à son identité. Vous faites face à Hermès, le dieu aux sandales ailées.',
    NORTH: 'E4',
    SOUTH: '',
    EAST: '',
    WEST: 'F3',
    EVENT: 'npc',
    SPEC: 'SphinxDial',
  },
  'A5': {
    ZONENAME: 'Un adversaire surprenant',
    DESCRIPTION: 'Vous arrivez dans un tunnel éclairé par de simples torches accrochées aux murs, et alors que vous le traversez, vous sentez une présence des plus perturbantes. Et c\'est là que vous l\'apercevez. Une créature effroyable vous bloque le chemin. Deux pattes aux serres acérés, un corps démesuré d\'où sortent deux grandes ailes, une tête des plus affreuses vous menaçant d\'un regard féroce et orné d\'une crête écarlate ainsi que d\'un bec des plus terrifiant. Vous voilà face à un redoutable poulet.',
    NORTH: '',
    SOUTH: 'B5',
    EAST: '',
    WEST: 'A4',
    EVENT: 'fight',
    SPEC: 'ChickenStats',
  },
  'B5': {
    ZONENAME: 'De zéro à héros',
    DESCRIPTION: 'Alors que vous continuez votre route vous vous retrouvez face à un énorme autel d\'où trône une massue, encastrée dans celui-ci. L\'autel est orné de plusieurs fresques démontrant le courage d\'un héros oublié. Vous arrivez à en compter 12 en tout. Après avoir gravit les quelques marches menant au haut de l\'autel vous y récupérer l\'arme avec énormément de difficulté car celle ci était encastré dans la pierre de l\'altar. En la tenant dans vos mais vous ressentez toute la force de son ancien propriétaire.',
    NORTH: 'A5',
    SOUTH: 'C5',
    EAST: '',
    WEST: 'B4',
    EVENT: 'object',
    SPEC: 'club',
  },
  'C5': {
    ZONENAME: 'Un adversaire de taille',
    DESCRIPTION: 'Quel spectacle d\'horreur. Le sol devant vous est jonché d\'ossements. En examinant de plus près vous confirmez la présence d\'ossements humains et non animaux. Puis le sol se mit à trembler. Une ombre gigantesque s\'avance vers vous. Ni une ni deux vous vous préparez au combat et c\'est là que vous l\'apercevez. Il ressemble à un homme mais ce n\'en est pas. Il est beaucoup trop grand, beaucoup trop massif pour être un simple homme. Non ce ne peut être qu\'un Lestrygon, une abomination anthropophage. Et celui là n\'a l\'air de souhaiter qu\'une chose: vous dévorer.',
    NORTH: 'B5',
    SOUTH: '',
    EAST: '',
    WEST: 'C4',
    EVENT: 'fight',
    SPEC: 'LestrygonStats',
  },
  'D5': {
    ZONENAME: 'La boisson des dieux',
    DESCRIPTION: 'En continuant sur la route vous croisez les restes d\'un voyageur égaré. Le pauvre avait dû se faire attaquer par une quelconque créature et son combat résultat d\'un dessein funeste. Cependant bien qu\'il ne lui reste presque plus de chair sur les os, il peut peut être y avoir quelques objets qui pourrait vous être utile pour votre voyage. En cherchant dans les affaires du mort, vous y trouver une boite avec une flacon contenant un liquide doré. Une petite étiquette pendouille accrochée au bouchon indiquant : " Ambroisie ! La boisson des dieux qui vous revigorera immédiatement ! " ainsi que diverses mentions légales au dos de l\'étiquette sur une possibles présence d\'effets secondaires sur les mortels.',
    NORTH: '',
    SOUTH: 'E5',
    EAST: '',
    WEST: 'D4',
    EVENT: 'object',
    SPEC: 'ambrosia',
  },
  'E5': {
    ZONENAME: 'Beaucoup trop de pattes à mon goût',
    DESCRIPTION: 'La nuit tombe mais vous décidez de continuer votre chemin pour aller le plus loin possible et trouver un abri pour passer la nuit sereinement. Enfin vous trouvez une petite cave toute en pierre à même la paroi d\'un des murs du labyrinthe. Vous y serez au chaud ! Mais alors que vous commencez à vous installer vous entendez des petits cliquetis sur la roche non loin de vous. Vous levez votre torche pour éclairer et vous la voyez. Toutes ces pattes... vous voilà face à une araignée d\'Héphaïstos.',
    NORTH: 'D5',
    SOUTH: 'F5',
    EAST: '',
    WEST: 'E4',
    EVENT: 'fight',
    SPEC: 'SpiderStats',
  },
  'F5': {
    ZONENAME: 'Une trempette vivifiante',
    DESCRIPTION: 'C\'est avec un grand soulagement que vous trouvez un fleuve, dont la fraîcheur est plus que bienvenue. Seulement, en vous approchant, vous réalisez que c\'est plutôt une profonde froideur qui en ressort. Stupéfié, vous constatez la présence d\'une femme, en train d\'y tremper son enfant, peut-être pour faire sa toilette. Soudain, vous vous rendez compte de la scène à laquelle vous assistez. Ulysse vous avait prévenu, dans le labyrinthe, l\'espace et le temps sont distordus. Cette femme et son enfant, ce sont Thétis et son fils, Achille, le héros légendaire de la Guerre de Troie. Une idée vous traverse alors l\'esprit. Une idée risquée, certes, mais payante. Prenant garde de vous accrocher à un rocher pour ne pas vous faire emporter, vous vous baignez dans le Styx.',
    NORTH: 'E5',
    SOUTH: '',
    EAST: '',
    WEST: '',
    EVENT: 'blessing',
    SPEC: 'Styx',
  },
}

#display the location of the player
def PrintLocation():
  if(ActiveCase[Player.pos] == True):
    promptSlow(ZoneMap[Player.pos][ZONENAME].upper())
    promptSlow(ZoneMap[Player.pos][DESCRIPTION])
  else:
    promptSlow('Vous êtes déjà passé par ici, il ne reste plus rien d\'intéressant')
  

#main display with actions of the player
def prompt():
  if (ZoneMap[Player.pos][EVENT] == 'fight' and ActiveCase[Player.pos] == True):
    testlecombat()
  elif (ZoneMap[Player.pos][EVENT] == 'npc' and ActiveCase[Player.pos] == True):
    testnpc()
  elif (ZoneMap[Player.pos][EVENT] == 'object' and ActiveCase[Player.pos] == True):
    testobject()
  elif (ZoneMap[Player.pos][EVENT] == 'curse' and ActiveCase[Player.pos] == True):
    testcurse()
  elif (ZoneMap[Player.pos][EVENT] == 'blessing' and ActiveCase[Player.pos] == True):
    testblessing()
  elif (ZoneMap[Player.pos][EVENT] == 'easter' and ActiveCase[Player.pos] == True):
    testeaster()
  else:
    promptSlow('Que souhaitez vous faire ?')
    action = input('\n > ')
    if action.lower() == 'quitter':
      sys.exit()
    elif action.lower() == 'voyager':
      PlayerMove(action.lower())
    elif action.lower() == 'aide':
      promptSlow('Liste des commandes: ')
      promptSlow('voyager        -       vous permets de vous déplacer')
      promptSlow('inventaire     -       vous permets d\'accéder à votre inventaire')
      promptSlow('stats     -       vous permets d\'accéder à vos stats')
      # promptSlow('carte          -       vous permets d\'accéder à votre carte')
      promptSlow('aide           -       vous permet d\'avoir une liste des commandes')
      promptSlow('quitter        -       vous permet de quitter le jeu')
    elif action.lower() == 'inventaire':
      displayInventory()
    elif action.lower() == 'stats':
      displayStats()
    else:
      print("Commande invalide, essayez 'aide' pour avoir la liste des commandes.\n")

#function for the movement of the player
def PlayerMove(MyAction):
  ask = "Où souhaitez-vous aller ?"
  dest = input(ask + '\n > ')

  if dest == 'est':
    if ZoneMap[Player.pos][EAST] == '':
      promptSlow('Impossible d\'aller dans cette direction, un mur vous bloque la route.')
      PlayerMove(MyAction)
    elif (ZoneMap[ZoneMap[Player.pos][EAST]][EVENT] == 'BOSS'):
      promptSlow('Vous êtes face au combat ultime, vous ne pourrez plus revenir en arrière, êtes vous sûr de vouloir continuer ?')
      print('Oui / Non')
      ask = input('>' ).lower()
      if (ask == 'oui'):
        destination = ZoneMap[Player.pos][EAST]
        MovementHandler(destination)
      elif (ask == 'non'):
        ActiveCase[Player.pos] = True
        prompt()
    else :
      destination = ZoneMap[Player.pos][EAST]
      MovementHandler(destination)

  elif dest == 'nord':
    if ZoneMap[Player.pos][NORTH] == '':
      promptSlow('Impossible d\'aller dans cette direction, un mur vous bloque la route.')
      PlayerMove(MyAction)
    elif (ZoneMap[ZoneMap[Player.pos][NORTH]][EVENT] == 'BOSS'):
      promptSlow('Vous êtes face au combat ultime, vous ne pourrez plus revenir en arrière, êtes vous sûr de vouloir continuer ?')
      print('Oui / Non')
      ask = input('>' ).lower()
      if (ask == 'oui'):
        destination = ZoneMap[Player.pos][NORTH]
        MovementHandler(destination)
      elif (ask == 'non'):
        ActiveCase[Player.pos] = True
        prompt()
    else :
      destination = ZoneMap[Player.pos][NORTH]
      MovementHandler(destination)

  elif dest == 'sud':
    if ZoneMap[Player.pos][SOUTH] == '':
      promptSlow('Impossible d\'aller dans cette direction, un mur vous bloque la route.')
      PlayerMove(MyAction)
    elif (ZoneMap[ZoneMap[Player.pos][SOUTH]][EVENT] == 'BOSS'):
      promptSlow('Vous êtes face au combat ultime, vous ne pourrez plus revenir en arrière, êtes vous sûr de vouloir continuer ?')
      print('Oui / Non')
      ask = input('>' ).lower()
      if (ask == 'oui'):
        destination = ZoneMap[Player.pos][SOUTH]
        MovementHandler(destination)
      elif (ask == 'non'):
        ActiveCase[Player.pos] = True
        prompt()
    else :
      destination = ZoneMap[Player.pos][SOUTH]
      MovementHandler(destination)

  elif dest == 'ouest':
    if ZoneMap[Player.pos][WEST] == '':
      promptSlow('Impossible d\'aller dans cette direction, un mur vous bloque la route.')
      PlayerMove(MyAction)
    elif (ZoneMap[ZoneMap[Player.pos][WEST]][EVENT] == 'BOSS'):
      promptSlow('Vous êtes face au combat ultime, vous ne pourrez plus revenir en arrière, êtes vous sûr de vouloir continuer ?')
      print('Oui / Non')
      ask = input('>' ).lower()
      if (ask == 'oui'):
        destination = ZoneMap[Player.pos][WEST]
        MovementHandler(destination)
      elif (ask == 'non'):
        ActiveCase[Player.pos] = True
        prompt()
    else :
      destination = ZoneMap[Player.pos][WEST]
      MovementHandler(destination)
  else :
    print("Commande invalide, essayez avec nord, sud, est ou ouest.\n")
    PlayerMove(MyAction)

#Movement of the player
def MovementHandler(destination):
  Player.pos = destination
  PrintLocation()

def displayStats():
  print("Joueur : " + Player.name + " fils de " + Player.father)
  print("Niveau : " + str(Player.lvl) + " Expérience : " + str(Player.xp))
  print("HP : " + str(Player.Hp) + " | CHA : " + str(Player.Cha) + " |  ATK : " + str(Player.Atk))
  print("")

#Main game loop function
def main_game_loop():
  while Player.dead is False:
    passiveObject()
    prompt()

########## ZONE DE TESTS ##########
#test 001
def testlecombat():
  StartCombat(ZoneMap[Player.pos][SPEC])
  ActiveCase[Player.pos] = False
  time.sleep(0.5)
  prompt()

def testeaster():
  print('easter')
  ActiveCase[Player.pos] = False
  time.sleep(0.5)
  prompt()

def testblessing():
  Blessing(ZoneMap[Player.pos][SPEC])
  ActiveCase[Player.pos] = False
  time.sleep(0.5)
  prompt()

def testcurse():
  Curse(ZoneMap[Player.pos][SPEC])
  ActiveCase[Player.pos] = False
  time.sleep(0.5)
  prompt()

def testobject():
  ObjectInventory(ZoneMap[Player.pos][SPEC])
  ActiveCase[Player.pos] = False
  time.sleep(0.5)
  prompt()

def testnpc():
  Dialogue(ZoneMap[Player.pos][SPEC])
  ActiveCase[Player.pos] = False
  time.sleep(0.5)
  prompt()

# main_game_loop()

