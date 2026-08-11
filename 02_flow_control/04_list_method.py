###
#03- Listas Metodos
# Metodos mas importantes de las listas
###

import os
os.system("cls")

lista = [1, 2, 3, 4, 5]

#Añadir o eliminar elementos de una lista

lista.append(6)  # Añade un elemento al final de la lista
print(lista)

lista.insert(2, 20)  # Añade un elemento en la posición especificada
print(lista)

lista.extend([7, 8, 9])  # Añade varios elementos al final de la lista
print(lista)

#Eliminar elementos de una lista
lista.remove(20)  # Elimina la primera ocurrencia del elemento especificado
print(lista)

ultimo = lista.pop()  # Elimina el último elemento de la lista o le pasamos un índice para eliminar un elemento específico
print(lista)
print(f"Elemento eliminado: {ultimo}")

lista.pop(1)
print(lista)

#Elimina a lo vestia
del lista[-1]  # Elimina el elemento en la posición especificada
print(lista)

lista.clear()  # Elimina todos los elementos de la lista
print(lista)

#Eliminar un rango concreto
lista=[1, 2, 3, 4, 5, 6, 7, 8, 9]
del lista[2:5]  # Elimina los elementos desde el índice 2 hasta el índice 4 (5 no incluido)
print(lista)

#Mas metodos
print("\nOrdenar listas modificando la original")
numbers = [5, 2, 9, 1, 5, 6]
numbers.sort()  # Ordena la lista en orden ascendente
print(numbers)

print("\nOrdenar listas modificando la original")
numbers = [5, 2, 9, 1, 5, 6]
sorted_numbers = sorted(numbers)  # Devuelve una nueva lista ordenada sin modificar la original
print(sorted_numbers)

print("\nOrdenar una lista de cadenas de texto (minusculas)")
words = ["banana", "apple", "cherry", "date"]
words_sorted = sorted(words)  # Ordena la lista de cadenas de texto en orden alfabético
print(words_sorted)

print("\nOrdenar una lista de cadenas de texto (minusculas y mayusculas)")
words = ["Banana", "apple", "cherry", "Date"]
sorted_words = sorted(words, key=str.lower)  # Ordena la lista de cadenas de texto ignorando mayúsculas y minúsculas
print(sorted_words)

#Mas metodos utilies
animals = ["dog", "cat", "elephant", "bear"]
print("\n",len(animals))  # Devuelve el número de elementos en la lista
print(animals.count("cat"))  # Devuelve el número de veces que aparece un elemento en la lista
print("cat" in animals)  # Devuelve True si el elemento está en la lista, False en caso contrario
print("hamster" not in animals)  # Devuelve el índice de la primera ocurrencia del elemento en la lista