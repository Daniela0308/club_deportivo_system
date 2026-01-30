from datetime import datetime
from .player import Player

class Club:
    def __init__(self, name):
        self.name = name
        self.players = []
        self.__id_counter = 1 # __ encapsula la variable a privada para evitar su acceso desde otro sistema
    
    def register_player(self, name_player, category_player):
        """Registra los jugadores con un ID"""
        #Validar que no exista un jugador activo con ese nombre
        for player in self.players:
            if player.is_active() and player.name.lower() == name_player.lower():
                return f"El jugador: {player.name}, ya se encuentra creado"

        #Creamos el jugador
        new_player = Player(
            id_player= self.__id_counter,
            name= name_player,
            category= category_player
        )
        #Aumentamos el counter para el proximo jugador
        self.__id_counter += 1

        #Agregamos nuevo jugador a la lista
        self.players.append(new_player)
        return True #registro exitoso
    
    def search_player_id(self, id_player):
        """Buscar un jugador por su id"""
        #Buscamos y retornamos el jugador con ese id
        for player in self.players:
            if player.id == id_player:
                return player
        return None
    
    def show_players(self):
        """Generar listado de los jugadores registrados"""
        player_list = []
        #Verificamos que existan jugadores para mostrar
        if not self.players:
            return f"No existen jugadores registrados"
            
        #Mostramos jugadores
        for player in self.players:
            player_list.append(player)
        
        return player_list
    
    def activate_player(self, id_player):
        """Activar jugador"""
        player = self.search_player_id(id_player)
        player.activate()
        return True
    
    def deactivate_player(self, id_player):
        """Inactivar jugador"""
        player = self.search_player_id(id_player)
        player.deactivate()
        return True
    
    def update_last_month_paid_player(self, id_player, month: str):
        """Actualizar último mes pagado, formato del mes "YYYY-MM"""
        player = self.search_player_id(id_player)
        player.update_last_month_paid(month)
    
    def list_of_debtors(self):
        """Mostrar todos los jugadores activos que tienen meses pendientes de pago."""
        debtors_player_list = []
        for player in self.players:
            if player.is_active():
                current_date = datetime.today().strftime("%Y-%m")
                if not player.is_up_to_date(current_date):
                    debtors_player_list.append(player)
        return debtors_player_list