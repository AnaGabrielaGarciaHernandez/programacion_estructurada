lista=[]

if len(lista)==0:
    resp="S"
    while resp=="S":
        agregar=input("Ingrese un registro: ").upper().strip()
        lista.append(agregar)
        resp=input("Desea ingresar otro? (S/N): ").upper().strip()

    for fila in lista:
        print(f"{lista[0]}")
