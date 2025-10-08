

#Este archivo define la plantilla o clase para un solo objeto Tarea.

import uuid
from datetime import datetime

class Task:
    "Representacion de una unica tarea en el listado de tareas pendientes"

    def __init__(self, description: str, due_date: str= None, is_completed: bool =False, task_id: str=None, created_at: str =None):

        """inicializa un nuevo objeto Task
        :param description: La descripción textual de la tarea.
        :param due_date: Fecha límite para la tarea (opcional).
        :param is_completed: Estado de la tarea (por defecto es False).
        :param task_id: Un identificador único. Si no se proporciona, se genera uno nuevo."""
        #Genera un ID único (UUID) si no se proporciona uno (crucial para identificar la tarea

        self.id = task_id if task_id else str(uuid.uuid4())
        self.description = description
        self.due_date = due_date
        self.is_completed = is_completed
        self.created_at = created_at if created_at else datetime.now().isoformat()


    def __str__(self):
        """Define cómo debe imprimirse el objeto Task."""
        status = "^[COMPLETADA]" if self.is_completed else "[PENDIENTE]"
        date_info = f" | Plazo: {self.due_date}" if self.due_date else ""
        # Muestra los primeros 8 caracteres del ID para referencia
        return f"{status} (ID:{self.id[:8]}...)-{self.description}{date_info}"
    

    def to_dict(self):
        """Convierte la tarea en un diccionario para guardarla en JSON/CSV."""
        return {
            # CAMBIA 'id' a 'task_id' para que coincida con el constructor
            'task_id': self.id, 
            'description': self.description,
            'due_date': self.due_date,
            'is_completed': self.is_completed,
            'created_at': self.created_at
        }




 

         