# main/combate

from random import choice
from rich import print
from rich.panel import Panel

from utilidades import menu, cabecalho

from classes.racas import (
    Humano,
    Elfo,
    Anao,
    Fantasma,
    Demonio,
    Orc
)

from classes.classes import (
    Mago,
    Guerreiro,
    Ladino,
    Clerigo,
    Barbaro,
    Bardo,
    Paladino,
    Druida,
    Patrulheiro,
    Monge
)


# ============================================================
# LISTAS DE RAÇAS E CLASSES
# ============================================================

racas = [
    Humano,
    Elfo,
    Anao,
    Fantasma,
    Demonio,
    Orc
]

classes = [
    Mago,
    Guerreiro,
    Ladino,
    Clerigo,
    Barbaro,
    Bardo,
    Paladino,
    Druida,
    Patrulheiro,
    Monge
]


# ============================================================
# SORTEIO
# ============================================================

def sortear_raca():
    return choice(racas)


def sortear_classe():
    return choice(classes)


# ============================================================
# CRIAÇÃO DO MONSTRO
# ============================================================

def criar_monstro(dificuldade=1):

    raca = sortear_raca()
    classe = sortear_classe()

    vida = raca.vida * classe.modificador_vida
    ataque = raca.ataque * classe.modificador_ataque
    defesa = raca.defesa * classe.modificador_defesa
    velocidade = raca.velocidade * classe.modificador_velocidade

    # A dificuldade aumenta os atributos do monstro
    vida += dificuldade * 5
    ataque += dificuldade * 2
    defesa += dificuldade
    velocidade += dificuldade

    monstro = {
        'nome': f'{raca.nome} {classe.nome}',
        'raca': raca,
        'classe': classe,
        'vida': round(vida),
        'vida_maxima': round(vida),
        'ataque': round(ataque),
        'defesa': round(defesa),
        'velocidade': round(velocidade)
    }

    return monstro


# ============================================================
# STATUS
# ============================================================

def mostrar_status(personagem, monstro):

    print()

    painel = (
        f'[blue]VOCÊ[/blue]\n'
        f'Vida: {personagem.vida}\n'
        f'Ataque: {personagem.ataque}\n'
        f'Defesa: {personagem.defesa}\n'
        f'Velocidade: {personagem.velocidade}\n'
        f'\n'
        f'[red]{monstro["nome"].upper()}[/red]\n'
        f'Raça: {monstro["raca"].nome}\n'
        f'Classe: {monstro["classe"].nome}\n'
        f'Vida: {monstro["vida"]}\n'
        f'Ataque: {monstro["ataque"]}\n'
        f'Defesa: {monstro["defesa"]}\n'
        f'Velocidade: {monstro["velocidade"]}'
    )

    print(
        Panel(
            painel,
            title='STATUS DO COMBATE',
            border_style='red'
        )
    )


# ============================================================
# CÁLCULO DE DANO
# ============================================================

def calcular_dano(ataque, defesa):

    # Só existe dano se o ataque for maior que a defesa.
    if ataque <= defesa:
        return 0

    return ataque - defesa


# ============================================================
# ATAQUE DO JOGADOR
# ============================================================

def atacar_jogador(personagem, monstro):

    dano = calcular_dano(
        personagem.ataque,
        monstro['defesa']
    )

    print()

    if dano == 0:

        print(
            '[yellow]Seu ataque não conseguiu '
            'superar a defesa do monstro![/yellow]'
        )

    else:

        monstro['vida'] -= dano

        print(
            f'[blue]Você atacou![/blue]'
        )

        print(
            f'O ataque causou '
            f'[red]{dano}[/red] de dano.'
        )

        if monstro['vida'] < 0:
            monstro['vida'] = 0


# ============================================================
# ATAQUE DO MONSTRO
# ============================================================

def atacar_monstro(personagem, monstro, jogador_defendendo=False):

    dano = calcular_dano(
        monstro['ataque'],
        personagem.defesa
    )

    print()

    if dano == 0:

        print(
            f'[green]{monstro["nome"]} atacou, '
            f'mas não conseguiu superar sua defesa![/green]'
        )

        return

    # Se o jogador estiver defendendo,
    # o dano recebido é reduzido pela metade.
    if jogador_defendendo:

        dano = dano // 2

        if dano < 1:
            dano = 1

        print(
            '[blue]Você estava defendendo! '
            'O dano foi reduzido pela metade.[/blue]'
        )

    personagem.vida -= dano

    if personagem.vida < 0:
        personagem.vida = 0

    print(
        f'[red]{monstro["nome"]} atacou![/red]'
    )

    print(
        f'Você recebeu '
        f'[red]{dano}[/red] de dano.'
    )


