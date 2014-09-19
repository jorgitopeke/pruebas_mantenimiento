import unittest
from figuras import figuras
class TestFiguras(unittest.TestCase):

    def tes_Area_Circulo(self):
        f = figuras()
        self.assertEqual(12.5664,f.areaCirculo(2))

    def tes_Area_Circulo(self):
        f = figuras()
        self.assertEqual(78.54, f.areaCirculo(5))

    def tes_Area_Circulo(self):
        f = figuras()
        self.assertEqual(380.1336, f.areaCirculo(11))
	
	
    def tes_Area_Cuadrado(self):
        f = figuras()
        self.assertEqual(3, f.areaCuadrado(2))
	
    def tes_Area_Cuadrado(self):
        f = figuras()
        self.assertEqual(100, f.areaCuadrado(10))

    def tes_Area_Cuadrado(self):
        f = figuras()
        self.assertEqual(0.04, f.areaCuadrado(.2))

    def tes_Area_Triangulo(self):
        f = figuras()
        self.assertEqual(2, f.areaTriangulo(2,2))
	
    def tes_Area_Triangulo(self):
        f = figuras()
        self.assertEqual(6, f.areaTriangulo(6,2))

    def tes_Area_Triangulo(self):
        f = figuras()
        self.assertEqual(25, f.areaTriangulo(10,5))

    def tes_Area_Rectangulo(self):
        f = figuras()
        self.assertEqual(4, f.areaRectangulo(2,2))

    def tes_Area_Rectangulo(self):
        f = figuras()
        self.assertEqual(100, f.areaRectangulo(2,50))

    def tes_Area_Rectangulo(self):
        f = figuras()
        self.assertEqual(80, f.areaRectangulo(80,1))
	
    def tes_Area_Rombo(self):
        f = figuras()
        self.assertEqual(2, f.areaRombo(2,2))

    def tes_Area_Rombo(self):
        f = figuras()
        self.assertEqual(150, f.areaRombo(100,3))

    def tes_Area_Rombo(self):
        f = figuras()
        self.assertEqual(20, f.areaRombo(5,8))
if __name__=="__main__":
    unittest.main() 
