
from Bomb import Bomb
from Create import Create

 
 #place(x,y)
#higher: (x-1, y)
#bottom: (x+1, y)
#right: (x, y+1)
#left: (x, y-1)
# higher left: (x-1, y-1)
# higher right: (x-1, y+1)
# bottom left: (X+1, y-1)
# bottom right: (x+1, y-1)

class Verify:
    def __init__(self, bomb):
        #self.coordx = coordx
       # self.coordy = coordy
        self.bomb = bomb
        self.choice = set()
        self.points = {}
     
    def gameOver(self, coordx, coordy):
        coordinates = self.bomb.see() #bomb places
        for i in range(5):
            for j in range(8):
                if (i==coordx-1) and (j==coordy-1): #choice
                    if (i,j) in coordinates: #find bomb
                        print("Game Over")
                        return True 
                    else:
                        cont = 0
                        # near bombs
                        for dx in [-1, 0, 1]:
                            for dy in [-1, 0, 1]:
                                if (dx != 0 or dy != 0) and (i+dx, j+dy) in coordinates:
                                    cont += 1
                        self.points[(i, j)] = cont
                        if cont == 0:
                            self.choice.add((i, j))  
                            print("O", end="  ")
                        else: 
                            print(self.points[(i,j)], end="  ")
                elif (i,j) in self.choice:
                    print("O", end="  ")
                elif (i,j) in self.points:
                    print(self.points[(i,j)], end="  ")
                else:
                    print("_", end="  ")  
            print("")
            print("")
        print("Continua o jogo")

        return False

    