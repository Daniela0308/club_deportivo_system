from utils import (agregar_tareas, mostrar_tareas, completar_tarea, eliminar_tareas)

list_tareas = []

#Menu de mi CRUD tareas
while True:
    print("--- MENÚ DE TAREAS ---")
    print("1. Agregar tareas \n2. Mostrar tareas \n3. Completar tarea \n4. Eliminar Tarea \n5. Salir")
    opcion = int(input('Selecciona una opción: '))
    if opcion == 1:
        agregar_tareas(list_tareas)
    elif opcion == 2:
        mostrar_tareas(list_tareas)
    elif opcion == 3:
        completar_tarea(list_tareas)
    elif opcion == 4:
        eliminar_tareas(list_tareas)
    elif opcion == 5:
        print("Saliendo del programa...")
        break
    else:
        print("Opción no valida. Intente de nuevo.")



