"""Ejercicios para la carpeta 03_loops

Genera ejercicios que cubran los conceptos vistos en:
- 01_loop_while.py
- 02_loop_for.py
- 03_range.py
- 04_functions.py

Cada ejercicio incluye problemas de completar, detectar errores y escribir código.
"""

# Ejercicio 1: Completa el bucle while
# ------------------------------------
# El siguiente código debe sumar todos los números positivos ingresados
# por el usuario hasta que el usuario escriba '0'. Completa el bloque faltante.

# total = 0
# while True:
#     numero = int(input("Ingresa un número (0 para terminar): "))
#     if numero == 0:
#         break
#     # COMPLETA AQUÍ: actualiza el total con el número ingresado
#
# print("Suma total:", total)


# Ejercicio 2: Detecta el error en el bucle for
# ---------------------------------------------
# El siguiente fragmento debe imprimir los números del 1 al 5, pero tiene un error.
# Identifica el problema y escribe la corrección debajo.

# for i in range(1, 5):
#     print(i)

# Corrección:
# for i in range(1, 6):
#     print(i)


# Ejercicio 3: Rellena el código con range()
# ------------------------------------------
# Completa el código para que imprima solo los números pares entre 2 y 10.

# for numero in range(___________):
#     print(numero)


# Ejercicio 4: Función con bucle while
# -----------------------------------
# Escribe una función llamada 'contar_descendente' que reciba un número entero 'n'
# y devuelva una lista con los números desde 'n' hasta 1 usando un bucle while.
# Ejemplo: contar_descendente(4) -> [4, 3, 2, 1]

# def contar_descendente(n):
#     resultados = []
#     ____________
#     while n > 0:
#         resultados.append(n)
#         n -= 1
#     return resultados


# Ejercicio 5: Detecta el error en la función
# -------------------------------------------
# El siguiente código intenta retornar la suma de los números de una lista,
# pero tiene un error lógico. Encuentra el error y corrige la función.

# def suma_lista(numeros):
#     total = 0
#     for numero in numeros:
#         total += numero
#     return total
#
# lista = [1, 2, 3, 4]
# print(suma_lista(lista))  # Debe imprimir 10


# Ejercicio 6: Completa el bucle y la función
# -------------------------------------------
# Escribe una función 'multiplica_pares' que reciba una lista de números
# y devuelva una nueva lista con cada número par multiplicado por 2.
# Usa un bucle for.

# def multiplica_pares(numeros):
#     resultado = []
#     for numero in numeros:
#         if numero % 2 == 0:
#             resultado.append(numero * 2)
#     return resultado


# Ejercicio 7: Ejercicio combinado
# -------------------------------
# Usa un bucle for y la función range() para crear una lista con los
# cuadrados de los números del 1 al 7.

# cuadrados = []
# for i in range(1, 8):
#     cuadrados.append(i * i)
# print(cuadrados)  # Debe imprimir [1, 4, 9, 16, 25, 36, 49]


# Ejercicio 8: Rellena el código con un bucle for anidado
# ------------------------------------------------------
# Completa el siguiente código para imprimir una tabla de multiplicar
# de 1 a 3. El resultado debe verse así:
# 1 x 1 = 1
# 1 x 2 = 2
# ...

# for a in range(1, 4):
#     for b in range(1, 4):
#         print(f"{a} x {b} = {a * b}")


# Ejercicio 9: Detecta el error de indentación
# -------------------------------------------
# El siguiente código debe contar hasta 3 y luego imprimir "Listo".
# Encuentra el error de indentación.

# contador = 1
# while contador <= 3:
#     print(contador)
#     contador += 1
# print("Listo")


# Ejercicio 10: Crea una función con parámetros y bucle
# ---------------------------------------------------
# Escribe una función 'generar_multiplos' que reciba dos parámetros:
# 'n' y 'cantidad'. La función debe devolver una lista con los primeros
# 'cantidad' múltiplos de 'n'. Usa un bucle for.

# def generar_multiplos(n, cantidad):
#     multiplos = []
#     for i in range(1, cantidad + 1):
#         multiplos.append(n * i)
#     return multiplos
#
# print(generar_multiplos(3, 5))  # Debe imprimir [3, 6, 9, 12, 15]
