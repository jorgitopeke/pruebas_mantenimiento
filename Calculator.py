import unittest
from calcula import Calculator
class TestCalcula(unittest.TestCase):
	
	def testSumma(self):
		c = Calculator()
        	self.assertEquals(2, c.suma(1,1))

	def testSumma(self):
		c = Calculator()
        	self.assertEquals(101, c.suma(100,1))

	def testSumma(self):
		c = Calculator()
        	self.assertEquals(5200, c.suma(5000,200))
	
	def testResta(self):
		c = Calculator()
        	self.assertEquals(0, c.resta(1,1))

	def testResta(self):
		c = Calculator()
        	self.assertEquals(9, c.resta(10,1))

	def testResta(self):
		c = Calculator()
        	self.assertEquals(10, c.resta(14,4))

	def testMult(self):
		c = Calculator()
        	self.assertEquals(9, c.mult(1,9))

	def testMult(self):
		c = Calculator()
        	self.assertEquals(90, c.mult(10,9))

	def testMult(self):
		c = Calculator()
        	self.assertEquals(900, c.mult(100,9))

	def testDiv(self):
		c = Calculator()
        	self.assertEquals(1, c.div(1,1))

	def testDiv(self):
		c = Calculator()
        	self.assertEquals(9, c.div(9,1))

	def testDiv(self):
		c = Calculator()
        	self.assertEquals(5, c.div(10,2))	

if __name__=="__main__":
    unittest.main() 
