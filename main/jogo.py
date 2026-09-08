# main/jogo
from time import sleep
from utilidades import menu, cabecalho, linha

def escrever(msg):
    print(linha)
    for caractere in msg:
        print(caractere, end='', flush=True)
        sleep(0.1)
    print()


def jogar():
    escrever('Você acorda...')

    escrever('Não sabe onde está.')

    escrever('Parece estar em um labirinto.')

    escolha_menu = menu('O QUE FAZER? ', '>>> Escolha: ', ['Sair', 'Explorar', 'Gritar por ajuda'], simb='-')
    match escolha_menu:
        case 0:
            cabecalho('SAINDO...')
        case 1:
            cabecalho('EXPLORAR')
        case 2:
            cabecalho('SOCORROOOOO!!!')
            escrever('Ninguém te ouviu...')
            

