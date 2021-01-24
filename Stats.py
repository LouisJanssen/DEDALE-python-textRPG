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
XP = 'XP'

MobStats = {
  'ChickenStats':{
    NAME: 'Poule',
    HP: 1,
    ATK: 0,
    XP: 10,
  },
  'SpiderStats':{
    NAME: 'Arraignée mécanique',
    HP: 5,
    ATK: 3,
    XP: 20,
  },
  'BoarStats':{
    NAME: 'Sanglier',
    HP: 8,
    ATK: 5,
    XP: 30,
  },
  'HydraStats':{
    NAME: 'Hydre',
    HP: 15,
    ATK: 10,
    XP: 50,
  },
  'SirensStats':{
    NAME: 'Sirène',
    HP: 10,
    ATK: 10,
    XP: 40,
  },
  'CyclopStats':{
    NAME: 'Cyclope',
    HP: 15,
    ATK: 15,
    XP: 60,
  },
  'LestrygonStats':{
    NAME: 'Lestrygon',
    HP: 10,
    ATK: 15,
    XP: 50,
  },
  'MinotaurStats':{
    NAME: 'Minotaure',
    HP: 50,
    ATK: 25,
    XP: 0,
  },
}

# Test = MobStats['CyclopStats'][HP]
# print(Test)