#### Tuplas ####
#Las tuplas son inmutables.

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (18, 1.74,"Antonio","Juan", "Juan")
my_other_tuple = (18, 19, 25, 76)


print(my_tuple)
print(type(my_tuple))

print(my_tuple[-1])
print(my_tuple[-2])
print(my_tuple[2])
print(my_tuple[1])

print(my_tuple.count("Juan"))
print(my_tuple.count("19"))

#my_tuple[1] = 19 -> Las tuplas no permiten cambio de variables.


my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

print(my_sum_tuple[3:6])

my_tuple = list(my_tuple)
print(type(my_tuple))

my_tuple[4] = "ITLA"
my_tuple.insert(1, "Marron")
my_tuple = tuple(my_tuple) # -> Es importante reasignar los valores para desconvertirlos o convertirlos.
print(my_tuple)
print(type(my_tuple))

del my_tuple # -> elimina la tupla.
print(my_tuple)