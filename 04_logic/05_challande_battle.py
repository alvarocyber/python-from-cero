"""
Reto: batalla de listas

Dos jugadores comparan sus números por parejas. El número mayor gana la ronda
y la diferencia se añade al siguiente número de su propia lista. Gana quien
vence en la última ronda, indicando también la diferencia de esa ronda.
"""


def batalla(lista_1, lista_2):
    """Devuelve el ganador de la última ronda y su diferencia."""

    # Copias para no modificar las listas originales.
    ganador = "Empate"
    ultima_diferencia = 0

    for indice in range(len(lista_1)):
        numero_1 = lista_1[indice]
        numero_2 = lista_2[indice]
        diferencia = abs(numero_1 - numero_2)

        if numero_1 > numero_2:
            ganador = "Jugador 1"
            ultima_diferencia = diferencia
            if indice + 1 < len(lista_1):
                lista_1[indice + 1] += diferencia
        elif numero_2 > numero_1:
            ganador = "Jugador 2"
            ultima_diferencia = diferencia
            if indice + 1 < len(lista_2):
                lista_2[indice + 1] += diferencia
        else:
            ganador = "Empate"
            ultima_diferencia = 0

    return ganador, ultima_diferencia


lista_jugador_1 = [3, 4, 2, 8]
lista_jugador_2 = [2, 7, 6, 4]

ganador, diferencia = batalla(lista_jugador_1, lista_jugador_2)
print(f"Ha ganado: {ganador}")
print(f"La última diferencia ha sido: {diferencia}")
