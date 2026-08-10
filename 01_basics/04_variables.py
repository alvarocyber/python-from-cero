###
## 04_variables.py
# Aqui lo que hacemos es mirar como funcionan las variables en Python
# Para ello hacemos diferentes pruebas con las variables y sus operaciones
###

my_name =  "Alvaro"
print(type(my_name))

age = 20
print(age)

age = 19
print(age)

#Es de tipado dinamico, no hace falta declarar el tipo de variable, Python lo hace automáticamente

my_name =  32
print(type(my_name))

#Es de tipado fuerte, no se puede cambiar el tipo de variable, Python no lo permite
print(f"Hola, mi nombre es {my_name} y tengo {age+1} años")#Permite concatenar variables de diferentes tipos, pero no permite cambiar el tipo de variable
#No recomendada forma de asignar variables,
name,age,city="Alvaro",20,"Madrid"
print(f"Me llamo {name}, tengo {age} años y vivo en {city}")

#Convenciones de variable
mi_nombre_de_variable = "Alvaro" #snake_case
miNombreDeVariable = "Alvaro" #camelCase, no suele
miNombreDeVariable123 = "Alvaro" #PascalCase, no suele

Mi_CONSTANTE = 3.1416 #Upper case para determinar constantes, no suele cambiar

#nombres no validos de variables
#1nombre = "Alvaro" #No puede empezar por un numero
#mi nombre = "Alvaro" #No puede tener espacios
#mi-nombre = "Alvaro" #No puede tener guiones

is_user_logged_in: bool = True #Booleano, suele empezar por is_ o has_
print(is_user_logged_in) #Python es de tipado dinamico, no hace falta declarar el tipo de variable, Python lo hace automáticamente
#Lo que hace es anotar el tipo de variable, pero no lo impide, es decir, se puede cambiar el tipo de variable

is_user_logged_in = 42
print(is_user_logged_in) #Python es de tipado dinamico, no hace falta declarar el tipo de variable, Python lo hace automáticamente
#Podemos cambiarlo en las preferencias del editor para que nos avise si cambiamos el tipo de variable, pero no lo impide, es decir, se puede cambiar el tipo de variable

my_name: str = "Alvaro" #String, suele empezar por my_
print(my_name) #Python es de tipado dinamico, no hace falta declarar el tipo