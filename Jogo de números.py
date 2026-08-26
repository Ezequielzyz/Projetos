print("\nBem-vindo ao jogo de números!\n")
import random

numero_escolhido = int(input("Escolha um número entre 1 e 100: "))

numero_sorteado = random.randint(1, 100)

diferenca = abs(numero_escolhido - numero_sorteado)


while numero_escolhido != numero_sorteado:

        if numero_escolhido > 100 or numero_escolhido < 1:
            print("Escolha um número válido entre 1 e 100")
            numero_escolhido = int(input("Escolha um número entre 1 e 100: "))
            diferenca = abs(numero_escolhido - numero_sorteado)

        elif diferenca >= 1 and diferenca <=10:
                 print("Você está perto!")
                 numero_escolhido = int(input("Escolha um número entre 1 e 100: "))
                 diferenca = abs(numero_escolhido - numero_sorteado)

        else:
               print("Você está longe!")
               numero_escolhido = int(input("Escolha um número entre 1 e 100: "))
               diferenca = abs(numero_escolhido - numero_sorteado)
               
if numero_escolhido == numero_sorteado:
     print("Parabéns! Você acertou o número sorteado:", numero_sorteado)