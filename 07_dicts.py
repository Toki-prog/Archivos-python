### Diccionarios ###

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Nombre":"Juan", "Apellido":"Perez", "Edad":18, 1:"Python"} #-> su sintaxis es {'clave1':'valor1', 'clave2':'valor2'}.

my_dict = {
    "Nombre": "Lextter",
    "Apellido": "Perez",
    "Edad": 15,
    "Lenguajes": {"Python", "Html", "CSS"}, # -> Tiene un valor Set.
    1:1.69
}

print(my_other_dict)
print(my_dict)

print(len(my_other_dict)) 
print(len(my_dict)) # -> En este caso len() cuenta cuantas clave tiene el diccionario.

#Buscando en un diccionario
print(my_dict["Lenguajes"]) # -> Aqui le pasamos la clave 

#Cambiando valor
my_dict["Lenguajes"] = "Ingles"
print(my_dict["Lenguajes"])

#Agregando clave
my_dict["Calle"] = "Los alcarrizos"
print(my_dict)

#Eliminando Clave
del my_dict["Calle"]
print(my_dict)

#Verificando si un elemento esta en el diccionario 
print("Lextter" in my_dict) # -> Da false, por que con esta forma estamos buscando Claves no valores

#Probando funciones de los diccionarios
print(my_dict.items()) # -> Retorna un listado con cada uno de los items
print(my_dict.keys()) # -> Retorna un listado con las claves
print(my_dict.values()) # -> Retorna un listado con los valores

my_list = ["Nombre", 6, "Hipo"]

new_dict = dict.fromkeys((my_list)) # -> Crea un diccionario nuevo sin valores, Lo mas correcto seria usar dict, en ves de una diccionario en uso.
print(new_dict)
print(dict.fromkeys(("Nombre", 6, "Hipo"))) # -> Es exactamente lo mismo
new_dict = dict.fromkeys(my_dict) # -> Es como una copia del diccionario pero se queda con las claves.
print(new_dict)
new_dict = dict.fromkeys(my_dict, "Goku")
print(new_dict)

print(list(new_dict.values()))
print(tuple(new_dict))
print(set(new_dict))