# Variable

my_string_variable = "My string variable"
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_boleal_variable = False
print(my_boleal_variable)

# con la , juntas variables
# Cadena de Variables con print
print(my_boleal_variable, my_string_variable) 
print("Este es el valor de:, my_int_variable")

# Funciones del sistema

print(len(my_string_variable))
# Sirve para contar los caracteres (los espacios incluidos)

#Variables en una sola linia

name, surname, alias, age = "Marc", "Liotto Puskas", "ItsCalps", 16

print("me llamo:", name, surname, "mi edad", age, "mi alias", alias)

# Imputs (Tipo preguntas)
"""
name = input("Cual es nombre: ")

age = input("Cual es tu edad: ")

print(name)
print(age)
"""

# Se cambia el tipo
name = 34
age = "Jose Antonio"

print(name)
print(age)

#Forzar el tipo

address : str = "Mi direccion" #Aqui decimos que solo puede ser str
address = 32

print(type(address)) 