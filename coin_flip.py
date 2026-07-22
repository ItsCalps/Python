import random

volver_a_jugar = True

while volver_a_jugar:
    resultados = ["cara", "cruz"]
    resultado = random.choice(resultados)

    eleccion_usuario = input("Elije 'Cara o Cruz': ").lower()

    if eleccion_usuario == resultado:
        print("Has ganado!")
    else:
        print("Has perdido!!")

    respuesta = input("Quieres volver a jugar? ").lower()
    if respuesta == "no":
        break