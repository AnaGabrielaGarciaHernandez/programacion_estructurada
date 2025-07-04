"""
disct.-
Es un tipo de datos que se utilizan para alamcenar datos de
diferente tipo de datos pero en lugar de tener como las listas idices numericos,
tiene alfanumericos. Es decir es algo parecido como los Objetos

Tambien se conoce como arreglo asosiativo u objeto json

El diccionario es una coleccion ordenada y modificable. No hay miembros duplicados.
"""

import os
os.system("cls")

#Lista
#paises=["Mexico","Brasil","Canada","España"]

#Dict o objeto, no atributos iguales
paises_mexico={
    "Nombre":"Mexico",
    "Capital":"CDMEX",
    "Poblacion":1200000,
    "Idioma":"Español",
    "Estatus":True
    }

paises_brasil={
    "Nombre":"Brasil",
    "Capital":"Brasilia",
    "Poblacion":1000000,
    "Idioma":"Portugues",
    "Estatus":True
    }

paises_canada={
    "Nombre":"Canada",
    "Capital":"Ottawa",
    "Poblacion":900000,
    "Idioma":{"Ingles","Frances"},
    "Estatus":False
    }

alumno1={
    "Nombre":"Astrid",
    "Apellido Paterno":"Zapata",
    "Apellido Materino":"Garcia",
    "Carrera":"TI",
    "Area":"Software Multiplataforma",
    "Modalidad":"Bis",
    "Matricula":"123456",
    "Semestre":"2"
}

print(alumno1)

#Imprime solo los atributos
for i in alumno1:
    print(i)

#Imprime solo los valores
for i in (alumno1[i]):
    print(i)

#Imprime ambos
for i in alumno1:
    print(f"{i}={alumno1[i]}")

#Agregar
alumno1["Telefono"]="6181234567"
for i in alumno1:
    print(f"{i}={alumno1[i]}")