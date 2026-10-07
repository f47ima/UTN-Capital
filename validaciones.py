
def verificar_minuscula(letra:str):
    """Verifica si un caracter es minuscula.
    Recibe un caracter.
    Devuelve True si es minusucla, False si no lo es o le pasaron algo mas largo que un solo caracter.
    """
    minuscula = False
    if len(letra) == 1:
        if (ord(letra) >= 97 and ord(letra) <= 122) or ord(letra) == 164 or ord(letra) == 241:
            minuscula = True
    return minuscula

def verificar_mayuscula(letra:str):
    """Verifica si un caracter es mayuscula.
    Recibe un caracter.
    Devuelve True si es mayuscula, False si no lo es o le pasaron algo mas largo que un solo caracter.
    """
    mayuscula = False
    if len(letra) == 1:
        if (ord(letra) >= 65 and ord(letra) <= 90) or ord(letra) == 165 or ord(letra) == 209:
            mayuscula = True
    return mayuscula

def cambiar_letra_minus_mayus(letra:str, booleano:bool = True) -> str:
    """Cambia una letra de mayuscula a minuscula o viceversa dependiendo del booleano indicado. Si la letra ya esta en el formato indicado no realiza ningun cambio y la devuelve igual.
    Recibe una letra (string de un carácter) y un booleano (True por defecto para convertir a mayúsculas).
    Devuelve una letra convertida o el mismo valor si no es un carácter único."""
    if type(letra) == str and len(letra) == 1:
        if booleano and verificar_minuscula(letra):
            letra = chr(ord(letra) - 32) 
        elif not booleano and verificar_mayuscula(letra):
            letra = chr(ord(letra) + 32) 
    return letra

def cambiar_cadena_minus_mayus(cadena:str, booleano:bool = True) -> str:
    """Cambia una cadena de mayuscula a minuscula o viceversa segun el booleano indicado.
    Recibe una cadena de texto y un booleano (True por defecto para convertir a mayúsculas).
    Devuelve una nueva cadena con los caracteres convertidos según el parámetro booleano."""
    nueva_cadena = ""
    if len(cadena) > 0:
        for i in range(len(cadena)):
            nueva_cadena += cambiar_letra_minus_mayus(cadena[i], booleano)
    return nueva_cadena

def capitalizar_cadena(cadena:str) -> str:
    """Capitaliza una cadena poniendo la primera letra en mayúscula y el resto en minúsculas.
    Recibe una cadena de texto.
    Devuelve una nueva cadena capitalizada."""
    cadena_capitalizada = ""
    if len(cadena) > 0:
        primer_caracter = cambiar_letra_minus_mayus(cadena[0], True)
        resto_cadena = cambiar_cadena_minus_mayus(cadena[1:],False)
        cadena_capitalizada = primer_caracter + resto_cadena
    return cadena_capitalizada

def devolver_lista_capitalizada(lista_cadenas:list) -> list:
    """Capitaliza todas las cadenas de una lista aplicando capitalizar_cadena a cada elemento.
    Recibe una lista de cadenas de texto.
    Devuelve una nueva lista con todas las cadenas capitalizadas."""
    lista = []
    for i in range(len(lista_cadenas)):
        lista += [capitalizar_cadena(lista_cadenas[i])]
    return lista 

def devolver_lista_convertida_a_mayus(lista_cadenas:list) -> list:
    """Convierte todas las cadenas de una lista a mayúsculas.
    Recibe una lista de cadenas de texto.
    Devuelve una nueva lista con todas las cadenas en mayúsculas."""
    lista = []
    for i in range(len(lista_cadenas)):
        lista += [cambiar_cadena_minus_mayus(lista_cadenas[i])]
    return lista

def devolver_lista_formateada(lista_cadenas:list, booleano:bool) -> list:
    """Formatea una lista de cadenas según el valor booleano: capitaliza si es True, convierte a mayúsculas si es False.
    Recibe una lista de cadenas de texto y un booleano.
    Devuelve una nueva lista formateada según el parámetro booleano."""
    if booleano:
        lista = devolver_lista_capitalizada(lista_cadenas)
    if not booleano:
        lista = devolver_lista_convertida_a_mayus(lista_cadenas)
    return lista

def encontrar_elemento_en_lista(elemento, lista:list) -> bool:
    """Valida que el ingreso se encuentre dentro de la lista indicada.
    Recibe un elemento de cualquier tipo y una lista.
    Devuelve True si el elemento está en la lista, False en caso contrario."""
    bandera = False
    for i in range(len(lista)):
        if elemento == lista[i]:
            bandera = True
            break
    return bandera

def validar_float(ingreso:str) -> bool:
    """Valida si una cadena representa un número flotante válido, incluyendo signos opcionales.
    Recibe una cadena de texto.
    Devuelve True si la cadena es un float válido, False en caso contrario."""
    inicio = 0
    valido = True
    punto= False
    digito = False
    if len(ingreso) > 0 and (ord(ingreso[0]) == 43 or ord(ingreso[0]) == 45):
        inicio = 1 
    if len(ingreso) > inicio:
        for i in range(inicio,len(ingreso)):
            orden = ord(ingreso[i])
            if orden == 46:
                if not punto:
                    punto = True
                else:
                    valido = False
            elif orden >= 48 and orden <= 57:
                digito = True
            else:
                valido = False
    else:
        valido = False
    bandera = valido and digito
    return bandera

def validar_entero(ingreso:str) -> bool:
    """Valida si una cadena representa un número entero válido, incluyendo signos opcionales.
    Recibe una cadena de texto.
    Devuelve True si la cadena es un entero válido, False en caso contrario."""
    bandera = False
    inicio = 0
    if len(ingreso) > 0 and (ord(ingreso[0]) == 43 or ord(ingreso[0]) == 45):
        inicio = 1 
    if len(ingreso) > inicio:
        for i in range(inicio,len(ingreso)):
            orden_numero = ord(ingreso[i])
            if (orden_numero >= 48 and orden_numero <= 57):
                bandera = True
            else:
                bandera = False
                break
    return bandera