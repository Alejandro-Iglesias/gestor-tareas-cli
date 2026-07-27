# 🐍 Gestor de Tareas CLI (Command-Line Interface)

## 📌 Descripción del Proyecto

Este proyecto es un gestor de tareas implementado como una aplicación de consola (CLI) utilizando Python. Demuestra un conocimiento sólido de los principios de la **Programación Orientada a Objetos (POO)**, la **Persistencia de Datos** (guardado y carga en formato JSON) y el manejo de argumentos de línea de comandos (`argparse`).


## 🏗️ Estructura y Tecnologías

El proyecto se divide en tres módulos principales para garantizar la modularidad y escalabilidad:

| Archivo | Rol | POO Concepto |

| **`task.py`** | **Modelo de Datos.** Define la plantilla de una tarea (`Task`) con atributos (ID, descripción, estado) y métodos de serialización (`to_dict`). | Encapsulamiento, Clases. |
| **`task_manager.py`** | **Lógica de Negocio.** Contiene la clase `TaskManager` que gestiona la colección de tareas y las operaciones **CRUD** (Crear, Leer, Actualizar, Eliminar). | POO, CRUD, Persistencia (JSON). |
| **`todo.py`** | **Interfaz CLI.** Punto de entrada principal. Utiliza `argparse` para interpretar los comandos de usuario y llamar a los métodos de `TaskManager`. | Interfaz de Usuario. |
| **`tasks.json`** | **Datos.** Archivo generado automáticamente para persistir las tareas. | Persistencia de Datos. |

**Tecnologías:** Python 3.13.2 (Librerías estándar: `argparse`, `json`, `uuid`, `datetime`).

---

## 🚀 Instalación y Uso

### Instalación

1.  **Clonar el Repositorio:**
    ```bash
    git clone [https://github.com/Alejandro-Iglesias/gestor-tareas-cli.git](https://github.com/Alejandro0708/gestor-tareas-cli.git)
    cd gestor-tareas-cli
    ```
2.  **Crear y Activar el Entorno Virtual (Recomendado):**
    ```bash
    python -m venv venv
    .\venv\Scripts\activate   # Windows PowerShell
    # source venv/bin/activate # Linux/macOS
    ```
3.  **Instalar Dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

### Comandos de Uso

La aplicación se ejecuta utilizando el comando `python todo.py` seguido del subcomando deseado.

| Comando | Descripción | Ejemplo |

| **`add`** | Añade una tarea. | `python todo.py add "Subir código a Git" -d 2025-10-10` |
| **`list`** | Muestra tareas pendientes y completadas. | `python todo.py list` |
| **`complete`** | Marca una tarea como completada (usando el ID parcial). | `python todo.py complete a1b2c3d4` |
| **`delete`** | Elimina permanentemente una tarea (usando el ID parcial). | `python todo.py delete a1b2c3d4` |
| **`--help`** | Muestra el menú de ayuda. | `python todo.py --help` |
