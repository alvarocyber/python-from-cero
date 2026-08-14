###
# 01 - Expresiones Regulares
#

"""
 Las expresiones regulares son una secuencia de caracteres que forman un patron de busqueda
 Se utilizan para la busqueda de cadenas de texto, validación de datos, etc...
"""


#Siempre primero importar re
import re

# Crear un patron, que es una cadena de texto que describe lo que queremos encontrar

patron = "Hola"

# El texto donde vamos a buscar
text = "Hola mundo"

#Usar la fucion search
result = re.search(patron,text)

if result:
    print("Se ha encontrado patron")
else:
    print("No se ha encontrado")

#Devuelve la cadena que coincide con el patron
print(result.group())

#.start devuelve donde empieza el patron
print(result.start())

#.end indica donde acaba el patron
print(result.end())

#Ejemplo: Encuenta la primera ocurrencia de la palabra IA en el siguiente texto, e indica en que posicion empieza y termina

text = "Todo el mundo dice que la IA nos va a quitar el trabajo. Pero solo hace falta ver como la puede cagar" \
"con las regex para ir con cuidado"

pattern = "IA"

found = re.search(pattern,text)

if found:
    print(f"Se ha encontrado el patron entre las posiciones {found.start()} y  {found.end()}")
else:
    print("No se ha encontrado el patron")

#Encontrar todas las coincidencias de un patron, para ello el .findall() devuleve una lista con todas ellas

text = "Me gusta Python. Python es lo máximo. Aunque Python no es tan dificil, ojo con Python"
pattern = "Python"

find = re.findall(pattern,text)
print(len(find))

# -------------------------------------------------------------------------------------------

#Iter() devuelve un iterador que contiene todos los resuktados de la busqueda

text = "Me gusta Python. Python es lo máximo. Aunque Python no es tan dificil, ojo con Python"
pattern = "Python"

finds = re.finditer(pattern,text)

for find in finds:
    print(find.group(), find.start(), find.end())

#Modificadores

#Los modificadores son opciones que se pueden agregar para cambiar su comportamiento
text = "Todo el mundo dice que la IA nos va a quitar el trabajo. Pero la Ia no es tan mala. ¡VIVA la ia!"

pattern = "IA"

found = re.findall(pattern,text,re.IGNORECASE)

if found:
    print(found)
else:
    print("No se ha encontrado el patron")

#Reemplazar texto

text = "Hola mundo. Hola de nuevo"
pattern = "Hola"
replacement = "Adios"

new_text = re.sub(pattern, replacement,text)
print(new_text)