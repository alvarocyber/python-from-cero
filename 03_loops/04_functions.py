###
# 04 - Funicones
# Bloques de código que se pueden reutilizar y ejecutar cuando se les llama.
###

""" Definición de una función simple

    def nombre_de_la_funcion(parametro1, parametro2, ...):
        # docstring
        # cuerpo de la funcion
        return valor_de_retorno #opcional
    

"""

def saludar():
    print( "Hola, soy una función" )

saludar() #Llamada a la función

#Ejemplo de función con parámetros y valor de retorno
def saludar_a(nombre:str):
    print( f"Hola, {nombre}" )

saludar_a( "Alvaro" ) #Llamada a la función con parámetro

#Parametros es lo que acepta la función, argumentos es lo que le pasamos a la función

#Funciones con más de un parámetro
def sumar(a:int, b:int) -> int:
    """Suma dos números y devuelve el resultado"""
    return a + b

print(sumar(10,5))

#Documentar las funciones con docstring

def restar(a, b):
    """Resta dos números y devuelve el resultado"""
    return a - b

#Parametros por defecto

def multiplicar(a , b=2):
    return a*b

print(multiplicar(1))



def describir_persona(nombre,edad,sexo):
    print(f"Soy {nombre}, tengo {edad} años y soy {sexo}")

# Parametros preposicionales

describir_persona("alvaro",20,"hombre")

#Argumentos por clave

describir_persona(sexo="masculino",nombre="alvaro",edad=20)

#Argumentos de longitud de variables
def sumar_nums(*args):
    suma = 0
    for num in args:
        suma += num
    return suma

print(sumar_nums(10,2,34,345,35,2345))

#Argumentos de clave-valor variable
def mostrar_info(**kwargs):
    for clave,valor in kwargs.items():
        print(f"{clave}: {valor}")

mostrar_info(nombre="alvaro", edad = 20, sexo = "gato")