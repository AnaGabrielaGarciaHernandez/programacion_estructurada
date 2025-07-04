"""Crear un programa que calcule e imprima cualquier tabla de multiplicar.
Requisitos:
Con funciones que regrese valor y utilice parametros.
"""
numero=int(input("Dame el numero de la tabla de multiplicar a calcular: "))
print(f"{numero} X 1 = {numero*1}")
print(f"{numero} X 2 = {numero*2}")
print(f"{numero} X 3 = {numero*3}")
print(f"{numero} X 4 = {numero*4}")
print(f"{numero} X 5 = {numero*5}")
print(f"{numero} X 6 = {numero*6}")
print(f"{numero} X 7 = {numero*7}")
print(f"{numero} X 8 = {numero*8}")
print(f"{numero} X 9 = {numero*9}")
print(f"{numero} X 10 = {numero*10}")

numero=int(input("Dame el numero de la tabla de multiplicar a calcular: "))
for i in range(1, 11,1):
    print(f"{numero} X {i} = {numero*i}")

numero=int(input("Dame el numero de la tabla de multiplicar a calcular: "))
i=1
while i<=10:
    print(f"{numero} X {i} = {numero*i}")
    i+=1

def TablasMulti(numero):
    num=numero
    respuesta=""
    for i in range(1, 11,1):
        respuesta+=f"{num} X {i} = {num*i} \n" 
    return respuesta

numero=int(input("Dame el numero de la tabla de multiplicar a calcular: "))
resultado=TablasMulti(numero)
print(f"{resultado}")