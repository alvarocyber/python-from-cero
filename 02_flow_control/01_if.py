###
#01- Sentencias condicionales
# Permiten ejecutar blqoyes de codigo solo si se cumle x funcion
###
import os

os.system("cls")

print("Sentencias condicionales")

edad = 22

if edad >= 18:
    print("Enhorabuena, eres mayor de edad, a por el A2")
elif edad < 17:
    print("Puedes sacarte el AM")
else:
    print("Puedes sacarte el A1, eso es poque eres >= a 16")

nota = 10
print("\nSentencia con if-elseif")

if nota >= 9:
    print("¡Enhorabuena! Has sacado un sobresaliente")
elif nota >= 7:
    print("Tienes un notable, buen trabajo")
elif nota >= 6:
    print("Es un aceptable, sigue dandole caña")
elif nota >=5:
    print("Aprobado, pero no te confies")
else:
    print("No te vengas abajo")

tienes_carnet = True

print("\nSentencia con if-else con and")
###Tienen que cumplir ambos requisitos

if edad >= 16 and tienes_carnet:
    print("Puedes conducir moto")
else:
    print("Policia!!!!!!")

print("\nSentencia con if-else con or")
###Solo necesitas cumplir 1 requisito

if edad >= 16 or tienes_carnet:
    print("Puedes conducir")
else:
    print("Paga al poli")

es_finde = False

# Not -> !
if not es_finde:
    print("Tienes que trabajar\n")

tienes_dinero = True
if edad >=18:
    if tienes_dinero:
        print("puedes pasar a la disco")
    else:
        print("Trabaja")
else:
    print("Jodete y espera")

numero = 5
if numero:
    print("\nEl numero es distinto de 0")

nombre = "Juan"
if nombre:
    print("\nEl nombre no esta vacio")

numero = 3#Asignacion de valor
es_tres= numero == 3 #Comparacion de igualdad

if es_tres:
    print("\nEl numero es 3")

print("\nLa condicion ternaria:")
#Forma concisa de un if-else en una sola linea
#[Código si cumple la condicion] if [condicion], else [codigo si no cumple]

edad = 21
print("\nEs mayor de edad" if edad >= 18 else "Es menor de edad")
