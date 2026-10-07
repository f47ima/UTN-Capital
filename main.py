import subprocess
from os import name
import sys
from entrada import *
from modulo import *
from validaciones import *
from output import *

def main() -> None:
    usuarios = ["lunatico_pixel","sombra_cristal","ecoerrante","navefantasma","bytesdelabahia","tintaenelviento","relojoxidado","miradacodificada","circuitoazul","fuego_niebla","teclaerrante","nebulosa_urbana","sueño_binario","saltofantasma","claveoculta"]
    usuarios_capitalizados = devolver_lista_formateada(usuarios,True)
    acciones= ["Apple", "Tesla", "NVIDIA"]
    acciones_mayusculas = devolver_lista_formateada(acciones,False)
    precio_acciones = [10.41,7.71,8.50]
    base_establecida = [[100.0, 50.0, 300.0],[200.0, 0.0, 450.0],[500.0, 150.0, 250.0],[400.0, 350.0, 50.0],[250.0, 100.0, 0.0],[300.0, 200.0, 500.0],[50.0, 450.0, 150.0],[350.0, 400.0, 100.0],[0.0, 500.0, 200.0],[150.0, 250.0, 300.0],[450.0, 50.0, 400.0],[200.0, 350.0, 250.0],[100.0, 500.0, 0.0],[300.0, 150.0, 450.0],[50.0, 400.0, 200.0]]
    print("Bienvenido a UTN Capital.")
    primer_paso = decidir_con_enteros("¿Como desea realizar la operacion?\n1.Inicializar una nueva base de datos.\n2.Cargar la base establecida con nuevas compras.\n3.Utilizar base de datos establecida.\n4.Salir.\n> ", "Seleccione solo uno de los numeros disponibles:\n>",1,4)
    requerimiento_de_carga = False
    match primer_paso:
        case 1:
            acciones_compradas = crear_matriz(len(usuarios), len(acciones), 0.0)
            menu_carga = True
            menu_principal = True
        case 2:
            acciones_compradas = base_establecida
            menu_carga = True
            menu_principal = True
        case 3:
            acciones_compradas = base_establecida
            menu_carga = False
            visualizacion = True
            menu_principal = True
        case 4:
            menu_principal = False
            menu_carga = False
            visualizacion = False
            submenu = False

    while menu_principal:
        while menu_carga:
            if requerimiento_de_carga and primer_paso == 1:
                cargar_o_cerrar = decidir_con_enteros("La inicializacion de la nueva base de datos precisa que cargue al menos un usuario con una compra mayor a 0.\nSeleccione como desea continuar:\n1.Continuar cargando datos.\n2.Salir del programa.", "Seleccione solo uno de los numeros disponibles:\n>",1,2)
                if cargar_o_cerrar == 2:
                    menu_principal = False
                    break
            usuario = cargar_usuario(usuarios_capitalizados,"Usuario: ","Solo se admiten usuarios VIP: ")
            posicion_fila = encontrar_posicion(usuarios_capitalizados,usuario)
            accion = cargar_accion(acciones_mayusculas,"Accion: ","Ingrese su eleccion: ")
            posicion_columna = encontrar_posicion(acciones_mayusculas,accion)
            compra = cargar_inversion("Ingrese el monto comprado: ", "EL rango de compra es entre 0 y 500:",0,500)
            if compra == 0:
                requerimiento_de_carga = True
            elif type(posicion_fila)== int and type(posicion_columna) == int and type(compra) == float:
                acciones_compradas[posicion_fila][posicion_columna] += compra
                total_transaccion = compra * precio_acciones[posicion_columna]  #ver aca
                
                requerimiento_de_carga = False
                print(f"El total invertido de esta transaccion fue: {total_transaccion}")
                continuar_carga = decidir_con_enteros("¿Desea continuar cargando compras?\n1.Si\n2.No\n>","Seleccione solo uno de los numeros disponibles:\n>",1,2)
                if continuar_carga == 2:
                    menu_carga = False
                    visualizacion = True
        while visualizacion:
            segundo_paso = decidir_con_enteros("¿Como desea continuar?\n1.Visualizar los datos y mostrar menu de opciones.\n2.Ir directamente al menu de opciones.\n3.Salir.\n>","Seleccione solo uno de los numeros disponibles:\n>",1,3)
            match segundo_paso:
                case 1:
                    ordenar_dos_listas_segun_filas(acciones_compradas,usuarios_capitalizados,True)
                    visualizar_datos(usuarios_capitalizados,acciones_mayusculas,precio_acciones,acciones_compradas)
                    submenu = True
                    visualizacion = False
                case 2:
                    submenu = True
                    visualizacion = False
                case 3:
                    menu_principal = False
                    visualizacion = False
                    submenu = False
        while submenu:
            print("______________________________________________________________________________________________")
            print("1.Cantidad total de acciones adquiridas por usuario.\n2.Promedio de acciones adquiridas de cada empresa entre todos los usuarios.\n3. Usuarios ordenados alfabéticamente de la Z-A junto con el total invertido en las distintas empresas.\n4.Inversión total acumulada por toda la cartera de usuarios.\n5.Por cada usuario, la empresa en la que compró más acciones.\n6. Acción con mayor inversión total (USD) en toda la cartera.\n7.Porcentaje de inversión por usuario respecto a la inversión total acumulada.\n8.Listado de los usuarios cuya inversión total supere la inversión promedio.\n9.Usuarios con acciones superior a promedio de Tesla.\n10.Salir")
            print("______________________________________________________________________________________________")
            tercer_paso  = decidir_con_enteros("Ingrese su preferencia:\n>", "Seleccione solo uno de los numeros disponibles:\n>",1,10)
            match tercer_paso:
                case 1:
                    ordenar_dos_listas_segun_filas(acciones_compradas,usuarios_capitalizados,True)
                    total_acciones_por_usuario = sumar_fila_matriz(acciones_compradas)
                    mostrar_dos_columnas(usuarios_capitalizados,total_acciones_por_usuario)
                case 2:
                    lista_suma_acciones = sumar_columna_matriz(acciones_compradas)
                    lista_promedios_acciones = promediar_lista(lista_suma_acciones,len(usuarios_capitalizados))
                    mostrar_dos_columnas(acciones_mayusculas,lista_promedios_acciones)
                case 3:
                    ordenar_dos_listas_segun_filas(acciones_compradas,usuarios_capitalizados,False)
                    lista_inversion_por_usuario = sumar_filas_con_precio_unitario(acciones_compradas,precio_acciones)
                    mostrar_dos_columnas(usuarios_capitalizados,lista_inversion_por_usuario,"USD")
                case 4:
                    lista_inversion_por_usuario = sumar_filas_con_precio_unitario(acciones_compradas,precio_acciones)
                    total_inversion = sumar_lista(lista_inversion_por_usuario)
                    print(f"EL total invertido por todos los usuarios es: {total_inversion} USD.")
                case 5:
                    ordenar_dos_listas_segun_filas(acciones_compradas,usuarios_capitalizados,True)
                    posiciones_maxima_accion_x_usuario = encontrar_maxima_accion(acciones_compradas)
                    mostrar_maximos(usuarios_capitalizados,posiciones_maxima_accion_x_usuario,acciones_mayusculas)
                case 6:
                    matriz_acciones_dolares = multiplicar_elementos_matriz(acciones_compradas,precio_acciones)
                    coordenadas_maxima_inversion_accion = encontrar_maximo_matriz(matriz_acciones_dolares)
                    nombre_maxima_inversion = acciones_mayusculas[coordenadas_maxima_inversion_accion[2]]
                    fila = coordenadas_maxima_inversion_accion[1]
                    columna= coordenadas_maxima_inversion_accion[2]
                    print(f"La accion con mayor inversion en cartera es: {nombre_maxima_inversion} con {matriz_acciones_dolares[fila][columna]}USD.")
                case 7:
                    lista_inversion_por_usuario = sumar_filas_con_precio_unitario(acciones_compradas,precio_acciones)
                    total_inversion = sumar_lista(lista_inversion_por_usuario)
                    ordenar_dos_listas_filas_ascendente(lista_inversion_por_usuario,usuarios_capitalizados)
                    lista_porcentajes_usuarios = porcentajes_de_usuarios_sobre_inversion_total(lista_inversion_por_usuario,total_inversion)
                    mostrar_dos_columnas(usuarios_capitalizados,lista_porcentajes_usuarios)
                case 8:
                    lista_inversion_por_usuario = sumar_filas_con_precio_unitario(acciones_compradas,precio_acciones)
                    total_inversion = sumar_lista(lista_inversion_por_usuario)
                    promedio_inversion = total_inversion / len(usuarios_capitalizados)

                    lista_posicion_promedios_superiores = posicionar_promedios_superiores(lista_inversion_por_usuario,promedio_inversion)
                    usuarios_superior_promedio = crear_lista_segun_posiciones(lista_posicion_promedios_superiores,usuarios_capitalizados)

                    ordenar_lista_filas_ascendente(usuarios_superior_promedio)
                    mostrar_elementos_lista(usuarios_superior_promedio)
                case 9:
                    lista_suma_acciones = sumar_columna_matriz(acciones_compradas)
                    lista_promedios_acciones = promediar_lista(lista_suma_acciones,len(usuarios_capitalizados))

                    posicion_tesla = encontrar_posicion(acciones_mayusculas,"TESLA")
                    if type(posicion_tesla) == int:
                        promedio_tesla = lista_promedios_acciones[posicion_tesla]

                        lista_tesla = crear_lista_elementos_columna(acciones_compradas, posicion_tesla)

                        lista_posicion_promedios_superiores = posicionar_promedios_superiores(lista_tesla,promedio_tesla)
                        usuarios_superior_tesla = crear_lista_segun_posiciones(lista_posicion_promedios_superiores,usuarios_capitalizados)
                        ordenar_lista_filas_ascendente(usuarios_superior_tesla)
                        mostrar_elementos_lista(usuarios_superior_tesla)
                case 10:
                    menu_principal = False
                    break

        if not menu_principal:
            subprocess.run(["cmd", "/c", "cls"] if name == "nt" else ["clear"])

if __name__ == "__main__":
    sys.exit(main())