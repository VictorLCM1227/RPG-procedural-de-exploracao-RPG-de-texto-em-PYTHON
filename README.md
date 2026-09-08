# RPG Procedural em Python

Um RPG de texto desenvolvido em Python com foco em **geração procedural**, aleatoriedade, combate, exploração e gerenciamento de inventário.

O objetivo do projeto é criar uma experiência de RPG em que cada partida seja diferente, utilizando Python para gerar personagens, mapas, monstros, tesouros e itens automaticamente.

> **Status:** Em desenvolvimento

---

## Sobre o jogo

A humanidade enfrenta diversas doenças e existe apenas uma esperança: **o Elixir**, uma substância lendária capaz de curar todas as doenças da humanidade.

O jogador assume o papel de um aventureiro em busca desse elixir.

No início da aventura, o jogo gera automaticamente um personagem com **classe, atributos e itens aleatórios**. O jogador escolhe apenas o nome do personagem.

A partir daí, começa uma jornada por **labirintos gerados proceduralmente pelo Python**, onde será necessário explorar, enfrentar monstros, encontrar tesouros e procurar a verdadeira saída.

Mas nem toda saída é o que parece.

---

## Fluxo inicial

Antes de começar uma aventura, o jogador poderá:

* Criar uma conta
* Fazer login
* Sair do jogo

O sistema de contas será utilizado para armazenar o progresso e os dados dos jogadores.

---

## Criação do personagem

Ao iniciar um novo jogo, o sistema gera automaticamente:

* Classe do personagem
* Atributos
* Itens iniciais
* Outros elementos aleatórios da aventura

O jogador deverá escolher apenas o **nome do personagem**.

Cada personagem poderá ser diferente, tornando cada partida uma experiência única.

---

## Exploração

A aventura começa em um **labirinto gerado proceduralmente pelo Python**.

Durante a exploração, diferentes elementos podem surgir aleatoriamente pelo mapa:

* Monstros
* Tesouros
* Itens
* Saídas

A posição e o tipo desses elementos serão determinados pelo sistema de geração procedural.

O jogador precisará decidir quando explorar, lutar, fugir ou procurar uma maneira de avançar.

---

## Combate

Ao encontrar um monstro, o jogador poderá escolher entre:

* **Atacar**
* **Defender**
* **Fugir**

Os resultados das ações serão determinados pelos atributos do personagem, atributos do monstro e elementos de aleatoriedade.

Os monstros também terão diferentes níveis de força.

Quanto mais a aventura avançar, maior será a possibilidade de encontrar inimigos perigosos.

---

## Monstros

Os monstros serão gerados automaticamente durante a exploração.

Existirão diferentes níveis de poder, fazendo com que alguns encontros sejam mais perigosos que outros.

A dificuldade será dinâmica:

> A cada novo turno da aventura, a probabilidade de surgirem monstros mais fortes aumenta.

Isso fará com que permanecer muito tempo explorando o mesmo labirinto se torne cada vez mais arriscado.

---

## Tesouros e itens

Além dos monstros, o mapa poderá gerar aleatoriamente:

* Tesouros
* Armas
* Equipamentos
* Itens consumíveis
* Outros itens úteis para a aventura

Esses elementos poderão aparecer em diferentes posições do labirinto.

O jogador poderá coletar e administrar os itens encontrados através do **inventário**.

---

## Inventário

O jogador terá um sistema de inventário para armazenar os itens encontrados durante a aventura.

O inventário será responsável por controlar os recursos disponíveis para o personagem e poderá influenciar diretamente suas decisões durante a exploração e os combates.

---

## As saídas

Cada labirinto possuirá duas possibilidades principais:

### Saída verdadeira

A saída verdadeira leva ao objetivo final da aventura.

Ao encontrá-la, o jogador consegue alcançar o **Elixir** e vence o jogo.

### Saída falsa

A saída falsa não encerra a aventura.

Em vez disso, o jogador será levado para **outro labirinto**, com uma dificuldade maior.

A cada novo labirinto:

* A dificuldade aumenta
* Monstros mais fortes tornam-se mais prováveis
* A exploração fica mais perigosa
* O jogador precisa administrar melhor seus recursos

---

## Objetivo

O objetivo final é simples:

> **Encontrar o Elixir capaz de curar todas as doenças da humanidade.**

Para isso, o jogador deverá sobreviver aos labirintos, administrar seu inventário, enfrentar ou evitar monstros e descobrir a verdadeira saída.

---

## Características planejadas

* [x] Sistema inicial de menu
* [ ] Criar conta
* [ ] Login
* [ ] Geração procedural de personagem
* [ ] Sistema de classes
* [ ] Sistema de atributos
* [ ] Geração procedural de labirintos
* [ ] Sistema de exploração
* [ ] Geração aleatória de monstros
* [ ] Geração aleatória de tesouros
* [ ] Geração aleatória de itens
* [ ] Sistema de combate
* [ ] Sistema de fuga
* [ ] Sistema de defesa
* [ ] Sistema de inventário
* [ ] Sistema de turnos
* [ ] Escalonamento de dificuldade
* [ ] Saída verdadeira
* [ ] Saída falsa
* [ ] Progressão entre labirintos
* [ ] Condição de vitória
* [ ] Sistema de salvamento
* [ ] Balanceamento do jogo

---

## Tecnologias

O projeto será desenvolvido utilizando principalmente:

* **Python**
* Programação procedural
* Programação orientada a objetos
* Módulos
* Estruturas de dados
* Manipulação de arquivos
* Geração de números aleatórios

---

## Objetivo do projeto

Este projeto está sendo desenvolvido como uma forma de praticar e consolidar conhecimentos de programação em Python através de um projeto maior.

A ideia é transformar os conceitos aprendidos durante os estudos em um sistema completo, começando por uma versão simples e adicionando novas funcionalidades progressivamente.

---

## Futuras possibilidades

Dependendo da evolução do projeto, novas mecânicas poderão ser adicionadas, como:

* Novas classes
* Novos tipos de monstros
* Equipamentos
* Poções
* Sistema de experiência
* Níveis do personagem
* Atributos mais complexos
* Eventos aleatórios
* Diferentes tipos de labirinto
* Chefes
* Sistema de conquistas
* Ranking de jogadores
* Sistema de salvamento mais completo

---

## Autor

**Victor**

Projeto desenvolvido para estudo e prática de programação em Python.
