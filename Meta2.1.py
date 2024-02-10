lista = []
while True:
    print("menu")
    print("1. Agregar elemento")
    print("2. Borrar elemento")
    print("3. Mostrar lista")
    print("4. Salir")
    a= input("Elige Opcion:")
    if a == "1":
        elemento=input("Ingrese elemento: ")
        lista.append(elemento)
        print("elemento guardado")
    elif a == "2":
        if lista:
            print("lista actual", lista)
            b = int(input("Ingrese el numero de elemento a borrar: "))
            if 0 <= b < len(lista):
                elementoborrado = lista.pop(b)
                print("elemento Borrado")
    elif a == "3":
        print("Lista actual", lista)
    elif a == "4":
        print("saliendo")
        break
    else:
        print("incorrecto")
