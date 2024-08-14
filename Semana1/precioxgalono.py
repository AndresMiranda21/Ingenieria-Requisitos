class PrecioPorGalon:
    def __init__(self):
        self.litrosProducidos = float(input("Digite la cantidad de litros: "))
        self.precioGalon = float(input("Digite el precio por galón: "))

    def calcularTotal(self):
        galonProducidos = self.litrosProducidos / 3.785
        total = galonProducidos * self.precioGalon
        return total

solucion = PrecioPorGalon()

print("El productor ganará: ", solucion.calcularTotal())
