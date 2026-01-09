# Gestor de Contactos / Personas

## Descripción
Gestor de contactos en consola que permite agregar, ver, editar y eliminar personas.
El objetivo es practicar **listas y diccionarios en Python** y la **persistencia de datos usando JSON**.

## Funcionalidades
- Agregar contactos con: nombre, documento, categoría, teléfono y acudiente
- Ver todos los contactos registrados
- Editar datos de un contacto existente
- Eliminar contactos por número de documento
- Guardar y cargar datos automáticamente usando archivos JSON

## Tecnologías utilizadas
- Python
- Terminal / Consola
- JSON para almacenamiento de datos
- Módulo `storage.py` para manejar la lectura y escritura de contactos

## Cómo funciona
El programa muestra un menú en consola con distintas opciones.
El usuario elige una opción y el sistema ejecuta la acción correspondiente.

Los contactos se guardan en una lista de diccionarios mientras el programa está en ejecución y se actualizan automáticamente en un archivo JSON cada vez que se agregan, editan o eliminan.

## Estructura del proyecto
📌 Objetivo: persistencia de datos en JSON

- `02_datos_archivos/`
  Carpeta principal del proyecto.

  - `contactos.py`
    Lógica principal del programa y menú interactivo.
    Funciones clave:
    - `show_contacts()`: muestra todos los contactos
    - `add_contact()`: agrega un contacto nuevo
    - `edit_contact()`: modifica los datos de un contacto existente
    - `delete_contact()`: elimina contactos según el documento

  - `storage.py`
    Funciones para guardar y cargar contactos usando JSON.
    Funciones clave:
    - `load_data()`: carga los contactos desde el archivo JSON
    - `save_data()`: guarda los contactos en el archivo JSON

  - `data/`
    Carpeta donde se almacenan los archivos de datos.

    - `contactos.json`
      Archivo que contiene los contactos guardados.

  - `README.md`
    Documentación del proyecto.


## Aprendizajes
- Manejo de listas y diccionarios
- Uso de funciones para organizar la lógica del programa
- Modificación y eliminación segura de datos
- Persistencia de información mediante **lectura y escritura de archivos JSON**
- Separación de responsabilidades entre archivos y funciones










