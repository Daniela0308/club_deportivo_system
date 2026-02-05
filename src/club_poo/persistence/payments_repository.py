import json
import os

from club_poo.config.paths import FILE_PATH_PAYMENTS
from club_poo.models.payment import Payment

class PaymentsRepository:
    def __init__(self, file=FILE_PATH_PAYMENTS):
        self.file = file

    def load_payments(self):
        """Cargar archivo JSON con información de pagos"""
        if not os.path.exists(self.file) or os.path.getsize(self.file) == 0:
            return []

        try:
            with open(self.file, "r", encoding="utf-8") as file:
                data = json.load(file)
        except json.JSONDecodeError:
            return[]
        #Crea la lista de pagos usando el classmthod From_dict
        payments_list = [Payment.from_dict(d) for d in data]

        #Se retorna la lista de pagos cargados
        return payments_list

    def save_payments(self, payments_list):
        """Guardar información de los pagos en el archivo JSON"""
        #Se convierte el objeto en dic para que json lo pueda guardar
        data = [payment.to_dict() for payment in payments_list]

        with open(self.file, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
