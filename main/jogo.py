# main/jogo
from time import sleep
from utilidades import menu, cabecalho

msg = 'Você acorda...'
for caractere in msg:
    print(caractere, end='', flush=True)
    sleep(0.1)
print()

msg = 'Não sabe onde está.'
for caractere in msg:
    print(caractere, end='', flush=True)
    sleep(0.1)
print()

msg = 'Parece estar em um labirinto.'
for caractere in msg:
    print(caractere, end='', flush=True)
    sleep(0.1)
print()

escolha_menu = menu('O QUE FAZER? ', '>>> Escolha: ', ['Sair', 'Explorar', 'Gritar por ajuda'], simb='-')
