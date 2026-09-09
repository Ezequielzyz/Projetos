print("Gerenciador de Finanças Pessoais")
saldo = {"Saldo": 0}

while True:
    print("1. Cadastar Ganhos")
    print("2. Cadastrar Gastos")
    print("3. Ver histórico")
    print("4. Fechar programa")
    escolha = int(input("Escolha uma opção: "))

    if escolha == 4:
        print("Saindo...")
        break