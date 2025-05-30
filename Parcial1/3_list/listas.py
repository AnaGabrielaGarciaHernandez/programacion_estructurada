#Ejemplo 1: Crear una lista de numeros e imprimir el contenido
import os
#Op1
numeros=[1,2,3,6,5,10]
print(numeros)
#op2
for i in numeros:
    print(i)
#op3
for i in range(0,len(numeros)):
    print(numeros[i])

#Ejemplo 2: crear una lista de palabras y posteriormente buscar la coincidencia de una palabra
os.system("cls")
palabras=["avion","carro","sueño","avion"]
print(palabras)
buscar=input("Dame la palabras: ")
#op1
print(f"El numero de veces que se encontro es: {palabras.count(buscar)}")
if buscar in palabras:
    print("Si la encontre")
else:
    print("No la encontre")
#op2
encontro=False
for i in range(0,len(palabras)):
    if palabras[i]==buscar:
        encontro=True

if encontro:
    print("Si la encontre")
else:
    print("No la encontre")
#op3
encontro2=False
for i in palabras:
    if i==buscar:
        encontro2=True

if encontro2:
    print("Si la encontre")
else:
    print("No la encontre")

input("Oprime tecla")

#Ejemplo 3: Añadir elementos a una lista
os.system("cls")
numeros=[]
print(numeros)
opc=True
while opc:
    numero=float(input("Dame un numero entero o decimal: "))
    numeros.append(numero)
    resp=(input("Desea ingresar otro? ")).lower()
    if resp=="si":
        opc=True
    else:
        opc=False
print(numeros)
input("Oprime tecla")

#Ejemplo 4: crear una lista multidimensional que sea una agenda
agenda=[
    ["Carlos","6181234567"],
    ["Beto","1654516541"],
    ["Mario","64587468"]
    ]

for i in agenda:
    print(i)

cadena=""
for r in range(0,3):
    for c in range(0,2):
        cadena+=f"{agenda [r][c]}, "
    cadena+="\n"
print(cadena)