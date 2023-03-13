import math 

class punto:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __str__(self):
        return "({0},{1})".format(self.x,self.y)

    @staticmethod 
    def cuadrante(self):
        if self.x>0 and self.y>0:
            return f"El punto {self} pertence al primer cuadrante"

        elif self.x<0 and self.y>0:
            return f"El punto {self} pertenece al segundo cuadrante"
        
        elif self.x<0 and self.y<0:
            return f"El punto {self} pertenece al tercer cuadrante"

        elif self.x>0 and self.y<0:
            return f"El punto {self} pertence al cuarto cuadrante "
        elif self.x==0 and self.y==0:
            return f"El punto {self} está sobre el origen de coordeandas"

    
    @staticmethod 
    def vector(self,punto):
        return f"El vector entre {self} y {punto} es ({punto.x-self.x},{punto.y-self.y})"
    
    @staticmethod
    def distancia(self,punto):
        distancia = math.sqrt((punto.x-self.x)**2+(punto.y-self.y)**2)
        return f"La distancia entre {self} y {punto} es {distancia}"
    







        
        