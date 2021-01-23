from Stats import PlayerStats
from Tools import promptSlow
Player = PlayerStats()

def Curse(Cursetype):
  if Cursetype == 'Vines':
    promptSlow('Vous subissez : HP - 1 et ATK - 1')
    Player.Hp = Player.Hp - 1
    Player.Str = Player.Atk - 1
  elif Cursetype == 'Flower':
    promptSlow('Vous subissez : CHA + 1 et HP - 2')
    Player.Cha = Player.Cha + 1
    Player.Hp = Player.Hp - 2

def Blessing(Blesstype):
  if Blesstype == 'Styx':
    promptSlow('Vous gagnez : HP + 5')
    Player.Hp = Player.Hp + 5
  elif Blesstype == 'Work':
    promptSlow('Vous gagnez : ATK + 5')
    Player.Atk = Player.Atk + 5