import validaciones
import procesamiento


def carga_de_alumnos():
    """Pide los datos de todos los alumnos y devuelve las cuatro listas
    paralelas: nombres, notas del parcial 1, notas del parcial 2 y
    promedios."""
    nombres = []
    notas_parcial_1 = []
    notas_parcial_2 = []
    promedios = []

    cantidad = validaciones.pedir_cantidad_alumnos()

    for i in range(cantidad):
        print("Alumno", i + 1, "de", cantidad)
        nombre = validaciones.pedir_nombre()
        nota_1 = validaciones.pedir_nota(1)
        nota_2 = validaciones.pedir_nota(2)
        promedio = procesamiento.calcular_promedio(nota_1, nota_2)

        nombres = nombres + [nombre]
        notas_parcial_1 = notas_parcial_1 + [nota_1]
        notas_parcial_2 = notas_parcial_2 + [nota_2]
        promedios = promedios + [promedio]

    print("Se cargaron", cantidad, "alumnos correctamente.")
    return nombres, notas_parcial_1, notas_parcial_2, promedios


def mostrar_listado(nombres,nota_1,nota_2,promedios):
    """Muestra el nombre, las dos notas y el promedio total"""
    for i in range(len(nombres)):
        print(nombres[i], "1° Parcial:", nota_1[i], "2° Parcial:", nota_2[i], "Prom:", promedios[i])

#punto 3)
def mostrar_estadisticas(nombres,promedios):
    """Muestro el promedio gral, el mayor y peor promedio y los alumnos aprobados/desaprobados"""
    promedio_general = procesamiento.calcular_promedio_general(promedios)
    mayor_indice = procesamiento.mayor_indice_prom(promedios)
    menor_indice = procesamiento.menor_indice_prom(promedios)
    promocionados, aprobados, desaprobados = procesamiento.contar_por_nota(promedios)
    print("El promedio general es: ", promedio_general)
    print("El mayor promedio es: ", promedios[mayor_indice], "y corresponde a: ", nombres[mayor_indice])
    print("El menor promedio es: ", promedios[menor_indice], "y corresponde a: ", nombres[menor_indice])
    print("La cantidad de alumnos promocionados son: ", promocionados)
    print("La cantidad de alumnos aprobados son: ", aprobados)
    print("La cantidad de alumnos desaprobados son: ", desaprobados)

#Punto 5)
def buscar_alumno(nombres, nota_1, nota_2, promedios):
    nombre_buscado = input("Ingrese el nombre del alumno a buscar: ")
    indice_buscado = procesamiento.buscar_alumno(nombres, nombre_buscado)

    if indice_buscado == -1:
        print("El alumno ingresado no existe")
    else:
        print("Alumno: ", nombres[indice_buscado])
        print("Nota 1°: ", nota_1[indice_buscado])
        print("Nota 2|: ", nota_2[indice_buscado])
        print("Promedio: ", promedios[indice_buscado])

#Punto 6)
def jugar_con_nombre():
    nombre = validaciones.pedir_nombre()
    print("Nombre invertido: ", procesamiento.invertir_nombre(nombre))
    print("Cantidad de vocales contadas: ", procesamiento.contar_cant_vocales(nombre))
    
def mostrar_menu():
    """Muestra las opciones del menú principal."""
    print()
    print("===== NOTAFÁCIL =====")
    print("1. Cargar alumnos")
    print("2. Mostrar listado")
    print("3. Mostrar estadísticas")
    print("4. Ver ranking (ordenado)")
    print("5. Buscar alumno")
    print("6. Juegos con un nombre")
    print("0. Salir")


def main():
    """Repite el menú hasta que el usuario elija salir."""
    nombres = []
    notas_parcial_1 = []
    notas_parcial_2 = []
    promedios = []

    opcion = ""
    while opcion != "0":
        mostrar_menu()
        opcion = input("Elegí una opción: ")
        match opcion:
            case "1":
                nombres, notas_parcial_1, notas_parcial_2, promedios = (carga_de_alumnos())
            case "2":
                mostrar_listado(nombres, notas_parcial_1, notas_parcial_2, promedios)
            case "3":
                if len(nombres) == 0:
                    print("No se pueden mostrar estadisticas sin que se carguen alumnos.")
                else:
                    mostrar_estadisticas(nombres,promedios)
            case "4":
                print("Opción en mantenimiento.")
            case "5":
                if len(nombres) == 0:
                    print("No se pueden mostrar estadisticas sin que se carguen alumnos.")
                else:
                    buscar_alumno(nombres, notas_parcial_1, notas_parcial_2, promedios)
            case "6":
                jugar_con_nombre()
            case "0":
                print("Cerrando programa...")
            case _:
                print("Opción inválida")


main()
