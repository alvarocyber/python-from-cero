###
# 04 - Diccionarios
# Los diccionarios son coleeciones de pares clase-valor.
#Sirven oara almacenar datos relacionados
#

persona = {
    "nombre": "Alvaro",
    "edad": 25,
    "es_estudiante":True,
    "calificaciones": [5,6,5.4],
    "socials":{
        "twitter":"alvarocyber",
        "instagram":"alvaroogrc__",
    }

}

#Para acceder a los valores

print(persona["nombre"])
print(persona["calificaciones"][2])
print(persona["socials"]["instagram"])

print(persona)

# Para eliminar algo del diccionario
del persona["calificaciones"]
print(persona)

es_estudiante=persona.pop("es_estudiante")
print(es_estudiante)

#sobreescribir un diccionario con otro
a = {"nombre":"alvaro", "edad":25}
b = {"nombre":"pepe", "es_estudiante":True}

a.update(b)
print(a)

print("nombre" in persona)

#obtener claves
print("\n keys:")
print(persona.keys())

#obtener valores
print("\n valores:")
print(persona.values())

#obtener items
print("\n items:")
print(persona.items())

