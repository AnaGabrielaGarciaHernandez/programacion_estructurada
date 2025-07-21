def borrarPantalla():
    import os
    os.system("cls")

def esperarTecla():
    input("\n\t\t oprima cualquier tecla para continuar...")

def menuPrincipal():
  print("\n\t..::: \U0001F4DD Sistema de Gestión de Notas \U0001F4DD :::...\n\t\t1️⃣- Registro  \n\t\t2️⃣- Login \n\t\t3️⃣- Salir")
  opcion=input("\n\t\t\t \U0001F4DD Elige una opción (1-4): ").upper()
  return opcion
