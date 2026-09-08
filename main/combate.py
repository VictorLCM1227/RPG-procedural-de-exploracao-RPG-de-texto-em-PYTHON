# main/combate.py

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

    # Atributos base da raça
    vida = raca.vida
    ataque = raca.ataque
    defesa = raca.defesa
    velocidade = raca.velocidade

    # Modificadores da classe
    vida *= classe.modificador_vida
    ataque *= classe.modificador_ataque
    defesa *= classe.modificador_defesa
    velocidade *= classe.modificador_velocidade

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
        'velocidade': round(velocidade),

        # Indica se o monstro está defendendo
        'defendendo': False
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

    if monstro['defendendo']:

        painel += (
            '\n\n'
            '[yellow]MONSTRO ESTÁ DEFENDENDO[/yellow]'
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

    # O ataque precisa ser maior que a defesa.
    if ataque <= defesa:
        return 0

    return ataque - defesa


# ============================================================
# ATAQUE DO JOGADOR
# ============================================================

def atacar_jogador(personagem, monstro):

    defesa = monstro['defesa']

    # Se o monstro estiver defendendo,
    # sua defesa é dobrada neste ataque.
    if monstro['defendendo']:

        defesa *= 2

        print()

        print(
            '[yellow]O monstro está defendendo! '
            'A defesa dele foi aumentada.[/yellow]'
        )

    dano = calcular_dano(
        personagem.ataque,
        defesa
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
            '[blue]Você atacou![/blue]'
        )

        print(
            f'O ataque causou '
            f'[red]{dano}[/red] de dano.'
        )

        if monstro['vida'] < 0:
            monstro['vida'] = 0

    # A defesa dura somente um ataque.
    monstro['defendendo'] = False


# ============================================================
# ATAQUE DO MONSTRO
# ============================================================

def atacar_monstro(
    personagem,
    monstro,
    jogador_defendendo=False
):

    dano = calcular_dano(
        monstro['ataque'],
        personagem.defesa
    )

    print()

    # O ataque não superou a defesa
    if dano == 0:

        print(
            f'[green]{monstro["nome"]} atacou, '
            f'mas não conseguiu superar sua defesa![/green]'
        )

        return

    # Se o jogador estiver defendendo,
    # o dano recebido será reduzido pela metade.
    if jogador_defendendo:

        dano //= 2

        # Garante pelo menos 1 de dano
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

    monstro['defendendo'] = True

    print()

    print(
        f'[red]{monstro["nome"]} '
        f'assumiu uma posição defensiva![/red]'
    )

    print(
        '[yellow]A defesa do monstro será aumentada '
        'contra o próximo ataque.[/yellow]'
    )


# ============================================================
# TURNO DO MONSTRO
# ============================================================

def turno_monstro(
    personagem,
    monstro,
    jogador_defendendo=False
):

    print()

    cabecalho(
        'TURNO DO MONSTRO',
        '-'
    )

    # O monstro escolhe aleatoriamente
    # entre atacar e defender.
    escolha = choice([
        'atacar',
        'defender'
    ])

    if escolha == 'atacar':

        atacar_monstro(
            personagem,
            monstro,
            jogador_defendendo
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

    print(
        f'Sua velocidade: '
        f'[blue]{personagem.velocidade}[/blue]'
    )

    print(
        f'Velocidade do monstro: '
        f'[red]{monstro["velocidade"]}[/red]'
    )

    # O jogador precisa ser mais rápido.
    if personagem.velocidade > monstro['velocidade']:

        print()

        print(
            '[green]Você é mais rápido que o monstro![/green]'
        )

        print(
            '[green]Você conseguiu escapar![/green]'
        )

        return True

    print()

    print(
        '[red]Você não é mais rápido que o monstro![/red]'
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

    # Cria um novo monstro
    monstro = criar_monstro(dificuldade)

    # --------------------------------------------------------
    # APRESENTAÇÃO DO MONSTRO
    # --------------------------------------------------------

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

    # ========================================================
    # LOOP DO COMBATE
    # ========================================================

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


        # Por padrão, o jogador não está defendendo.
        jogador_defendendo = False


        # ====================================================
        # ATAQUE DO JOGADOR
        # ====================================================

        if escolha == 0:

            atacar_jogador(
                personagem,
                monstro
            )

            # Se o monstro morreu,
            # ele não terá um turno.
            if monstro['vida'] <= 0:

                vitoria_combate(monstro)

                return 'vitoria'


        # ====================================================
        # DEFESA DO JOGADOR
        # ====================================================

        elif escolha == 1:

            jogador_defendendo = True

            print()

            print(
                '[blue]Você entrou em posição defensiva![/blue]'
            )

            print(
                '[yellow]O próximo ataque do monstro '
                'causará metade do dano.[/yellow]'
            )


        # ====================================================
        # FUGA
        # ====================================================

        elif escolha == 2:

            conseguiu_fugir = tentar_fugir(
                personagem,
                monstro
            )

            # ------------------------------------------------
            # CONSEGUIU FUGIR
            # ------------------------------------------------

            if conseguiu_fugir:

                print()

                print(
                    '[green]Você voltou para o labirinto.[/green]'
                )

                return 'fugiu'


            # ------------------------------------------------
            # NÃO CONSEGUIU FUGIR
            # ------------------------------------------------

            print()

            print(
                '[red]O monstro aproveitou sua tentativa '
                'de fuga e atacou![/red]'
            )

            turno_monstro(
                personagem,
                monstro
            )

            # Verifica se morreu depois do ataque.
            if personagem.vida <= 0:

                game_over()

                return 'derrota'

            continue


        # ----------------------------------------------------
        # TURNO DO MONSTRO
        # ----------------------------------------------------

        turno_monstro(
            personagem,
            monstro,
            jogador_defendendo
        )

        # ----------------------------------------------------
        # VERIFICA SE O JOGADOR MORREU
        # ----------------------------------------------------

        if personagem.vida <= 0:

            game_over()

            return 'derrota'