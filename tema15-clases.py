import os


class OperasBas:
    #declaracion de propiedades de la clase
    num1=0
    num2=0
    res=0
    
    #declaracion de constructor
    
    def __init__(self, a,b):
        self.num1=a
        self.num2=b
    
     #declaracion de metodos de clase
    def suma(self):
        #num1=12
        #num2=10
        self.res=self.num1+self.num2
        print("La suma es: {} ".format(self.res))
    
def main():
        os.system('cls')
        obj=OperasBas(3,4)
        obj.suma()
        
        
if __name__ == "__main__":
        main()
    
   
    
    




