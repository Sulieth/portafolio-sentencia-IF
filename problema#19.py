print("--------------------------------")
print(" Determinar si un año es un siglo")
print("-------------------------------- \n")

año = int(input("Introduce un año: "))

# Determinar si el año es el primer año de un siglo
if año % 100 == 0:
    print(f"El año {año} es el primer año de un siglo.")
else:
    print(f"El año {año} no es el primer año de un siglo.")
