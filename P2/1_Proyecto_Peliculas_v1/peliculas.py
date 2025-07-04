"""Funciones para borrar pantalla, esperar tecla y agregar una pelicula"""
import os
def borrar_pantalla():
    os.system("cls")

def esperar_tecla():
    input("\n ...Oprima un boton para continuar...")

peliculas=[]
def agregar():
    ingresar=input("\n Por favor ingrese una pelicula: ")
    peliculas.append(ingresar)

def borrar():
    print(f"\n Estas son sus pelicylas guardadas: \n {peliculas}")
    borrar=input("¿Que pelicula desea borrar?: ")
    peliculas.remove(borrar)
    print(f"\n Su nueva lista de peliculas es: \ns {peliculas}")
    return peliculas

def consultar():
  print(".:: Consultar o Mostrar las Peliculas ::.")
  if len(peliculas)>0:
    for i in range(0,len(peliculas)):
      print(f"{i+1}:{peliculas}")
  else:
    print("\t .:: No hay peliculas en el Sistema ::.")

def buscar():
  print("\n\t.:: Buscar peliculas ::.")
  pelicula_buscar=input("Ingrese el nombre de la pelicula a buscar: ").upper().strip()
  encontro=0
  if not(pelicula_buscar in peliculas):
    print("\n\t\t ¡No se encuentra la pelicula a buscar!")
  else:
    for i in range (0,len(peliculas)):
      if pelicula_buscar==peliculas[i]:
        print(f"La pelicula {pelicula_buscar} si la tenemos y esta en la casilla: {i+1}")
        encontro+=1
    if encontro>=0:
      print(f"Tenemos {encontro} pelicula(s) con este titulo")
      input("\n\t\t\t :::LA OPERACION SE REALIZO CORRECTAMENTE:::")

def actualizar():
   print("\n\t.:: Modificar Películas ::. \n")
   pelicula_buscar=input("Ingrese el nombre de la película que desea buscar: ").upper().strip()
   encontro=0
   if not(pelicula_buscar in peliculas): 
      print("\n\t\t ¡No se encuentra la película a buscar!")   
   else:   
      for i in range(0,len(peliculas)):
        if pelicula_buscar==peliculas[i]:
          resp=input("¿Deseas actualizar la pelicula? (Si/No) ").lower()
          if resp=="si":
             peliculas[i]=input("\nIntroduce el nuevo nombre de la película: ").upper().strip()
             encontro+=1
             print("\n\t\t::: ¡LA OPERACION SE REALIZO CON ÉXITO! :::")
      
      print(f"\nSe modifico {encontro} pelicula(s) con este titulo")

def vaciar_lista():
    peliculas.clear
    print("\n Su lista fue borrada...")
    print(peliculas)