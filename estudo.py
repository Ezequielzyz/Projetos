print("Gerenciador de Finanças Pessoais")

saldo = 0
despesas = {}
ganhos = {}

while True:
    print("1. Cadastar Ganhos")
    print("2. Cadastrar Gastos")
    print("3. Ver histórico")
    print("4. Fechar programa")
    escolha = int(input("Escolha uma opção: "))
    

    if escolha == 1:
        tipo_ganho = input("Qual a origem do ganho? :")
        while True:
            try:
                ganhos[tipo_ganho] = int(input("Valor do ganho? :"))
                print("Ganho armazenado com sucesso!")
                saldo += ganhos[tipo_ganho]
                print(saldo)
                break
            except ValueError:
                print("Insira um valor válido!")

    elif escolha == 2:
        tipo_despesa = input("Qual origem da despesa? :")
        while True:
            try:   
                despesas[tipo_despesa] = int(input("Valor da despesa:"))
                print("Despesa armazenada com sucesso!")
                saldo -= despesas[tipo_despesa]
                print(saldo)
            except ValueError:
                print("Insira um valor válido!")

    elif escolha == 4:
        print("Fechando...")
        break