from Stats import PlayerStats

Player = PlayerStats()
ActiveCase = {'A1': True, 'A2': True, 'A3': True,'A4': True, 'A5': True,
              'B1': True, 'B2': True, 'B3': True,'B4': True, 'B5': True,
              'C1': True, 'C2': True, 'C3': True,'C4': True, 'C5': True,
              'D1': False, 'D2': False, 'D3': True,'D4': True, 'D5': True,
              'E1': False, 'E2': True, 'E3': True,'E4': True, 'E5': True,
              'F1': False, 'F2': False, 'F3': False,'F4': True, 'F5': True
              }
MapCase = {'A1': 'o', 'A2': 'o', 'A3': 'o','A4': 'o', 'A5': 'o',
           'B1': 'o', 'B2': 'o', 'B3': 'o','B4': 'o', 'B5': 'o',
           'C1': 'o', 'C2': 'o', 'C3': 'o','C4': 'o', 'C5': 'o',
           'D1': 'o', 'D2': 'o', 'D3': 'o','D4': 'o', 'D5': 'o',
           'E1': 'o', 'E2': 'o', 'E3': 'o','E4': 'o', 'E5': 'o',
           'F1': 'o', 'F2': 'o', 'F3': 'o','F4': 'o', 'F5': 'o'
           }
# print(Player.pos)
# if ActiveCase[Player.pos] == False:
#   print(MapCase[Player.pos])
#   MapCase[Player.pos] = 'x'
#   print(MapCase[Player.pos])
for i in ActiveCase:
  if ActiveCase[i] == False:
    MapCase[i] = '-'
  MapCase[Player.pos] = 'x'

def MapDisplay():
  for i in ActiveCase:
    if ActiveCase[i] == False:
      MapCase[i] = '-'
  MapCase[Player.pos] = 'x'
  print("   1  2  3  4  5 ")
  print("A [" + MapCase['A1'] + "][" + MapCase['A2'] + "][" + MapCase['A3'] + "][" + MapCase['A4'] + "][" + MapCase['A5'] + "]")
  print("B [" + MapCase['B1'] + "][" + MapCase['B2'] + "][" + MapCase['B3'] + "][" + MapCase['B4'] + "][" + MapCase['B5'] + "]")
  print("C [" + MapCase['C1'] + "][" + MapCase['C2'] + "][" + MapCase['C3'] + "][" + MapCase['C4'] + "][" + MapCase['C5'] + "]")
  print("D [" + MapCase['D1'] + "][" + MapCase['D2'] + "][" + MapCase['D3'] + "][" + MapCase['D4'] + "][" + MapCase['D5'] + "]")
  print("E [" + MapCase['E1'] + "][" + MapCase['E2'] + "][" + MapCase['E3'] + "][" + MapCase['E4'] + "][" + MapCase['E5'] + "]")
  print("F [" + MapCase['F1'] + "][" + MapCase['F2'] + "][" + MapCase['F3'] + "][" + MapCase['F4'] + "][" + MapCase['F5'] + "]")

MapDisplay()