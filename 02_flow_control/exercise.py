# Ejercicios: control de flujo y booleanos
# Temas: if, elif, else, comparaciones, operadores lógicos y valores booleanos.
# Cuatro ejercicios más completos.

# 1) Calculadora básica
#    Pide al usuario dos números y una operación (+, -, *, /).
#    Imprime el resultado de la operación o un mensaje de error si la
#    operación no es válida o si hay una división por cero.
print("Calculadora básica")
n1,n2 = input("Introduce dos numeros separados por espacio:").split()
n1 = float(n1)
n2 = float(n2)
operacion = input("Introduce la operación (+, -, *, /): ")
if operacion == "+":
    resultado = n1 + n2
    print(f"El resultado de {n1} + {n2} es: {resultado}")
elif operacion == "-":
    resultado = n1 - n2
    print(f"El resultado de {n1} - {n2} es: {resultado}")
elif operacion == "*":
    resultado = n1 * n2
    print(f"El resultado de {n1} * {n2} es: {resultado}")
elif operacion == "/":
    if n2 != 0:
        resultado = n1 / n2
        print(f"El resultado de {n1} / {n2} es: {resultado}")
    else:
        print("Error: División por cero no permitida.")
else:
    print("Error: Operación no válida. Usa +, -, * o /.")
#
# 2) Mayor de dos números
#    Escribe un programa que pida dos números y muestre cuál es mayor.
#    Si ambos son iguales, debe mostrar "Los números son iguales".
print("\nMayor de dos números")
num1,num2 = input("Introduce dos numeros separados por espacio:").split()
num1 = float(num1)
num2 = float(num2)
if num1 > num2:
    print(f"El número mayor es: {num1}")
elif num2 > num1:
    print(f"El número mayor es: {num2}")
else:
    print("Los números son iguales")
#
# 3) Año bisiesto
#    Pide un año al usuario y comprueba si es bisiesto.
#    Un año es bisiesto si es divisible entre 4, pero no entre 100,
#    salvo que también sea divisible entre 400.
#    Imprime "Es bisiesto" o "No es bisiesto".
print("\nAño bisiesto")
year = input("Introduce un año: ")
year = int(year)
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} es bisiesto")
else:
    print(f"{year} no es bisiesto")
#
# 4) Categoriza edades
#    Pide la edad de una persona y muestra su categoría:
#    - "Niño" para edades menores de 12
#    - "Adolescente" para edades de 12 a 17
#    - "Adulto" para edades de 18 a 64
#    - "Anciano" para 65 o más
#    También debe manejar edades negativas con un mensaje de error.
print("\nCategoriza edades")
edad = input("Introduce tu edad: ")
edad = int(edad)

if edad < 0:
    print("Error: La edad no puede ser negativa.")
elif edad < 12:
    print("Categoría: Niño")
elif edad < 18:
    print("Categoría: Adolescente")
elif edad < 65:
    print("Categoría: Adulto")
else:
    print("Categoría: Anciano")
