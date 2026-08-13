###
# Reto 1: Trataremos sobre los 4 fantasticos y debemos de mirar is Red Richars y Johnny Storm estan en alianza para ello,
# debemos de ver si en un texto hay las mismas letras de J como de R
#

def check_is_balance(text:str):
    text= text.upper()

    countR = text.count("R")
    print(f"Hay {countR} R´s")

    countJ = text.count("J")
    print(f"Hay {countJ} J´S")

    return countJ ==  countR

cadena = input("Introduzca la frase para comprobar si estan en equilibrio")
print(check_is_balance(cadena))
