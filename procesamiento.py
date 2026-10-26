#CONSTANTES

NOTA_PROMOCION = 6
NOTA_APROBACION = 4


def calcular_promedio(nota_1, nota_2):
    """Devuelve el promedio entre las dos notas de un alumno."""
    return (nota_1 + nota_2) / 2


def calcular_promedio_general(promedios):
    """Devuelve el promedio de todos los promedios del curso."""
    acumulador = 0
    for i in range(len(promedios)):
        acumulador = acumulador + promedios[i]
    return acumulador / len(promedios)


def mayor_indice_prom(promedios):
    """Devuelve la posición del alumno con el promedio más alto, buscando por indice [i]."""
    mayor_indice = 0
    for i in range(1, len(promedios)):
        if promedios[i] > promedios[mayor_indice]:
            mayor_indice =i
    return mayor_indice


def menor_indice_prom(promedios):
    """Devuelve la posición del alumno con el promedio más alto, buscando por indice [i]."""
    menor_indice = 0
    for i in range(1, len(promedios)):
        if promedios[i] < promedios[menor_indice]:
            menor_indice = i
    return menor_indice


def contar_por_nota(promedios):
    """cuenta los alumnos dependiendo de la nota"""
    promocion = 0
    aprobados = 0
    desaprobados = 0
    for i in range(len(promedios)):
        if promedios[i] >= NOTA_PROMOCION:
            promocion = promocion + 1
        elif promedios[i] >= NOTA_APROBACION:
            aprobados = aprobados + 1
        else:
            desaprobados = desaprobados + 1
    return promocion, aprobados, desaprobados