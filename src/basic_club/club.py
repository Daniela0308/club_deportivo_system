"""
BLOQUE 1: PERSISTENCIA DE DATOS

Este bloque se encarga de la carga y el guardado de la información del sistema
mediante archivos JSON. Su objetivo es garantizar la persistencia de los datos,
permitiendo que la información se conserve aunque el programa se cierre.

Las funciones definidas aquí son utilizadas por los demás bloques del sistema
para acceder y actualizar los datos de forma segura y organizada.
No contiene lógica de negocio, únicamente lectura y escritura de datos.


BLOQUE 2: GESTIÓN DE JUGADORES

Este bloque administra la información básica de los jugadores del club
deportivo. Permite registrar jugadores, listarlos, buscarlos por ID
y cambiar su estado (activo o inactivo).

Los jugadores no se eliminan del sistema; únicamente se inactivan para
conservar el historial y la integridad de la información.

Este bloque no gestiona pagos, pero define la estructura del jugador
y prepara los datos que serán utilizados en el bloque de pagos.


BLOQUE 3: GESTIÓN DE PAGOS

Este bloque gestiona el registro y control de pagos de mensualidades
de los jugadores del club.

Permite:
- Registrar pagos por uno o varios meses
- Generar identificadores únicos de pago
- Actualizar automáticamente el último mes pagado del jugador
- Consultar pagos por jugador
- Generar listados de jugadores con deuda

Las reglas de negocio aseguran que solo los jugadores activos
puedan realizar pagos y que los pagos se registren de forma
cronológica mes a mes.
"""

import os
import json
from datetime import datetime
from dateutil import relativedelta



#Ruta segura al archivo JSON (independiente del directorio de ejecución)
#Creamos dos, una para los datos de jugadores y otra para los datos de pagos
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH_PLAYERS = os.path.join(BASE_DIR, "data", "players.json")
FILE_PATH_PAYMENTS = os.path.join(BASE_DIR, "data", "payments.json")

#BLOQUE 1

def load_players():
    """Cargar archivo JSON con información de jugadores"""
    if not os.path.exists(FILE_PATH_PLAYERS) or os.path.getsize(FILE_PATH_PLAYERS) == 0:
        return []

    try:
        with open(FILE_PATH_PLAYERS, "r", encoding="utf-8") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return[]


def save_players(players_list):
    """Guardar información de los jugadores en el archivo JSON"""
    with open(FILE_PATH_PLAYERS, "w", encoding="utf-8") as file:
        json.dump(players_list, file, indent=4, ensure_ascii=False)


def load_payments():
    """Cargar archivo JSON con información de pagos"""
    if not os.path.exists(FILE_PATH_PAYMENTS) or os.path.getsize(FILE_PATH_PAYMENTS) == 0:
        return []

    try:
        with open(FILE_PATH_PAYMENTS, "r", encoding="utf-8") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return[]


def save_payments(payments_list):
    """Guardar información de los pagos en el archivo JSON"""
    with open(FILE_PATH_PAYMENTS, "w", encoding="utf-8") as file:
        json.dump(payments_list, file, indent=4, ensure_ascii=False)

#BLOQUE 2

def register_player(players_list, name, category):
    """Registra los jugadores con un ID"""
    #Validar que no exista un jugador activo con ese nombre
    for player in players_list:
        if player["active_status"] and player["name"].lower() == name.lower():
            return False

    #Generar ID único para cada jugador
    new_id = 0
    if players_list:
        id_max = 0
        #Verificamos cual es el id máximo ya asignado, para poder asignar el siguiente
        for player in players_list:
            if player["id"] > id_max:
                id_max = player["id"]
        new_id = id_max + 1

    #Creamos el jugador
    new_player = {
        "id": new_id,
        "name": name,
        "category": category,
        "active_status": True,
        "last_month_paid": None
    }
    #Agregamos nuevo jugador a la lista
    players_list.append(new_player)
    save_players(players_list)
    return True #registro exitoso


