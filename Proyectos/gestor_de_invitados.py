
lista = ["carlos", "marc", "maria", "lucas", "lucia"]

invitados = input("Que invitados hay en la lista? ").lower()

if invitados in lista:
    print("Ese invitado esta en la lista!")
else:
    print("Ese invitado no esta en la lista!")