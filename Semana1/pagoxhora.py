class PagoPorHoras:
    def __init__(self):
        self.horasTrabajadas = float(input("Digite el número de horas trabajadas: "))
        self.pagoHora = float(input("Digite el valor por hora: "))

    def calcularSueldoSemanal(self):
        sueldoSemanal = self.horasTrabajadas * self.pagoHora
        return sueldoSemanal

solucion = PagoPorHoras()

print("Recibe un sueldo semanal de:", solucion.calcularSueldoSemanal())
