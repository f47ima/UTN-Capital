from validaciones import *
def mostrar_elementos_lista(lista:list):
    if len(lista) > 0:
        for i in range(len(lista)):
            print(lista[i])

def visualizar_datos(lista_usuarios, lista_acciones, lista_precio_unitario, matriz_datos):
    #se puede declarar una variable por cada print 
    print("______________________________________________________________________________________________")
    print(f"{'Usuario':<20} {'Acción':<10} {'Precio/u':>10} {'Cantidad':>10} {'Total':>12}")
    print("-" * 100)
    for i in range(len(lista_usuarios)):
        for j in range(len(lista_acciones)):
            usuario = lista_usuarios[i]
            accion = lista_acciones[j]
            precio = lista_precio_unitario[j]
            cantidad_acciones = matriz_datos[i][j]
            total = precio * cantidad_acciones
            print(f"{usuario:<20} {accion:<10} {precio:>10.2f} {cantidad_acciones:>10} {total:>12.2f}")
    print("______________________________________________________________________________________________")

def mostrar_dos_columnas(lista_descripcion,lista_con_datos,aclaracion:str= ""):
    for i in range(len(lista_con_datos)):
        definicion = lista_descripcion[i]
        dato = lista_con_datos[i]
        # if validar_float(dato):  
        #     dato = f"{dato:.2f}"
        print(f"{definicion:<20} {dato:<10} {aclaracion}")

def mostrar_maximos(lista_descripcion,lista_con_posiciones, lista_descripcion_de_posicion):
    for i in range(len(lista_descripcion)):
        if lista_con_posiciones[i] == -1:
            usuario = lista_descripcion[i]
            maximo = "No tuvo un maximo de compra."
        else:
            usuario = lista_descripcion[i]
            maximo = lista_descripcion_de_posicion[lista_con_posiciones[i]]
        print(f"{usuario:<20} {maximo:<30}")