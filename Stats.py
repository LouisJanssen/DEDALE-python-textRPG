class PlayerStats:
  def __init__(self):
    self.name = ""
    self.Hp = 10
    self.Atk = 3
    self.Cha = 5
    self.pos = 'F3'
    self.dead = False
    self.lvl = 1
    self.xp = 0
    self.father = ""

#======================================================================================
# Library monsters and stats

NAME = 'NAME'
HP = 'HP'
ATK = 'ATK'
LOOT = 'loot'
XP = 'XP'

MobStats = {
  'ChickenStats':{
    NAME: 'Poule',
    HP: 1,
    ATK: 0,
    LOOT: 'not defined',
    XP: 10,
  },
  'SpiderStats':{
    NAME: 'Arraignée mécanique',
    HP: 5,
    ATK: 3,
    LOOT: 'not defined',
    XP: 20,
  },
  'BoarStats':{
    NAME: 'Sanglier',
    HP: 8,
    ATK: 5,
    LOOT: 'not defined',
    XP: 30,
  },
  'HydraStats':{
    NAME: 'Hydre',
    HP: 15,
    ATK: 10,
    LOOT: 'not defined',
    XP: 50,
  },
  'SirensStats':{
    NAME: 'Sirène',
    HP: 10,
    ATK: 10,
    LOOT: 'not defined',
    XP: 40,
  },
  'CyclopStats':{
    NAME: 'Cyclope',
    HP: 15,
    ATK: 15,
    LOOT: 'not defined',
    XP: 60,
  },
  'LestrygonStats':{
    NAME: 'Lestrygon',
    HP: 10,
    ATK: 15,
    LOOT: 'not defined',
    XP: 50,
  },
}

# Test = MobStats['CyclopStats'][HP]
# print(Test)