"""
Agenda de contatos em terminal
"""
def add_contact(contacts, name, phone_number, email, favorite = False):
    contacts.append({
        "name": name,
        "phone_number": phone_number,
        "email": email,
        "favorite": favorite
    })

    print("Contato adicionado com sucesso")
    return


def list_contacts(contacts, favorites_only):
    print(f"\n----- Lista de contatos {'favoritos ' if favorites_only else ''}-----")
    for key, item in enumerate(contacts):
        if favorites_only and not item['favorite']:
            continue
        print(f"Código: {key + 1}, Nome: {item['name']}, Telefone: {item['phone_number']}, E-mail: {item['email']}, Favorito: {'sim' if item['favorite'] else 'não'}")
    return


def update_contact(contacts, name, phone_number, email, option):
    if option.isdigit() and int(option) >= 1 and int(option) <= len(contacts):
        index =  int(option) - 1
        contacts[index] = {
            "name": name or contacts[index]["name"],
            "phone_number": phone_number or contacts[index]["phone_number"],
            "email": email or contacts[index]["email"],
            "favorite": contacts[index]["favorite"]
        }

        print("Contato atualizado com sucesso")
        return

    print("Contato não encontrado")

    return
    

def toggle_favorite(contacts, option, favorite = True):
    if option.isdigit() and int(option) >= 1 and int(option) <= len(contacts):
        index =  int(option) - 1

        contacts[index]["favorite"] = favorite

        print(f"Contato \"{contacts[index]['name']}\" { 'marcado' if favorite else 'desmarcado' } como favorito.")
        return

    print("Contato não encontrado")

    return

def remove_contact(contacts, option):
    if option.isdigit() and int(option) >= 1 and int(option) <= len(contacts):
        contacts.pop(int(option) - 1)
        print("Contato removido")
        return
    
    print("Contato não encontrado")

    return

contacts = []

while True:
    print("\n===== Menu da Agenda de Contatos =====")
    print("1. Adicionar um novo contato")
    print("2. Ver contatos")
    print("3. Ver contatos favoritos")
    print("4. Atualizar contato")
    print("5. Marcar/desmarcar contato como favorito")
    print("6. Remover contato")
    print("7. Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        name = input("Informe o nome do contato: ")
        phone_number = input("Informe o telefone do contato: ")
        email = input("Informe o email do contato: ")
        add_contact(contacts, name, phone_number, email)

    elif escolha == "2":
        list_contacts(contacts, False)

    elif escolha == "3":
        list_contacts(contacts, True)

    elif escolha == "4":
        code = input("Informe o codigo do contato a ser atualizado (Utilize \"2. Ver contatos\" para obter o código): ")
        name = input("Informe o novo nome do contato: ")
        email = input("Informe o novo email do contato: ")
        phone_number = input("Informe o novo telefone do contato: ")
        update_contact(contacts, name, phone_number, email, code)

    elif escolha == "5":
        print("1. Favoritar")
        print("2. Desfavoritar")
        option = input("Escolha sua opção: ")
        if option == "1":
            favorite = True
        elif option == "2":
            favorite = False
        else:
            favorite = None

        if favorite is not None:
            code = input("Informe o código do contato a ser atualizado: ")
            toggle_favorite(contacts, code, favorite)
        
        else:
            print("Opção inválida")

    elif escolha == "6":
        code = input("Informe o código do contato a ser removido: ")
        remove_contact(contacts, code)

    elif escolha == "7":
        break

    else: 
        print("Opção inválida")

print("Programa finalizado")