# ============================================================
# DEFESA DO MONSTRO
# ============================================================

def defesa_monstro(monstro):

    print()

    print(
        f'[red]{monstro["nome"]} '
        f'assumiu uma posição defensiva![/red]'
    )


# ============================================================
# TURNO DO MONSTRO
# ============================================================

def turno_monstro(personagem, monstro):

    print()

    cabecalho('TURNO DO MONSTRO', '-')

    escolha = choice([
        'atacar',
        'defender'
    ])

    if escolha == 'atacar':

        atacar_monstro(
            personagem,
            monstro
        )

        return 'atacar'

    else:

        defesa_monstro(monstro)

        return 'defender'


# ============================================================
# FUGA
# ============================================================

def tentar_fugir(personagem, monstro):

    print()

    print(
        '[yellow]Você tentou fugir![/yellow]'
    )

    if personagem.velocidade > monstro['velocidade']:

        print(
            '[green]Você é mais rápido que o monstro![/green]'
        )

        print(
            '[green]Você conseguiu escapar![/green]'
        )

        return True

    print(
        '[red]Você é mais lento que o monstro![/red]'
    )

    print(
        '[red]Você não conseguiu fugir![/red]'
    )

    return False


# ============================================================
# GAME OVER
# ============================================================

def game_over():

    cabecalho(
        'GAME OVER',
        '-'
    )

    print(
        '[red]Você foi derrotado.[/red]'
    )

    print(
        'Sua busca pelo Elixir chegou ao fim.'
    )

    print()


# ============================================================
# VITÓRIA
# ============================================================

def vitoria_combate(monstro):

    cabecalho(
        'MONSTRO DERROTADO',
        '-'
    )

    print(
        f'[green]Você derrotou '
        f'{monstro["nome"]}![/green]'
    )

    print(
        'Você pode continuar explorando o labirinto.'
    )

    print()


# ============================================================
# COMBATE PRINCIPAL
# ============================================================

def combate(personagem, dificuldade=1):

    monstro = criar_monstro(dificuldade)

    cabecalho(
        'ENCONTRO',
        '-'
    )

    print(
        f'[red]Um {monstro["nome"]} apareceu![/red]'
    )

    print(
        f'Raça: {monstro["raca"].nome}'
    )

    print(
        f'Classe: {monstro["classe"].nome}'
    )

    print()

    while True:

        # ----------------------------------------------------
        # VERIFICA SE O JOGADOR MORREU
        # ----------------------------------------------------

        if personagem.vida <= 0:

            game_over()

            return 'derrota'


        # ----------------------------------------------------
        # VERIFICA SE O MONSTRO MORREU
        # ----------------------------------------------------

        if monstro['vida'] <= 0:

            vitoria_combate(monstro)

            return 'vitoria'


        # ----------------------------------------------------
        # MOSTRA STATUS
        # ----------------------------------------------------

        mostrar_status(
            personagem,
            monstro
        )


        # ----------------------------------------------------
        # TURNO DO JOGADOR
        # ----------------------------------------------------

        cabecalho(
            'SEU TURNO',
            '-'
        )

        escolha = menu(
            'O QUE FAZER?',
            '>>> Escolha: ',
            [
                'Atacar',
                'Defender',
                'Fugir'
            ],
            simb='-'
        )


        jogador_defendendo = False


        # ====================================================
        # ATAQUE
        # ====================================================

        if escolha == 0:

            atacar_jogador(
                personagem,
                monstro
            )

            # Se o monstro morreu pelo ataque,
            # ele não terá outro turno.
            if monstro['vida'] <= 0:

                vitoria_combate(monstro)

                return 'vitoria'


        # ====================================================
        # DEFESA
        # ====================================================

        elif escolha == 1:

            jogador_defendendo = True

            print()

            print(
                '[blue]Você entrou em posição defensiva![/blue]'
            )


        # ====================================================
        # FUGA
        # ====================================================

        elif escolha == 2:

            conseguiu_fugir = tentar_fugir(
                personagem,
                monstro
            )

            if conseguiu_fugir:

                print()

                print(
                    '[green]Você voltou para o labirinto.[/green]'
                )

                return 'fugiu'

            # Se não conseguiu fugir,
            # o monstro ganha o turno e ataca.
            turno_monstro(
                personagem,
                monstro
            )

            continue


        # ----------------------------------------------------
        # TURNO DO MONSTRO
        # ----------------------------------------------------

        turno_monstro(
            personagem,
            monstro
        ) 