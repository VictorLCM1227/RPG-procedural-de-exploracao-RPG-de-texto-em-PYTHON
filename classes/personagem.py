class Personagem:
    def __init__(self):
        self.vida = 10 # mecanica: o ataque só causa dano na vida os pontos superiores a defesa, pode escolher atacar ou defender
        self.ataque = 10
        self.defesa = 10
        self.velocidade = 10 # a velocidade é para a opção de fugir, se escolher fugir e o personagem tiver mais velocidade que o montro, escapa, senao leva ataque


class Protagonista(Personagem):
    def __init__(self, vida, ataque, defesa, velocidade):
        super().__init__(vida, ataque, defesa, velocidade)

    def dar_aula(self):
        print(f'Prof. {self.nome} começou a dar aula')