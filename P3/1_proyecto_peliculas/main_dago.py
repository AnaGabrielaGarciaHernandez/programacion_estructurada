"""
Crear un proyecto que permita gestonar (administrar) peliculas, colocar un menu de opciones
para agregar, eliminar, modificar y consultar peliculas
Notas:
1.- Utilizar funciones y mandar llamar desde otro archivo.
2.-Utilizar listas para almacenar los nombres de peliculas.
3.- Utilizar bases de datos para gestionar las peliculas.

"""
import peliculas_dago

opcion=True
while opcion:
    peliculas_dago.borrarPantalla()
    print("\n\t\t\t..::: CINEPOLIS CLON :::... \n\t\t..::: Sistema de Gestión de Peliculas :::...\n\t\t\t 1.- Crear  \n\t\t\t 2.- Borrar \n\t\t\t 3.- Mostrar \n\t\t\t 4.- Modificar\n\t\t\t 5.- Buscar \n\t\t\t 6.- SALIR ")
    opcion=input("\n\t\t\t Elige una opción: ").upper()

    match opcion:
        case "1":
            peliculas_dago.crearPeliculas()
            peliculas_dago.esperarTecla()
        case "2":
            peliculas_dago.borrarPeliculas()
            peliculas_dago.esperarTecla()
        case "3":
            peliculas_dago.mostrarPeliculas()
            peliculas_dago.esperarTecla() 
        case "4":
            peliculas_dago.modificarPeliculas()
            peliculas_dago.esperarTecla()
        case "5":
            peliculas_dago.buscarPeliculas()
            peliculas_dago.esperarTecla()
        case "6":
            opcion=False    
            peliculas_dago.borrarPantalla()
            print("\n\t`\u2705`Terminaste la ejecucion del SW`\u2705`")
        case _:
            peliculas_dago.borrarPantalla()
            input("\n\t`\u274C`Opción invalida vuelva a intentarlo ... por favor`\u274C`")