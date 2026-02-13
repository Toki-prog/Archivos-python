# Esto es un comentario: Hola mundo
print("Hola, Python!") #-> lo que esta dentro del parentesis es una cadena de texto, se puede usar con un comillas simple.
print('Hola, Python!')

"""
Este es un 
comentario
en varias lineas
"""

'''
Este tambien es un 
comentario
en varias lineas
'''

#Consulta del tipo de dato.
print(type("Soy un dato Str")) #String -> Es un dato de cadena de texto.
print(type(10)) #Int -> Es un dato numero entero
print(type(10.2)) #Float -> Es un dato numero decimal
print(type(1 + 3j)) #Complex -> Es un dato numero complejo
print(type(True)) #Bool -> Es un valor booleano, valores booleano son True y False

print(type(print("Mi cadena de texto"))) #NoneType -> Es un tipo de dato que representa la ausencia de valor, se obtiene cuando una función no retorna nada.