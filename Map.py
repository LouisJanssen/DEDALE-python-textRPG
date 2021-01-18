#Import of tools needed
import sys
import time
from Stats import PlayerStats

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
              'F1': True, 'F2': True, 'F3': True,'F4': True, 'F5': True
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
    SPEC: '',
  },
  'C1': {
    ZONENAME: 'Le vieux pêcheur perdu en mer',
    DESCRIPTION: 'Cela va faire une semaine maintenant que vous avez pris la mer. C\'est une journée calme, et l\'absence de vent semble distordre le temps, l\'aboutissement de votre odyssée vous paraît bien loin. La monotonie de votre voyage est troublée alors que votre navire s\'enfonce dans une brume étrange. Au milieu de cette brume, vous décelez une lumière ainsi qu\'une silhouette. Piqué de curiosité, vous allez à sa rencontre. Vous croyez d\'abord halluciner quand vous découvrez un homme en train de pêcher, installé dans une barque, au beau milieu de l\'océan. Une atmosphère paisible règne. De nombreuses secondes passent sans que le vieux pêcheur ne vous adresse la parole. Finissant par perdre patience, vous vous raclez la gorge pour signaler votre présence. Après un léger froncement de sourcil, le vieil homme se tourne vers vous, l\'index collé à ses lèvres souriantes : "Chut ! Vous allez faire fuir le poisson !". Vous êtes alors frappé par le regard du vieillard, d\'un vert strictement semblable à celui de la mer, empreint à la fois de sagesse et de malice.',
    NORTH: 'B1',
    SOUTH: 'D1',
    EAST: 'C2',
    WEST: '',
    EVENT: 'npc',
    SPEC: '',
  },
  'D1': {
    ZONENAME: 'Le domaine d\'Artémis',
    DESCRIPTION: 'Vous ressentez un soulagement indescriptible lorsque vous arrivez enfin à la lisière d\'une forêt luxuriante vous offrant l\'abri parfait contre le soleil. Seulement, la chaleur laisse peu à peu place à la faim. D\'une flèche bien tirée, vous transpercez un écureuil bien portant qui passait par là. Alors que vous vous approchez de votre futur repas, vous constatez à quel point la vie semble grouiller dans les environs. Les écureuils du même acabit que votre proie sont nombreux et vous avez même croisé le regard d\'un cerf majestueux à quelques mètres de là.  Vous en profitez pour chasser un autre écureuil afin d\'en faire l\'offrande aux dieux. Soudain, un grouinement féroce se fait entendre dans votre dos. Vous vous retournez aussitôt, prêt au combat, et tombez nez à nez avec un sanglier. Cela n\'aurait pas vraiment posé problème, si celui-ci n\'avait pas fait près de deux fois votre taille.',
    NORTH: 'C1',
    SOUTH: 'E1',
    EAST: 'D2',
    WEST: '',
    EVENT: 'fight',
    SPEC: '',
  },
  'E1': {
    ZONENAME: 'Les yeux revolver',
    DESCRIPTION: 'Enfin, la lumière du jour ! Il faut un temps à vos yeux pour se réhabituer, mais vous réalisez que vous êtes arrivé dans ce qui semble être un temple en l\'honneur d\'Athéna. Celui-ci est décoré par des centaines de statues, dont le réalisme vous impressionne. Celui qui les avait sculptées devait être béni des dieux. En vous enfonçant un peu plus à travers ce champ de pierre, vous vous rendez compte que les scènes représentées possèdent une aura étrange. Les visages des statues reflètent une peur incontrôlable, et beaucoup d\'entre elles sont dirigées vers la direction opposée au temple. Au centre de celui-ci, vous découvrez, posé sur un autel, un bouclier orné d\'un visage monstrueux. Ce visage, celui d\'une gorgone, provoque chez vous un mouvement de recul et une frayeur que vous peinez à surmonter.',
    NORTH: 'D1',
    SOUTH: 'F1',
    EAST: 'E2',
    WEST: '',
    EVENT: 'object',
    SPEC: '',
  },
  'F1': {
    ZONENAME: 'Forges d\'Héphaïstos',
    DESCRIPTION: 'Quelle idée d\'avoir décidé de passer par cette étrange caverne ! Ce n\'est pas les raisons de vous plaindre qui manquent entre cette chaleur étouffante, les cliquetis incessant qui retentissent jusqu\'à se graver dans votre crâne et cette obscurité constante interrompue uniquement par le passage peu rassurant de fines coulées de lave. Vous perdez presque espoir avant d\'enfin apercevoir la lumière du jour, loin devant vous. Soulagé, vous hurlez de joie et vous précipitez dans cette direction. C\'est alors qu\'une masse lourde tombe pile devant vous. À y regarder de plus près, il semblerait qu\'il s\'agisse d\'une boule, faite entièrement de métal... Tout à coup, celle-ci se met à grincer, déployant ses membres jusqu\'à former une araignée vous arrivant facilement à la taille.',
    NORTH: 'E1',
    SOUTH: '',
    EAST: 'F2',
    WEST: '',
    EVENT: 'fight',
    SPEC: '',
  },
  'A2': {
    ZONENAME: 'Le secret de Thanatos',
    DESCRIPTION: 'Les terres que vous foulez sont de plus en plus mornes et il devient difficile de trouver de quoi vous sustenter. Vous envisagez un instant de tenter d\'attraper l\'un des nombreux corbeaux qui parcourent le ciel gris au-dessus de vous, mais qui sait de quelle funeste maladie Apollon a bien pu les affubler. Durant votre voyage, vous passez par bien des villages, tous rasés par l\'arc du dieu musicien. Vous avez soif. Et faim. Si faim... Vous finissez par perdre conscience au milieu de l\'un de ces villages, comme l\'ont fait les centaines de famille qui avaient du vivre ici autrefois. Lorsque vous rouvrez les yeux, vous vous trouvez au milieu d\'une pièce sombre et très étendue, dépourvue de tout meuble à l\'exception d\'un bureau et d\'une chaise en son centre. Assis à ce bureau, un jeune garçon est penché sur une feuille de papier, compas à la main. Debout à côté de lui se trouve une silhouette ailée, la main posée sur l\'épaule du garçon. Vous décelez ce qui ressemble à de la tristesse dans son regard à première vue sinistre.',
    NORTH: '',
    SOUTH: '',
    EAST: 'A3',
    WEST: 'A1',
    EVENT: 'npc',
    SPEC: '',
  },
  'B2': {
    ZONENAME: 'Le treizième travail',
    DESCRIPTION: 'Enfin, vous arrivez dans ce qui semble être en tout point un havre de paix au beau milieu d\'une clairière. Une cascade se déverse dans une source d\'eau douce dont le toucher tempéré vous invite à vous détendre - et à vous décrasser - pour la première fois depuis bien longtemps. Seulement, un cri retentissant vient troubler votre quiétude, faisant fuir toutes les créatures alentour : "TOI ! Je savais bien que je finirais par te trouver ! Papa m\'a donné un boulot, il veut que je fasse de toi un guerrier à ma hauteur. J\'ai bien essayé de lui faire comprendre que c\'était impossible, hein, mais il est du type assez borné... Moi c\'est Héraclès, au fait. Sors de l\'eau, on a du pain sur la planche. Et enfile quelque-chose !".',
    NORTH: '',
    SOUTH: '',
    EAST: 'B3',
    WEST: '',
    EVENT: 'blessing',
    SPEC: '',
  },
  'C2': {
    ZONENAME: 'Chant funeste',
    DESCRIPTION: 'Il faut être particulièrement prudent quand on prend la mer, on vous l\'a assez répété quand vous étiez jeune. Vous voguez donc sur les mers, prenant garde à ne pas fracasser votre embarcation sur le premier rocher venu. Vous êtes impressionné par vos talents de navigateur, bien que l\'idée de potentiellement tomber sur Charybde et Scylla vous terrifie. Mais bon, personne n\'est tombé sur ces monstres depuis le grand Ulysse, alors... Vous vous rendez soudain compte que vous avez légèrement dévié de cap. Alors que vous vous apprêtez à rectifier la trajectoire, une douce mélodie parvient à vos oreilles. Si douce que vous avez du mal à vous en détourner... Désormais, trouver la source de ce chant est devenu votre priorité. Malheureusement pour vous, c\'est face à une sorte d\'oiseau à taille humaine et au visage de femme que vous vous retrouvez. Aucun doute, il s\'agit d\'une sirène.',
    NORTH: '',
    SOUTH: 'D2',
    EAST: '',
    WEST: 'C1',
    EVENT: 'fight',
    SPEC: '',
  },
  'D2': {
    ZONENAME: '',
    DESCRIPTION: '',
    NORTH: 'C2',
    SOUTH: '',
    EAST: 'D3',
    WEST: 'D1',
    EVENT: 'easter',
    SPEC: '',
  },
  'E2': {
    ZONENAME: '',
    DESCRIPTION: '',
    NORTH: '',
    SOUTH: '',
    EAST: '',
    WEST: 'E1',
    EVENT: 'curse',
    SPEC: '',
  },
  'F2': {
    ZONENAME: '',
    DESCRIPTION: '',
    NORTH: '',
    SOUTH: '',
    EAST: 'F3',
    WEST: 'F1',
    EVENT: 'npc',
    SPEC: '',
  },
  'A3': {
    ZONENAME: '',
    DESCRIPTION: '',
    NORTH: '',
    SOUTH: 'B3',
    EAST: 'A4',
    WEST: 'A2',
    EVENT: 'BOSS',
    SPEC: '',
  },
  'B3': {
    ZONENAME: '',
    DESCRIPTION: '',
    NORTH: 'A3',
    SOUTH: 'C3',
    EAST: '',
    WEST: 'B2',
    EVENT: 'npc',
    SPEC: '',
  },
  'C3': {
    ZONENAME: '',
    DESCRIPTION: '',
    NORTH: 'B3',
    SOUTH: 'D3',
    EAST: '',
    WEST: '',
    EVENT: 'easter',
    SPEC: '',
  },
  #### FRANCIS PART ^^^^^^^^^^^^
  'D3': {
    ZONENAME: '',
    DESCRIPTION: '',
    NORTH: 'C3',
    SOUTH: 'E3',
    EAST: 'D4',
    WEST: 'D2',
    EVENT: 'object',
    SPEC: '',
  },
  'E3': {
    ZONENAME: '',
    DESCRIPTION: '',
    NORTH: 'D3',
    SOUTH: '',
    EAST: 'E4',
    WEST: '',
    EVENT: 'npc',
    SPEC: '',
  },
  'F3': {
    ZONENAME: '',
    DESCRIPTION: '',
    NORTH: '',
    SOUTH: '',
    EAST: 'F4',
    WEST: 'F2',
    EVENT: 'start',
    SPEC: '',
  },
  'A4': {
    ZONENAME: '',
    DESCRIPTION: '',
    NORTH: '',
    SOUTH: '',
    EAST: 'A5',
    WEST: 'A3',
    EVENT: 'npc',
    SPEC: '',
  },
  'B4': {
    ZONENAME: '',
    DESCRIPTION: '',
    NORTH: '',
    SOUTH: '',
    EAST: 'B5',
    WEST: '',
    EVENT: 'curse',
    SPEC: '',
  },
  'C4': {
    ZONENAME: '',
    DESCRIPTION: '',
    NORTH: '',
    SOUTH: 'D4',
    EAST: 'C5',
    WEST: '',
    EVENT: 'npc',
    SPEC: '',
  },
  'D4': {
    ZONENAME: '',
    DESCRIPTION: '',
    NORTH: 'C4',
    SOUTH: '',
    EAST: 'D5',
    WEST: 'D3',
    EVENT: 'fight',
    SPEC: '',
  },
  'E4': {
    ZONENAME: '',
    DESCRIPTION: '',
    NORTH: '',
    SOUTH: 'F4',
    EAST: 'E5',
    WEST: 'E3',
    EVENT: 'easter',
    SPEC: '',
  },
  'F4': {
    ZONENAME: '',
    DESCRIPTION: '',
    NORTH: 'E4',
    SOUTH: '',
    EAST: '',
    WEST: 'F3',
    EVENT: 'npc',
    SPEC: '',
  },
  'A5': {
    ZONENAME: '',
    DESCRIPTION: '',
    NORTH: '',
    SOUTH: 'B5',
    EAST: '',
    WEST: 'A4',
    EVENT: 'fight',
    SPEC: '',
  },
  'B5': {
    ZONENAME: '',
    DESCRIPTION: '',
    NORTH: 'A5',
    SOUTH: 'C5',
    EAST: '',
    WEST: 'B4',
    EVENT: 'object',
    SPEC: '',
  },
  'C5': {
    ZONENAME: '',
    DESCRIPTION: '',
    NORTH: 'B5',
    SOUTH: '',
    EAST: '',
    WEST: 'C4',
    EVENT: 'fight',
    SPEC: '',
  },
  'D5': {
    ZONENAME: '',
    DESCRIPTION: '',
    NORTH: '',
    SOUTH: 'E5',
    EAST: '',
    WEST: 'D4',
    EVENT: 'object',
    SPEC: '',
  },
  'E5': {
    ZONENAME: '',
    DESCRIPTION: '',
    NORTH: 'D5',
    SOUTH: 'F5',
    EAST: '',
    WEST: 'E4',
    EVENT: 'fight',
    SPEC: '',
  },
  'F5': {
    ZONENAME: '',
    DESCRIPTION: '',
    NORTH: 'E5',
    SOUTH: '',
    EAST: '',
    WEST: '',
    EVENT: 'blessing',
    SPEC: '',
  },
}

