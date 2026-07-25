import os
import sys
import re

def main():
    clients_dir = "clients"
    if not os.path.exists(clients_dir):
        return

    # Si se pasa un cliente como argumento, lista sus proyectos activos
    if len(sys.argv) > 1:
        target_client = sys.argv[1]
        readme_path = os.path.join(clients_dir, target_client, "README.md")
        if os.path.isfile(readme_path):
            with open(readme_path, "r", encoding="utf-8") as f:
                lines = f.read().split('\n')
                in_table = False
                for line in lines:
                    if line.startswith('| Proyecto'):
                        in_table = True; continue
                    if in_table and line.startswith('| :---'):
                        continue
                    if in_table and line.startswith('|'):
                        parts = [p.strip() for p in line.split('|')]
                        if len(parts) >= 5:
                            # Columna 4 es Archivado
                            if parts[4].lower() not in ['sí', 'si', 'yes', 'true']:
                                match = re.search(r'\[(.*?)\]', parts[1])
                                if match:
                                    print(match.group(1))
                    elif in_table and not line.strip():
                        in_table = False
        return

    # Si no hay argumentos, lista solo los clientes
    for client in os.listdir(clients_dir):
        if os.path.isdir(os.path.join(clients_dir, client)) and not client.startswith('_'):
            print(client)

if __name__ == "__main__":
    main()
