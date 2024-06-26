L_1=[]
L_2=["Viña" , "Valparaiso" , "Quilpue"]
def Pedido_uwu():
            cliente=input(" Ingrese Nombre \n")
            direccion=input(" Ingrese Direccion \n ")
            sector=input(" Ingrese Sector \n ")
            print(" Seleccione Peso de cilindro ")
            cil_5=input(" 5Kg - Ingrese cantidad \n ")
            cil_15=input(" 15Kg - Ingrese cantidad \n")
            cil_45=input(" 45Kg - Ingrese cantidad \n")
            L_1.append([cliente, direccion, sector, ("5kg" ,cil_5 ), ("15kg" ,cil_15 ), ("45kg" ,cil_45)])

def imprimir_hoja_ruta():
    print(" Lugares disponibles para envios ")
    print(L_2)
    opcion_envio=input(" Ingrese lugar a revisar : ")
    if opcion_envio in (L_2):
        L_escribir=[]
        for pedido in L_1:
            sector_envio_pedido=pedido[2]
            #print(sector_envio_pedido)
            if opcion_envio.lower()==sector_envio_pedido.lower():
                L_escribir.append(pedido)

        if opcion_envio.lower()=="viña":
            with open("viña.txt", "w", ) as viña_txt:
                viña_txt.write(str(L_escribir))
        elif opcion_envio.lower()=="valparaiso":  
            with open("valparaiso.txt", "w", ) as valpo_txt:
                valpo_txt.write(str(L_escribir))
        elif opcion_envio.lower()=="quilpue":  
            with open("quilpue.txt", "w", ) as quilpue_txt:
                quilpue_txt.write(str(L_escribir))      
        print(" Archivo de texto escrito ")
    else:
        print("Lugar invalido")


while True:
        print("Elija una opcion : ")
        print("1.- Registrar pedido ")
        print("2.- Lista final de pedidos ")
        print("3.- Hoja de ruta ")
        print("4.- Salir ")
        x=input(" Elija una opcion : ")
        if x.lower()=="1":
            Pedido_uwu()
        elif x.lower()=="2":
            print(" Lista Final ")
            print(L_1)
        elif x.lower()=="3":
            imprimir_hoja_ruta()
        elif x.lower()=="4":
            print(" Fin del programa ")
            break
        print(" ------------------ ")