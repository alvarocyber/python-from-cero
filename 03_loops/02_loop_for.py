###
# 02 - Bucles (for)
# Permiten ejecutar un bloque de código un número determinado de veces.
###
import os 
os.system("cls")

print( "\nBucle for: " )

#Iterar sobre una lista
frutas = ["manzana", "banana", "cereza"]
for fruta in frutas:
    print( "Fruta: ", fruta )

#Iterar sobre cualquier cosa iterable
cadena = "alvarocyber"
for caracter in cadena:
    print( "Caracter: ", caracter )

#enumerate: permite obtener el índice de cada elemento
frutas = ["manzana", "banana", "cereza"]
for indice, fruta in enumerate(frutas): #Importante siempre primero el indice, luego valor
    print( f"Fruta {indice}: {fruta}" )

#Bucles anidados
print( "\nBucle for anidado: " )
letras = ["A", "B", "C"]
numeros = [1, 2, 3]

for letra in letras:
    for numero in numeros:
        print( f"{letra}{numero}" )

print( "\nBreak:" )
#break: permite salir del bucle
animales = ["perro", "gato", "conejo", "pez"]
for idx, animal in enumerate(animales):
    print( f"Animal {idx}: {animal}" )
    if animal == "conejo":
        print( f"Se ha encontrado un conejo en la posición {idx}, saliendo del bucle" )
        break

print( "\nContinue: " )
#continue: permite continuar con la siguiente iteración del bucle
animales = ["perro", "gato", "conejo", "pez"]
for idx, animal in enumerate(animales):
    if animal == "conejo":
        continue
    print( f"Animal {idx}: {animal}" )

#Comprensión de listas: permite crear una lista a partir de otra lista
print( "\nComprensión de listas: " )
animales = ["perro", "gato", "conejo", "pez"]
animales_mayusculas = [animal.upper() for animal in animales]
print( "Animales en mayúsculas: ", animales_mayusculas )

#Muestra los numeros pares de una lista
pares = [num for num in range(10) if num % 2 == 0]
print( "Números pares: ", pares )