# ### SAVES ###
# import os.path
# file_exists = os.path.isfile('loadfile.txt')

# def load():
#   if file_exists:
#     file = open('loadfile.txt','r')
#     room = file.read()
#     file.close()
#   else:
#     room='startroom'
#   roomchooser(room)

# def save(s):
#   file = open('loadfile.txt','w')
#   file.write(s)
#   file.close()

# def roomchooser(room):
#   if room=='startroom':
#     startroom()
#   elif room=='secondroom':
#     secondroom()

# def startroom():
#   s='startroom'
#   save(s)
#   print('you are in the bitch\'s sources go left or right?')
#   direction=input()
#   if direction == 'right':
#     secondroom()
#   quit()

# def secondroom():
#   s='secondroom'
#   save(s)
#   print('you are in hell, left or right?')
#   direction=input()
#   if direction == 'right':
#     startroom()
#   quit()

# load()

# # def do_save(self, arg):
# #     saveGame = open('savegame.txt', 'wb')
# #     saveValues = (inventory, gold, location)
# #     pickle.dump(saveValues, saveGame)
# #     saveGame.close()

# # def do_load(self, arg):
# #     loadGame = open('savegame.txt', 'rb')
# #     loadValues = pickle.load(loadGame)
# #     inventory = loadValues[0]
# #     gold = loadValues[1]
# #     location = loadValues[2]
# #     loadGame.close()

# #  elif option == "3":
# #         os.system('clear')
# #         with open('savefile', 'wb') as f:
# #             pickle.dump(PlayerIG, f)
# #             print "\nGame has been saved!\n"
# #         option = raw_input(' ')
# #         start1()

# Python3 program to illustrate store  
# efficiently using pickle module  
# Module translates an in-memory Python object  
# into a serialized byte stream—a string of  
# bytes that can be written to any file-like object. 
  
import pickle 
  
def storeData(): 
    # initializing data to be stored in db 
    Omkar = {'key' : 'Omkar', 'name' : 'Omkar Pathak', 
    'age' : 21, 'pay' : 40000} 
    Jagdish = {'key' : 'Jagdish', 'name' : 'Jagdish Pathak', 
    'age' : 50, 'pay' : 50000} 
  
    # database 
    db = {} 
    db['Omkar'] = Omkar 
    db['Jagdish'] = Jagdish 
      
    # Its important to use binary mode 
    dbfile = open('examplePickle', 'ab') 
      
    # source, destination 
    pickle.dump(db, dbfile)                      
    dbfile.close() 
  
def loadData(): 
    # for reading also binary mode is important 
    dbfile = open('examplePickle', 'rb')      
    db = pickle.load(dbfile) 
    for keys in db: 
        print(keys, '=>', db[keys]) 
    dbfile.close() 
  
if __name__ == '__main__': 
    storeData() 
    loadData() 