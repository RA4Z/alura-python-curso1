import random

def jogar():
    imprime_mensagem_abertura()
    palavra_secreta = carrega_palavra_secreta()

    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)
    
    while(not enforcou and not acertou):

        chute = input('Qual letra? ')
        chute = chute.strip().upper()

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[index] = chute
                index += 1
        else:
            erros += 1
            print('Errou! \nO número de tentativas restantes é {}'.format(6 - erros))
        
        enforcou = erros == 6
        acertou = '_' not in letras_acertadas
        print(letras_acertadas)

    if(acertou):
        print('Você ganhou!!')
    else:
        print('Você perdeu!!')

# Mostra mensagem de abertura do jogo
def imprime_mensagem_abertura():
    print('*********************************')
    print('***Bem vindo ao jogo da Forca!***')
    print('*********************************')

# Carregar palavra secreta do arquivo TXT
def carrega_palavra_secreta():
    palavras = []
    with open("palavras.txt", 'r') as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)

    numero = random.randrange(0,len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta
    
# Mostrar '_' para cada letra existente na palavra secreta
def inicializa_letras_acertadas(palavra_secreta):
    return ['_' for letra in palavra_secreta]

# Rodar função do jogo ao executar este arquivo
if(__name__ == '__main__'):
    jogar()