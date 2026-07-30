# ✅ Gestor de Tareas (terminal)

> Gestor de tareas sencillo por línea de comandos, en Python puro (sin librerías externas).
> Las tareas se guardan en un archivo de texto, así que **no se pierden al cerrar** el programa.

## Qué hace

- Añadir tareas.
- Listar las tareas numeradas, con marca `[X]` (completada) o `[ ]` (pendiente).
- Marcar una tarea como completada.
- Eliminar una tarea.

## Cómo funciona (decisiones)

- **Persistencia en `tareas.txt`:** cada tarea se guarda como `estado|texto` (una línea por
  tarea). Al abrir el programa se cargan; al cambiar algo, se reescribe el archivo. Sin base
  de datos: para este tamaño, un archivo de texto es lo más simple que funciona.
- **Cada tarea es un diccionario** `{"texto": ..., "completada": True/False}`, fácil de leer
  y de ampliar más adelante (por ejemplo, añadir una fecha).
- **Tolerante a la primera ejecución:** si `tareas.txt` aún no existe, empieza con una lista
  vacía en vez de fallar.

## Uso

```bash
python tareas.py
```

Sigue el menú por pantalla para añadir, listar, completar o eliminar tareas.

## Qué aprendí aquí

- Leer y escribir archivos de texto en Python (`open`, `with`, encoding UTF-8).
- Guardar datos con un formato propio (`estado|texto`) y volver a interpretarlos al cargar.
- Manejar el caso de que el archivo no exista todavía (`try/except FileNotFoundError`).
- Estructurar el programa en funciones pequeñas (cargar, guardar, listar, añadir…).

## Requisitos

- Python 3. Sin dependencias externas.
