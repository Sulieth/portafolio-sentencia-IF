print("-------------------------------------")
print(" Verificar si un triángulo es válido")
print("------------------------------------- \n")


lado1 = float(input("Ingrese la longitud del primer lado del triángulo: "))
lado2 = float(input("Ingrese la longitud del segundo lado del triángulo: "))
lado3 = float(input("Ingrese la longitud del tercer lado del triángulo: "))


if ((lado1 + lado2) > lado3) or ((lado1 + lado3) > lado2) or ((lado2 + lado3) > lado1):
    print("Los lados ingresados forman un triángulo válido.")
else:
    print("Los lados ingresados no forman un triángulo válido.")