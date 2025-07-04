"""Funciones es un conjunto de instrucciones agrupadas bajo un nombre en particular como un programa
mas pequeño que cumple una funcion especifica. Se puede reutilizar solo con invocarla

Sintaxos
  def nombredeMifuncion(parametros):
    bloque o conjunto de instrucciones
    
nombredeMifuncion(parametros)
las funciones pueden ser de 4 tipos
 Funciones de tipo de "Procedimiento"
 1.- Funcion que no recice parametros y no regresa valor.
 3.- Funcion que recibe parametros y no regresa valor.
 
 Funciones de tipo "Funcion".
 2.- Funcion que no recibe parametros y regresa valor.
 4-. Funcion que recibe parametros y regresa valor.
 """

#1.-Funcion que no recibe parametros y no regresa valor.
def SolicitarDatos1():
    nombre1=input("Nombre: ")
    telefono1=input("Telefono: ")
    print(f"Soy funcion 1 y El nombre es: {nombre1} y su telefono es: {telefono1}")

#3.-Funcion que recibe parametros y no regresa valor.
def SolicitarDatos3(nombre3,telefono3):
    nom3=nombre3
    tel3=telefono3
    print(f"Soy funcion 3 y El nombre es: {nom3} y su telefono es: {tel3}")


#2.- Funcion que no recibe parametros y regresa valor.
def SolicitarDatos2():
    nombre2=input("Nombre: ")
    telefono2=input("Telefono: ")
    return nombre2,telefono2

#4.- Funcion que recibe parametros y regresa valor.
def SolicitarDatos4(nombre4,telefono4):
    nom4=nombre4
    tel4=telefono4
    return nom4,tel4

#LLamar funciones.
SolicitarDatos1()

nombre3=input("Nombre: ")
telefono3=input("Telefono: ")
SolicitarDatos3(nombre3,telefono3)

nomnbre2,telefono2=SolicitarDatos2()
print(f"Soy funcion 2 Nombre: {nomnbre2} \n Telefono: {telefono2}")

nom4=input("Nombre: ")
tel4=input("Telefono: ")
nombre4,telefono4=SolicitarDatos4(nom4,tel4)
print(f"Soy funcion 4 Nombre: {nombre4} \n Telefono: {telefono4}")
