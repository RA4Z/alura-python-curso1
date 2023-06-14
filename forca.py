
def jogar():
    print('*********************************')
    print('***Bem vindo ao jogo da Forca!***')
    print('*********************************')

    palavra_secreta = 'palavra'
    enforcou = False
    acertou = False

    #Enquanto não enforcou e não acertou
    while(not enforcou and not acertou):

        chute = input('Qual letra? ')
        chute = chute.strip()

        index = 0
        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()):
                print('Encontrado a letra {} na posição {}'.format(chute.upper(),index))
            index = index + 1

        print('jogando ...')

    print('Fim de jogo')

if(__name__ == '__main__'):
    jogar()