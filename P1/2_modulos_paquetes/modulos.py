"""Un modulo es simplemente un archivo con extenión .py que contiene código de Python 
(funciones, clases, variables, etc.)

Un paquete es una carpeta que contiene varios módulos (archivos .py) y un archivo especial 
llamado __init__.py, que le indica a Python que esa carpeta debe tratarseb como un paquete."""

import os

def solicitarDatos1():
    nombre=input("Nombre: ")
    tel=input("Telefono: ")
    print(f"Soy funcion 1 El nombre es: {nombre} y su telefono es: {tel}")

def solicitarDatos3(nombre,tel):
    nomb=nombre
    telefono=tel
    print(f"Soy funcion 3 El nombre es: {nomb} y su telefono es: {telefono}")
    
def solicitarDatos2():
    nombre=input("Nombre: ")
    tel=input("Telefono: ")
    return nombre, tel

def solicitarDatos4(nombre,tel):
    nom=nombre
    telefono=tel
    return nom, telefono

def borrarPantalla():
    os.system("cls")


def espereTecla():
    input("...Oprima una tecla para continuar...")

def saludar(nombre):
    nom=nombre
    return f"Hola, bienvenido: {nom}!"