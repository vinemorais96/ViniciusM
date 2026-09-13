from mod_rh import cadastrar_colaborador, exibir_colaboradores


def main():
    colaboradores = []

    while True:
        print("\n=== MENU RH ===")
        print("1 - Cadastrar Colaborador")
        print("2 - Listar Colaboradores")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            nome = input("Digite o nome do colaborador: ").strip()
            cargo = input("Digite o cargo: ").strip()
            try:
                salario = float(input("Digite o salário: "))
                colaborador = cadastrar_colaborador(nome, cargo, salario)
                colaboradores.append(colaborador)
                print("[SUCESSO] Colaborador cadastrado!")
            except ValueError:
                print("[ERRO] Salário inválido. Digite um número.")

        elif opcao == "2":
            exibir_colaboradores(colaboradores)

        elif opcao == "0":
            print("Encerrando o sistema...")
            break

        else:
            print("[ERRO] Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
    