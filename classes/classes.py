# classes/classes
class Mago:
    nome = 'Mago'

    # Modificadores dos atributos básicos
    modificador_vida = 0.80
    modificador_ataque = 0.90
    modificador_defesa = 0.90
    modificador_velocidade = 1.00

    # Atributos especiais
    mana = 100
    poder_magico = 20


class Guerreiro:
    nome = 'Guerreiro'

    # Modificadores dos atributos básicos
    modificador_vida = 1.15
    modificador_ataque = 1.15
    modificador_defesa = 1.10
    modificador_velocidade = 0.90

    # Atributos especiais
    resistencia = 20
    bloqueio = 10


class Ladino:
    nome = 'Ladino'

    # Modificadores dos atributos básicos
    modificador_vida = 0.85
    modificador_ataque = 1.10
    modificador_defesa = 0.80
    modificador_velocidade = 1.25

    # Atributos especiais
    energia = 100
    chance_critico = 20


class Clerigo:
    nome = 'Clérigo'

    # Modificadores dos atributos básicos
    modificador_vida = 1.00
    modificador_ataque = 0.85
    modificador_defesa = 1.05
    modificador_velocidade = 0.95

    # Atributos especiais
    mana = 80
    poder_cura = 25


class Barbaro:
    nome = 'Bárbaro'

    # Modificadores dos atributos básicos
    modificador_vida = 1.25
    modificador_ataque = 1.30
    modificador_defesa = 0.90
    modificador_velocidade = 0.80

    # Atributos especiais
    furia = 0
    resistencia = 15


class Bardo:
    nome = 'Bardo'

    # Modificadores dos atributos básicos
    modificador_vida = 0.95
    modificador_ataque = 0.85
    modificador_defesa = 0.95
    modificador_velocidade = 1.10

    # Atributos especiais
    mana = 70
    inspiracao = 20


class Paladino:
    nome = 'Paladino'

    # Modificadores dos atributos básicos
    modificador_vida = 1.15
    modificador_ataque = 1.05
    modificador_defesa = 1.20
    modificador_velocidade = 0.85

    # Atributos especiais
    mana = 50
    poder_sagrado = 20


class Druida:
    nome = 'Druida'

    # Modificadores dos atributos básicos
    modificador_vida = 1.00
    modificador_ataque = 0.90
    modificador_defesa = 1.00
    modificador_velocidade = 1.05

    # Atributos especiais
    mana = 90
    poder_natural = 20


class Patrulheiro:
    nome = 'Patrulheiro'

    # Modificadores dos atributos básicos
    modificador_vida = 1.00
    modificador_ataque = 1.10
    modificador_defesa = 0.95
    modificador_velocidade = 1.15

    # Atributos especiais
    energia = 80
    precisao = 20


class Monge:
    nome = 'Monge'

    # Modificadores dos atributos básicos
    modificador_vida = 0.95
    modificador_ataque = 1.05
    modificador_defesa = 1.00
    modificador_velocidade = 1.25

    # Atributos especiais
    energia = 100
    ki = 50
