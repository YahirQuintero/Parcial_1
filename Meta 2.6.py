print("===Calificaciones===")
cal = float(input("Ingresa una calificacion: "))

if cal == 100:
    print("Excelente")
elif cal >=90  and cal <= 99.9:
    print("Muy bien")
elif cal >=80 and cal <= 89.9:
    print("Bien")
elif cal >=70 and cal <= 79.9:
    print("Regular")
elif cal >=60 and cal <= 69.0:
    print("Suficiente")
elif cal>=0 and cal<59.9:
    print("Reprobado")
else:
    print("error")