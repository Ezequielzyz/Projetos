opcao = None

while opcao != 0:

        print("""--Calculadora--

1. Soma
2. Subtração
3. Multiplicação
4. Divisão
0. Sair""")

        opcao = int(input("\nEscolha uma opção:"))

        if 1 <= opcao <= 4:
                
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))

                if opcao == 1:
                        resultado = num1 + num2
                        print(f"O resultado da soma é: {resultado}")


                elif opcao == 2:
                        resultado = num1 - num2
                        print(f"O resultado da subtração é: {resultado}")


                elif opcao == 3:
                        resultado = num1 * num2
                        print(f"O resultado da multiplicação é: {resultado}")


                elif opcao == 4:
                        if num2 != 0:
                                resultado = num1 / num2
                                print(f"O resultado da divisão é: {resultado}")


                else:
                    print("Erro: Divisão por zero não é permitida.")

        else:
                print("Opção inválida. Por favor, escolha uma opção válida.")

#Calculadora completa!