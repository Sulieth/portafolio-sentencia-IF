print("-------------------------------------")
print("         Clasificar el IMC"           )
print("------------------------------------- \n")

altura=float(input("ingrese altura en metros"))
peso=float(input("ingrese su peso en kilogramos"))

imc= peso/altura**2

if imc< 18.5:
   clasificacion="bajo peso"

elif imc>18.5 and imc <=24.9:
   clasificacion="normal"

elif imc>25 and imc <= 29.9:
   clasificacion= "sobre peso "

else:
   clasificacion="obesidad " 

print("su imc es de: ",imc)
print("indica que tiene:",clasificacion)