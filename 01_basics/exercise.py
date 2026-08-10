# Ejercicios: conceptos básicos de Python
# Temas: print, tipos, conversiones, variables e input.
#
# Resuelve cada ejercicio debajo de su enunciado. Los fragmentos que contienen
# errores están comentados para que el archivo siga pudiendo ejecutarse.


# -----------------------------------------------------------------------------
# 1. print()
# -----------------------------------------------------------------------------

# 1) Escribe un print que muestre exactamente: Hola, Python!


# 2) Muestra las palabras "Python", "es" y "genial" separadas por " - ".


# 3) Completa el código para que se imprima en una sola línea:
#    Estoy aprendiendo Python
# print("Estoy aprendiendo", end=___)
# print("Python")


# 4) Predice la salida antes de ejecutarlo:
# print("A", "B", "C", sep="*")


# -----------------------------------------------------------------------------
# 2. Tipos de datos
# -----------------------------------------------------------------------------

# 5) Indica qué tipo devolverá type() en cada caso. Después compruébalo
#    descomentando los print.
# print(type(25)) 
# print(type(3.5)) 
# print(type("25")) 
# print(type(True))
# print(type(None))
# print(type(2 + 4j))


# 6) Crea una variable de cada tipo: int, float, str, bool y NoneType.
#    Imprime el tipo de todas ellas con type().


# 7) ¿Cuál de estas expresiones produce un booleano? Explica por qué.
# a) "False"
# b) False
# c) 4 == 4


# -----------------------------------------------------------------------------
# 3. Conversión de tipos (casting)
# -----------------------------------------------------------------------------

# 8) Completa los huecos para que el resultado sea el número 102 (int).
# texto_numero = "100"
# resultado = ___(texto_numero) + 2
# print(resultado)


# 9) Convierte "8.75" a float, súmale 1.25 e imprime el resultado.


# 10) Detecta y corrige el error. ¿Por qué ocurre?
# edad = "20"
# print(edad + 1)


# 11) Sin ejecutar, predice los resultados y después compruébalos:
# print(int(9.99))
# print(bool(0))
# print(bool(""))
# print(bool("Python"))


# -----------------------------------------------------------------------------
# 4. Variables y f-strings
# -----------------------------------------------------------------------------

# 12) Crea las variables nombre, edad y ciudad. Usa un f-string para mostrar:
#    Me llamo <nombre>, tengo <edad> años y vivo en <ciudad>.


# 13) Corrige los nombres de variable no válidos:
# 1nombre = "Ana"
# mi ciudad = "Madrid"
# mi-nombre = "Ana"


# 14) ¿Qué mostrará este código? Razona por qué Python permite hacerlo.
# dato = "hola"
# dato = 10
# print(type(dato))


# 15) Asigna en una sola línea los valores "Lucía", 21 y "Sevilla" a las
#    variables nombre, edad y ciudad. Después imprímelas con un f-string.


# 16) Crea una constante llamada PI con el valor 3.1416 e imprime su valor.
#    Recuerda la convención de nombres para constantes.


# -----------------------------------------------------------------------------
# 5. input()
# -----------------------------------------------------------------------------

# 17) Pide al usuario su nombre y salúdalo con: Hola, <nombre>!


# 18) Pide al usuario su edad. Convierte el dato a int e indica cuántos años
#    tendrá dentro de 10 años.


# 19) Detecta y corrige el error:
# numero = input("Introduce un número: ")
# print(numero + 5)


# 20) Pide en una sola entrada el país y la ciudad, separados por un espacio.
#    Guarda ambos valores en dos variables usando split() e imprime:
#    Vives en <ciudad>, <país>.


# Reto final:
# Crea un pequeño programa que pida nombre, edad y ciudad. Debe mostrar una
# frase con esos datos y la edad que tendrá la persona dentro de 5 años.
