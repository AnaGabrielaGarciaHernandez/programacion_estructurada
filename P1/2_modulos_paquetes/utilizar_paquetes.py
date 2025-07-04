from paquete1 import modulos

print(modulos.saludar("DADDf"))

modulos.borrarPantalla()
nom,tel=modulos.solicitarDatos2()
print(f"\n\t.::Agenta Telefonica::.\n\t\tNombre: {nom}\n\t\tTelefono: {tel}")
modulos.espereTecla()