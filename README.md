# 🏆 Club Deportivo Management System

Sistema de gestión administrativa para un club deportivo desarrollado progresivamente como proyecto de aprendizaje y portafolio profesional.

---

## 🎯 Objetivo

Desarrollar un sistema completo para administrar jugadores, pagos, roles y control interno de un club deportivo, aplicando buenas prácticas de programación, arquitectura de software y desarrollo backend.

---

## 🧱 Tecnologías

- Python
- Git & GitHub
- JSON (persistencia actual)
- PostgreSQL (base de datos futura)
- FastAPI (próximamente)
- Frontend web (próximamente)

---

## 🚀 Progreso del Proyecto

- 🟢 Nivel 1 – Fundamentos (Completado)
- 🟢 Nivel 2 – Persistencia con archivos (Completado)
- 🟢 Nivel 3 – Sistema básico del club (Completado)
- 🟢 Nivel 4 – Programación orientada a objetos (Completado)
- ⏳ Nivel 5 – Base de datos con PostgreSQL
- ⏳ Nivel 6 – API Backend
- ⏳ Nivel 7 – Autenticación y roles
- ⏳ Nivel 8 – Frontend web
- ⏳ Nivel 9 – Sistema completo

---

## 📊 Estado Actual del Proyecto

### 🟢 Nivel 1 – Fundamentos

Se desarrolló un gestor de tareas en consola enfocado en:

- Uso de variables
- Condicionales
- Ciclos
- Funciones
- Organización básica del código

Este nivel permitió comprender la lógica fundamental de programación en Python.

---

### 🟢 Nivel 2 – Persistencia con Archivos

Se desarrolló un gestor de contactos que permite:

- Agregar contactos
- Ver contactos registrados
- Editar contactos
- Eliminar contactos
- Persistencia de datos usando archivos JSON
- Separación de responsabilidades mediante módulo de almacenamiento

Se implementaron funciones principales:

- `load_data()`
- `save_data()`

---

### 🟢 Nivel 3 – Sistema Básico del Club Deportivo

Se desarrolló un sistema funcional para administración deportiva que permite:

- Registrar jugadores
- Buscar jugadores
- Activar o desactivar jugadores
- Registrar pagos de mensualidades
- Registrar pagos por múltiples meses consecutivos
- Mantener historial completo de pagos
- Actualizar automáticamente el último mes pagado
- Generar listado de jugadores con deuda

Características técnicas:

- Uso de listas y diccionarios
- Persistencia con archivos JSON
- Separación entre lógica del sistema y presentación

---

### 🟢 Nivel 4 – Programación Orientada a Objetos

El sistema fue rediseñado completamente aplicando principios de POO y arquitectura por capas.

Se implementó:

#### 🧩 Modelado Orientado a Objetos
- Clase `Club`
- Clase `Player`
- Clase `Payment`

#### 🏗️ Arquitectura por Capas
- Models (lógica del negocio)
- Services (casos de uso)
- Repositories (persistencia de datos)
- Config (mensajes y rutas del sistema)
- UI (interfaz de usuario)

#### ⚙️ Mejoras Técnicas Implementadas
- Encapsulamiento de atributos
- Uso de propiedades (`@property`)
- Métodos de clase (`@classmethod`)
- Manejo desacoplado de mensajes del sistema
- Persistencia modular con repositorios
- Organización profesional del proyecto
- Manejo automático de mensualidades y fechas
- Recalculo automático de identificadores internos

---

## 🏗️ Arquitectura del Proyecto

El sistema implementa una arquitectura escalable basada en capas:

```
UI Layer
   ↓
Services Layer
   ↓
Business Logic (Models)
   ↓
Repository Layer
   ↓
Data Storage (JSON → PostgreSQL)
```

---

## 📌 Roadmap del Proyecto

### ⏳ Nivel 5 – Base de Datos con PostgreSQL

Se realizará la migración del sistema de almacenamiento en JSON hacia una base de datos relacional PostgreSQL.

Objetivos:

- Diseño del modelo relacional del sistema
- Implementación de tablas para jugadores y pagos
- Uso de claves primarias y foráneas
- Integración mediante ORM (SQLAlchemy)
- Implementación de migraciones de base de datos

---

### ⏳ Nivel 6 – API Backend

- Desarrollo de API REST
- Implementación con FastAPI
- Serialización y validación de datos

---

### ⏳ Nivel 7 – Autenticación y Roles

- Sistema de usuarios
- Control de permisos
- Seguridad de endpoints

---

### ⏳ Nivel 8 – Frontend Web

- Interfaz gráfica del sistema
- Consumo de API
- Panel administrativo

---

### ⏳ Nivel 9 – Sistema Completo

- Integración total del sistema
- Optimización
- Despliegue del proyecto

---

## 📚 Objetivos de Aprendizaje del Proyecto

- Programación orientada a objetos
- Arquitectura de software
- Persistencia de datos
- Modelado relacional
- Desarrollo backend
- Diseño de sistemas escalables
- Buenas prácticas de desarrollo
- Control de versiones con Git
- Desarrollo progresivo por niveles

---

## 👨‍💻 Autor

Daniela Villamizar Tapias
Proyecto personal de aprendizaje y construcción de portafolio profesional.

---

## 📌 Estado del Proyecto

🚧 Proyecto en desarrollo activo