def show_players():
    """Generar listado de los jugadores registrados"""
    #Cargamos lista
    players_list = load_players()
    #Verificamos que existan jugadores para mostrar
    if not players_list:
        print(f'No existen jugadores registrados')
        return
    #Mostramos jugadores
    for player in players_list:
        print(f'\nId_Jugador: {player["id"]} \nNombre: {player["name"]} \nCategoria: {player["category"]} \nActivo: {player["active_status"]} \nUltimo mes pagado: {player["last_month_paid"]}\n')


def search_player_id(players_list, id_player):
    """Buscar un jugador por su id"""
    #Buscamos y retornamos el jugador con ese id
    for player in players_list:
        if player["id"] == id_player:
            return player
    return None


def print_player(players_list):
    """Función de imprime un jugador"""
    for player in players_list:
        print(f"""
Id_Jugador: {player['id']}
Nombre: {player['name']}
Categoria: {player['category']}
Activo: {player['active_status']}
Ultimo mes pagado: {player['last_month_paid']}
""")



def change_player_status(id_player):
    """Cambia el estado de un jugador (activo/inactivo)"""
    players_list = load_players()
    for player in players_list:
        if player["id"] == id_player:
            player["active_status"] = not player["active_status"]
            save_players(players_list)
            return True
    return False


#BLOQUE 3: PAGOS

def generate_payment_id(payments_list):
    """Generar ID de pago"""
    new_pay_id = 1
    if payments_list:
        id_pay_max = 0
        #Verificamos cual es el id máximo ya asignado, para poder asignar el siguiente
        for pay in payments_list:
            if pay["id_pay"] > id_pay_max:
                id_pay_max = pay["id_pay"]
        new_pay_id = id_pay_max + 1
    return new_pay_id


def get_last_month_paid(player):
    """Obtener último mes pagado de un jugador"""
    if player["last_month_paid"]:
        #Convertimos string "YYYY-MM" a objeto datetime
        last_month = datetime.strptime(player["last_month_paid"], "%Y-%m")
    else:
        #Si no tiene historial, tomamos el mes y año actual
        last_month = datetime.today() - relativedelta(months=1)
    return last_month


def register_payment(id_player, number_of_months):
    """Registra el pago de una jugador, genera un ID de pago y actualiza el último mes pagado"""
    #Cargamos lista de jugadores
    players_list = load_players()
    #Buscamos el jugador
    player = search_player_id(players_list, id_player)
    #Verificamos que el jugador si exista y que el jugador este activo
    if not player:
        return False
    if not player["active_status"]:
        return False

    #Cargamos lista de pagos
    payments_list = load_payments()

    #Obtener último mes pagado
    last_month = get_last_month_paid(player)

    #Registrar cada mes pagado
    for _ in range(number_of_months):
        #¿Qué mes se va a pagar?
        next_month = last_month + relativedelta(months=1)

        #registramos pagos
        pay = {
            "id_pay": generate_payment_id(payments_list),
            "id_player": player["id"],
            "paid_month": next_month.strftime("%Y-%m"), #lo devolvemos al formato de fecha
            "payment_date": datetime.today().strftime("%Y-%m-%d")
        }
        #Agregamos el pago a la lista de pagos
        payments_list.append(pay)

        #Actualizamos el último mes pagado
        last_month = next_month
        player["last_month_paid"] = next_month.strftime("%Y-%m")

    #Guardamos el pago
    save_payments(payments_list)
    save_players(players_list)

    return True


def show_payments():
    """Generar listado de los pagos registrados"""
    #Cargamos lista
    payments_list = load_payments()
    #Verificamos que existan pagos para mostrar
    if not payments_list:
        print(f'No existen pagos registrados')
        return
    #Mostramos pagos
    for pay in payments_list:
        print(f"""
Id_Pago: {pay["id_pay"]}
Id_Jugador: {pay["id_player"]}
Mes pagado: {pay["paid_month"]}
Fecha del pago: {pay["payment_date"]}
""")


