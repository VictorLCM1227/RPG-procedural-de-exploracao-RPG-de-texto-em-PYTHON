from random import choice, randint

linhas = 21
colunas = 81

mapa = []

# Cria o mapa inteiro com paredes
for linha in range(linhas):
    nova_linha = []

    for coluna in range(colunas):
        nova_linha.append('#')

    mapa.append(nova_linha)


def dentro_do_mapa(linha, coluna):
    return (
        0 < linha < linhas - 1
        and 0 < coluna < colunas - 1
    )


def gerar_labirinto(linha, coluna):
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

        if dentro_do_mapa(nova_linha, nova_coluna):

            if mapa[nova_linha][nova_coluna] == '#':

                meio_linha = linha + direcao[0] // 2
                meio_coluna = coluna + direcao[1] // 2

                mapa[meio_linha][meio_coluna] = ' '

                gerar_labirinto(nova_linha, nova_coluna)


# -------------------------
# GERA O LABIRINTO
# -------------------------

gerar_labirinto(1, 1)


# -------------------------
# JOGADOR
# -------------------------

jogador_linha = 1
jogador_coluna = 1

mapa[jogador_linha][jogador_coluna] = 'P'


# -------------------------
# SAÍDA VERDADEIRA
# -------------------------

saida_linha = linhas - 2
saida_coluna = colunas - 2

mapa[saida_linha][saida_coluna] = 'S'


# -------------------------
# SAÍDA FALSA
# -------------------------

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


# -------------------------
# EVENTOS
# -------------------------

def criar_eventos():

    for linha in range(1, linhas - 1, 2):

        for coluna in range(1, colunas - 1, 2):

            if mapa[linha][coluna] != ' ':
                continue

            # Não coloca evento no início
            if linha == jogador_linha and coluna == jogador_coluna:
                continue

            # Não coloca evento nas saídas
            if (
                linha == saida_linha
                and coluna == saida_coluna
            ):
                continue

            evento = randint(1, 100)

            # MONSTRO - 30%
            if evento <= 30:
                mapa[linha][coluna] = 'M'

            # ITEM - 10%
            elif evento <= 40:
                mapa[linha][coluna] = 'I'

            # TESOURO - 5%
            elif evento <= 45:
                mapa[linha][coluna] = 'T'


criar_eventos()


# -------------------------
# MOSTRA O MAPA
# -------------------------

for linha in mapa:
    print(''.join(linha))