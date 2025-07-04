

def borrarPantalla():
  import os  
  os.system("cls")

def esperarTecla():
  input("\n\t\t `\u26A0`Oprima cualquier tecla para continuar ...`\u26A0`")  

def menuPrincipal():
  print("\n\t..:::`\U0001F4DD`Sistema de Gestión de Calificaciones`\U0001F4DD`:::...\n\t\t1️⃣ Agregar Calificacion  \n\t\t2️⃣ Mostrar Calificacion\n\t\t3️⃣ Calcular Promedio\n\t\t4️⃣ SALIR ")
  opcion2=input("\n\t\t\t `\U0001F4DD`Elige una opción (1-4): ").upper()
  return opcion2

def agregar_calificaciones(lista):
    borrarPantalla()
    print("\n\t\t `\u2705` .::Agregar Calificaciones::.`\u2705` ")
    nombre=input("\n\t\t`\U0001F4DD`Nombre del alumno: ").upper().strip()
    calificaciones=[]
    for i in range(1,4):
        continua=True
        while continua:
            try:
                cal=float(input(f"\n\t\t `\U0001F4DD`Calificacion {i}: "))
                if cal >= 0 and cal < 11:
                    calificaciones.append(cal)
                    continua=False
                else:
                    print("\n\t`\u26A0`Ingresa un numero valido`\u26A0`")
            except ValueError:
                print("\n\t`\u26A0` Ingresa un valor numerico`\u26A0`")
    lista.append([nombre]+calificaciones)
    print("\n\t\t `\u2705`Accion realizada con exito `\u2705`")

def mostrar_calificaciones(lista):
    borrarPantalla()
    print("\n\t\t `\u2705` .:: Consultar o Mostrar las Calificaciones ::.`\u2705` ")
    if len(lista)>0:
        print(f"\n\t\t{'Nombre':<15}{'Cal.1':<10}{'Cal.2':<10}{'Cal.3':<10}")
        print(f"\n\t\t-"*40)
        for fila in lista:
            print(f"\n\t\t{fila[0]:<15}{fila[1]:<10}{fila[2]:<10}{fila[3]:<10}")
        print(f"\n\t\t-"*40)
        cuantos=len(lista)
        print(f"`\U0001F464`Son {cuantos} alumnos`\U0001F464`")
    else:
        ("\n\t\t`\u274C`No hay calificaciones registradas en el sistema`\u274C`")
    print("\n\t\t`\u2705`Accion realizada con exito`\u2705`")

def calcular_promedio(lista):
    borrarPantalla()
    print("\n\t\t`\U0001F4DD`.:: Consultar el Promedio ::.`\U0001F4DD`")
    if len(lista)>0:
        print(f"\n\t\t\U0001F464`{'Nombre':<15}`\U0001F4DD`{'Promedio':<10}")
        print(f"\n\t\t--"*20)
        promedio_grupal=0
        for fila in lista:
            nombre=fila[0]
            i=1
            suma=0
            promedio=0
            while i<=3:
                suma+=fila[i]
                i+=1
            promedio=suma/3
            print(f"{nombre:<15}{promedio:.2f}")
            promedio_grupal+=promedio
        print(f"\n\t\t--"*30)
        promedio_grupal=promedio_grupal/len(lista)
        print(f"\n\t\t`\U0001F389`El promedio grupal es: {promedio_grupal}")

    else:
        ("\n\t\t`\u274C`No hay calificaciones registradas en el sistema`\u274C`")
    print("\n\t\t `\u2705`Accion realizada con exito`\u2705`")

def calcular_promedio2(lista):
    borrarPantalla()
    print("`\U0001F4DD.:: Consultar el Promedio ::.`\U0001F4DD")
    if len(lista)>0:
        print(f"\n\t\t\U0001F464`{'Nombre':<15}`\U0001F4DD`{'Promedio':<10}")
        print(f"\n\t\t--"*20)
        promedio_grupal=0
        for fila in lista:
            nombre=fila[0]
            promedio=sum(fila[1:])/3
            print(f"{nombre:<15}{promedio:.2f}")
            promedio_grupal+=promedio
        print(f"\n\t\t--"*30)
        promedio_grupal=promedio_grupal/len(lista)
        print(f"\n\t\t `\U0001F389`El promedio grupal es: {promedio_grupal}")

    else:
        ("\n\t\t`\u274C`No hay calificaciones registradas en el sistema`\u274C`")
    print("\n\t\t `\u2705`Accion realizada con exito`\u2705`")


def buscar_calificaciones(lista):
    borrarPantalla()
    nom=input("\n\t\t Ingrese el nombre del alumno a buscar?").upper
    enc=0
    if len(lista)>0:
        for i in lista:
            if nom==i[0]:
                print(f"\n\t\t{'Nombre':<15}{'Cal.1':<10}{'Cal.2':<10}{'Cal.3':<10}")
                print(f"\n\t\t-"*40)
                print(f"\n\t\t{i[0]:<15}{i[1]:<10}{i[2]:<10}{i[3]:<10}")
                enc+=1
            else:
                print("No hay almuno con este nombre")
            print(f"Se encontro {enc} alumno(s) con ese nombre")
            