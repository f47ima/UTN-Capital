from validaciones  import *
from output import *

def cargar_usuario(lista_usuarios:list,mensaje:str,mensaje_error:str):
    entrada_usuario = input(mensaje)
    normalizacion_usuario = capitalizar_cadena(entrada_usuario)
    while encontrar_elemento_en_lista(normalizacion_usuario,lista_usuarios) == False:
        entrada_usuario = input(mensaje_error)
        normalizacion_usuario = capitalizar_cadena(entrada_usuario)
    return normalizacion_usuario

def cargar_accion(lista_acciones:list,mensaje:str,mensaje_error:str):
    entrada_accion = input(mensaje)
    normalizacion_accion = cambiar_cadena_minus_mayus(entrada_accion)
    while encontrar_elemento_en_lista(normalizacion_accion,lista_acciones) == False:
        print("Solo se admiten acciones de: ") 
        mostrar_elementos_lista(lista_acciones)
        entrada_accion = input(mensaje_error)
        normalizacion_accion = cambiar_cadena_minus_mayus(entrada_accion)
    return normalizacion_accion

def cargar_inversion(mensaje, mensaje_error, minimo_importe,maximo_importe):
    entrada_inversion = input(mensaje)
    normalizacion_inversion = None
    validar_ingreso = False
    while not validar_ingreso:
        if validar_float(entrada_inversion):
            normalizacion_inversion = float(entrada_inversion)
            if normalizacion_inversion >= minimo_importe and normalizacion_inversion <= maximo_importe:
                validar_ingreso = True
            else:
                entrada_inversion = input(mensaje_error)
        else:
            entrada_inversion = input(mensaje_error)
    return normalizacion_inversion

def decidir_con_enteros(mensaje,mensaje_error,minimo:int,maximo:int):
    eleccion = input(mensaje)
    parsear_eleccion = None
    validacion_eleccion = False
    while not validacion_eleccion:
        if validar_entero(eleccion):
            parsear_eleccion = int(eleccion)
            if parsear_eleccion >= minimo and parsear_eleccion <= maximo:
                validacion_eleccion = True
            else:
                eleccion = input(mensaje_error)
        else:
            eleccion = input(mensaje_error)
    return parsear_eleccion









