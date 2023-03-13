import math 

class punto:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def constructor(self)
        return f"({self.x},{self.y})"

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

class rectangulo():
    def __init__(self,ptoinicial=punto(),ptofinal=punto())
        self.ptoincial=ptoinicial
        self.ptofinal=ptofinal
    
    @staticmethod 
    def base(self):
        return abs(self.ptofinal.x-self.ptoincial.x)
    
    @staticmethod 
    def altura(self):
        return abs(self.ptofinal.y-self.ptoincial.y)
    
    @staticmethod 

    def area(self):
        return self.base()*self.altura()
    

    
    







        
        