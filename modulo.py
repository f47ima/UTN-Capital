def crear_lista(valor_inicial, cantidad_elementos:int)-> list:
    """Crea una lista de elementos idénticos según lo que se indique como valor inicial.
    Recibe None | str | float | int para el valor incial y un int para la cantidad de elementos.
    Devuelve una lista con valores idénticos o una lista vacia. """
    lista = []
    if type(cantidad_elementos) == int:
        lista = [valor_inicial] * cantidad_elementos
    return lista

def crear_matriz(filas: int, columnas:int ,valor_inicial) -> list:
    """Crea una matriz de elementos idénticos según lo que se indique como valor inicial.
    Recibe None | str | float | int para el valor incial y un int para las filas y columnas de la matriz.
    Devuelve una matriz con valores idénticos o una matriz vacia. """
    matriz = []
    if type(filas) == int and type(columnas)== int:
        i = 0
        while i < filas: # El for me subrayaba la i y me molestaba
            matriz += [crear_lista(valor_inicial,columnas)] 
            i += 1
    return matriz


def encontrar_posicion(lista:list,elemento):
    posicion = None
    if len(lista)> 0 and len(elemento) > 0:
        for i in range(len(lista)):
            if elemento == lista[i]:
                posicion = i
    return posicion

def swap(lista, i, j):
    auxiliar = lista[i]
    lista[i] = lista[j]
    lista[j] = auxiliar

def ordenar_dos_listas_filas_ascendente(lista_datos,lista_filas):
    for i in range(0, len(lista_filas)-1):
        for j in range(i+1, len(lista_filas)):
            if lista_filas[i] > lista_filas[j]:
                swap(lista_filas,i,j)
                swap(lista_datos,i,j)

def ordenar_dos_listas_filas_descendente(lista_datos,lista_filas):
    for i in range(0, len(lista_filas)-1):
        for j in range(i+1, len(lista_filas)):
            if lista_filas[i] < lista_filas[j]:
                swap(lista_filas,i,j)
                swap(lista_datos,i,j)

def ordenar_dos_listas_segun_filas(lista_datos,lista_filas,booleano:bool= True):
    if booleano:
        ordenar_dos_listas_filas_ascendente(lista_datos,lista_filas)
    if not booleano:
        ordenar_dos_listas_filas_descendente(lista_datos,lista_filas)
    
def sumar_fila_matriz(matriz:list):
    lista = []
    for i in range(len(matriz)):
        suma = 0
        for j in range(len(matriz[0])):
            suma += matriz[i][j]
        lista = lista + [suma]
    return lista

def sumar_columna_matriz(matriz:list):
    lista = []
    for j in range(len(matriz[0])):
        suma = 0
        for i in range(len(matriz)):
            suma += matriz[i][j]
        lista = lista + [suma]
    return lista

def promediar_lista(lista_a_promediar,divisor):
    lista_promedios = []
    for i in range(len(lista_a_promediar)):
        promedio = lista_a_promediar[i] / divisor
        lista_promedios = lista_promedios +[promedio]
    return lista_promedios

def sumar_filas_con_precio_unitario(matriz_multiplicando:list,lista_multiplicador):
    lista = []
    for i in range(len(matriz_multiplicando)):
        suma_con_unitario = 0
        for j in range(len(matriz_multiplicando[0])):
            suma_con_unitario += matriz_multiplicando[i][j] * lista_multiplicador[j]
        lista = lista + [suma_con_unitario]
    return lista

def sumar_lista(lista):
    suma = 0
    for i in range(len(lista)):
        suma += lista[i]
    return suma 

def encontrar_maxima_accion(matriz:list):
    "Devuelve una lista de posiciones"
    lista = []
    for i in range(len(matriz)):
        bandera_primer_entrada = False
        for j in range(len(matriz[0])):
            if bandera_primer_entrada == True and maximo == matriz[i][j]:
                maximo = matriz[i][j]
                posicion_maximo = -1
            if bandera_primer_entrada == False or matriz[i][j] > maximo:
                maximo = matriz[i][j]
                posicion_maximo = j
                bandera_primer_entrada = True
        lista = lista +[posicion_maximo]
    return lista

def multiplicar_elementos_matriz(matriz_multipicando,lista_multiplicador):
    matriz = crear_matriz(len(matriz_multipicando),len(lista_multiplicador),0)
    for i in range(len(matriz_multipicando)):
        for j in range(len(matriz_multipicando[0])):
            matriz[i][j] = matriz_multipicando[i][j] * lista_multiplicador[j]
    return matriz

def encontrar_maximo_matriz(matriz):
    bandera = True
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if bandera or matriz[i][j] > maximo :
                maximo = matriz[i][j]
                fila_maximo = i
                columna_maximo = j
                bandera = False
    return maximo,fila_maximo,columna_maximo

def porcentajes_de_usuarios_sobre_inversion_total(lista_valores,valor_comparacion):
    lista_porcentajes = []
    for i in range(len(lista_valores)):
        porcentaje_usuario = (lista_valores[i]/ valor_comparacion) *100
        lista_porcentajes += [porcentaje_usuario]
    return lista_porcentajes

def posicionar_promedios_superiores(lista_valores,valor_comparacion):
    lista_posicion_promedios = []
    for i in range(len(lista_valores)):
        if lista_valores[i] > valor_comparacion:
            lista_posicion_promedios += [i]
    return lista_posicion_promedios

def crear_lista_segun_posiciones(lista_posiciones,lista_datos_existente):
    lista = []
    for i in range(len(lista_posiciones)):
        for j in range(len(lista_datos_existente)):
            if lista_posiciones[i] == j:
                posicion = lista_posiciones[i]
                lista = lista + [lista_datos_existente[posicion]]
    return lista 

def ordenar_lista_filas_ascendente(lista):
    for i in range(0, len(lista)-1):
        for j in range(i+1, len(lista)):
            if lista[i] > lista[j]:
                swap(lista,i,j)

def crear_lista_segun_posicion(posicion,matriz_datos_existente):
    lista = []
    for i in range(len(matriz_datos_existente)):
        for j in range(len(matriz_datos_existente)):
            lista += [matriz_datos_existente[i][posicion]]
    return lista 

def crear_lista_elementos_columna(matriz,posicion):
    lista = []
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if j == posicion:
                lista = lista + [matriz[i][j]]
    return lista