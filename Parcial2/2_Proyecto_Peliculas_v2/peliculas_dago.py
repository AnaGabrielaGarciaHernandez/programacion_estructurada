peliculas=[]

#Dic u objetonpara almacenar los atributos(nombre, categoria,clasificacion,genero,idioma de las peliculas)
#peliculas{
#  "nombre":"",
#  "categoria":"",
#  "clasificacion":"",
#  "genero":"",
#  "idioma":""
#}

pelicula={}
def borrarPantalla():
  import os  
  os.system("cls")

def esperarTecla():
  print("`\u26A0`Oprima cualquier tecla para continuar ...`\u26A0`")
  input()  

def crearPeliculas():
  borrarPantalla()
  print(".:: Alta de Peliculas ::. ")
  pelicula.update({"nombre":input("`\U0001F4DD` nombre: ").upper().strip()})
  pelicula.update({"categoria":input("`\U0001F4DD` categoria: ").upper().strip()})
  pelicula.update({"clasificacion":input("`\U0001F4DD` clasificacion: ").upper().strip()})
  pelicula.update({"genero":input("`\U0001F4DD` genero: ").upper().strip()})
  pelicula.update({"idioma":input("`\U0001F4DD` idioma: ").upper().strip()})
  print("\n\t\t\t `\U0001F389`:::LA OPERACION SE REALIZO CORRECTAMENTE:::`\U0001F389`")

def mostrarPeliculas():
  borrarPantalla()
  print(".:: Consultar o Mostrar las Peliculas ::.")
  if len(pelicula)>0:
    for i in pelicula:
      print(f"{(i)}:{pelicula[i]}")
  else:
    print("\t `\u274C`.:: No hay peliculas en el Sistema ::.`\u274C`")

def borrarPeliculas():
  borrarPantalla()
  print("\n\t.:: Borrar o quitar TODAS las peliculas ::.")
  resp=input("`\u26A0`¿Deseas quitar o borrar todas las peliculas del sistema? (Si/No)`\u26A0`").lower()
  if resp=="si":
    pelicula.clear()
    print("\n\t\t\t `\U0001F389`:::LA OPERACION SE REALIZO CORRECTAMENTE:::`\U0001F389`")

def agregarCaracteristicaPeliculas():
  borrarPantalla()
  print("\n\t.:: Agregar Caracteristica a Peliculas ::.")
  atributo=input("Ingresa la nueva caracteristica de la peliculas: ").lower().strip()
  valor=input("El valor de la caracteristica de la pelicula: ").upper().strip()
  pelicula.update({atributo:valor})
  print("\n\t\t\t `\U0001F389`:::LA OPERACION SE REALIZO CORRECTAMENTE:::`\U0001F389`")

def modificarCaracteriscticaPeliculas():
  borrarPantalla()
  print("\n\t.:: Modificar Caracteristicas a Peliculas ::.")
  if len(pelicula)>0:
    print("\n\Valores Actuales: \n")
    for i in pelicula:
      print(f"{(i)}: {pelicula[i]}")
      resp=input(f"\t¿Desea cambiar el valor de {i}? (si/no)").lower().strip()
      if resp=="si":
        pelicula.update({f"{i}":input("\tEl valor nuevo: ").upper().strip()})
        print("\n\t\t`\U0001F389`::: ¡LA OPERACION SE REALIZO CON ÉXITO! :::`\U0001F389`")
        esperarTecla()
        borrarPantalla()
  else:
    print("\t`\u26A0` No hay Peliculas en el Sistemta...`\u26A0` ")
    esperarTecla()
    borrarPantalla()

def borrarCaracteristicaPeliculas():
  borrarPantalla()
  print("\n\t.::Borrar Caracteristicas a Peliculas::.")
  if len(pelicula)>0:
    print("\n\tValores Actuales: \n")
    for i in pelicula:
      print(f"\t{(i)}: {pelicula[i]}")
    resp=input(f"\n\tDesea borrar una caracteristica? (si/no)").lower().strip() 
    if resp== "si":
      atributo=input("Ingresa la caracteristica de la pelicula que quieras borrar o quitar?") 
      pelicula.pop(atributo)
      print("\n\t\t`\U0001F389`::: ¡LA OPERACION SE REALIZO CON ÉXITO! :::`\U0001F389`")
      esperarTecla()
      borrarPantalla()
  else:
    print("\t`\u26A0`No hay Peliculas en el Sistemta...`\u26A0`")
    esperarTecla()
    borrarPantalla()


"""def modificarCaracteristicaPeliculas():
  borrarPantalla()
  print("\n\t.:: Modificar Caracteristicas a Peliculas ::.")
  pelicula_buscar=input("Ingrese el nombre de la película que desea buscar: ").upper().strip()
  encontro=0
  if not(pelicula_buscar in pelicula): 
    print("\n\t\t `\u274C`¡No se encuentra la película a buscar!`\u274C`")   
  else:  
    for i in range(0,len(pelicula)):
      if pelicula_buscar==pelicula[i]:
        resp=input("`\u26A0`¿Deseas actualizar la pelicula? (Si/No) `\u26A0`").lower()
        if resp=="si":
          atributo=input("Ingresa la nueva caracteristica de la peliculas: ").lower().strip()
          valor=input("El valor de la caracteristica de la pelicula: ").upper().strip()
          pelicula.update({atributo:valor})
          encontro+=1
          print("\n\t\t`\U0001F389`::: ¡LA OPERACION SE REALIZO CON ÉXITO! :::`\U0001F389`")
    print(f"\nSe modifico {encontro} pelicula(s) con este titulo")"""

"""def borrarCaracteristicaPeliculas():
  borrarPantalla()
  print("\n\t.:: Borrar Caracteristica de una Pelicula ::.\n")
  pelicula_buscar=input("Ingrese el nombre de la pelicula que desea buscar: ").upper().strip()
  encontro=0
  if not(pelicula_buscar in pelicula): 
    print("\n\t\t `\u274C`¡No se encuentra la pelicula a buscar!`\u274C`")   
  else: 
    resp="si"  
    while pelicula_buscar in pelicula and resp=="si":
        resp=input("`\u26A0`¿Deseas quitar o borrar alguna caracterisica de la pelicula (Si/No)?`\u26A0`").lower()
        if resp=="si":
          atributo=input("Ingresa la nueva caracteristica de la peliculas: ").lower().strip()
          valor=input("El valor de la caracteristica de la pelicula: ").upper().strip()
          pelicula.pop({atributo:valor})
          print(f"\nLa caracteristica que se borro es: {valor} del atributo: {atributo}")
          encontro+=1
          print("\n\t\t`\U0001F389`::: ¡LA OPERACION SE REALIZO CON ÉXITO! :::`\U0001F389`")
    print(f"Se borro {encontro} pelicula(s) con este titulo")"""

