a = 1
suma = 0
while a <= 100:
    suma=suma+a
    a=a+1
print("La suma de los numeros del 1  al 100 es: ",suma)

numero=int(input("ingresa numero de multiplicar: "))
for i in range (1,13):
    resultado= i * numero
    print(numero, "x", i, "=",resultado)