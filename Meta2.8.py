numero=int(input("Ingresa numero: "))
factorial = 1
for a in range(2, numero + 1):
    factorial = factorial * a
print(numero, "! =", factorial)
