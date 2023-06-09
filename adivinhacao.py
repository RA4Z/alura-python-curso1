print('*********************************')
print('Bem vindo ao jogo de Adivinhação!')
print('*********************************')

numero_secreto = 42

chute = input('Digite o seu número: ')
chute = int(chute)

acertou     = chute == numero_secreto
maior       = chute > numero_secreto
menor       = chute < numero_secreto

print('Você digitou ', chute)

if (acertou):
    print('Você acertou')
else:
    if(maior):
        print('Você errou! O seu chute foi maior do que o número secreto!')
    elif(menor):
        print('Você errou! O seu chute foi menor do que o número secreto!')


print('Fim do jogo!')