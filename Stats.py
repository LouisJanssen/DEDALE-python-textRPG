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

#======================================================================================

# class ChickenStats :
#   def __init__(self): # Ajouter ,NomDuLoot
#     self.name = 'Poule'
#     self.Hp = 1
#     self.Atk = 0
#     #self.loot = CuisseDePoulet

# class SpiderStats :
#   def __init__(self):
#     self.name = 'Araignée d\'Héphaïstos'
#     self.Hp = 5
#     self.Atk = 3
    #self.loot = ???

#======================================================================================
# Bibliothèque monstres & stats

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
}

# MobStats['SpiderStats'][HP]