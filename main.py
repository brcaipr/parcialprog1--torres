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
        print("*** Alumno", i + 1, "de", cantidad, "***")
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


def mostrar_estadisticas(nombres,promedios):
    """Muestro el promedio gral, el mayor y peor promedio y los alumnos aprobados/desaprobados"""
    promedio_general = procesamiento.calcular_promedio_general(promedios)
    mayor_indice = procesamiento.mayor_indice_prom(promedios)
    menor_indice = procesamiento.menor_indice_prom(promedios)

    print("El promedio general es: ", promedio_general)
    print("El mayor promedio es: ", promedios[mayor_indice], "y corresponde a: ", nombres[mayor_indice])
    print("El menor promedio es: ", promedios[menor_indice], "y corresponde a: ", nombres[menor_indice])



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
            case "4" | "5" | "6":
                print("Opción en mantenimiento.")
            case "0":
                print("Cerrando programa...")
            case _:
                print("Opción inválida")


main()
