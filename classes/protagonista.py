from personagem import Personagem

class Protagonista(Personagem):
    def __init__(self, vida, ataque, defesa, velocidade):
        super().__init__(vida, ataque, defesa, velocidade)

    def dar_aula(self):
        print(f'Prof. {self.nome} começou a dar aula')