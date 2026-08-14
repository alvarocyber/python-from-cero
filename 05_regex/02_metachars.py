###
# 02 - Meta caracteres
#Los metacaracteres son simbolos especiales con significados especificos en las expresiones regulares
###

import re


#1. El punto (.)
#Coincide con cualquier caracter excepto una nueva linea

text = "Hola Mundo. H0la de nuevo, H0la otra vez"
pattern = "H.la"

found = re.findall(pattern,text)
print(found)

text = " casa caasa cosa cisa cesa causa"
pattern = "c.sa"

found = re.findall(pattern,text)
print(found)

# ----------------------------------------------------------------------------------------------------------


text = "Hola Mundo. H0la de nuevo, H$la otra vez"
pattern = r"H.la"

found = re.findall(pattern,text)
print(found)


text = "Mi casa es blanca. Y el coche es negro"
pattern = r"\."

found = re.findall(pattern,text)
print(found)

# Con la barra invertida , lo que hace es quitarle el sentido al punto y convertirlo en caracter

text="El numero de telefono es 1345563463, apuntalo"
find = re.findall(r"\d{9}",text)
print(find)

#Ejemplo detectar un un número con prefijo de españa

text = "Aqui tienes mi numero apuntalo +34 123912340"
pattern = r"\+34 \d{9}"

find = re.findall(pattern,text)
print(find)

#\w: Coincide con cualquier caracter alphanumerico

text = "@@@el_rubius_98@"
pattern = r"\w"

find = re.findall(pattern,text)
print(find)

# \s: Coincide con cualquier espacio en blanco

text = "Hola mundo\nComo estas\t"
pattern = r"\s"

find = re.findall(pattern,text)
print(find)

# ^: coincide con el principio de una cadena

text = "123_name"
pattern = r"^\w" #Validador de username

find = re.search(pattern,text)
if find:
    print("El nombre es valido")
else : 
    print("El username no es valido")

phone = "+34 505603523"
pattern = r"^\+\d{1,3} "

valid = re.search(pattern, phone)

if valid:
    print("El telefono es valido")
else : 
    print("El telefono no es valido")

# $: Para mirar si coincide con el final

text = "Hola mundo"
pattern = "mundo$"

valid = re.search(pattern, text)

if valid:
    print("La cadena es valido")
else : 
    print("La cadena no es valido")


# ------------------------------------------------------------------------------------------------------
#Ejemplo validacion de un correo

correo = "alvaorgc@gmail.com"
pattern = r"@gmail.com$"

valid = re.search(pattern, correo)

if valid:
    print("El correo es valido")
else : 
    print("El correo no es valido")

# ---------------------------------------------------------------------------------------------------------

#\b: coincide con el principio o final de una palabra

text = "casa cascada casado"
pattern = r"\bcasa\b"

valid = re.findall(pattern, text)

print(valid)

# |: Coincidir con una opcion u otra

fruits = "platano, manzana, aguacate, palta, pera"
pattern = r"palta|aguacate|p..a| \b\w{7}\b"

matches = re.findall(pattern,fruits)
print(matches)