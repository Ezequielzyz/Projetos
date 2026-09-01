opcao = 1

while opcao != 0:

        print("""--Calculadora--

1. Soma
2. Subtração
3. Multiplicação
4. Divisão
0. Sair""")

        opcao = int(input("\nEscolha uma opção:"))

        if opcao == 1:
                
                num1 = int(input("\nColoque o primeiro número:"))
                num2 = int(input("\nColoque o segundo número:"))
                print(f"\nO resultado é: {num1 + num2}\n")

        elif opcao == 2:
                
                num1 = int(input("\nColoque o primeiro número:"))
                num2 = int(input("\nColoque o segundo número:"))
                print(f"\nO resultado é: {num1 - num2}\n")

        elif opcao == 3:
                
            num1 = int(input("\nColoque o primeiro número:"))
            num2 = int(input("\nColoque o segundo número:"))
            print(f"\nO resultado é: {num1 * num2}\n")

        elif opcao == 4:
                
                num1 = int(input("\nColoque o primeiro número:"))
                num2 = int(input("\nColoque o segundo número:"))
                print(f"\nO resultado é: {num1 / num2}\n")

        elif opcao not in (0, 1, 2, 3, 4): 
                print("\nOpção inválida!\n")