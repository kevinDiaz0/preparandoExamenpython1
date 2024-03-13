bandas=[]


#construyendo la interfaz
print("***Altavoz es tu voz***")
print("***********************")

opcion = 100
while(opcion != 5):
    print("1. Registrar Banda")
    print("2. buscar bandas")
    print("3. agenda del evento")
    print("4. Modificar bandas")
    print("5. SALIR")
    opcion = int(input("Digita una opcion: "))

    if opcion==1:
        banda={}
        #creando los datos del diccionario
        banda["id"]=int(input("digite el id "))
        banda["nombre"]=input("Nombre de la banda: ")
        banda["genero"]=input("Genero: ")
        banda["clasificacion"]=input("Clasificacion: ")
        banda["tiempo"]=int(input("Tiempo: "))
        banda["costo"]=(input("digite el coste de la banda: $"))
        print(banda)

        bandas.append(banda)

    elif opcion==2:
        bandaBuscad =input("Digita el nombre de la banda que estas buscando: ")
        for bandaAx in bandas:
            if(bandaAx["nombre"] == bandaBuscad):
                print(f"id: {bandaAx["id"]} --- Nombre: {bandaAx["nombre"]}")
            else:
                print("false")
    elif opcion==3:
        print(bandas)
    elif opcion==4:
        pass
    elif opcion==5:
        pass
    else:
        pass

