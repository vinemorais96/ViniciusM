def cadastrar_colaborador(nome: str, cargo: str, salario: float) -> dict:
    """Retorna um dicionário estruturado com os dados do colaborador."""
    return {
        "nome": nome,
        "cargo": cargo,
        "salario": salario
    }


def exibir_colaboradores(lista_colaboradores: list) -> None:
    """Percorre a lista e exibe os colaboradores formatados."""
    if not lista_colaboradores:
        print("\nNenhum colaborador cadastrado.")
        return

    print("\n--- Lista de Colaboradores ---")
    for colaborador in lista_colaboradores:
        print(f"Nome: {colaborador['nome']} | Cargo: {colaborador['cargo']} | Salário: R$ {colaborador['salario']:.2f}")
        