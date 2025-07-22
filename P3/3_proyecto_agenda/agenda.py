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

def main_principal():
    print("\n\t..:::\U0001F4C5 Sistema de Gestión de Agenda de Contactos \U0001F4C5:::...\n\t\t1️⃣- Agregar contacto  \n\t\t2️⃣- Mostrar Todos los contactos \n\t\t3️⃣- Buscar contacto por nombre \n\t\t4️⃣- Modificar contacto \n\t\t5- Eliminar contacto \n\t\t6- SALIR ")
    opcion=input("\n\t\t\t \U0001F4DD Elige una opción (1-6): ").upper().strip()
    return opcion

def agregar_contacto(agenda):
    borrarPantalla()
    conexionBD=conectar()
    if conexionBD!=None:
      print("\n\t\t .:: \U0001F464 Agregar Contactos \U0001F464")
      nombre=input("\U0001F4DD Nombre del contacto: ").upper().strip()
      if nombre in agenda:
          print(f"\n\t\t \u274C El contacto {nombre} ya existe \u274C")
      else:
        tel=input("\U0001F4DD Telefono: ").strip()
        email=input("\U0001F4DD E-mail: ").lower().strip()
        #Agregar un atributo "nombre" al diccionario con los valores de tel y email en una lista
        agenda[nombre]=[tel,email]
        try:
            cursor=conexionBD.cursor()
            sql="insert into agenda (nombre,telefono,email) values (%s,%s,%s)"
            val=(nombre,tel,email)
            cursor.execute(sql,val)
            conexionBD.commit()
            input("\n\t\t \u2705 ..Accion realizada con exito.. \u2705")
        except Error as e:
            print(f"\n\t\t Sucedio algo inesperado en la base de datos {e}")

def mostrar_contacto(agenda):
    borrarPantalla()
    conexionBD=conectar()
    if conexionBD!=None:
      print("\n\t\t .::Mostrar Contacto::.")
      cursor=conexionBD.cursor()
      sql="select * from agenda"
      cursor.execute(sql)
      registros=cursor.fetchall()
      if registros:
          print(f"{'ID':<10}{'Nombre':<15}{'Telefono':<15}{'Email':<15}")
          print(f"-"*70)
          for fila in registros:
            print(f"{fila[0]:<10}{fila[1]:15}{fila[2]:<15}{fila[3]:<15}")
            print(f"-"*70)
          contactos=len(registros)
          print(f"\n\t\t ...Son {contactos} en tu agenda...")
      else:
          print("\n\t\t No existen contactos en la agenda")
      input("\n\t\t ..Accion realizada con exito..")

def buscar_contacto(agenda):
    borrarPantalla()
    conexionBD=conectar()
    if conexionBD!= None:
        print("\n\t\t .:: Buscar Contacto ::.")
        cursor=conexionBD.cursor()
        nombre = input("\n\t\tIngresa el nombre del contacto a buscar: ").upper().strip()
        sql="select * from agenda where nombre = %s"
        val=(nombre,)
        cursor.execute(sql,val)
        registros=cursor.fetchall()
        if registros:
            print(f"{'ID':<10}{'Nombre':<15}{'Telefono':<15}{'Email':<15}")
            print(f"-"*60)
            for fila in registros:
                print(f"{fila[0]:<10}{fila[1]:<15}{fila[2]:<15}{fila[3]:<15}")
                print(f"-"*60)
        else:
            print(f"\n\t\tEl contacto '{nombre}' no existe en la agenda.")
        input("\n\t\tPresiona Enter para continuar...")

def modificar_contacto(agenda):
    borrarPantalla()
    conexionBD=conectar()
    if conexionBD!=None:
        print("\n\t\t .:: Modificar Contacto ::.")
        cursor=conexionBD.cursor()
        nombre=input("\n\t\t Dame el nombre del contacto a modificar: ").upper().strip()
        sql="select* from agenda where nombre = %s"
        val=(nombre,)
        cursor.execute(sql,val)
        registros=cursor.fetchall()
        if registros:
            print("\n\t\t Informacion del contacto ingresado: ")
            print(f"{'ID':<10}{'Nombre':<15}{'Telefono':<15}{'Email':<15}")
            print(f"-"*60)
            for fila in registros:
                print(f"{fila[0]:<10}{fila[1]:<15}{fila[2]:<15}{fila[3]:<15}")
                print(f"-"*60)
            resp=input("\n\t\t Desea modificar el contacto? S/N: ").upper().strip()
            if resp=="S":
                nuevo_nombre = input("\n\t\t Nuevo nombre: ").upper().strip()
                nuevo_num= input("\n\t\t Nuevo telefono: ").strip()
                nuevo_mail= input("\n\t\t Nuevo email: ").lower().strip()
                sql="update agenda set nombre=%s, telefono=%s, email=%s where nombre=%s"
                val=(nuevo_nombre,nuevo_num,nuevo_mail,nombre)
                cursor.execute(sql,val)
                conexionBD.commit()
                print(f"\n\t\t el contacto de : {nombre} se cambio con exito")
        else:
            print(f"El contacto de: {nombre} no se encuentra en la agenda")
        input("\n\t\tPresiona Enter para continuar...")

def eliminar_contacto(agenda):
    borrarPantalla()
    conexionBD=conectar()
    if conexionBD!=None:
        print("\n\t\t .::Eliminar contacto::.")
        cursor=conexionBD.cursor()
        nombre=input("\n\t\t Ingrese el nombre del contacto a borrar: ").upper().strip()
        sql="select * from agenda where nombre=%s"
        val=(nombre,)
        cursor.execute(sql,val)
        registros=cursor.fetchall()
        if registros:
            print("\n\t\t Informacion del contacto ingresado: ")
            print(f"{'ID':<10}{'Nombre':<15}{'Telefono':<15}{'Email':<15}")
            print(f"-"*60)
            for fila in registros:
                print(f"{fila[0]:<10}{fila[1]:<15}{fila[2]:<15}{fila[3]:<15}")
            print(f"-"*60)
            resp=input(f"\n\t\t ¿Deseas borrar a {nombre} de tus contactos? S/N: ").upper().strip()
            if resp=="S":
                sql="delete from agenda where nombre = %s"
                val=(nombre,)
                cursor.execute(sql,val)
                conexionBD.commit()
                print(f"\n\t\t El contacto de {nombre} se borro con exito...")
        else:
            print(f"\n\t\t El contacto de: {nombre} no esta en la lista...")
        input("\n\t\tPresiona Enter para continuar...")

