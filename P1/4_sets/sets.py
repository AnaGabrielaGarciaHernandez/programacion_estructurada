"""Set es una coleccion desordenada, inmutable y no indexada.
No hay miembros duplicados."""

import os
os.system("cls")
#No hay posiciones ni duplicados
personas={"Ramiro","Choche","Lupe"}
print(personas)
personas.add("Peje")
print(personas)
#Pop borra al ultimo, pero no se sabe cual borrara 
personas.pop()
print(personas)
#Borrar todo
personas.clear()
print(personas)
varios={3.12,1,True,"Hola"}
print(varios)

"""Ejemplo: crear un programa que solicite los emails de los alumnos y 
almacenar en una list y posteriormente mostrar los emails sin duplicados"""

opc="si"
emails=[]
while opc=="si":
    emails.append(input("Dame el email: "))
    #print(emails)
    opc=input("¿Deseas solicitar otro email? (si/no)").lower()

#Imprimir los emails sin duplicados
print(emails)
set1=set(emails)
print(set1)
emails=list(set1)
print(emails)