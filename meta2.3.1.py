import pandas as pd
import scipy.stats as stats
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

num_datos = 10
num_grupos = 3
alpha = 0.05

def obtener_numeros(num_datos):
    numeros = []
    print(f"Ingrese {num_datos} numeros:")
    for i in range(num_datos):
        num = float(input(f"Numero {i + 1}: "))
        numeros.append(num)
    return numeros

def obtener_datos_anova(num_datos, num_grupos):
    data = {'Grupo': [], 'Valor': []}
    for i in range(num_grupos):
        print(f"Ingrese {num_datos} valores para el Grupo {i + 1}:")
        for j in range(num_datos):
            valor = float(input(f"Grupo {i + 1}, valor {j + 1}: "))
            data['Grupo'].append(f"Grupo {i + 1}")
            data['Valor'].append(valor)
    return pd.DataFrame(data)


def obtener_datos_para_t_student(num_datos):
    print(f"Ingrese {num_datos} valores para cada grupo:")
    grupo_a = []
    grupo_b = []
    for i in range(num_datos):
        valor = float(input(f"Grupo A, valor {i + 1}: "))
        grupo_a.append(valor)
    for i in range(num_datos):
        valor = float(input(f"Grupo B, valor {i + 1}: "))
        grupo_b.append(valor)
    return grupo_a, grupo_b

salir = 0
while salir != 4:
    print("Pruebas de comparacion")
    print("1- ANOVA")
    print("2- T-Student")
    print("3- Coeficiente de Correlacion")
    print("4- Salir")
    opcion = int(input("Ingrese opcion: "))

    if opcion == 1:
        print("Prueba ANOVA")

        df = obtener_datos_anova(num_datos, num_grupos)

        sns.boxplot(x='Grupo', y='Valor', data=df)
        plt.title('Distribucion por Grupo')
        plt.xlabel('Grupo')
        plt.ylabel('Valor')
        plt.show()

        f_statistic, p_value = stats.f_oneway(
            df[df['Grupo'] == 'Grupo 1']['Valor'],
            df[df['Grupo'] == 'Grupo 2']['Valor'],
            df[df['Grupo'] == 'Grupo 3']['Valor']
        )
        if p_value < alpha:
            print(f"El valor p ({p_value:.4f}) es menor que {alpha}, por lo que rechazamos la hipotesis nula.")
            print("Hay diferencias significativas entre los grupos.")
        else:
            print(f"El valor p ({p_value:.4f}) no es menor que {alpha}. No hay evidencia suficiente para rechazar la hipotesis nula.")
            print("No hay diferencias significativas entre los grupos.")

    elif opcion == 2:
        print("Prueba T-Student")
        grupo_a, grupo_b = obtener_datos_para_t_student(10)
        t_stat, p_valor = stats.ttest_ind(grupo_a, grupo_b)
        print(f"Estadístico t: {t_stat:.2f}")
        print(f"P-Valor: {p_valor:.3f}")
        if p_valor < alpha:
            print(
                "Rechazamos la hipotesis nula: Existe una diferencia significativa entre las medias de los dos grupos.")
        else:
            print("No se rechaza la hipotesis nula: No hay evidencia de diferencias significativas entre las medias.")

    elif opcion == 3:
        print("Coeficiente de Correlacion de Pearson")
        print("Ingrese valores de la Serie X:")
        datos_x = obtener_numeros(num_datos)

        print("Ingrese valores de la Serie Y:")
        datos_y = obtener_numeros(num_datos)

        serie_x = pd.Series(datos_x)
        serie_y = pd.Series(datos_y)

        coeficiente_pearson = serie_x.corr(serie_y)

        print(f"Coeficiente de correlacion de Pearson: {coeficiente_pearson:.2f}")
        plt.scatter(serie_x, serie_y)
        plt.title(f"Grafico de Dispersion con Coeficiente de Pearson: {coeficiente_pearson:.2f}")
        plt.xlabel('Datos X')
        plt.ylabel('Datos Y')
        plt.show()

    elif opcion == 4:
        print("Saliendo...")
        salir = 4

