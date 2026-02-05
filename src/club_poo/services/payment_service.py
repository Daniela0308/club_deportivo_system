def register_payment_service(club, persistence_payments, id_player, number_months):
    """
    Caso de uso: registrar un pago
    """
    ok, message = club.register_payment(id_player, number_months)

    if ok:
        persistence_payments.save_payments(club.payments)

    return ok, message

def player_payments_history_service(club, id_player):
    """
    Caso de uso: historial de pagos de un jugador
    """
    ok, message, data = club.player_payments_history(id_player)
    return ok, message, data

def show_payments_service(club):
    """
    Caso de uso: mostrar todos los pagos
    """
    ok, message, data = club.show_payments()

    return ok, message, data