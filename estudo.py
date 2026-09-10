print("Gerenciador de Finanças Pessoais")

saldo = 0
historico = []

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
                valor = float(input("Valor do ganho? :"))
                transacao = {"Tipo": "Ganho", "Origem": tipo_ganho, "Valor": valor}
                historico.append(transacao)
                print("Ganho armazenado com sucesso!")
                saldo += transacao["Valor"]
                print(f"Seu saldo é: {saldo}!")
                break
            
            except ValueError:
                print("Insira um valor válido!")

    elif escolha == 2:
        tipo_despesa = input("Qual origem da despesa? :")

        while True:
            
            try:   
                valor = float(input("Valor da despesa:"))
                transacao = {"Tipo": "Despesa", "Origem": tipo_despesa, "Valor": valor}
                historico.append(transacao)
                print("Despesa armazenada com sucesso!")
                saldo -= transacao["Valor"]
                print(f"Seu saldo é: {saldo}!")
                break
            
            except ValueError:
                print("Insira um valor válido!")

    elif escolha == 3:

        for transacao in historico:
            tipo = transacao["Tipo"]
            origem = transacao["Origem"]
            valor = transacao["Valor"]

            if tipo == "Ganho":
                print(f" [+] R${valor} {origem}")

    elif escolha == 4:
        print("Fechando...")
        break