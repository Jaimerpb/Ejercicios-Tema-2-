import unittest 
from ejercicio1 import punto,rectangulo 

class test_ejercicio1(unittest.TestCase):
    
    def test_constructor(self):
        A=punto(2,3)
        B=punto(5,5)
        C=punto(-3,-1)
        D=punto(0,0)
        self.assertEqual(A.constructor(),"(2,3)")
        self.assertEqual(B.constructor(),"(5,5)")
        self.assertEqual(C.constructor(),"(-3,-1)")
        self.assertEqual(D.constructor(),"(0,0)")
    
    def test_cuadrante(self):
        A=punto(2,3)
        C=punto(-3,-1)
        D=punto(0,0)
        self.assertEqual(A.cuadrante(),"El punto (2,3) pertence al primer cuadrante")
        self.assertEqual(C.cuadrante(),"El punto (-3,-1) pertenece al tercer cuadrante")
        self.assertEqual(D.cuadrante(),"El punto (0,0) está sobre el origen de coordeandas")

    def test_vector(self):
        A=punto(2,3)
        B=punto(5,5)
        self.assertEqual(A.vector(B),"El vector entre (2,3) y (5,5) es (3,2)")
        self.assertEqual(B.vector(A),"El vector entre (5,5) y (2,3) es (-3,-2)")

    def test_distancia(self):
        A=punto(2,3)
        B=punto(5,5)   
        self.assertEqual(A.distancia(B),"La distancia entre (2,3) y (5,5) es 3.605551275463989")
        self.assertEqual(B.distancia(A),"La distancia entre (5,5) y (2,3) es 3.605551275463989")
    
    def test_puntomaslejano(self):
        A=punto(2,3)
        B=punto(5,5)
        C=punto(-3,-1)
        puntomaslejano= A
        if B.distancia() > puntomaslejano.distancia():
            puntomaslejano=B
        if C.distancia() > puntomaslejano.distancia():
            puntomaslejano=C
        self.assertEqual(puntomaslejano,B)
        
    
    def test_crear_rectangulo():
        A=punto(2,3)
        B=punto(5,5)
        rectangulo=rectangulo(A,B)
        self.assertEqual(rectangulo.A)
    
    def test_base(self):
        A=punto(2,3)
        B=punto(5,5)
        rectangulo_1=rectangulo(A,B)
        self.assertEqual(rectangulo.base(),3)
    
    def test_altura(self):
        A=punto(2,3)
        B=punto(5,5)
        rectangulo_1=rectangulo(A,B)
        self.assertEqual(rectangulo.altura(),2)
    
    def test_area(self):
        A=punto(2,3)
        B=punto(5,5)
        rectangulo_1=rectangulo(A,B)
        self.assertEqual(rectangulo.area(),6)