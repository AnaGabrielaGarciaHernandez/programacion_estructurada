def borrarPantalla():
    import os
    os.system("cls")

def esperarTecla():
    input("\n\t\t \u2705 Presione una tecla para continuar... \u2705")

def main_principal():
    print("\n\t..:::\U0001F4C5 Sistema de Gestión de Agenda de Contactos \U0001F4C5:::...\n\t\t1️⃣- Agregar contacto  \n\t\t2️⃣- Mostrar Todos los contactos \n\t\t3️⃣- Buscar contacto por nombre \n\t\t4️⃣- Modificar contacto \n\t\t5- Eliminar contacto \n\t\t6- SALIR ")
    opcion=input("\n\t\t\t \U0001F4DD Elige una opción (1-6): ").upper().strip()
    return opcion

def agregar_contacto(agenda):
    borrarPantalla()
    print("\n\t\t .:: \U0001F464 Agregar Contactos \U0001F464")
    nombre=input("\U0001F4DD Nombre del contacto: ").upper().strip()
    if nombre in agenda:
        print(f"\n\t\t \u274C El contacto {nombre} ya existe \u274C")
    else:
        tel=input("\U0001F4DD Telefono: ").strip()
        email=input("\U0001F4DD E-mail: ").lower().strip()
        #Agregar un atributo "nombre" al diccionario con los valores de tel y email en una lista
        agenda[nombre]=[tel,email]
        input("\n\t\t \u2705 ..Accion realizada con exito.. \u2705")

def mostrar_contacto(agenda):
    borrarPantalla()
    print("\n\t\t .::Mostrar Contacto::.")
    if not agenda:
        print("\n\t\t No existen contactos en la agenda")
    else:
        for nombre, datos in agenda.items():
            print(f"\n\t\t{'Nombre: '+nombre}\n\t\t{'Telefono: '+datos[0]}\n\t\t{'Email: '+datos[1]}")
    input("\n\t\t ..Accion realizada con exito..")

def buscar_contacto(agenda):
    borrarPantalla()
    print("\n\t\t .:: Buscar Contacto ::.")
    if not agenda:
        print("\n\t\t No existen contactos en la agenda.")
    else:
        nombre = input("\n\t\tIngresa el nombre del contacto a buscar: ").upper().strip()
        if nombre in agenda:
            datos=agenda[nombre]
            print(f"\n\t\t{'Nombre: '+nombre}\n\t\t{'Telefono: '+datos[0]}\n\t\t{'Email: '+datos[1]}")
        else:
            print(f"\n\t\tEl contacto '{nombre}' no existe en la agenda.")

    input("\n\t\tPresiona Enter para continuar...")

def modificar_contacto(agenda):
    borrarPantalla()
    print("\n\t\t .:: Modificar Contacto ::.")

    if not agenda:
        print("\n\t\t No existen contactos en la agenda.")
    else:
        buscar = input("\n\t\tIngresa el nombre del contacto a buscar: ").upper().strip()

        if buscar in agenda:
            datos = agenda[buscar]
            resp_nombre = input("\n\t\t¿Deseas modificar el nombre? (S/N): ").upper().strip()
            if resp_nombre == "S":
                nuevo_nombre = input("\t\tNuevo nombre: ").upper().strip()
                if nuevo_nombre and nuevo_nombre != buscar:
                    agenda[nuevo_nombre] = datos
                    agenda.pop(buscar)
                    buscar = nuevo_nombre

            campos = ["Teléfono", "Email"]
            for i in range(len(campos)):
                resp = input(f"\n\t\t¿Deseas modificar el {campos[i]}? (si/no): ").strip().lower()
                if resp == "si":
                    nuevo_valor = input(f"\t\tNuevo {campos[i]}: ").strip()
                    if nuevo_valor:
                        agenda[buscar][i] = nuevo_valor
        input("\n\t\tPresiona Enter para continuar...")

def eliminar_contacto(agenda):
    borrarPantalla()
    print("\n\t\t .::Eliminar contacto::.")
    if not agenda:
        print("\n\t\t No existen contactos en la agenda")
    else:
        borrar=input("\n\t\t Ingresa el nombre del contacto a borrar: ").upper().strip()
        if borrar in agenda:
            datos=agenda[borrar]
            print(f"\n\t\t{'Nombre: '+borrar}\n\t\t{'Telefono: '+datos[0]}\n\t\t{'Email: '+datos[1]}")
            resp=input(f"\n\tDesea borrar este contacto? (si/no) ").lower().strip() 
            if resp== "si":
                agenda.pop(borrar)
        input("\n\t\tPresiona Enter para continuar...")
