# 🏆 Sistema de Gestión Club Deportivo (POO)

## Descripción
Sistema de gestión administrativa para un club deportivo desarrollado en consola.  
Permite registrar jugadores, controlar su estado, registrar pagos mensuales y consultar historiales.

El objetivo del proyecto es practicar **Programación Orientada a Objetos (POO)**, **arquitectura por capas** y **persistencia de datos usando JSON**.

---

## Funcionalidades

- Registrar jugadores con nombre y categoría  
- Ver todos los jugadores registrados  
- Activar e inactivar jugadores  
- Registrar pagos de mensualidades  
- Consultar historial de pagos por jugador  
- Ver listado general de pagos  
- Identificar jugadores con deudas  
- Guardar y cargar datos automáticamente usando archivos JSON  

---

## Tecnologías utilizadas

- Python  
- Terminal / Consola  
- JSON para almacenamiento de datos  
- Librería `datetime` para manejo de fechas  
- Librería `dateutil` para cálculo de meses  
- Arquitectura modular basada en capas  

---

## Cómo funciona

El programa muestra un menú en consola con distintas opciones.

El usuario selecciona una opción y el sistema ejecuta la acción correspondiente mediante:

- Capa de interfaz (UI)
- Capa de servicios (casos de uso)
- Capa de modelos (lógica del negocio)
- Capa de repositorios (persistencia de datos)

Los jugadores y pagos se almacenan en listas mientras el programa está en ejecución y se guardan automáticamente en archivos JSON después de cada operación.

---

## Estructura del proyecto

📌 Objetivo: aplicar POO y persistencia de datos en JSON

```
club_poo/
│
├── models/
│   ├── __init__.py
│   ├── club.py
│   ├── player.py
│   └── payment.py
│
├── services/
│   ├── __init__.py
│   ├── player_service.py
│   └── payment_service.py
│
├── persistence/
│   ├── __init__.py
│   ├── player_repository.py
│   └── payments_repository.py
│
├── config/
│   ├── __init__.py
│   ├── error_codes.py
│   ├── paths.py
│   ├── messages.py
│   └── message_translator.py
│
├── ui/
│   └── main_menu.py
│
├── data/
│   ├── players.json
│   └── payments.json
│
└── main.py
```

---

### 📂 models/
Contiene las clases principales del sistema.

#### club.py
Maneja la lógica general del club.

Funciones principales:
- Registrar jugadores
- Registrar pagos
- Controlar deudores
- Generar historial de pagos

#### player.py
Representa un jugador del club.

#### payment.py
Representa un pago realizado por un jugador.

---

### 📂 services/
Contiene los casos de uso del sistema.

#### player_service.py
Maneja operaciones relacionadas con jugadores.

#### payment_service.py
Maneja operaciones relacionadas con pagos.

---

### 📂 repositories/
Gestiona la persistencia de datos usando JSON.

#### player_repository.py
Carga y guarda jugadores.

#### payments_repository.py
Carga y guarda pagos.

---

### 📂 config/
Contiene configuraciones generales del sistema.

#### paths.py
Define rutas seguras hacia los archivos JSON.

#### messages.py
Contiene los mensajes del sistema.

#### message_translator.py
Traduce códigos internos a mensajes para el usuario.

---

### 📂 ui/
Contiene la interfaz del sistema.

#### ui_main.py
Maneja el menú interactivo y la comunicación con el usuario.

---

### 📄 main.py
Punto de entrada del programa.

Funciones principales:
- Inicializa el club
- Carga datos desde JSON
- Ejecuta la interfaz del sistema

---

## Cómo ejecutar el proyecto

1. Clonar el repositorio

```bash
git clone <URL_DEL_REPOSITORIO>
```

2. Entrar a la carpeta del proyecto

```bash
cd club_deportivo_system/src
```

3. Ejecutar el programa

```bash
python -m club_poo.main.py
```

---

## Aprendizajes

- Implementación de Programación Orientada a Objetos
- Uso de clases, propiedades y métodos
- Separación de responsabilidades mediante arquitectura por capas
- Manejo de persistencia con archivos JSON
- Organización modular del código
- Manejo de fechas y cálculos de mensualidades
- Uso de repositorios y servicios para desacoplar lógica del sistema

