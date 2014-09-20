class figuras():
    def areaCirculo(self, radio):
        return 3.1416 * (radio * radio)
	
    def areaCuadrado(self, lado):
        return lado * lado

    def areaTriangulo(self, base,altura):
        return (base * altura)/2
    
    def areaRectangulo(self, base, altura):
        return base * altura

    def areaRombo(self, dmayor, dmenor):
        return (dmayor * dmenor)/2
