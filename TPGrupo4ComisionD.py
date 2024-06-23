from funcionesGrupo4ComisionD import *

print("--------------------")

loop=True
while loop: 
    opcion1 = menu_principal()
    print ("--------------------")
    if opcion1 == 1:
        print("Cargando datos...")
        cargar_datos()
        print ("--------------------")
    elif opcion1 == 2:
        loop2 = True
        while loop2:
            opcion2 = menu_secundario()
            print ("--------------------")

            if opcion2 == 1:
                print("\tMostrando Las 5 publicaciones con mejor calificación")
                mejores_5()
                print ("--------------------")
            elif opcion2 == 2:
                print("\tEl usuario publicador con más comentarios positivos.")
                suma_mas_alta()
                print ("--------------------")

            elif opcion2 == 3:
                print("\t El usuario con mayor participación.")
                participaciones_usuarios()
                print ("--------------------")

            elif opcion2 == 4:
                print("Saliendo del menu secundario")
                loop2 = False
                print ("--------------------")
                    
    elif opcion1 == 3:
        print("\t\t REPORTES ")
        loop3 = True
        while loop3:

            opcion3 = menu_reportes()

            if opcion3 == None:
                print ("Intentos excedidos. Volviendo al menu principal...")
                loop3 = False
                print ("--------------------")

            else:
                reporte(opcion3)
                print ("--------------------")
                loop3= False
                


    elif opcion1 == 4:
        print("Saliendo del menu principal. Gracias por utlizar el programa.")
        loop = False

