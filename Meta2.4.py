import pandas as pd
df= pd.read_csv("aliespress.csv")
print(df)

print("Minimo Precio de Descuento")
print(df["MinDiscountPrice"].min())

print("Maximo Precio de Descuento")
print(df["MaxDiscountPrice"].max())

print("La media es :")
print(df["wishedCount"].mean)

print("La Mediana de las cantidades es:")
print(df["quantity"].median)

print("Descripcion")
print(df["title"].describe)

print("Cantidades mayor a 100")
print(df[df["quantity"]>100])

print(df[df["averageStar"]==5])