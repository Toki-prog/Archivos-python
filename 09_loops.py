### Loops ###

'''while
my_conditions = 0
while my_conditions < 10: # -> se imprime INFINITAMENTE desde el 1 al 10, si quitas la condicion marcada imprimira infinitamente el numero 0 
    my_conditions += 1 # -> esta es la condicion marcada, No quitar esta condicion explota el pc
    print(my_conditions)
'''

my_condition1 = 0
while my_condition1 < 10: # -> Se imprimi INFINITAMENTE desde el 0 al 9, El While se puede utilizar con un else
    print(my_condition1)
    my_condition1 += 1

if my_condition1 == 10:
    print("Mi condicion es igual a 10")
else:
    print("Mi condicion es mayor o igual que 10")

while my_condition1 < 20:
    my_condition1 += 1
    if my_condition1 == 15:
        print("Se detiene la ejecucion")
        break # -> corta el bucle

    print(my_condition1)


print("La ejecucion continua")


# For -> Sirve para iterar, se repite tanta veces como elementos tengamos iterables.

for_for = [123, 454, 321, 12, "Avion", "Judias"]
una_tupla = (18, 1.75, "Juan", "Tokiño", "Antonio")
un_set = {"Juan", "Antonio", 18}
un_dict = {"Nombre": "Juan", "Apellido": "Perez", "Edad": 18, 1: "avion"}

for element in for_for:
    print(element)

for element1 in una_tupla: # -> imprime la tupla completa
    print(element1)

for element2 in un_set: # -> imprime los valores desorganizados
    print(element2)

for element3 in un_dict: # -> imprime todas las claves
    print(element3)

for element3 in un_dict.values(): # -> imprime todas los valores
    print(element3)
    if element3 == 18:
        continue # -> Continua volviendo al for
    print("Se ejecuta")
else:
    print("El bucle for para diccionario ha finalizado")