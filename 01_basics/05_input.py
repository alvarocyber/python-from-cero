###
## 05_input.py
# La funcion input() nos permite leer datos desde la entrada estándar (teclado)
# La función input() devuelve una cadena de texto (str)
###

name = input("Introduce tu nombre:\n")
print(f"Hola, {name}!, encantado de conocerte.")

age = input("Introduce tu edad:\n")
age = int(age)
print(f"Dentro de 20 años tendras {age+20} años.")

print("Obtener multiples valores a la vez")
county,city = input("Introduce tu pais y ciudad:\n").split()#Lo que hace es detectar la separacion por espacios y lo devuelve en una lista, que luego se puede desempaquetar en varias variables
print(f"Vives en {city}, {county}.")