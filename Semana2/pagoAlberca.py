class PagoAlberca:
    
    def __init__(self):
        self.lado = float(input('Ingrese la longitud de la alberca en metros: '))
        self.ancho = float(input('Ingrese el ancho de la alberca en metros: '))
        self.prof = float(input('Ingrese la profundidad de la alberca en metros:'))

        self.pagoMetro = float(input('Ingrese el costo por metro cúbico de agua: '))

    def calcularVolumen(self):
        vol = self.lado * self.ancho * self.prof
        return vol
    
    def calcularPago(self):
        pago = self.calcularVolumen() * self.pagoMetro
        return pago
    
solucion = PagoAlberca()

print('El pago total por el agua utilizada es:', solucion.calcularPago())
    

