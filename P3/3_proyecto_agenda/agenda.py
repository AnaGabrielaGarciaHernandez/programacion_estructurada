import mysql.connector
from mysql.connector import Error

def conectar():
  try:
      conexion=mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="bd_agenda"
      )
      return conexion
  except Error as e:
    print(f"El error que sucedio es: {e}")
    return None

def borrarPantalla():
  import os  
  os.system("cls")

def esperarTecla():
  input("\n\t\t \u26A0 Oprima cualquier tecla para continuar ...\u26A0")  

