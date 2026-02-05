import json
import os

from club_poo.config.paths import FILE_PATH_PLAYERS
from club_poo.models.player import Player


class PlayerRepository:
    def __init__(self, file=FILE_PATH_PLAYERS):
        self.file = file

    def load_players(self):
        """Cargar archivo JSON con información de jugadores"""

        #Si el archivo no existe o está vacío retornamos una lista vacia
        if not os.path.exists(self.file) or os.path.getsize(self.file) == 0:
            return []

        try:
            #Se guarda la información del json en data
            with open(self.file, "r", encoding="utf-8") as file:
                data = json.load(file)
        except json.JSONDecodeError:
            return []
        #Crea la lista de jugadores usando el classmthod From_dict
        return [Player.from_dict(d) for d in data]

        
    def save_players(self, players_list):
        """Guardar información de los jugadores en el archivo JSON"""
        #Se convierte el objeto en dic para que json lo pueda guardar
        data = [player.to_dict() for player in players_list]
        #Escribimos los datos en el archivo json
        with open(self.file, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)


        
