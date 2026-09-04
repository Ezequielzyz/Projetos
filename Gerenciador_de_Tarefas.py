tarefas = {}
tarefas[1] = {"atividade": "Comprar pão", "concluida": False}

print("\nGerenciador de tarefas\n")

while True:

    opcao = (input("1 - Adicionar tarefa\n2 - Listar tarefas\n3 - Concluir tarefa\n4 - Remover tarefa\n5 - Sair\n\nEscolha uma opção:"))

    
    if opcao == "1":
        print("\nAdicionar tarefa\n")

    elif opcao == "2":
        print("\nListar tarefas\n")

    elif opcao == "3":
        print("\nConcluir tarefa\n")

    elif opcao == "4":
        print("\nRemover tarefa\n")

    elif opcao == "5":
        print("Saindo do gerenciador de tarefas...")
        break

    else:
        print("Opção inválida. Tente novamente.")

