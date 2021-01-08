class Player:
  def __init__(self):
    self.name = ""
    self.Hp = 10
    self.Atk = 3
    self.Str = 5
    self.Agi = 5
    self.Int = 5
    self.Cha = 5
    self.Gold = 0

Player = Player()
Player.Atk = 6
print(Player.Atk)
Player.Atk += 1
print(Player.Atk)
