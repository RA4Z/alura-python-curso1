import random

print('*********************************')
print('Bem vindo ao jogo de Adivinhação!')
print('*********************************')

numero_secreto = random.randrange(1,101)

print('Qual nível de dificuldade?')
print('(1) Fácil \n(2) Médio \n(3) Difícil')
nivel = int(input('Defina o nível: '))

if(nivel == 1):
    total_de_tentativas = 20
elif(nivel == 2):
    total_de_tentativas = 10
else:
    total_de_tentativas = 5

for rodada in range(1,total_de_tentativas + 1):
    print('Tentativa {} de {}'.format(rodada, total_de_tentativas))
    chute = input('Digite um número entre 1 e 100: ')
    chute = int(chute)
    print('Você digitou ', chute)

    if(chute < 1 or chute > 100):
        print('Você deve digitar um número entre 1 e 100!')
        continue

    acertou     = chute == numero_secreto
    maior       = chute > numero_secreto
    menor       = chute < numero_secreto

    if (acertou):
        print('Você acertou!')
        break
    else:
        if(maior):
            print('Você errou! O seu chute foi maior do que o número secreto!')
        elif(menor):
            print('Você errou! O seu chute foi menor do que o número secreto!')

print('Fim do jogo!')