def player_payments(payments_list, id_player):
    """Genera los pagos de un solo jugador"""
    player_payments_list = []

    for pay in payments_list:
        if pay["id_player"] == id_player:
            player_payments_list.append(pay)

    return player_payments_list


def print_player_payments(payments_list):
    """Función que imprime los pagos"""
    for pay in payments_list:
        print(f"""
Id_Pago: {pay['id_pay']}
Id_Jugador: {pay['id_player']}
Mes pagado: {pay['paid_month']}
Fecha del pago: {pay['payment_date']}
    """)
        

def list_of_debtors():
    """Mostrar todos los jugadores activos que tienen meses pendientes de pago."""
    players_list = load_players()
    debtors_player_list = []
    for player in players_list:
        if player["active_status"]:
            if not player["last_month_paid"]:
                debtors_player_list.append(player)
            elif player["last_month_paid"] < datetime.today().strftime("%Y-%m"):
                debtors_player_list.append(player)
    
    return debtors_player_list


#MENÚ PRINCIPAL
def show_menu_players():
    players = load_players()
    while True:
        print(f'1. Agregar Jugador \n2. Listar Jugadores \n3. Activar / Inactivar Jugador \n4. Buscar Jugador \n5. Salir')
        option = int(input(f"Elige una opción: "))

        match option:
            case 1:
                name = input(f"Escribe el nombre completo del jugador: ")
                category = input(f"Escribe la categoría del jugador (año nacimiento): ")
                sucess = register_player(players, name, category)
                if sucess:
                    print("✅ Jugador registrado correctamente")
                else:
                    print("⚠️ El jugador ya se encuentra registrado")
            case 2:
                print(f"-----LISTADO DE JUGADORES-----")
                show_players()
            case 3:
                id = int(input(f"Escribe el id del jugador: "))
                if not change_player_status(id):
                    print("Jugador no encontrado")
                else:
                    print("Estado del jugador actualizado")      
            case 4:
                id_search = int(input(f"Escribe el id del jugador: "))
                player = search_player_id(players, id_search)
                if not player:
                    print(f"El jugador no existe...")
                else:
                    print_player([player])
            case 5:
                print(f'Volviendo al menú principal...')
                break

def show_menu_payments():
    payments = load_payments()
    while True:
        print(f'1. Agregar Pago \n2. Ver todos los pagos \n3. Ver pagos de un Jugador \n4. Listado de deudores \n5. Salir')
        option = int(input(f"Elige una opción: "))

        match option:
            case 1:
                id_player = int(input(f"Escribe el id del jugador: "))
                number_of_months = int(input(f"¿Cuántos meses desea pagar?: "))
                success = register_payment(id_player, number_of_months)
                if success:
                    print("Pago registrado correctamente")
                else:
                    print("Error: Jugador no existe o está inactivo")
            case 2:
                print(f"-----LISTADO DE PAGOS-----")
                show_payments()
            case 3:
                id_player = int(input(f"Escribe el id del jugador: "))
                player_payments_list  = player_payments(payments, id_player)
                if not player_payments_list:
                    print("El jugador no tiene pagos registrados")
                else:
                    print_player_payments(player_payments_list) 
            case 4:
                debtors = list_of_debtors()
                if not debtors:
                    print("No hay jugadores con deuda")
                else:
                    print("-----JUGADORES CON DEUDA-----")
                    print_player(debtors)
            case 5:
                print(f'Volviendo al menú principal...')
                break

def main_menu():
    while True:
        print(f'1. Gestión de jugadores \n2. Gestión de pagos \n3.Salir')
        menu_option = int(input(f"Elige una opción: "))

        match menu_option:
            case 1:
                show_menu_players()
            case 2:
                show_menu_payments()
            case 3:
                print(f'Saliendo del programa...')
                break
            case _:
                print(f'Opción no válida')


        