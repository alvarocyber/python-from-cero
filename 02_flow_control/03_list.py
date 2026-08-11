###
#03- Listas
# Secuencias mutables de elementos
# Pueden contener elementos de cualquier tipo, incluso otras listas
###
import os
os.system("cls")

print("\nCrear listas")
lista1 = [1, 2, 3, 4, 5]
lista2 = ["a", "b", "c", "d"]
lista3 = [1, "a", 2.5, True]
lista3: list[int|str|float|bool]  #Lista con anotacion de tipos

lista_vacia = []
lista_de_listas = [[1, 2], ["a", "b"], [True, False]]
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(lista1)
print(lista2)
print(lista3)
print(lista_vacia)
print(lista_de_listas)
print(matrix)

#Acceso a elementos de la lista por indice
print("\nAcceso a elementos de la lista por indice")
print(lista1[0])  # Primer elemento
print(lista1[-1])  # Último elemento
print(lista2[-2])  # Penúltimo elemento

print(lista_de_listas[1][0])

#Slicing de listas
print("\nSlicing de listas")
lista1 = [1, 2, 3, 4, 5]
print(lista1[1:4])  # Elementos desde el índice 1 hasta el 4
print(lista1[:3])  # Elementos desde el inicio hasta el índice 3
print(lista1[3:]) # Elementos desde el índice 2 hasta el final
print(lista1[:])  
print(lista1[::3])  # Elementos desde el inicio hasta el final, saltando de 3 en 3
print(lista1[::-1])  # Elementos desde el final hasta el inicio (inverso)

#Modificar una lista

lista1[0] = 10
print(lista1)

#Añadir elementos a una lista (forma 1)
lista1 = lista1 + [6, 7, 8]
print(lista1)

#Añadir elementos a una lista (forma 2)
lista1+= [9, 10]
print(lista1)

#Recuperar el tamaño de una lista
print("\nRecuperar el tamaño de una lista")
print(len(lista1))  # Devuelve el número de elementos en la lista