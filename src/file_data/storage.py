import os
import json

#Ruta segura al archivo JSON (independiente del directorio de ejecución)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, "data", "contacts.json")

#Creamos función para cargar datos
def load_data():
    if not os.path.exists(FILE_PATH) or os.path.getsize(FILE_PATH) == 0:
        return []

    try:
        with open(FILE_PATH, "r", encoding="utf-8") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return[]

def save_data(contact_list):
    with open(FILE_PATH, "w", encoding="utf-8") as file:
        json.dump(contact_list, file, indent=4, ensure_ascii=False)
