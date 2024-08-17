class Conversion:
    def __init__(self):
        self.metros = float(input('Digite la cantidad de tela en metros: '))

    def conversion(self):
        pulgadas = self.metros / 0.0254
        return pulgadas
    
solucion = Conversion()

print ('La cantidad de tela en pulgadas es: ', solucion.conversion())