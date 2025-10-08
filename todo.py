import argparse
from task_manager import TaskManager
import sys # Añadimos sys para un manejo de errores más limpio

def main():
    # 1. Configuración de Argumentos
    parser = argparse.ArgumentParser(description="Gestor de Tareas CLI", 
                                     epilog="Usa python todo.py <comando> --help para más info.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Subcomando 'add'
    add_parser = subparsers.add_parser("add", help="Añade una nueva tarea")
    add_parser.add_argument("description", type=str, help="Descripción de la tarea")
    add_parser.add_argument("-d", "--due-date", type=str, default=None, help="Fecha límite (opcional, ej: 2025-12-31)")

    # Subcomando 'list'
    subparsers.add_parser("list", help="Muestra todas las tareas pendientes y completadas")

    # Subcomando 'complete'
    complete_parser = subparsers.add_parser("complete", help="Marca una tarea como completada")
    complete_parser.add_argument("task_id", type=str, help="Primeros 8 caracteres del ID de la tarea a completar (ver con el comando 'list')")

    # Subcomando 'delete'
    delete_parser = subparsers.add_parser("delete", help="Elimina una tarea de la lista")
    delete_parser.add_argument("task_id", type=str, help="Primeros 8 caracteres del ID de la tarea a eliminar")

    try:
        args = parser.parse_args()
    except SystemExit:
        # Si argparse lanza SystemExit (ej. por --help o comando inválido), salimos.
        return

    # 2. Lógica de Ejecución
    manager = TaskManager()

    if args.command == "add":
        manager.add_task(args.description, args.due_date)
        
    elif args.command == "list":
        manager.list_tasks()

    elif args.command == "complete":
        manager.complete_task(args.task_id)

    elif args.command == "delete":
        manager.delete_task(args.task_id)

    
if __name__ == "__main__":
    main()