# Guía de Instalación y Configuración

El framework **media-architect** requiere un entorno de Python configurado para que los scripts de optimización y los comandos de listado de base de datos (ej. `/media-in`) funcionen a máxima velocidad y sin errores de rutas del sistema operativo.

## 1. Requisitos Previos
- Antigravity CLI instalado.
- Python 3.9 o superior.

## 2. Creación del Entorno Virtual (venv)
Para evitar conflictos de dependencias (especialmente en entornos Windows/WSL), es **obligatorio** aislar el entorno de Python dentro de la carpeta del proyecto.

Abre tu terminal en la raíz de `media-architect` y ejecuta:

```bash
python3 -m venv venv
```

## 3. Activación e Instalación de Dependencias
Activa el entorno e instala las librerías necesarias:

**En Linux / macOS:**
```bash
source venv/bin/activate
pip install -r scripts/requirements.txt
```

**En Windows (Git Bash):**
```bash
source venv/Scripts/activate
pip install -r scripts/requirements.txt
```

## 4. Estructura de Scripts Backend
La carpeta `/scripts` contiene código Python que sirve como "backend" de alta velocidad para las habilidades de la IA. Esto permite que la IA no pierda tokens ni tiempo ejecutando operaciones básicas de sistema:
- `list_active.py`: Base de datos ultrarrápida que lee los archivos Markdown de los workspaces, filtra proyectos archivados y gestiona el menú del comando `/media-in`.
- `media_optimizer.py`: Script avanzado para procesar recursos y assets.
- `requirements.txt`: Dependencias del sistema.

Con el entorno virtual configurado, el agente detectará automáticamente la ruta `./venv/bin/python` y ejecutará todas las consultas de forma aislada y veloz.
