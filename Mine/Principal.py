from Create import Create
from Verify import Verify
from Bomb import Bomb

class Principal: 
    
    def __init__(self): 
        self.bomb = Bomb()
        self.create = Create(self.bomb)
        self.verify = Verify(self.bomb)

    def choice(self):
        self.create.printBomb()  
        coordx = int(input("Coordenada x: "))
        coordy = int(input("Coordenada y: "))

        while not self.verify.gameOver(coordx, coordy):
            coordx =  int(input("Coordenada x: "))
            coordy = int(input("Coordenada y: "))
      #print("Game over")

principal = Principal()
principal.choice()
