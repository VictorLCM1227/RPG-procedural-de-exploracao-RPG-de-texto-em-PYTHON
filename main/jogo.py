from time import sleep

from utilidades import menu, cabecalho, linha
from classes.personagem import Personagem
from labirinto import iniciar_labirinto


def escrever(msg):
    print(linha())

    for caractere in msg:
        print(caractere, end='', flush=True)
        sleep(0.1)

    print()


def game_over():
    cabecalho('GAME OVER', '=')

    print('Você morreu.')
    print()
    print('Sua busca pelo Elixir chegou ao fim.')
    print()

    escolha = menu(
        'GAME OVER',
        '>>> Escolha: ',
        [
            'Sair',
            'Voltar ao menu'
        ],
        simb='-'
    )

    return escolha

def tela_vitoria():
    cabecalho('VITÓRIA', '=')

    print('Você encontrou o Elixir!')
    print()
    print('Depois de atravessar os labirintos')
    print('e enfrentar seus perigos,')
    print('você finalmente alcançou seu objetivo.')
    print()
    print('O Elixir capaz de curar todas as doenças')
    print('da humanidade agora está em suas mãos.')
    print()

    print('Você venceu a aventura!')
    print()

    escolha = menu(
        'VITÓRIA',
        '>>> Escolha: ',
        [
            'Sair',
            'Voltar ao menu'
        ],
        simb='-'
    )

    return escolha


def jogar():

    escrever('Você acorda...')
    escrever('Não sabe onde está.')
    escrever('Parece estar em um labirinto.')

    print()

    nome = input('Qual é o seu nome? ').strip()

    personagem = Personagem(nome)

    escrever(
        f'Você percebe que é um '
        f'{personagem.raca.nome} {personagem.classe.nome}.'
    )

    print()

    cabecalho('SEU PERSONAGEM', '-')

    print(f'Nome: {personagem.nome}')
    print(f'Raça: {personagem.raca.nome}')
    print(f'Classe: {personagem.classe.nome}')

    print()

    print(f'Vida: {personagem.vida}')
    print(f'Ataque: {personagem.ataque}')
    print(f'Defesa: {personagem.defesa}')
    print(f'Velocidade: {personagem.velocidade}')

    print()

    escolha_menu = menu(
        'O QUE FAZER?',
        '>>> Escolha: ',
        [
            'Sair',
            'Explorar',
            'Gritar por ajuda'
        ],
        simb='-'
    )

    match escolha_menu:

        case 0:
            cabecalho('SAINDO...')

        case 1:
            cabecalho('EXPLORAR')

            resultado = iniciar_labirinto(personagem)

            if resultado == 'derrota':
                game_over()

            elif resultado == 'vitoria':
                tela_vitoria()

        case 2:
            cabecalho('SOCORROOOOO!!!')
            escrever('Ninguém te ouviu...')