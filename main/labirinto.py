from random import choice, randint
from rich import print

from combate import combate


def criar_mapa(linhas=21, colunas=41):
    mapa = []

    for linha in range(linhas):
        nova_linha = []

        for coluna in range(colunas):
            nova_linha.append('#')

        mapa.append(nova_linha)

    return mapa


def dentro_do_mapa(linha, coluna, linhas, colunas):
    return (
        0 < linha < linhas - 1
        and 0 < coluna < colunas - 1
    )


def gerar_labirinto(mapa, linhas, colunas):
    def cavar(linha, coluna):

        mapa[linha][coluna] = ' '

        direcoes = [
            (-2, 0),
            (2, 0),
            (0, -2),
            (0, 2)
        ]

        while direcoes:

            direcao = choice(direcoes)
            direcoes.remove(direcao)

            nova_linha = linha + direcao[0]
            nova_coluna = coluna + direcao[1]

            if dentro_do_mapa(
                nova_linha,
                nova_coluna,
                linhas,
                colunas
            ):

                if mapa[nova_linha][nova_coluna] == '#':

                    meio_linha = linha + direcao[0] // 2
                    meio_coluna = coluna + direcao[1] // 2

                    mapa[meio_linha][meio_coluna] = ' '

                    cavar(nova_linha, nova_coluna)

    cavar(1, 1)


def criar_saidas(mapa, linhas, colunas):

    saida_linha = linhas - 2
    saida_coluna = colunas - 2

    mapa[saida_linha][saida_coluna] = 'S'

    while True:

        falsa_linha = choice(range(1, linhas - 1, 2))
        falsa_coluna = choice(range(1, colunas - 1, 2))

        if mapa[falsa_linha][falsa_coluna] == ' ':

            if (
                falsa_linha != saida_linha
                or falsa_coluna != saida_coluna
            ):
                mapa[falsa_linha][falsa_coluna] = 'F'
                break


def criar_eventos(mapa, linhas, colunas):

    for linha in range(1, linhas - 1, 2):

        for coluna in range(1, colunas - 1, 2):

            if mapa[linha][coluna] != ' ':
                continue

            evento = randint(1, 100)

            if evento <= 30:
                mapa[linha][coluna] = 'M'

            elif evento <= 40:
                mapa[linha][coluna] = 'I'

            elif evento <= 45:
                mapa[linha][coluna] = 'T'


def mostrar_mapa(mapa):

    for linha in mapa:

        for simbolo in linha:

            if simbolo == '#':
                print('[black on white]#[/]', end='')

            elif simbolo == 'M':
                print('[red]M[/red]', end='')

            elif simbolo == 'P':
                print('[blue]P[/blue]', end='')

            elif simbolo == 'I':
                print('[green]I[/green]', end='')

            elif simbolo == 'T':
                print('[green]T[/green]', end='')

            elif simbolo == 'S':
                print('[yellow]S[/yellow]', end='')

            elif simbolo == 'F':
                print('[magenta]F[/magenta]', end='')

            else:
                print(' ', end='')

        print()


def encontrar_jogador(mapa):

    for linha in range(len(mapa)):

        for coluna in range(len(mapa[linha])):

            if mapa[linha][coluna] == 'P':
                return linha, coluna

    return None, None


def mover_jogador(mapa, linha, coluna, tecla):

    nova_linha = linha
    nova_coluna = coluna

    if tecla == 'w':
        nova_linha -= 1

    elif tecla == 's':
        nova_linha += 1

    elif tecla == 'a':
        nova_coluna -= 1

    elif tecla == 'd':
        nova_coluna += 1

    else:
        return linha, coluna, False

    if mapa[nova_linha][nova_coluna] == '#':
        print('Você bateu em uma parede!')
        return linha, coluna, False

    mapa[linha][coluna] = ' '

    linha = nova_linha
    coluna = nova_coluna

    evento = mapa[linha][coluna]

    mapa[linha][coluna] = 'P'

    return linha, coluna, evento

def remover_evento(mapa, linha, coluna):
    mapa[linha][coluna] = ' '

def iniciar_labirinto(personagem, dificuldade=1):

    linhas = 21
    colunas = 41

    mapa = criar_mapa(linhas, colunas)

    gerar_labirinto(mapa, linhas, colunas)

    criar_saidas(mapa, linhas, colunas)

    criar_eventos(mapa, linhas, colunas)

    jogador_linha = 1
    jogador_coluna = 1

    mapa[jogador_linha][jogador_coluna] = 'P'

    while True:

        print()
        print(f'LABIRINTO — DIFICULDADE {dificuldade}')
        print()

        mostrar_mapa(mapa)

        print()
        print('W = cima')
        print('S = baixo')
        print('A = esquerda')
        print('D = direita')
        print('Q = sair do labirinto')

        tecla = input('>>> ').strip().lower()

        if tecla == 'q':
            return 'sair'

        jogador_linha, jogador_coluna, evento = mover_jogador(
            mapa,
            jogador_linha,
            jogador_coluna,
            tecla
        )

        # =========================
        # SAÍDA VERDADEIRA
        # =========================

        if evento == 'S':

            print()
            print('Você encontrou a saída verdadeira!')
            print('O caminho para o Elixir está próximo...')

            return 'vitoria'

        # =========================
        # SAÍDA FALSA
        # =========================

        elif evento == 'F':

            print()
            print('Você encontrou uma saída...')
            print('Mas ela era falsa!')
            print('Você foi levado para outro labirinto.')

            dificuldade += 1

            return iniciar_labirinto(
                personagem,
                dificuldade
            )

        # =========================
        # MONSTRO
        # =========================

        elif evento == 'M':

            print()
            print('Você encontrou um MONSTRO!')

            resultado = combate(personagem, dificuldade)

            if resultado == 'vitoria':
                remover_evento(
                    mapa,
                    jogador_linha,
                    jogador_coluna
                )

            elif resultado == 'derrota':
                return 'derrota'

        elif evento == 'I':

            print()
            print('Você encontrou um ITEM!')

            # Futuramente:
            # adicionar_item(inventario)

            remover_evento(
                mapa,
                jogador_linha,
                jogador_coluna
            )

        elif evento == 'T':

            print()
            print('Você encontrou um TESOURO!')

            # Futuramente:
            # abrir_tesouro(inventario)

            remover_evento(
                mapa,
                jogador_linha,
                jogador_coluna
            )