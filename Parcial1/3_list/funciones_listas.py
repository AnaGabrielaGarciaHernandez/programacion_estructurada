"""

List (Array)
son colleciones o conjuntos de datos/valores bajo un mismo nombre, para acceder
a los valores se hace con un indice numerico.

Nota: sus valores si son modificables

La lista es una coleccion ordenada y modificable. Permite miembros duplicados.

"""
import os
os.system("cls")
#Funciones mas comunes en las listas

paises=["Mexico","Brasil","España","Canada"]

numeros=[23,12,100,34]

#Ordenar ascendentemente
print(numeros)
numeros.sort()
print(numeros)

print(paises)
paises.sort()
print(paises)

#Añadir o ingresar o insertar elementos a una lista
#Primer forma
print(paises)
paises.append("Honduras")

#Segunda forma
paises.insert(1,"Honduras")
print(paises)

#Eliminar o borrar o quitar elementos de una lista
#Primer forma con el indice
paises.pop(1)
print(paises)

#Segunda forma con el valor o a traves de las primary key
paises.remove("Honduras")
print(paises)

#Buscar un elemento dentro de la lista
#Primera forma
resp="Brasil" in paises
if resp:
    print("Si encontre el pais")
else:
    print("No existe")

#Segunda forma
for i in range(0,len(paises)):
    if paises[i]=="Brasil":
        print("Si encontre el pais")
    else:
        print("No lo encontre")

#Cuantas veces aparece un elemento dentro de una lista
print(f"Este numero 12 aparece: {numeros.count(12)} vez o veces")

numeros.append(12)
print(f"Este numero 12 aparece: {numeros.count(12)} vez o veces")

#Identificar o conocer el indice de un valor
indice=paises.index("España")
print(indice)
paises.pop(indice)
print(paises)

#Recorrer los valores de la lista
#Imprime hacia abajo
#Primer forma con los valores solo recorre la lista
for i in paises:
    print(i)

#2da forma con los indices 
for i in range(0,len(paises)):
    print(f"El valor {i} es {paises[i]}")

#Funcion que permite unir contenido de listas
print(paises)
print(numeros)
paises.extend(numeros)
print(paises)