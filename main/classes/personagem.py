from random import choice

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

def sortear_raca():
    return choice(racas)

def sortear_classe():
    return choice(classes)

class Personagem:
    def __init__(self, nome):
        self.nome = nome

        self.raca = sortear_raca()
        self.classe = sortear_classe()

        # Atributos básicos da raça
        self.vida = self.raca.vida
        self.ataque = self.raca.ataque
        self.defesa = self.raca.defesa
        self.velocidade = self.raca.velocidade

        # Modificadores da classe
        self.vida *= self.classe.modificador_vida
        self.ataque *= self.classe.modificador_ataque
        self.defesa *= self.classe.modificador_defesa
        self.velocidade *= self.classe.modificador_velocidade

