###
#03 - Quantifiers
#Los cuantificadores se utilizan para especificar cuantas ocurrencias de un caracter o grupo de caracteres se deben encontrar en una cadena
#

import re

#* : Puede aparecer 0 o más veces
text = "aaaaba"
pattern = "a*"

matches = re.findall(pattern, text)
print(matches)

# -------------------------------------------------------------------------------------------------------

text = "dddd aaa ccc bb"
pattern = "a+"

matches = re.findall(pattern, text)
print(matches)

# ------------------------------------------------------------------------------------------------------

# ?: 0 o una vez
text = "aaaabacb"
pattern = "a?b"

matches = re.findall(pattern, text)
print(matches)

# -------------------------------------------------------------------------------------------------------

phone = "+34 688999999"
pattern = r"(\+?34 \d{9})"

matches = re.findall(pattern, phone)
print(matches)

# --------------------------------------------------------------------------------------------------------

# {n}: exctamente n veces

text = "aaaaaaaaaaaa"
pattern= "a{3}"


matches = re.findall(pattern, text)
print(matches)

# {n,m}: de n a m

text = " u uuuuuu uuuuuuu uuu uu"
pattern = "u{2,3}"


matches = re.findall(pattern, text)
print(matches)

# ---------------------------------------------------------------------------------------------------------

text = "ala casa arbol león cinco murcielago"
pattern = r"\b\w{4,6}\b"

matches = re.findall(pattern, text)
print(matches)
