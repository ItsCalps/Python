
print("Bienvenido a la calculadora mejorada!")

metodo = input("Que metodo quieres usar? (Suma, Resta, Multiplicacion, Division, Raiz, potencia o porcentaje) ").lower()

if metodo == "suma":
    numero_1 = float(input("Que numero quieres sumar? "))
    numero_2 = float(input("Por que numero lo quieres sumar? "))
    resultado_suma = numero_1 + numero_2
    print(resultado_suma)
elif metodo == "resta":
    numero_1 = float(input("Que numero quieres restar? "))
    numero_2 = float(input("Por que numero lo quieres restar? "))
    resultado_resta = numero_1 - numero_2
    print(resultado_resta)
elif metodo == "multiplicacion":
    numero_1 = float(input("Que numero quieres multiplicar? "))
    numero_2 = float(input("Por que numero lo quieres multiplicar? "))
    resultado_multiplicacion = numero_1 * numero_2
    print(resultado_multiplicacion)
elif metodo == "division":
    numero_1 = float(input("Que numero quieres dividir? "))
    numero_2 = float(input("Por que numero lo quieres dividir? "))
    resultado_division = numero_1 / numero_2
    print(resultado_division)
elif metodo == "raiz":
    numero_1 = float(input("Que numero quieres radicar? "))
    resultado_raiz = numero_1 ** 0.5
    print(resultado_raiz)
elif metodo == "potencia":
    numero_1 = float(input("Que numero es la base (abajo)? "))
    numero_2 = float(input("A qué exponente lo quieres elevar (arriba)? "))
    resultado_exponente = numero_1 ** numero_2
    print(resultado_exponente)
elif metodo == "porcentaje":
    numero_1 = float(input("¿A qué número le quieres sacar el porcentaje? "))
    numero_2 = float(input("¿Qué porcentaje quieres calcular? "))
    resultado_porcentaje = (numero_1 * numero_2) / 100
    print(resultado_porcentaje)
else:
    print("Opción no válida.")