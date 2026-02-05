def register_player_service(club, persistence_players, name, category):
    """
    Caso de uso: registrar jugador
    Devuelve: (ok: bool, mensaje: str)
    """
    ok, message = club.register_player(name, category)

    if ok:
        persistence_players.save_players(club.players)

    return ok, message


def show_players_service(club):
    """
    Caso de uso: listar jugadores
    """
    ok, message, data = club.show_players()

    return ok, message, data

def activate_player_service(club, id_player):
    """
    Caso de uso: activar un jugador
    """
    ok, message = club.activate_player(id_player)
    return ok, message

def deactivate_player_service(club, id_player):
    """
    Caso de uso: desactivar un jugador
    """
    ok, message = club.deactivate_player(id_player)
    return ok, message

def list_of_debtors_service(club):
    """
    Caso de uso: listado de deudores
    """
    ok, data = club.list_of_debtors()

    return ok, data