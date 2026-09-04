print("\nAnalisador de notas\n")

quantidade = int(input("Quantas notas deseja inserir?:"))
notas = []

for i in range(quantidade):
    while True:
        try:
            notas.append(float(input("Insira a nota:")))
            break

        except ValueError:
            print("Valor inválido!")

