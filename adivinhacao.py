print('*********************************')
print('Bem vindo ao jogo de Adivinhação!')
print('*********************************')

numero_secreto = 42
total_de_tentativas = 3

for rodada in range(1,total_de_tentativas + 1):
    print('Tentativa {} de {}'.format(rodada, total_de_tentativas))
    chute = input('Digite o seu número: ')
    chute = int(chute)
    print('Você digitou ', chute)

    acertou     = chute == numero_secreto
    maior       = chute > numero_secreto
    menor       = chute < numero_secreto

    if (acertou):
        print('Você acertou')
        total_de_tentativas = 0
    else:
        if(maior):
            print('Você errou! O seu chute foi maior do que o número secreto!')
        elif(menor):
            print('Você errou! O seu chute foi menor do que o número secreto!')

print('Fim do jogo!')