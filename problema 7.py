print("Calcular el precio con descuento")
print("--------------------------------")

precio = float(input("Ingresa el precio: "))

if precio > 100:
    descuento = precio * 0.10
    precio_final = precio - descuento
    print(f"Se aplicó un descuento del 10%. el precio final es: ${precio_final:.2f}")   
else:
    precio_final = precio
    print(f"El precio es menor o igual a $100. El precio final: ${precio_final:.2f}")