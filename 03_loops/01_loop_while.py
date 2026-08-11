###
# 01 - Bucles (while)
# Permiten ejecutar un bloque de código mientras se cumpla una condición.
###
import os
os.system("cls")

print( "\nBucle while: " )

#Bucle simpre con condición
contador = 0
while contador < 5:
    print( "Contador: ", contador )
    contador += 1

print( "\nBucle while con break: " )
count = 0

while count <= 100:
    print( "Contador: ", count )
    count += 1
    if count % 5 == 0:
        print( "Contador es múltiplo de 5" )
        break

#continue: permite saltar a la siguiente iteración del bucle
print( "\nBucle while con continue: " )
contador = 0

while contador < 10:
    contador += 1
    if contador % 2 == 0:
        continue

    print( "Contador impar: ", contador )

#else, cuando se ejecuta?

print( "\nBucle while con else: " )
contador = 0
while contador < 5:
    print( "Contador: ", contador )
    contador += 1
else: #Solo se ejecuta cuando no se pueda meter en el bucle
    print( "Bucle finalizado" )

#Pedirle al ususario un numero que debe de ser positivo, si no lo es, volver a pedirlo
numero = -1
while numero < 0:
    numero = int(input( "Introduce un número positivo: " ))
    if numero < 0:
        print( "El número no es positivo, vuelve a intentarlo" )


print( f"El número introducido es {numero}" )

#Try/Except: permite capturar errores y manejarlos
#Pedirle al ususario un numero que debe de ser positivo, si no lo es, volver a pedirlo
numero = -1
while numero < 0:
    try:
        numero = int(input( "Introduce un número positivo: " ))
        if numero < 0:
            print( "El número no es positivo, vuelve a intentarlo" )
    except ValueError:
        print( "El valor introducido no es un número, vuelve a intentarlo" )
        continue



print( f"El número introducido es {numero}" )