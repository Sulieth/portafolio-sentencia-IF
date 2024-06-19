print("Determine cuál es mayor o si son iguales")
print("----------------------------------------")

a = int(input("Ingresa un numero: "))
b = int(input("Ingresa un numero: "))

if a == b:
    print("Los numeros son iguales")
elif a > b:
    print(f'el numero mayor es {a}')
    print(f'el numero menor es {b}')
elif a < b:
    print(f'el numero mayor es {b}')
    print(f'el numero menor es {a}')    