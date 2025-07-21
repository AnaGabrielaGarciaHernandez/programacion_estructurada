import calificaciones

def main():
    datos=[]

    opcion=True
    while opcion:
        calificaciones.borrarPantalla()
        opcion=calificaciones.menuPrincipal()

        match opcion:
            case "1":
                calificaciones.agregar_calificaciones(datos)
                calificaciones.esperarTecla()
            case "2":
                calificaciones.mostrar_calificaciones(datos)
                calificaciones.esperarTecla()
            case "3":
                calificaciones.calcular_promedios(datos)
                calificaciones.esperarTecla()
            case "4":
                calificaciones.buscar_calificaciones(datos)
                calificaciones.esperarTecla() 
            case "5":
                opcion=False    
                calificaciones.borrarPantalla()
                print("\n\t`\u2705`Terminaste la ejecucion del SW`\u2705`")
            case _:
                calificaciones.borrarPantalla()
                print("\n\t`\u274C`Opción invalida vuelva a intentarlo ... por favor`\u274C`")
                calificaciones.esperarTecla()

if __name__ == "__main__":
    main()