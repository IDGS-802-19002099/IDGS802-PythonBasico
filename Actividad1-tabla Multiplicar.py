""""
leer numero 5

5 x 1=5
5 x 2=10
.
.
5 x 10=50
"""

print("--------------Tabla de Multiplicar------------------")
x=int(input("Dame un numero: " ))

for i in range(1,11):
    print("{} x {} = {} ".format(x,i,(x*i)))