print("Clasificar la categoría de edad")
print("-------------------------------")

edad = float(input("Ingresa tu edad: "))

if edad >= 0 and edad <= 12:
    print("Es infantil.")
elif edad >= 13 and edad <= 19:
    print("Es adolescente.")
elif edad >= 20 and edad <= 59:
    print("Es adultx.")
else:
    print("Es adultx mayor.")