# Variables
 
my_string_variable = "My String variable"
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = False
print(my_bool_variable)

#Concatenacion de variables en un print
print(my_string_variable, my_int_to_str_variable, my_bool_variable)
print("Me gusta mucho el arroz:",my_bool_variable)

#Algunas funcion del sistema
print(len(my_string_variable))

#Variables en una sola linea, Esto es una mala practica NO HACERLO.
name, surname, alias, edad = "Juan", "Perez", "Tokiño", 18
print("Mi nombre es:",name, surname,",", "Mi edad es:",edad, "Y no me gusta que me llamen", alias)

#Inputs
primer_nombre = input("Escribe tu primer nombre: ")
edad = input("Que tan viejo eres?: ")

print(primer_nombre)
print(edad)

# Cambiamos su tipo
name = 35
edad = "Juan"
print(name)
print(edad)

# Forzamos el tipo?
address: str = "Mi direccion"
address = True
address = 5
address = 1.2
print(type(address))