print("\nBem-vindo ao jogo de números!\n")
import random

numero_escolhido = int(input("Escolha um número entre 1 e 100: "))

numero_sorteado = random.randint(1, 100)

diferenca = abs(numero_escolhido - numero_sorteado)

tentativas = 0


while numero_escolhido != numero_sorteado:
        
    tentativas += 1
    diferenca = (numero_escolhido - numero_sorteado)

    if numero_escolhido > 100 or numero_escolhido < 1:
        print("Escolha um número válido entre 1 e 100")
        numero_escolhido = int(input("Escolha um número entre 1 e 100: "))

    elif diferenca >= -10 and diferenca <= -1:
        print("Você está perto, chute mais alto!")
        numero_escolhido = int(input("Escolha um número entre 1 e 100: "))

    elif diferenca >= 1 and diferenca <= 10:
        print("Você está perto, chute mais baixo!")
        numero_escolhido = int(input("Escolha um número entre 1 e 100: "))

    elif diferenca >= -99 and diferenca <= -11:
        print("Você está longe, chute mais alto!")
        numero_escolhido = int(input("Escolha um número entre 1 e 100: "))
    
    elif diferenca >= 11 and diferenca <= 99:
        print("Você está longe, chute mais baixo!")
        numero_escolhido = int(input("Escolha um número entre 1 e 100: "))

if numero_escolhido == numero_sorteado:
    tentativas += 1
    print("Parabéns! Você acertou o número sorteado:", numero_sorteado)
    print("Número de tentativas:", tentativas)