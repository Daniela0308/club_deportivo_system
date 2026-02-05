import os
from pathlib import Path

#Ruta a la carpeta raíz del proyecto
ROOT_DIR = Path(__file__).parent.parent.parent.parent
#Ruta segura al archivo JSON (independiente del directorio de ejecución)
FILE_PATH_PLAYERS = os.path.join(ROOT_DIR, "data", "players.json")
FILE_PATH_PAYMENTS = os.path.join(ROOT_DIR, "data", "payments.json")
