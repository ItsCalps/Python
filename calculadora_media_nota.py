nota_1 = float(input("Escribe la 1 nota para hacer la media: "))
nota_2 = float(input("Escribe la 2 nota para hacer la media: "))
nota_3 = float(input("Escribe la 3 nota para hacer la media: "))

notas = [nota_1, nota_2, nota_3]

total_notas = nota_1 + nota_2 + nota_3

promedio = total_notas / len(notas)

promedio_redondeado = round(promedio, 3)

if promedio < 5:
    print("Te ha quedado el trimestre! Tu media ha sido de: ", promedio_redondeado)
else:
    print("Has pasado el trimestre! Tu media ha sido de: ", promedio_redondeado)