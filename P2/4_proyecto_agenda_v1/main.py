import agenda


def main():
    agenda_contacto={}
    opcion=True
    
    while opcion:
        agenda.borrarPantalla() 
        opcion=agenda.main_principal()
        
        match opcion:
            case "1":
                    agenda.agregar_contacto(agenda_contacto)
                    agenda.borrarPantalla()
            case "2":
                    agenda.mostrar_contacto(agenda_contacto)
                    agenda.borrarPantalla()
            case "3":
                    agenda.buscar_contacto(agenda_contacto)
                    agenda.borrarPantalla()
            case "4":
                    agenda.modificar_contacto(agenda_contacto)
                    agenda.borrarPantalla()
            case "5":
                    agenda.eliminar_contacto(agenda_contacto)
                    agenda.borrarPantalla()
            case _:
                    agenda.borrarPantalla()

if __name__ == "__main__":
    main()
        