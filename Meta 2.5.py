def conversor():
    print("Conversor de centigrados a fahrenheit")
    centigrado=int(input("Ingresa valor centigrado: "))
    multi= centigrado*9
    divi=multi/5
    sum=divi+32
    print("centigrado: ", centigrado, "=","Fahrenheit: ", sum)

def positivonegativo():
    print("Numero Positivo o Negativo")
    num=int(input("Ingresa un numero: "))
    if num < 0:
         print("Negativo")
    if num > 0:
        print("Positivo")

def imparpar():
    print("Par o Impar")
    num=int(input("Ingresa numero: "))
    if num%2==0:
        print("El numero es par")
    elif num:
        print("El numero es impar")

def convertorletra():
    print("====Convertir Numero a letra====")
    num=int(input("Ingresa numero del 1 al 10: "))
    if num == 1:
        print("Uno")
    elif num == 2:
        print("Dos")
    elif num == 3:
        print("Tres")
    elif num == 4:
        print("Cuatro")
    elif num == 5:
        print("Cinco")
    elif num == 6:
        print("Seis")
    elif num == 7:
        print("Siete")
    elif num == 8:
        print("Ocho")
    elif num == 9:
        print("Nueve")
    elif num == 10:
        print("Diez")
    else:
        print("error")
def sumanumeros():
    print("===Suma de 5 Numeros===")
    numeros=[0,0,0,0,0]
    numeros[0]=int(input("Ingresa numero: "))
    numeros[1]=int(input("Ingresa numero: "))
    numeros[2]=int(input("Ingresa numero: "))
    numeros[3]=int(input("Ingresa numero: "))
    numeros[4]=int(input("Ingresa numero: "))
    suma=numeros[0]+numeros[1]+numeros[2]+numeros[3]+numeros[4]
    print("La suma es=",suma)
        



salir =0

while (salir != 6):
    print("===menu===")
    print("1. Centrigados a fahrenheit")
    print("2. Numero Positivo o Negativo")
    print("3. Par o Impar")
    print("4. Convertir numero a letra")
    print("5. Suma de 5 numeros")
    print("6. Salir")
    opcion=input("Ingresa opcion: ")

    if opcion == '1':
        conversor()
    if opcion == '2':
        positivonegativo()
    if opcion == "3":
        imparpar()
    if opcion == "4":
        convertorletra()
    if opcion == "5":
        sumanumeros()
    if opcion == "6":
        print("Saliendo")
        break
