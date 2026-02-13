### Sets ###

my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set)) # -> Aqui te dice que es un diccionario.

my_other_set = {"Juan", "Perez", 18, "ITLA"}
print(type(my_other_set)) # -> Aqui ya se imprime como un Set.

print(len(my_other_set))

my_other_set.add("Antonio") # -> Agregar un elemento a la lista.
my_other_set.add(10)
print(my_other_set) # -> Un set no es una estructura ordenada.

my_other_set.add("Antonio") # -> Un set no admite repetidos
my_other_set.update(["Avion", "Jose", "Busy"]) # -> si nombras la funcion sin lo corchetes, pone los elementos por letra.
my_other_other_set = {"Joel", 12}
my_other_other_set.update("radio") # -> este elemento en la consola se ve letra por letra.

print(my_other_set) 
print(my_other_other_set)

print("Juan" in my_other_set)
print(11 in my_other_set)

my_other_set.remove("Antonio")
print(my_other_set)

my_other_set.clear() # -> Borra todos los elementos del set.
print(len(my_other_set))

num_12 = my_other_other_set.discard(12)
print()
print(my_other_other_set)

del my_other_set
#print(my_other_set) -> NameError: name 'my_other_set' is not defined.

my_set = {"Juan", "Perez", 18, "ITLA"}
my_list = list(my_set)
print(my_list)
print(my_list[3])

my_other_set = {"IA", "Mates", "Computadoras"}

my_new_set = my_set.union(my_other_set)
print(my_new_set.union({"Dune", "Homero"})) # -> Si le quieres agregar mas informacion en adelante al set, acuerdate siempre usar {}.

print(my_new_set.difference(my_set))#-> Aqui estamos quitandole elementos de 'my_set'.
