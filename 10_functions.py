### Functions ###

def my_functions (): # -> Se utiliza def para definir una funcion.
    print("Esto es una funcion")

my_functions()


def sum_two_values(firt_values: int, second_values): # -> Lo que esta dentro del parentesis se llama parametros.
    print(firt_values + second_values)

sum_two_values(5, 10)
sum_two_values('5', '10') # -> Son cadenas de textos.
sum_two_values(.31, 3.1) 

guard_var = sum_two_values(.31, 3.1) # -> Aqui tambien puedes guardar el resultado dentro de una variable
print(guard_var) # -> Esto no retorna nada. 

def sum_two_values_with_return(firt_values, second_values): # -> Esta funcion retorna el valor, por eso no se imprime en la consola, nos permite guardarlo dentro de una variable
    return firt_values + second_values

my_result = sum_two_values_with_return(6, 7) # -> Aqui guardamos dentro de una variable lo retornado
print(my_result) # -> Aqui imprimimos en la consola el resultado.

def another_sum_two_with_return(first, second):
    my_sum = first + second
    return my_sum

my_sum = another_sum_two_with_return(12, 123)
print(my_sum)

def print_name (name, surname):
    print(f"{name} {surname}")

print_name(surname="Juan", name="Dolio") # -> Aqui estamos definiendo como se llama cada cosa
print_name("Juan", "Dolio") # -> Aqui no lo definimos

def print_name_with_default (name, surname, alias = "Sin alias"): # -> Aqui ponemos un parametro por defecto
    print(f"{name} {surname} {alias}")

print_name_with_default("Juan", "Perez") 
print_name_with_default("Juan", "Perez", "Con alias") 

def print_texts(*text): # -> como pusimo el asterisco al principio, esto dice que podemos poner lo que nos de la gana
    print(text)

print_texts("Holaa", "Python", "Juan", 1, 43)

def print_upper_texts(*texts):
    for text in texts:
        print(text.upper())

print_upper_texts("Holaa", "Python", "Juan")