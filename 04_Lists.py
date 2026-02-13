### Lists ###

my_list = list()
my_other_list = []

print(len(my_list))

my_list = [18, 24, 62, 30, 30, 45, 12]


print(my_list)
print(len(my_list))

my_other_list = [18, 1.70, "Juan", "Perez"] 

print(type(my_other_list))

print(my_other_list[0]) # -> accede al primer elemento de la lista.
print(my_list[-1]) # -> es la forma mas rapida de acceder al ultimo elemento.
print(my_list.count(30)) # -> Busca elementos dentro de la lista.
#print(my_other_list[4]) IndexError.

print(my_other_list.index("Perez")) # -> Busca el indice del elemento sea lista o tupla.

age, height, name, surname = my_other_list # -> Para desempaquetar los elementos de la lista necesita las misma variables a segun de los elemetos de la lista.
print()

name, height, age, surname = my_other_list[1], my_other_list[0], my_other_list[3], my_other_list[2] # -> Malas practicas.
print(name)

print(my_list + my_other_list) 
print(my_other_list + my_list)

my_other_list.append("Itla") # -> agrega en la ultima posicion un elemento.
print(my_other_list)

my_other_list.insert(1, "Azul")  # -> Inserta un elemento en un indice especifico.
print(my_other_list)

my_other_list[1] = "Rojo"
print(my_other_list)

my_list.remove(30) # -> Elimina la primera ocurriencia del elemento especificado. Lanza ValueError si no existe.
print(my_list)

print(my_list.pop()) # -> Elimina y retorna el elemento en la posicion especificada (ultimo por defecto).

print(my_list.pop())

my_pop_element = my_list.pop(2) # -> Aqui estaba probando el pop haciendo que el ultima elemento este en otra variable.
print(my_pop_element)
print(my_list)

del my_list[2] # -> Elimina por indice.
print(my_list)

my_new_list = my_list.copy() # -> Retorna una copia superficial de la lista.

my_list.clear() # -> Vacea la lista.
print(my_list)
print(my_new_list)

my_new_list.reverse() # -> Le da la vuelta a la lista.
print(my_new_list)

my_new_list.sort() # -> Ordena automaticamente de menor a mayor. Dentro de sort(key=algo reverse=True o False).
print(my_new_list)

print(my_new_list[1:]) # -> Lista Rebanada secuencia[inicio:final:paso].

my_list = "Hola Python"
print(my_list)
print(type(my_list))