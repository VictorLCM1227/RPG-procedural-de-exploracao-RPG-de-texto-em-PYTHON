class Personagem:
    def __init__(self):
        self.vida = 10 # mecanica: o ataque só causa dano na vida os pontos superiores a defesa, pode escolher atacar ou defender
        self.ataque = 10
        self.defesa = 10
        self.velocidade = 10 # a velocidade é para a opção de fugir, se escolher fugir e o personagem tiver mais velocidade que o montro, escapa, senao leva ataque