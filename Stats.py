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

MOBNAME = 'MOBNAME'
HP = 'HP'
ATK = 'ATK'
XP = 'XP'

MobStats = {
  'ChickenStats':{
    MOBNAME: 'Poule',
    HP: 1,
    ATK: 0,
    XP: 10,
  },
  'SpiderStats':{
    MOBNAME: 'Arraignée mécanique',
    HP: 5,
    ATK: 3,
    XP: 20,
  },
  'BoarStats':{
    MOBNAME: 'Sanglier',
    HP: 8,
    ATK: 5,
    XP: 30,
  },
  'HydraStats':{
    MOBNAME: 'Hydre',
    HP: 15,
    ATK: 10,
    XP: 50,
  },
  'SirensStats':{
    MOBNAME: 'Sirène',
    HP: 10,
    ATK: 10,
    XP: 40,
  },
  'CyclopStats':{
    MOBNAME: 'Cyclope',
    HP: 15,
    ATK: 15,
    XP: 60,
  },
  'LestrygonStats':{
    MOBNAME: 'Lestrygon',
    HP: 10,
    ATK: 15,
    XP: 50,
  },
  'MinotaurStats':{
    MOBNAME: 'Minotaure',
    HP: 50,
    ATK: 25,
    XP: 0,
  },
}

# Test = MobStats['CyclopStats'][HP]
# print(Test)