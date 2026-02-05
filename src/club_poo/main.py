from club_poo.models.club import Club
from club_poo.persistence.payments_repository import PaymentsRepository
from club_poo.persistence.player_repository import PlayerRepository
from club_poo.ui.main_menu import main_menu

def main():
    club = Club("Club Deportivo Cuyabros")
    persistence_players = PlayerRepository()
    persistence_payments = PaymentsRepository()

    # Cargar datos a jugadores y pagos
    club.players = persistence_players.load_players()
    club.payments = persistence_payments.load_payments()

    club.recalculate_counters()


    main_menu(club, persistence_players, persistence_payments)

if __name__ == "__main__":
    main()
