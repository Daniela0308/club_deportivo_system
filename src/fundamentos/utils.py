#Funcion para agregar las tareas
def agregar_tareas(list_tareas):
    tarea = input('Ingresa la descripción de la tarea: ')
    if not tarea:
        print("La tarea NO puede estar vacía. Intenta de nuevo.")
    else:
        list_tareas.append({
            "Descripcion": tarea,
            "Completada": False})
        print("Tarea agregada corectamente!")

#Funcion para mostrar las tareas
def mostrar_tareas(list_tareas):
    if list_tareas:
        print("--- TAREAS ---")
        for contador, tarea in enumerate(list_tareas, start=1):
            estado = "Completado" if tarea["Completada"] else "Pendiente"
            print(f"{contador}. {tarea["Descripcion"]} [{estado}]")
    else:
        print(f'No hay tareas por mostrar')

#Funcion para completar las tareas
def completar_tarea(list_tareas):
    mostrar_tareas(list_tareas)
    id = int(input("Ingrese el número de la tarea a completar: "))

    if id < 0 or id > len(list_tareas):
        print("Índice inválido")
    else:
        list_tareas[id - 1]["Completada"] = True
        print(f'✅ Tarea marcada como realizada"')

#Funcion para eliminar las tareas
def eliminar_tareas(list_tareas):
    mostrar_tareas(list_tareas)
    id_eliminar = int(input("Ingrese el número de la tarea para eliminar: "))

    if id_eliminar < 0 or id_eliminar > len(list_tareas):
        print("Índice inválido")
    else:
        list_tareas.pop(id_eliminar-1)
    print("Tarea eliminada")