#display the location of the player
def PrintLocation():
  if(ActiveCase[Player.pos] == True):
    print(ZoneMap[Player.pos][ZONENAME].upper())
    print(ZoneMap[Player.pos][DESCRIPTION])
  else:
    print('Vous êtes déjà passé par ici, il ne reste plus rien d\'intéressant')
  

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
    print('Que souhaitez vous faire ?')
    action = input('\n > ')
    if action.lower() == 'quitter':
      sys.exit()
    elif action.lower() == 'voyager':
      PlayerMove(action.lower())
    elif action.lower() == 'aide':
      print('Liste des commandes: ')
      print('voyager        -       vous permets de vous déplacer')
      print('inventaire     -       vous permets d\'accéder à votre inventaire')
      print('carte          -       vous permets d\'accéder à votre carte')
      print('journal        -       vous permets d\'accéder à votre journal de quête')
      print('aide           -       vous permet d\'avoir une liste des commandes')
      print('quitter        -       vous permet de quitter le jeu')

#function for the movement of the player
def PlayerMove(MyAction):
  ask = "Où souhaitez-vous aller ?"
  dest = input(ask + '\n > ')

  if dest == 'est':
    if ZoneMap[Player.pos][EAST] == '':
      print('Impossible d\'aller dans cette direction, un mur vous bloque la route.')
      PlayerMove(MyAction)
    elif (ZoneMap[ZoneMap[Player.pos][EAST]][EVENT] == 'BOSS'):
      print('Vous êtes face au combat ultime, vous ne pourrez plus revenir en arrière, êtes vous sûr de vouloir continuer ?')
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
      print('Impossible d\'aller dans cette direction, un mur vous bloque la route.')
      PlayerMove(MyAction)
    elif (ZoneMap[ZoneMap[Player.pos][NORTH]][EVENT] == 'BOSS'):
      print('Vous êtes face au combat ultime, vous ne pourrez plus revenir en arrière, êtes vous sûr de vouloir continuer ?')
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
      print('Impossible d\'aller dans cette direction, un mur vous bloque la route.')
      PlayerMove(MyAction)
    elif (ZoneMap[ZoneMap[Player.pos][SOUTH]][EVENT] == 'BOSS'):
      print('Vous êtes face au combat ultime, vous ne pourrez plus revenir en arrière, êtes vous sûr de vouloir continuer ?')
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
      print('Impossible d\'aller dans cette direction, un mur vous bloque la route.')
      PlayerMove(MyAction)
    elif (ZoneMap[ZoneMap[Player.pos][WEST]][EVENT] == 'BOSS'):
      print('Vous êtes face au combat ultime, vous ne pourrez plus revenir en arrière, êtes vous sûr de vouloir continuer ?')
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

#Main game loop function
def main_game_loop():
  while Player.won is False:
    prompt()

########## ZONE DE TESTS ##########
#test 001
def testlecombat():
  print('boum boum')
  ActiveCase[Player.pos] = False
  time.sleep(2)
  prompt()

def testeaster():
  print('easter')
  ActiveCase[Player.pos] = False
  time.sleep(2)
  prompt()
def testblessing():
  print('blessing')
  ActiveCase[Player.pos] = False
  time.sleep(2)
  prompt()

def testcurse():
  print('curse')
  ActiveCase[Player.pos] = False
  time.sleep(2)
  prompt()

def testobject():
  print('object')
  ActiveCase[Player.pos] = False
  time.sleep(2)
  prompt()

def testnpc():
  print('npc')
  ActiveCase[Player.pos] = False
  time.sleep(2)
  prompt()

main_game_loop()

