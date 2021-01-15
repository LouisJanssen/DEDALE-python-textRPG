class PlayerStats:
  def __init__(self):
    self.name = ""
    self.Hp = 10
    self.Atk = 3
    self.Str = 5
    self.Agi = 5
    self.Int = 5
    self.Cha = 5
    self.Gold = 0
    self.pos = 'F3'
    self.won = False
    self.lvl = 1
    self.xp = 0

#======================================================================================
# Library monsters and stats

NAME = 'NAME'
HP = 'HP'
ATK = 'ATK'
LOOT = 'loot'

MobStats = {
  'ChickenStats':{
    NAME: 'Poule',
    HP: 1,
    ATK: 0,
    LOOT: 'not defined',
  },
  'SpiderStats':{
    NAME: 'Arraignée d\'Héphaïstos',
    HP: 5,
    ATK: 3,
    LOOT: 'not defined',
  },
  'BoarStats':{
    NAME: 'Sanglier',
    HP: 8,
    ATK: 5,
    LOOT: 'not defined',
  },
  'HydraStats':{
    NAME: 'Hydre',
    HP: 15,
    ATK: 10,
    LOOT: 'not defined',
  },
  'SirensStats':{
    NAME: 'Sirène',
    HP: 10,
    ATK: 10,
    LOOT: 'not defined',
  },
  'CyclopStats':{
    NAME: 'Cyclope',
    HP: 15,
    ATK: 15,
    LOOT: 'not defined',
  },
  'LestrygonStats':{
    NAME: 'Lestrygon',
    HP: 10,
    ATK: 15,
    LOOT: 'not defined',
  },
}

# Test = MobStats['CyclopStats'][HP]
# print(Test)