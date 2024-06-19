print("--------------------------------")
print("    Calcular el salario neto |")
print("-------------------------------- \n")

salario=float(input("Ingrese el salario bruto: "))

if salario > 2000:
    impr = salario * 0.20
    sal_brut = salario - impr
    
else:
    sal_brut = salario
    
print("Su salario neto es:", sal_brut)