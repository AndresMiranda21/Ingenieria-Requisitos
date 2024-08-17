class DeterminarMayor:

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def mayor(self):
        if (self.num1 > self.num2):
            print('El valor mayor es: ',self.num1)
        else:
            if (self.num2 > self.num1):
                print ('El valor mayor es: ', self.num2)
            else:
                print('Ambos valores son iguales')

num1 = float(input('Ingrese el primer valor: '))
num2 = float(input('Ingrese el segundo valor: '))

solucion = DeterminarMayor(num1, num2)

solucion.mayor()
