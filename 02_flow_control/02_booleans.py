###
#02- Booleans
# Valores logicos: True y False
# Fundamentales para el control de flujo y lógica 
###

print("Valores booleanos basicos")
print(True)
print(False)

print("\nOperadores de comparacion")
print("5 > 3:", 5 > 3)
print("5 < 3:", 5 < 3)
print("5 >= 5:", 5 >= 5)
print("5 <= 3:", 5 <= 3)
print("5 == 5:", 5 == 5)
print("5 != 3:", 5 != 3)

print("\nComparacion de cadenas")
print("'manza' < 'pera':", "manza" < "pera")
print("'manza' > 'pera':", "manza" > "pera")
print("'manza' == 'manza':", "manza" == "manza")
print("'Hola' != 'Hola':", "Hola" != "Hola")
"""Es lexicografica, compara letra por letra, si la primera letra es igual, pasa a la siguiente y asi sucesivamente"""

print("\nOperadores logicos")
print("True and True:", True and True)
print("True and False:", True and False)
print("False and False:", False and False)
print("True or True:", True or True)
print("True or False:", True or False)
print("False or False:", False or False)
print("not True:", not True)
print("not False:", not False)

print("\nTabla de verdad")
print("and:")
print("A | B | A and B")
print("T | T |", True and True)
print("T | F |", True and False)
print("F | T |", False and True)
print("F | F |", False and False)

print("\nor:")
print("A | B | A or B")
print("T | T |", True or True)
print("T | F |", True or False)
print("F | T |", False or True)
print("F | F |", False or False)

print("\nnot:")
print("A | not A")
print("T |", not True)
print("F |", not False)