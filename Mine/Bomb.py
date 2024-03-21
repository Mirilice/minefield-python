
import random
#y = 8
#x = 5
class Bomb:
    def __init__(self):
        self.bombs = set()

        while len(self.bombs)<6:
            x = random.randint(0,4)
            y = random.randint(0,7)
            coordinates = (x,y)
           # print(coordiante)
            self.bombs.add(coordinates)
        #self.bombs = list(self.bombs)
    
    def see(self):
        return self.bombs




   