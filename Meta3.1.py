import pandas as pd
numeros = []
i = 0
while i < 10:
    print("numero: ",i+1)
    numero = float(input("Ingresa numero: "))
    numeros.append(numero)
    i=i+1

salir=0
while (salir !=7):
    print("=======")
    print("Menu")
    print("=======")
    print("1. Media")
    print("2. Mediana")
    print("3. Moda")
    print("4. Min")
    print("5. Max")
    print("6. Desv. Estandar")
    print("7. salir")
    opcion=int(input("Ingresa opcion: "))
    if opcion == 1:
        df = pd.DataFrame(numeros)
        print("La media es:", df.mean())
    if opcion == 2:
        df = pd.DataFrame(numeros)
        print("La Mediana es :", df.median())
    if opcion == 3:
        df = pd.DataFrame(numeros)
        print("La Moda es: ", df.mode())
    if opcion == 4:
        df = pd.DataFrame(numeros)
        print("El minimo es: ", df.min())
    if opcion == 5:
        df = pd.DataFrame(numeros)
        print("El maximo es: ",df.max())
    if opcion == 6:
        df = pd.DataFrame(numeros)
        print("La desviacion estandar: ", df.std())
    if opcion == 7:
        print("saliendo")