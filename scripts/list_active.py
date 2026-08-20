import os
import sys
import re

def main():
    workspaces_dir = "workspaces"
    if not os.path.exists(workspaces_dir):
        return

    # Si se pasa un workspace como argumento, lista sus proyectos activos
    if len(sys.argv) > 1:
        target_workspace = sys.argv[1]
        target_path = os.path.join(workspaces_dir, target_workspace, "projects")
        if os.path.isdir(target_path):
            # Listar carpetas dentro del directorio projects
            for item in os.listdir(target_path):
                full_path = os.path.join(target_path, item)
                if os.path.isdir(full_path):
                    # Ignorar carpeta _archive
                    if not item.startswith('_'):
                        print(item)
        return

    # Si no hay argumentos, lista solo los workspaces
    for workspace in os.listdir(workspaces_dir):
        if os.path.isdir(os.path.join(workspaces_dir, workspace)) and not workspace.startswith('_'):
            print(workspace)

if __name__ == "__main__":
    main()
