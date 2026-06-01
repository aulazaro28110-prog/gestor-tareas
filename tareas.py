"""
Gestor de tareas sencillo para la terminal.

Permite:
  1. Anadir tareas
  2. Listar tareas numeradas
  3. Marcar una tarea como completada
  4. Eliminar una tarea

Las tareas se guardan en el archivo 'tareas.txt' para que no se
pierdan al cerrar el programa.
"""

# Nombre del archivo donde se guardan las tareas
ARCHIVO = "tareas.txt"


def cargar_tareas():
    """Lee las tareas guardadas en el archivo y las devuelve como una lista."""
    tareas = []
    try:
        with open(ARCHIVO, "r", encoding="utf-8") as f:
            for linea in f:
                linea = linea.strip()
                if not linea:
                    continue
                # Cada linea se guarda como  "estado|texto"
                # estado puede ser "1" (completada) o "0" (pendiente)
                estado, texto = linea.split("|", 1)
                tareas.append({"texto": texto, "completada": estado == "1"})
    except FileNotFoundError:
        # Si el archivo aun no existe, empezamos con una lista vacia
        pass
    return tareas


def guardar_tareas(tareas):
    """Guarda la lista de tareas en el archivo."""
    with open(ARCHIVO, "w", encoding="utf-8") as f:
        for tarea in tareas:
            estado = "1" if tarea["completada"] else "0"
            f.write(estado + "|" + tarea["texto"] + "\n")


def listar_tareas(tareas):
    """Muestra las tareas numeradas en pantalla."""
    if not tareas:
        print("\nNo hay tareas todavia.")
        return

    print("\nTus tareas:")
    for numero, tarea in enumerate(tareas, start=1):
        marca = "[X]" if tarea["completada"] else "[ ]"
        print(f"  {numero}. {marca} {tarea['texto']}")


def anadir_tarea(tareas):
    """Pide al usuario una tarea nueva y la anade a la lista."""
    texto = input("Escribe la nueva tarea: ").strip()
    if texto == "":
        print("La tarea esta vacia, no se ha anadido.")
        return
    tareas.append({"texto": texto, "completada": False})
    guardar_tareas(tareas)
    print("Tarea anadida.")


def pedir_numero(tareas):
    """Pide un numero de tarea valido y devuelve su posicion (indice)."""
    listar_tareas(tareas)
    if not tareas:
        return None
    try:
        numero = int(input("Escribe el numero de la tarea: "))
    except ValueError:
        print("Eso no es un numero valido.")
        return None

    if 1 <= numero <= len(tareas):
        return numero - 1  # convertimos a indice de lista (empieza en 0)
    else:
        print("Ese numero no existe en la lista.")
        return None


def completar_tarea(tareas):
    """Marca una tarea como completada."""
    indice = pedir_numero(tareas)
    if indice is None:
        return
    tareas[indice]["completada"] = True
    guardar_tareas(tareas)
    print("Tarea marcada como completada.")


def eliminar_tarea(tareas):
    """Elimina una tarea de la lista."""
    indice = pedir_numero(tareas)
    if indice is None:
        return
    tarea = tareas.pop(indice)
    guardar_tareas(tareas)
    print(f"Tarea eliminada: {tarea['texto']}")


def mostrar_menu():
    """Muestra las opciones del programa."""
    print("\n===== GESTOR DE TAREAS =====")
    print("1. Anadir tarea")
    print("2. Listar tareas")
    print("3. Marcar tarea como completada")
    print("4. Eliminar tarea")
    print("5. Salir")


def main():
    """Bucle principal del programa."""
    tareas = cargar_tareas()

    while True:
        mostrar_menu()
        opcion = input("Elige una opcion (1-5): ").strip()

        if opcion == "1":
            anadir_tarea(tareas)
        elif opcion == "2":
            listar_tareas(tareas)
        elif opcion == "3":
            completar_tarea(tareas)
        elif opcion == "4":
            eliminar_tarea(tareas)
        elif opcion == "5":
            print("Hasta luego!")
            break
        else:
            print("Opcion no valida. Escribe un numero del 1 al 5.")


# Esto hace que el programa se ejecute solo cuando lo lanzas tu
if __name__ == "__main__":
    main()
