from user_service import adicionar_usuario, listar_usuarios, desativar_usuario
from email_service import enviar_email_boas_vindas
from external_api import buscar_usuario_api

def menu():
    while True:
        print("\n=== Sistema de Usuários ===")
        print("1 - Adicionar usuário")
        print("2 - Listar usuários")
        print("3 - Desativar usuário")
        print("4 - Buscar usuário na API")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Digite o nome: ")
            email = input("Digite o email: ")
            usuario = adicionar_usuario(nome, email)
            enviar_email_boas_vindas(usuario)
            print(f"Usuário {nome} adicionado com sucesso!")

        elif opcao == "2":
            listar_usuarios()

        elif opcao == "3":
            user_id = int(input("Digite o ID do usuário: "))
            if desativar_usuario(user_id):
                print("Usuário desativado.")
            else:
                print("Usuário não encontrado.")

        elif opcao == "4":
            user_id = int(input("Digite o ID: "))
            dados = buscar_usuario_api(user_id)
            if dados:
                print(f"Usuário encontrado na API: {dados['nome']} ({dados['email']})")
            else:
                print("Usuário não encontrado.")

        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()
