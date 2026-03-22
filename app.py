"""Aplicativo de lista de tarefas com menu no terminal.

Execute com:
    python3 app.py
"""

from __future__ import annotations


def exibir_menu() -> None:
    """Mostra o menu principal na tela."""
    print("\n=== Lista de Tarefas ===")
    print("1. Adicionar tarefa")
    print("2. Listar tarefas")
    print("3. Remover tarefa")
    print("4. Sair")


def adicionar_tarefa(tarefas: list[str]) -> None:
    """Adiciona uma nova tarefa à lista."""
    descricao = input("Digite a nova tarefa: ").strip()

    if not descricao:
        print("Tarefa vazia não pode ser adicionada.")
        return

    tarefas.append(descricao)
    print(f"Tarefa adicionada: {descricao}")


def listar_tarefas(tarefas: list[str]) -> None:
    """Exibe todas as tarefas cadastradas."""
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return

    print("\nTarefas cadastradas:")
    for indice, tarefa in enumerate(tarefas, start=1):
        print(f"{indice}. {tarefa}")


def remover_tarefa(tarefas: list[str]) -> None:
    """Remove uma tarefa pelo número informado pelo usuário."""
    if not tarefas:
        print("Não há tarefas para remover.")
        return

    listar_tarefas(tarefas)
    escolha = input("Digite o número da tarefa que deseja remover: ").strip()

    if not escolha.isdigit():
        print("Entrada inválida. Digite um número válido.")
        return

    indice = int(escolha)
    if indice < 1 or indice > len(tarefas):
        print("Número de tarefa inválido.")
        return

    tarefa_removida = tarefas.pop(indice - 1)
    print(f"Tarefa removida: {tarefa_removida}")


def main() -> None:
    """Executa o loop principal do aplicativo."""
    tarefas: list[str] = []

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            adicionar_tarefa(tarefas)
        elif opcao == "2":
            listar_tarefas(tarefas)
        elif opcao == "3":
            remover_tarefa(tarefas)
        elif opcao == "4":
            print("Encerrando o aplicativo. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
