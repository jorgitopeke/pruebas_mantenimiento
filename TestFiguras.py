import unittest
from figuras import figuras
class TestFiguras(unittest.TestCase):

    def test_Area_Circulo(self):
        f = figuras()
        self.assertEqual(12.5664,f.areaCirculo(2))

    def test_Area_Circulo1(self):
        f = figuras()
        self.assertEqual(78.53999999999999, f.areaCirculo(5))

    def test_Area_Circulo2(self):
        f = figuras()
        self.assertEqual(380.1336, f.areaCirculo(11))
	
	
    def test_Area_Cuadrado(self):
        f = figuras()
        self.assertEqual(4, f.areaCuadrado(2))
	
    def test_Area_Cuadrado2(self):
        f = figuras()
        self.assertEqual(100, f.areaCuadrado(10))

    def test_Area_Cuadrado3(self):
        f = figuras()
        self.assertEqual(25, f.areaCuadrado(5))

    def test_Area_Triangulo(self):
        f = figuras()
        self.assertEqual(2, f.areaTriangulo(2,2))
	
    def test_Area_Triangulo1(self):
        f = figuras()
        self.assertEqual(6, f.areaTriangulo(6,2))

    def test_Area_Triangulo2(self):
        f = figuras()
        self.assertEqual(25, f.areaTriangulo(10,5))

    def test_Area_Rectangulo(self):
        f = figuras()
        self.assertEqual(4, f.areaRectangulo(2,2))

    def test_Area_Rectangulo2(self):
        f = figuras()
        self.assertEqual(100, f.areaRectangulo(2,50))

    def test_Area_Rectangulo3(self):
        f = figuras()
        self.assertEqual(80, f.areaRectangulo(80,1))
	
    def test_Area_Rombo(self):
        f = figuras()
        self.assertEqual(2, f.areaRombo(2,2))

    def test_Area_Rombo2(self):
        f = figuras()
        self.assertEqual(150, f.areaRombo(100,3))

    def test_Area_Rombo3(self):
        f = figuras()
        self.assertEqual(20, f.areaRombo(5,8))
if __name__=="__main__":
    unittest.main() 
