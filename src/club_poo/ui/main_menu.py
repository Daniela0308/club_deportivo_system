from club_poo.config.message_translator import get_message

from club_poo.services.payment_service import (
    register_payment_service,
    player_payments_history_service,
    show_payments_service
)
from club_poo.services.player_service import (
    register_player_service,
    show_players_service, 
    activate_player_service,
    deactivate_player_service,
    list_of_debtors_service
)


def main_menu(club, persistence_players, persistence_payments):
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Registrar jugador")
        print("2. Listar jugadores")
        print("3. Activar / desactivar jugador")
        print("4. Registrar pago")
        print("5. Ver historial de pagos de un jugador")
        print("6. Ver historial de pagos")
        print("7. Ver deudores")
        print("8. Salir")

        option = input("Seleccione una opción: ")

        match option:
            case "1":
                name = input("Nombre del jugador: ")
                category = input("Categoría: ")

                ok, message = register_player_service(club, persistence_players, name, category)
                print(get_message(message))
            
            case "2":
                ok, message, data = show_players_service(club)
                print("\nJugadores registrados: ")
                if not ok:
                    print(get_message(message))
                for player in data:
                    print(player.to_dict())

            case "3":
                print("1. Activar jugador")
                print("2. Desactivar jugador")
                state = input("¿Qué desea hacer?: ")
                id_player = int(input("Digite le ID del jugador: "))

                if state == "1":
                    result = activate_player_service(club, id_player)
                    print(get_message(message))
                elif state == "2":
                    result = deactivate_player_service(club, id_player)
                    print(get_message(message))
                else:
                    print("Opción inválida")

            case "4":
                id_player = int(input("Digite le ID del jugador: "))
                number_months = int(input("¿Cuántos meses dese pagar?: "))

                ok, message = register_payment_service(club, persistence_payments, id_player, number_months)
                print(get_message(message))
            
            case "5":
                id_player = int(input("Digite le ID del jugador: "))

                ok, message, data = player_payments_history_service(club, id_player)

                if not ok:
                    print(get_message(message))
                else:
                    print(f"\nPagos del jugador {player.name} son: ")
                    for payment in data:
                        print(payment.to_dict())

            case "6":
                ok, message, data = show_payments_service(club)
                print("\nHistorial completo de pagos: ")
                if not ok:
                    print(get_message(message))
                for payment in data:
                    print(payment.to_dict())

            case "7":
                ok, data = list_of_debtors_service(club)
                for player in data:
                    print(f"Jugadores con pagos pendientes: \n {player.to_dict()}")

            case "8":
                print("Saliendo del sistema...")
                break

            case _:
                print(f'Opción no válida')
       
