
#Esta clase es el cerebro de la aplicación. Contiene la lista de todas las tareas y la lógica para manipular esa lista.

# Importamos la clase Task 

from task import Task 
import json 
import os

class TaskManager:
    """
    Gestiona la colección de objetos Task, incluyendo la lógica CRUD 
    (Crear, Leer, Actualizar, Eliminar).
    """

    def __init__(self, filename = "tasks.json"):
        # Inicializamos con una lista vacía para almacenar los objetos Task
        self.tasks = []
        self.tasks = []
        self.filename = filename  # Almacena el nombre del archivo
        self.load_tasks()         # Llama a la función de carga al iniciar
        
    def add_task(self, description: str, due_date: str = None):
        """Crea y añade una nueva tarea a la lista."""
        new_task = Task(description=description, due_date=due_date)
        self.tasks.append(new_task)
        print(f" Tarea añadida: '{description}'")

    def list_tasks(self):
        """Muestra todas las tareas, separando completadas de pendientes."""
        if not self.tasks:
            print("La lista de tareas está vacía. ¡Añade una!")
            return

        pending = [t for t in self.tasks if not t.is_completed]
        completed = [t for t in self.tasks if t.is_completed]
        
        print("\n--- TAREAS PENDIENTES ---")
        for i, task in enumerate(pending, 1):
            # Usamos el índice de la lista (i) para la referencia rápida al mostrar
            print(f"{i}. {task}")
            
        if completed:
            print("\n--- TAREAS COMPLETADAS ---")
            for i, task in enumerate(completed, 1):
                 print(f"{i}. {task}")


    def save_tasks(self):
        """Convierte los objetos Task a diccionarios y los guarda en tasks.json."""
        data_to_save = []
        
        # 1. Serialización (Objeto -> Diccionario)
        # Recorre la lista de objetos 'Task' y llama a su método .to_dict()
        for task in self.tasks:
            data_to_save.append(task.to_dict())
            
        # 2. Escritura en el archivo
        try:
            with open(self.filename, 'w', encoding='utf-8') as f:
                # json.dump escribe la lista de diccionarios al archivo
                json.dump(data_to_save, f, indent=4) 
        except IOError as e:
            print(f"Error al intentar guardar el archivo {self.filename}: {e}")


    def load_tasks(self):
        """Carga los diccionarios del archivo y los convierte de nuevo a objetos Task."""
        
        # 1. Verifica si el archivo existe (para la primera ejecución)
        if not os.path.exists(self.filename):
            return  # No hay archivo, no hay nada que cargar
            
        try:
            # 2. Lectura del archivo
            with open(self.filename, 'r', encoding='utf-8') as f:
                data_loaded = json.load(f) # data_loaded es una lista de diccionarios
                
            # 3. Deserialización (Diccionario -> Objeto)
            # Por cada diccionario, crea un objeto Task
            for task_dict in data_loaded:
                # El truco es usar los valores del diccionario como argumentos para Task()
                task_object = Task(**task_dict) 
                self.tasks.append(task_object)
                
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error al cargar el archivo {self.filename}: {e}")
            self.tasks = [] # Limpia la lista si hay error de carga

    def add_task(self, description: str, due_date: str = None):
        """Crea y añade una nueva tarea a la lista."""
        new_task = Task(description=description, due_date=due_date)
        self.tasks.append(new_task)
        self.save_tasks() # <--- ¡Asegúrate de añadir esta línea!
        print(f"✅ Tarea añadida: '{description}'")
    
    def find_task_by_id(self, partial_id: str):
        """Busca una tarea cuyo ID comience con el ID parcial dado."""
        # Se busca el ID por sus primeros caracteres para hacerlo más fácil en la CLI
        found_tasks = [t for t in self.tasks if t.id.startswith(partial_id)]
        if len(found_tasks) == 1:
            return found_tasks[0]
        return None # Devuelve None si no encuentra o hay ambigüedad
    
    def complete_task(self, partial_id: str):
        """Marca una tarea como completada y guarda los cambios."""
        task = self.find_task_by_id(partial_id)
        if task:
            task.is_completed = True
            self.save_tasks()
            print(f"✅ Tarea {partial_id[:8]}... marcada como completada: {task.description}")
        else:
            print(f"❌ Error: Tarea con ID {partial_id} no encontrada o es ambigua.")

    def delete_task(self, partial_id: str):
        """Elimina una tarea de la lista y guarda los cambios."""
        task_to_delete = self.find_task_by_id(partial_id)
        if task_to_delete:
            self.tasks.remove(task_to_delete)
            self.save_tasks()
            print(f"🗑️ Tarea {partial_id[:8]}... eliminada: {task_to_delete.description}")
        else:
            print(f"❌ Error: Tarea con ID {partial_id} no encontrada o es ambigua.")