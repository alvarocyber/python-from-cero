import re

# []: coincide con cualquier caracter de dentro de los corchetes

username = "rub.ius_69+"
pattern = r"^[\w._%+-]+$"

matchs = re.search(pattern,username)

if matchs:
    print("Username valido")
else:
    print("Username invalido")

# --------------------------------------------------------------------------------------------------------

#Buscar voacales

text = "Hola mundo"
pattern = r"[aeiou]"

matchs = re.findall(pattern,text)
print(matchs)
