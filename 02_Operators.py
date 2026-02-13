### Operadores aritmeticos ###

print("Adicción:",3 + 4)
print("Sustrayendo:",3 - 4)               #Todos los numeros se pueden combinar con los operadores matematicos.
print("Division:",3 / 4)
print("Multitplicación:",3 * 4)
print("El resto de un numero:", 10 % 3) #->  10 % 3 da como resultado 1 (porque 3 cabe tres veces en 10 y sobra 1).
print("División entera:",10 // 3)
print("Potencia:",2 ** 3)

print("Hola " + "Python " + "Que tal?")
print("Hola " + str(5))
print("Hola " * 5)   
print("Hola " * (2 ** 3))   

my_float = 2.5 * 2
print("Me gusta el numero " * int(my_float)) 

### Operadores comparativos ###
# Devuelve un valor booleano

print(3 > 4)
print(3 < 4)
print(3 >= 4)
print(3 <= 4)
print(3 == 4)
print(3 != 4)

print("Hola" < "Python")
print("Hola" > "Python")
print("aaaa" >= "aaaa") # Ordenacion alfabetica, toma en cuenta el numero de caracteres, mayusculas y minusculas
print(len("aaaaa") >= len("aaaa")) # Cuenta caracteres
print("Hola" <= "Python")
print("Hola" == "Hola")
print("Hola" != "Python")

### Operadores Logicos ###

print(3 > 4 and "Hola" > "Python")
print(3 > 4 or "Hola" > "Python")
print(3 < 4 and "Hola" < "Python")
print(3 < 4 or "Hola" > "Python")
print(3 < 4 or ("Hola" > "Python" and 4 == 4))
print(not(3 > 4))