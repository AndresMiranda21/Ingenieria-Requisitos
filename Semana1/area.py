class Area:
    def __init__(self):
        self.ladoA = float(input("Ingrese el valor de A: "))
        self.ladoB = float(input("Ingrese el valor de B: "))
        self.ladoC = float(input("Ingrese el valor de C: "))

    def darAltura(self):
        altura = self.ladoA - self.ladoC
        return altura
    
    def darAreaTriangulo(self):
        areaTriangulo = (self.ladoB * self.darAltura()) / 2
        return areaTriangulo
    
    def darAreaRectangulo(self):
        areaRectangulo = self.ladoB * self.ladoC
        return areaRectangulo
    
    def areaTrianguloA(self):
        areaTrianguloA = self.darAreaTriangulo() + self.darAreaRectangulo()
        return areaTrianguloA


solucion = Area()

print('El área del triángulo es:', solucion.areaTrianguloA())
