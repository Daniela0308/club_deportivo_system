# Sistema de Gestión – Club Deportivo

## Descripción
Sistema de gestión en consola para un **club deportivo**, que permite administrar jugadores, pagos de mensualidades y control de deudas.

El objetivo del proyecto es practicar **programación estructurada en Python**, el uso de **listas y diccionarios**, y la **persistencia de datos mediante archivos JSON**, aplicando buenas prácticas de organización y separación de responsabilidades.

---

## Funcionalidades

### Gestión de jugadores
- Registrar jugadores con nombre y categoría
- Asignar ID único a cada jugador
- Cambiar el estado del jugador (activo / inactivo)
- Consultar información de un jugador
- Mostrar listados de jugadores

### Gestión de pagos
- Registrar pagos por uno o varios meses
- Generar IDs únicos para cada pago
- Actualizar automáticamente el último mes pagado
- Consultar pagos de un jugador
- Generar listado de jugadores con deuda

---

## Tecnologías utilizadas
- Python
- Terminal / Consola
- JSON para almacenamiento de datos
- Módulo estándar `datetime`
- Librería `dateutil.relativedelta` para el manejo de meses

---

## Cómo funciona

El sistema se ejecuta desde consola y muestra un **menú principal** que permite acceder a:

1. Gestión de jugadores
2. Gestión de pagos
3. Salir

Cada opción conduce a submenús que permiten realizar las distintas operaciones.

Los datos se almacenan en **listas de diccionarios** durante la ejecución y se guardan automáticamente en archivos JSON cada vez que se realiza una modificación.

---

## Estructura del proyecto
📌 Objetivo: gestión de jugadores y pagos con persistencia en JSON

- `club/`
  Carpeta principal del proyecto.

  - `main.py`
    Punto de entrada del sistema.
    Contiene los menús y controla el flujo del programa.

  - `club.py`
    Lógica principal del sistema.
    Funciones clave:
    - Registro y gestión de jugadores
    - Registro y consulta de pagos
    - Generación de listados (pagos y deudores)

  - `players.json`
    Archivo que almacena la información de los jugadores.

  - `payments.json`
    Archivo que almacena el historial de pagos.

  - `README.md`
    Documentación del proyecto.

---

## Aprendizajes
- Uso de listas y diccionarios para modelar información
- Persistencia de datos con archivos JSON
- Separación entre lógica del sistema y presentación
- Organización del código por bloques funcionales
- Aplicación de reglas de negocio
- Preparación del proyecto para una futura migración a **Programación Orientada a Objetos (POO)**



