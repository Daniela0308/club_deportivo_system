class Player:
    def __init__(self, id_player, name, category, active_status=True, last_month_paid=None):
        self.id_player = id_player
        self.name = name
        self.category = category
        self.active_status = active_status
        self.last_month_paid = last_month_paid #"YYYY-MM"

    def activate(self):
        """Cambia el estado de un jugador a activo"""
        self.active_status = True

    def deactivate(self):
        """Cambia el estado de un jugador a inactivo"""
        self.active_status = False

    @property
    def is_active(self):
        """Saber si un jugador está activo"""
        return self.active_status

    @property
    def last_month_paid_value(self):
        """Obtener último mes pagado de un jugador"""
        return self.last_month_paid
    
    def update_last_month_paid(self, month: str):
        """Actualizar último mes pagado, formato del mes "YYYY-MM"""
        self.last_month_paid = month

    def is_up_to_date(self, current_month: str) -> bool:
        "Saber si el jugador está al día con los pagos, formato del mes actual 'YYYY-MM'"
        if self.last_month_paid is None:
            return False
        return self.last_month_paid >= current_month
    
    def to_dict(self):
        """Convierte el jugador en un diccionario"""
        return {
            "id": self.id_player,
            "name": self.name,
            "category": self.category,
            "active_status": self.active_status,
            "last_month_paid": self.last_month_paid
        }

    @classmethod
    def from_dict(cls, data):
        # Crea y retorna el objeto del jugador (aprovechando el uso de classmethod)
        return cls(
            id_player=data["id"],
            name=data["name"],
            category=data["category"],
            active_status=data["active_status"],
            last_month_paid=data.get("last_month_paid")
        )
        
