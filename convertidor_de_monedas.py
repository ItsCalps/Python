pesos = float(input("Cuantos pesos colombianos te han quedado?"))
soles = float(input("Cuantos soles peruanos te han quedado?"))
reales = float(input("Cuantos reales brasileños te han quedado?"))

pesos_a_usd = 0.000247
soles_a_usd= 0.28
reales_a_usd= 0.18

Total = (pesos_a_usd * pesos) + (soles_a_usd * soles) + (reales_a_usd * reales)
print("Este es tu total en dólares:", Total)

