### Strings ###

text = "Mi texto"
text1 = 'Mi otro texto'

# Calcular la longitud de un string, cuenta cuantos elementos hay en algo.
print(len(text))
print(len(text1))

# Concatenar strings
print(text + " " + text1)

# Escape sequences en Strings
#\n: Nueva linea.
#\t: Tabulacion.
#\\: Ni idea de lo que hace.
#\': Le agrega una comilla al texto.
#\": Le agrega una doble comilla al texto.
new_text = "Este es un string\ncon salto de linea" #\n es un salto de linea.
print(new_text)

back_slash_text = "\\Lo ando probando"
print(back_slash_text)

single_quote_text = "\'Lo ando probando"
print(single_quote_text)

double_quote_text = "\"Lo ando probando"
print(double_quote_text)

tab_text = "\tQuiero comida"
print(tab_text)

scape_text = "\\tQuiero comida \n arroz"
print(scape_text)

# Formateo
#Formateo viejo
# %s -> String o cualquier objeto que represente un string, como un numero.
# %d -> Enteros.
# %f -> Numeros decimales.
ser, tecnologo, edad  =  "soy", "tecnologo de IA", 20

print("Hola soy Juan y {} {} y mi edad es {}".format(ser, tecnologo, edad)) #-> El metodo format() se utiliza para formatear cadenas de texto, permite insertar valores en una cadena de texto utilizando marcadores de posición.
print("Hola soy Juan y %s %s y mi edad es %d" %(ser, tecnologo, edad)) #-> El operador % se utiliza para formatear cadenas de texto, permite insertar valores en una cadena de texto utilizando marcadores de posición.
print(f"Hola soy Juan y {ser} {tecnologo} y mi edad es {edad}") #-> Las f-strings (formatted string literals) son una forma de formatear cadenas de texto introducida en Python 3.6, permiten insertar valores en una cadena de texto utilizando llaves {}. 

# Desempaquetado de caracteres
language = "python"
a, b, c, d, e, f = language
print(a)
print(b)

# Division
#El slice o rebanado en Python es una forma de extraer partes de secuencias como listas, tuplas o strings, funciona con la sintaxis [inicio:fin:paso]
#secuencia[inicio:fin]
language_slice = language[1:3]
print(language_slice)

language_slice = language[1:]
print(language_slice)

language_slice = language[-2]
print(language_slice)

language_slice = language[0:6:2]
print(language_slice)

# Reverse 
reverse_hint = "mi mama me mima"
print(reverse_hint[::-1])

reverse_language = language[::-1]
print(reverse_language)

#Funciones
print(language.capitalize()) # ->Pone la primera letra mayuscula.
print(language.upper()) # ->Pone todo en mayuscula.
print(language.count("t")) #-> Cuenta lo que le pongas en el parametro.
print(language.isnumeric()) # -> devuelve un valor booleano si es numerico.
print("1".isnumeric()) 
print(language.lower()) # ->Pone todo en minusculas.
print(language.isupper()) # -> Devuelve True si todas las letras son mayusculas.
print(language.startswith("py")) # -> Devuelve True si el argumento tiene lo mismo de la variable asignada.