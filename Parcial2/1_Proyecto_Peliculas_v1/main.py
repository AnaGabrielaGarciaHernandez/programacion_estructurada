"""
Crear un proyecto que permita gestonar (administrar) peliculas, colocar un menu de opciones
para agregar, eliminar, modificar y consultar peliculas
Notas:
1.- Utilizar funciones y mandar llamar desde otro archivo.
2.-Utilizar listas para almacenar los nombres de peliculas.

"""
import peliculas
opcion=True
while opcion:
    peliculas.borrar_pantalla()
    print("\n\t..::: CINEPOLIS CLON :::... \n..::: Sistema de Gestión de Peliculas :::...\n 1.- Agregar  \n 2.- Eliminar \n 3.- Actualizar \n 4.- Consultar \n 5.- Buscar \n 6.- Vaciar \n 7.- SALIR ")
    opcion=input("\t Elige una opción: ").upper()

    match opcion:
        case "1":
            peliculas.borrar_pantalla()
            print(".:: Agregar Peliculas ::.")
            peliculas.agregar()
            peliculas.esperar_tecla()
        case "2":
            peliculas.borrar_pantalla()
            print(".:: Eliminar Peliculas ::.")
            peliculas.borrar()
            peliculas.esperar_tecla() 
        case "3":
            peliculas.borrar_pantalla()
            print(".:: Modificar Peliculas ::.") 
            peliculas.esperar_tecla()    
        case "4":
            peliculas.borrar_pantalla()
            print(".:: Consultar Peliculas ::.")
            peliculas.consultar()
            peliculas.esperar_tecla()  
        case "5":
            peliculas.borrar_pantalla()
            print(".:: Buscar Peliculas ::.") 
            peliculas.buscar()
            peliculas.esperar_tecla()
        case "6":
            peliculas.borrar_pantalla()
            print(".:: Vacias Peliculas ::.")
            peliculas.vaciar_lista() 
            peliculas.esperar_tecla()
        case "7":
            peliculas.borrar_pantalla()
            opcion=False    
            print("Terminaste la ejecucion del SW")
        case _:
            peliculas.borrar_pantalla()
            input("Opción invalida vuelva a intentarlo...porfavor")