import sys
import os


class OperasBas:
    # declaracion de propiedades de la clase
    num1 = 0
    num2 = 0
    res = 0

    # declaracion de constructor

    def __init__(self, x, y):
        self.num1 = x
        self.num2 = y

     # declaracion de metodos de clase
    def suma(self):
        self.res = self.num1+self.num2
        print("La suma es: {} ".format(self.res))

    def resta(self):
            self.res = self.num1-self.num2
            print("La resta es: {} ".format(self.res))

    def multiplica(self):
            self.res = self.num1*self.num2
            print("La multiplicacion es: {} ".format(self.res))

    def div(self):
                    self.res = self.num1 / self.num2
                    print("La division es: {} ".format(self.res))
       
def main():
    
        print("-----Calculadora-------------")
        x = int((input("Dame el primer numero: ")))
        y = int((input("Dame el segundo numero: ")))
        obj = OperasBas(x,y)
        op = 0
        
        while op < 5:
            op = int(input(
                "Ingresa lo que deseas hacer (1-Suma, 2-Resta, 3-Multiplicacion,4-Division, 5-Salir: )"))
            if op == 1:
                obj.suma()
            elif op == 2:
                obj.resta()
            elif op == 3:
                obj.multiplica()
            elif op == 4:
                obj.div()
            else:
                print("Adios")
                
                


if __name__ == "__main__":
    main()

