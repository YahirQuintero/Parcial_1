diccionario={}
while True:
    print("=== Menu ===")
    print("1. Agregar elemento")
    print("2. Modificar Elemento")
    print("3. Borrar elemento")
    print("4. Mostrar diccionario")
    print("5. salir")
    dicc=input("Elige Opcion: ")
    if dicc == "1":
        elemento=input("Ingrese elemento: ")
        significado=input("Ingresa significado: ")
        diccionario[significado]=elemento
        print("elemento guarddao")
    elif dicc == "2":
        elemento=input("Ingresa elemento a modificar: ")
        if(elemento in diccionario.keys()):
            significado = input("Ingresa significado Nuevo: ")
            diccionario[elemento]= significado
            print("Significado modificado")
        else:
            print("Error")
    elif dicc == "3":
        elemento = input("Ingresa elemento a modificar: ")
        if elemento in diccionario:
            diccionario.pop(elemento)
            print("elemento borrado")
    elif dicc == "4":
        print("Elementos=")
        print("==============")
        for dato in diccionario:
            print("Elemento: ",dato,"Es =",diccionario[dato])
            print("==============")
    elif dicc == "5":
        print("saliendo")
        break
    else:
        print("incorrecto")
