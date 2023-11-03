import json

from helpers import absPath

datos = []

datos.append({
    "nombre": "hector",
    "empleo": "instructor",
    "email": "hetorgay@ejemplo.com"
})
# Definimos una lista de contactos
contactos = [
    ("Manuel", "Desarrollador Web", "manuel@ejemplo.com"),
    ("Lorena", "Gestora de proyectos", "lorena@ejemplo.com"),
    ("Javier", "Analista de datos", "javier@ejemplo.com"),
    ("Marta", "Experta en Python", "marta@ejemplo.com")
]

# Añadimos un contactos dinámicamente
for nombre, empleo, email in contactos:
    datos.append({
        "nombre": nombre,
        "empleo": empleo,
        "email": email
    })

with open(absPath("contactos.json"),"w") as fichero:
    json.dump(datos,fichero)

datos = None

with open(absPath("contactos.json")) as fichero:
    datos = json.load(fichero)
    for contacto in datos:
        print(contacto["nombre"])