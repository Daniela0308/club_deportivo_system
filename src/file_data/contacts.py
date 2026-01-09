from storage import load_data, save_data

def show_menu():
    print(f'1. Ver contactos \n2. Agregar Contactos \n3. Editar Contacto \n4.Eliminar Contacto \n5.Salir')

def show_contacts(contacts):
    if not contacts:
        print(f'No hay contactos registrados.')
        return

    for id in contacts:
        print(f'\nNombre: {id["nombre"]} \nDocumento: {id["documento"]} \nCategoria: {id["categoria"]} \nTelefono: {id["telefono"]} \nAcudiente: {id["acudiente"]} \n')

def add_contact(contacts):
    name = input("Nombre del jugador: ")
    document = input("Documento: ")
    category = input("Categoría: ")
    phone = input("Teléfono: ")
    attendant = input("Nombre del acudiente: ")

    contact = {
        "nombre": name,
        "documento": document,
        "categoria": category,
        "telefono": phone,
        "acudiente": attendant
    }

    contacts.append(contact)
    save_data(contacts)
    print(f'Contacto agregado correctamente.')

def edit_contact(contacts):
    id_edit = input(f'Ingrese el número de documento del contacto que quiere modificar: ')
    print(f'Ahora ingrese los datos nuevos: ')
    new_name = input(f'Nombre del jugador: ')
    new_document = input(f'Documento: ')
    new_category = input(f'Categoría: ')
    new_phone = input(f'Teléfono: ')
    new_attendant = input(f'Nombre del acudiente: ')

    for new_data in contacts:
        if id_edit == new_data["documento"]:
            new_data.update({"nombre": new_name, "documento": new_document, "categoria": new_category, "telefono": new_phone, "acudiente": new_attendant})
    print(f'Actualización de contacto completada')
    save_data(contacts)

def delete_contact(contacts):
    id_delete = input(f'Ingrese el número de documento del contacto que quiere modificar: ')
    contacts[:] = [new_data for new_data in contacts if new_data["documento"] != id_delete]
    save_data(contacts)


def main():
    contacts = load_data()
    #print(contacts,type(contacts))

    while True:
        show_menu()
        option = int(input('Selecciona una opción: '))
        if option == 1:
            print(f'\n LISTA DE CONTACTOS')
            show_contacts(contacts)
        elif option == 2:
            add_contact(contacts)
        elif option == 3:
            edit_contact(contacts)
        elif option == 4:
            delete_contact(contacts)
        elif option == 5:
            print(f'Saliendo del programa...')
            break
        else:
            print(f'Opción no válida')

main()