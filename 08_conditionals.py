### Conditionals ###

my_condition = False

if my_condition: # -> Para ejecutar el If la condicion tiene que ser verdadera
    print("Se ejecuta la condicion del if")

my_condition = 12 #int(input("Ingrese un numero: ")) -> Esto lo puse por que querias probar cositas nuevas (IGNOREN ESTE MENSAJE)

if my_condition == 10: 
 print("Se ejecuta la condicion del if")

elif my_condition > 10 and my_condition < 20: # -> if y elif necesitan una condicion para que funcionen.
    print("Es mayor que 10 y menor que 20")
elif my_condition == 25:
   print("Es igual a 25")
else:
   print("Es menor o igual que 10 o mayor o igual que 20")

print("La ejecucion continua")

my_string = ""

if not my_string:
   print("Mi cadena de texto es vacia")

if my_string == "Mi cadena de textooooo":
   print("Estas cadenas de texto coninciden")

