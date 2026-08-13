###
#
#
#
###

def count_carnivore_dinosaurs_eggs(egg_list) -> int:
    """
    Es una función que recibe una lista de numeros enteros que representan la cantidad de huevos que han puesto
    diferentes dinosaurios en el parque jurasico y los de numero par son de carnivoros. Devuelve un número con la 
    suma de todos los huevos de carnivoro
    """

    total = 0

    for num in egg_list:
        if num % 2 == 0:
            total += num

    return total

lista = [1,234152,3452345,345,26235,2345,72,45,234,5236]
print(count_carnivore_dinosaurs_eggs(lista))