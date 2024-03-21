
#from Bomb import Bomb
class Create:
   
    def __init__(self, bomb):
        self.bomb = bomb

    def printBomb(self):
       coordinates = self.bomb.see()
       print(coordinates)
       for i in range(5):
            for j in range(8):
                # if (i,j) in coordinates:
                #    print("B", end=" " )#str(i)+str(j)+
                # else:
                    print("_", end="  ") 
            print("")
            print("")

#bomb = Bomb()
# create = Create(bomb)
# create.printBomb()