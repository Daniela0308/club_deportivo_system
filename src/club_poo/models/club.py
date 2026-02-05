from datetime import datetime
from dateutil.relativedelta import relativedelta

from .player import Player
from .payment import Payment

from club_poo.config.error_codes import (
    PLAYER_SUCCESSFULLY_REGISTERED,
    PLAYER_ALREADY_EXISTS, 
    PLAYER_NOT_FOUND,
    PLAYER_ACTIVE, 
    PLAYER_INACTIVE, 
    INVALID_NUMBER_OF_MONTHS,
    NO_REGISTERED_PLAYERS,
    NO_REGISTERED_PAYMENTS
)

class Club:
    def __init__(self, name):
        self.name = name
        self.players = []
        self.payments = []
        self.__player_id_counter = 1 # __ encapsula la variable a privada para evitar su acceso desde otro sistema
        self.__payment_id_counter = 1

    def register_player(self, name_player, category_player):
        """Registra los jugadores con un ID"""
        #Validar que no exista un jugador con ese nombre
        for player in self.players:
            if player.name.lower() == name_player.lower():
                return False, PLAYER_ALREADY_EXISTS
            
        #Creamos el jugador
        new_player = Player(
            id_player= self.__player_id_counter,
            name= name_player,
            category= category_player
        )
 
        #Agregamos nuevo jugador a la lista
        self.players.append(new_player)
        #Aumentamos el ID
        self.__player_id_counter += 1

        return True, PLAYER_SUCCESSFULLY_REGISTERED
    
    def search_player_id(self, id_player):
        """Buscar un jugador por su id"""
        #Buscamos y retornamos el jugador con ese id
        for player in self.players:
            if player.id_player == id_player:
                return player
        return False, PLAYER_NOT_FOUND
    
    def show_players(self):
        """Generar listado de los jugadores registrados"""
        #Mostramos jugadores
        if not self.players:
            return False, NO_REGISTERED_PLAYERS, self.players
        return True, None, self.players

    def show_payments(self):
        """Genera listado de los pagos registrados"""
        if not self.payments:
            return False, NO_REGISTERED_PAYMENTS, self.payments
        return True, None, self.payments
    
    def activate_player(self, id_player):
        """Activar jugador"""
        player = self.search_player_id(id_player)
        player.activate()
        return True, PLAYER_ACTIVE
    
    def deactivate_player(self, id_player):
        """Inactivar jugador"""
        player = self.search_player_id(id_player)
        player.deactivate()
        return True, PLAYER_INACTIVE
    
    def update_last_month_paid_player(self, id_player, month: str):
        """Actualizar último mes pagado, formato del mes "YYYY-MM"""
        player = self.search_player_id(id_player)
        player.update_last_month_paid(month)
    
    def list_of_debtors(self):
        """Mostrar todos los jugadores activos que tienen meses pendientes de pago."""
        current_date = datetime.today().strftime("%Y-%m")
        return True, [
            player 
            for player in self.players 
            if player.is_active and not player.is_up_to_date(current_date)
        ]

    def register_payment(self, id_player, number_of_months):
        """Registra uno o varios pagos y actualiza el último mes pagado"""
        if number_of_months <= 0:
            return False, INVALID_NUMBER_OF_MONTHS
        #Buscamos el jugador
        player = self.search_player_id(id_player)
        #Verificar que el jugador si exista y que el jugador este activo
        if not player:
            return False, PLAYER_NOT_FOUND
        if not player.is_active:
            return False, PLAYER_INACTIVE

        #Obtener último mes pagado
        last_month_str = player.last_month_paid_value

        if last_month_str is None:
        # Si nunca ha pagado, empezamos desde el mes actual
            last_month_date = datetime.today().replace(day=1) - relativedelta(months=1)
        else:
            last_month_date = datetime.strptime(last_month_str, "%Y-%m")

        #Registrar cada mes pagado
        for _ in range(number_of_months):
            #¿Qué mes se va a pagar?
            next_month = last_month_date + relativedelta(months=1)

            #Se crea el pago
            payment = Payment(
                id_player= player.id_player,
                id_payment= self.__payment_id_counter,
                paid_month= next_month.strftime("%Y-%m"),
                payment_date= datetime.today().strftime("%Y-%m-%d")
            )
            #Agregamos el pago a la lista de pagos
            self.payments.append(payment)
            self.__payment_id_counter += 1

            #Actualizamos el último mes pagado
            player.update_last_month_paid(next_month.strftime("%Y-%m"))

            # mover el mes base
            last_month_date = next_month

        return True, PLAYER_SUCCESSFULLY_REGISTERED

    def player_payments_history(self, id_player):
        """Genera el historial de pagos de un jugador usando si id"""
        #Buscamos el jugador
        player = self.search_player_id(id_player)
        #Verificar que el jugador si exista y que el jugador este activo
        if not player:
            return False, PLAYER_NOT_FOUND, []
        if not player.is_active:
            return False, PLAYER_INACTIVE     
        return True, None, [payment for payment in self.payments if payment.id_player == id_player]
    


    def recalculate_counters(self):
        """Recalcula los contadores basándose en los datos cargados"""

        if self.players:
            self.__player_id_counter = max(player.id_player for player in self.players) + 1

        if self.payments:
            self.__payment_id_counter = max(payment.id_payment for payment in self.payments) + 1
