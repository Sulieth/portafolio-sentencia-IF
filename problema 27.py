print("Determinar si es un numero primo")
print("--------------------------------")

numero = int(input("Ingrese un numero entero positivo: "))

if es_primo(numero):
    print(numero, "es un numero primo.")
else:
    print(numero, "no es un numero primo.")