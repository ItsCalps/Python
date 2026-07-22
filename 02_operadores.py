# Operadores Aritmeticos

print(3 + 4) # suma
print(3 - 4) # resta
print(3 * 4) # multiplicacion
print(3 / 4) # division
print(10 % 2) # modulo
print(10 // 3) # division aproximada (numero entero)
print(2 ** 3) # El 3 actua como un exponente 2x2x2= 8
print(2 + 3 - 4 * 5 / 2 // 1) #se pueden hacer cadenas

print("Hola " + "Python")

"""
print("Hola" - "Python")
print("Hola" + 5)  
print("Hola" * 2.5)

Dan error
"""
print("Hola " + str(5)) #ya no da error porque lo conviertes en str
print("Hola " * 2) # "Hola" se multiplica saliendo 2 veces en terminal
print("Hola " * (2 ** 3)) # lo mismo primero se multiplica () y despues el hola

#Operadores comparativos

print(3 > 4) # mayor
print(3 < 4) # menor
print(3 >= 4 ) # mayor o igual
print(3 <= 4) # menor o igual
print(3 == 4) #igualdad
print(3 != 4) # Si es distinto

#Tambien se pueden usar letras
print("Hola" > "Python")
print("Hola" < "Python")
print("aaaa" >= "abaa")  #ordenacion alfabetica por ASCII (cuenta las mayus)
print(len("aaaa") >= len("abaa")) #si contamos caracteres con "len" si da true ya que tienen los mismos caracteres aunque varien
print("Hola" <= "Python")
print("Hola" == "Python")
print("Hola" != "Python")

# Operadores logicos

print(3 > 4 and "Hola" > "Python")
print(3 > 4 or "Hola" > "Python")
print(not(3 > 4 )) # cambia la condicion por ejemplo si sale falso lo cambia a true


