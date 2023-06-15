import random

def jogar():
    imprime_mensagem_abertura()
    palavra_secreta = carrega_palavra_secreta()

    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0

    while(not enforcou and not acertou):

        chute = pede_chute()

        if(chute in palavra_secreta):
            marca_chute_correto(palavra_secreta, chute, letras_acertadas)
        else:
            erros += 1
            print('Errou! \nO número de tentativas restantes é {}'.format(6 - erros))
        
        enforcou = erros == 6
        acertou = '_' not in letras_acertadas
        print(letras_acertadas)

    if(acertou):
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor()

# -------------------------------------------------------------------------------------------

def imprime_mensagem_vencedor():
    print('Você ganhou!!')

def imprime_mensagem_perdedor():
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

# Pedir para o usuário chutar uma letra
def pede_chute():
    chute = input('Qual letra? ')
    chute = chute.strip().upper()
    return chute

# Registrar na lista as letras quando são acertadas
def marca_chute_correto(palavra_secreta, chute, letras_acertadas):
    index = 0
    for letra in palavra_secreta:
        if(chute == letra):
            letras_acertadas[index] = chute
        index += 1

# Rodar função do jogo ao executar este arquivo
if(__name__ == '__main__'):
    jogar()