def pedir_cantidad_alumnos():
    """Pide la cantidad de alumnos (entre 1 y 30) y la devuelve."""
    return pedir_entero_en_rango("Cantidad de alumnos (1 a 30): ",1, 30)


def es_entero(texto):
    """Devuelve True si el texto tiene al menos un carácter y son
    todos dígitos del 0 al 9."""
    if len(texto) == 0:
        return False
    for i in range(len(texto)):
        if not ("0" <= texto[i] <= "9"):
            return False
    return True


def es_letra_o_espacio(caracter):
    """Devuelve True si el carácter es una letra (a-z, A-Z) o un
    espacio."""
    es_minuscula = "a" <= caracter <= "z"
    es_mayuscula = "A" <= caracter <= "Z"
    es_espacio = caracter == " "
    return es_minuscula or es_mayuscula or es_espacio


def es_nombre_valido(nombre):
    """Devuelve True si el nombre tiene al menos 5 caracteres y
    contiene solo letras y espacios."""
    if len(nombre) < 5:
        return False
    for i in range(len(nombre)):
        if not es_letra_o_espacio(nombre[i]):
            return False
    return True


def pedir_entero_en_rango(mensaje, minimo, maximo):
    """Pide un número entero hasta que esté entre minimo y maximo
    (inclusive) y lo devuelve."""
    texto = input(mensaje)
    while not es_entero(texto) or not (minimo <= int(texto) <= maximo):
        print("Error: ingresá un número entero entre", minimo, "y",
              maximo)
        texto = input(mensaje)
    return int(texto)


def pedir_nota(numero_parcial):
    """Pide la nota del parcial indicado (entre 0 y 10) y la devuelve."""
    mensaje = "Nota del parcial " + str(numero_parcial) + " (0 a 10): "
    return pedir_entero_en_rango(mensaje, 0, 10)


def pedir_nombre():
    """Pide un nombre hasta que sea válido y lo devuelve."""
    nombre = input("Nombre del alumno: ")
    while not es_nombre_valido(nombre):
        print("Error: el nombre debe tener al menos", 5, "caracteres y solo letras y espacios.")
        nombre = input("Nombre del alumno: ")
    return nombre
