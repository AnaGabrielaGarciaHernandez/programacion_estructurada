import mysql.connector
from mysql.connector import Error

def conectar():
  try:
      conexion=mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="bd_calificaciones"
      )
      return conexion
  except Error as e:
    print(f"El error que sucedio es: {e}")
    return None

def borrarPantalla():
  import os  
  os.system("cls")

def esperarTecla():
  input("\n\t\t `\u26A0`Oprima cualquier tecla para continuar ...`\u26A0`")  

def menuPrincipal():
  print("\n\t..:::`\U0001F4DD`Sistema de Gestión de Calificaciones`\U0001F4DD`:::...\n\t\t1️⃣ -Agregar Calificacion  \n\t\t2️⃣ -Mostrar Calificacion \n\t\t3️⃣ -Calcular Promedio \n\t\t4️⃣ -Buscar Alumno \n\t\t 5-SALIR ")
  opcion=input("\n\t\t\t `\U0001F4DD`Elige una opción (1-5): ").upper()
  return opcion

def agregar_calificaciones(lista):
  borrarPantalla()
  conexionbd=conectar()
  if conexionbd!=None:
   print("\n\t\t\t\U0001F4DD Agregar Calificaiones")
   nombre=input("\n\t\t \U0001F464 Nombre del Alumno: ").upper().strip()
   calificaciones=[]
   for i in range(1,4):
      continua=True
      while continua:
       try:
        cal=float(input(f" \t\t\t \U0001F4DD Calificación {i}: "))
        if cal>=0 and cal<11:
         calificaciones.append(cal)
         continua=False
        else:
          print("\n\t\t \u274C Ingresa un numero válido \u274C")
       except ValueError:
        print(" \n\t\t \u274CIngresa un valor númerico \u274C") 
   lista.append([nombre]+calificaciones)
   try:
     cursor=conexionbd.cursor()
     sql="INSERT INTO calificaciones (nombre, calificacion1, calificacion2, calificacion3) VALUES (%s, %s, %s, %s)"
     val=(lista[0][0],calificaciones[0],calificaciones[1],calificaciones[2])
     cursor.execute(sql,val)
     conexionbd.commit() 
     print(" \n\t\t \u2705 Acción realizada con éxito!")
   except Error as e:
     print(f"Error al intentar insertar un registro en la base de datos {e}")

def mostrar_calificaciones(lista):
    borrarPantalla()
    conexionBD=conectar()
    if conexionBD!=None:
        print("\n\t\t `\u2705` .:: Consultar o Mostrar las Calificaciones ::.`\u2705` ")
        cursor=conexionBD.cursor()
        sql="select * from calificaciones"
        cursor.execute(sql)
        registros=cursor.fetchall()
        if registros:
            print("\n\t\t Mostrar las calificaciones")
            print(f"{'ID':<10}{'Nombre':<15}{'Cal.1':<10}{'Cal.2':<10}{'Cal.3':<10}")
            print(f"-"*60)
            for fila in registros:
                print(f"{fila[0]:<10}{fila[1]:<15}{fila[2]:<10}{fila[3]:<10}{fila[4]:<10}")
            print(f"-"*60)
            cuantos=len(registros)
            print(f"`\U0001F464`Son {cuantos} alumnos`\U0001F464`")
        else:
            ("\n\t\t`\u274C`No hay calificaciones registradas en el sistema`\u274C`")
        print("\n\t\t`\u2705`Accion realizada con exito`\u2705`")

def calcular_promedios(lista):
    borrarPantalla()
    conexionBD=conectar()
    if conexionBD!=None:
        print("\n\t\t`\U0001F4DD`.:: Consultar el Promedio ::.`\U0001F4DD`")
        cursor=conexionBD.cursor()
        sql="select * from calificaciones"
        cursor.execute(sql)
        registros=cursor.fetchall()
        print(f"\U0001F464{'Nombre':<15}`\U0001F4DD`{'Promedio':<10}")
        print(f"-"*20)
        if registros:
            promedio_grupal=0
            for fila in registros:
                nombre=fila[1]
                calificaciones=fila[2:]
                promedio=sum(calificaciones)/3
                promedio_grupal+=promedio
                print(f"{nombre:<15}{promedio:.2f}")
                promedio_grupal+=promedio
            print(f"-"*30)
            promedio_grupal=promedio_grupal/len(registros)
            print(f"\n\t\t`\U0001F389`El promedio grupal es: {promedio_grupal:.2f}")
        else:
            ("\n\t\t`\u274C`No hay calificaciones registradas en el sistema`\u274C`")

def buscar_calificaciones(lista):
    borrarPantalla()
    conexionBD=conectar()
    if conexionBD!=None:
        print("\n\t\t`\U0001F4DD .::Buscar Alumno::.\U0001F4DD")
        cursor=conexionBD.cursor()
        sql="select * from calificaciones"
        cursor.execute(sql)
        registros=cursor.fetchall()
        if registros:
            nom=input("\n\t\t Ingrese el nombre del alumno a buscar: ").upper()
            for i in registros:
               if nom==i[1]:
                  print(f"-"*80)
                  print(f"{'ID':<10}{'Nombre':<15}{'Cal.1':<10}{'Cal.2':<10}{'Cal.3':<10}{'Promedio':<10}")
                  print(f"-"*80)
                  print(f"{i[0]:<10}{i[1]:<15}{i[2]:<10}{i[3]:<10}{i[4]:<10}{sum(i[2:])/3:.2f}")
                  print(f"-"*80)
        else:
            print("No hay almuno con este nombre")
