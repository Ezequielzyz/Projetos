import csv
import os

print("\nGerenciador de Finanças Pessoais\n")

arquivos_dados = "historico_financas"

saldo = 0
historico = []

if os.path.exists(arquivos_dados)

while True:
    try:
        print("1. Cadastar Ganhos")
        print("2. Cadastrar Gastos")
        print("3. Ver histórico")
        print("4. Fechar programa")
        escolha = int(input("\nEscolha uma opção: "))

    except ValueError:
        print("\nInsira um valor válido!\n")
        continue
    

    if escolha == 1:
        
        tipo_ganho = input("\nQual a origem do ganho? :")

        while True:

            try:
                valor = float(input("Valor do ganho? :"))
                transacao = {"Tipo": "Ganho", "Origem": tipo_ganho, "Valor": valor}
                historico.append(transacao)
                print("\nGanho armazenado com sucesso!")
                saldo += transacao["Valor"]
                print(f"\nSeu saldo é: R${saldo:.2f}!\n")
                break
            
            except ValueError:
                print("Insira um valor válido!")

    elif escolha == 2:
        tipo_despesa = input("\nQual origem da despesa? :")

        while True:
            
            try:   
                valor = float(input("Valor da despesa:"))
                transacao = {"Tipo": "Despesa", "Origem": tipo_despesa, "Valor": valor}
                historico.append(transacao)
                print("\nDespesa armazenada com sucesso!")
                saldo -= transacao["Valor"]
                print(f"\nSeu saldo é: R${saldo:.2f}!\n")
                break
            
            except ValueError:
                print("Insira um valor válido!")

    elif escolha == 3:

        for transacao in historico:
            tipo = transacao["Tipo"]
            origem = transacao["Origem"]
            valor = transacao["Valor"]

            if tipo == "Ganho":
                print(f"\n [+] R${valor:.2f} - {origem}\n")

            else:
                print(f"\n [-] R${abs(valor):.2f} - {origem}\n")

        if saldo > 0:
            print(f"\nSALDO: [+] R${saldo:.2f}\n")
        
        else:
            print(f"\nSALDO: [-] R${abs(saldo):.2f}\n")
        

    elif escolha == 4:
        print("Fechando...")
        break

    else:
        print("\nInsira um valor válido\n")