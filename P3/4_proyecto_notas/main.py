import funciones
import conexionBD

def main():
    opcion=True
    while opcion:
        funciones.borrarPantalla()
        opcion=funciones.menuPrincipal()

        if opcion=="1" or opcion=="REGISTRO":
            print("Estoy en la opcion 1")
            funciones.esperarTecla()
        elif opcion=="2" or opcion=="LOGIN":
            print("Estoy en la opcion 2")
            funciones.esperarTecla()
        elif opcion=="3" or opcion=="SALIR":
            print("Termino la ejecucion del sistema")
            opcion=False
            funciones.esperarTecla()
        else:
            print("Opcion no valida")
            opcion=True
            funciones.esperarTecla()

if __name__=="__main__":
    main()
