#Calculadora salario 
h_trabajadas = float(input("Cuantas horas trabajas al dia? "))
d_trabajados = int(input("Cuantas dias a la semana trabajas? "))
salario_mensual = int(input ("cuanto dinero ganas al mes "))


semanas_mes = 4

h_por_semana = h_trabajadas * d_trabajados

h_totales_mes = h_por_semana * semanas_mes

salario_por_hora = round(salario_mensual / h_totales_mes)

print("El total que ganas por hora es: ", salario_por_hora, "$")