# Strings

my_string = "Mi string"
my_other_string = 'Mi otro string'

print(len(my_string))
print(len(my_other_string))

print(my_string, my_other_string)

my_new_line_string = "mi string\nde dos linias" 
#La \n te permite hacer un cambio de linias
print(my_new_line_string)

my_tab_string = "\tmi string con tabulacion" 
#La \t te permite hacer una tabulacion
print(my_tab_string)

my_scape_string = "\\tEste es un esting \\n de escape"
# la \\ te permite anular los \t y \n
print(my_scape_string)

# Formateo

name, surname, age = "Alex", "Torres", 21

print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))
print("Mi nombre es %s %s y mi edad es %s" %(name, surname, age))
print(f"Mi nombre es {name} {surname} y mi edad es {age}")

# Desempaquetado de caracteres

language = "python"
a, b, c, d, e, f = language #cada letra es un caracter del "python"
print(a)
print(b)
print(c)
print(d)
print(f)
print(e)

# Division 

languge_slice = language[1:3] #coge las letras elegidas usando [X:Y]
print(languge_slice)

languge_slice = language[1:] #quita las letras elegidas usando [X:]
print(languge_slice)

languge_slice = language[-2:] #Coge la letra del final [-X:]
print(languge_slice)

languge_slice = language[0:6:2] 
print(languge_slice)

# Reverse

reversed_language = language[ ::-1 ] # Para que le de la vuelta a una palabra
print(reversed_language)

# Metodos/Funciones del sistema

print(language.capitalize()) #Pone la primera letra en mayus
print(language.upper()) #Pone todo en mayus
print(language.count("t")) #Dice cuantos caracters hay en la palabra
print(language.isnumeric()) #Dice si es un numero
print("1".isnumeric()) #Dice si es un numero
print(language.lower()) #Pone todo en minusculas
print(language.upper().isupper) #.isuper es para comprobar si esta en mayus
print(language.startswith("py")) # te dice si empieza con...



