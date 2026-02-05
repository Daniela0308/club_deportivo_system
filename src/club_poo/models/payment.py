class Payment:
    def __init__(self, id_player, id_payment, paid_month, payment_date):
        self.id_player = id_player
        self.id_payment = id_payment
        self.paid_month = paid_month #"YYYY-MM"
        self.payment_date = payment_date #"YYYY-MM-DD"

    def to_dict(self):
            """Convierte el pago en un diccionario"""
            return {
                "id_player": self.id_player,
                "id_payment": self.id_payment,
                "paid_month": self.paid_month,
                "payment_date": self.payment_date
            }

    @classmethod
    def from_dict(cls, data):
        # Crea y retorna el objeto del pago (aprovechando el uso de classmethod)
        return cls(
            id_player= data["id_player"],
            id_payment= data["id_payment"],
            paid_month= data["paid_month"],
            payment_date= data["payment_date"]
        )
        