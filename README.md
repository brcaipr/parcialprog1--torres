# NotaFácil

Este proyecto es el primer parcial de Programación I Div 313. Hice un programa de consola para que Laura, coordinadora del Instituto Horizonte, pueda cargar las notas de sus alumnos y ver las estadísticas del curso sin usar la calculadora.

Qué hace el programa

Desde un menú se puede:

1. Cargar entre 1 y 30 alumnos con su nombre y las notas de los dos parciales.
2. Ver el listado de alumnos con sus notas y su promedio.
3. Ver las estadísticas: promedio general, mejor y peor promedio, y cuántos alumnos promocionan, aprueban y desaprueban.
4. Ver el ranking del curso, ordenado de mayor a menor promedio con el método burbuja.
5. Buscar un alumno por su nombre y ver cómo le fue.
6. Jugar con un nombre: contar sus vocales y mostrarlo al revés.

Qué contiene
main.py - El menú principal y el flujo del programa
validaciones.py - Funciones que validan nombre, notas y cantidad de alumnos
procesamiento.py - Promedios, estadísticas, ordenamiento burbuja y funciones sobre cadenas

Cómo ejecutarlo

Desde la carpeta del proyecto:

python main.py

Como pedía la consigna, lo resolví sin métodos de listas ni de strings, sin try/except y sin funciones como sum(), max() o sorted(). Todo está hecho con bucles, índices y funciones propias.
