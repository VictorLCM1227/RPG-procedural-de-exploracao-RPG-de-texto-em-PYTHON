# main/main

from jogo import jogar
from utilidades import menu, cabecalho
from conta import criar_conta, login


escolha_menu = menu('RPG: ELIXIR', '>>> Escolha: ', ['Sair', 'Criar conta', 'Fazer login'])

match escolha_menu: 
    case 0:
        cabecalho('SAINDO', '-')
    case 1:
        cabecalho('CRIAR CONTA', '-')
        criar_conta()

    case 2:
        cabecalho('FAZER LOGIN', '-')
        conta = login()
        if conta:
            escolha_jogo = menu('RPG: ELIXIR', '>>> Escolha: ', ['Sair', 'Iniciar novo jogo'])
            match escolha_jogo:
                case 0:
                    cabecalho('SAINDO...')
                case 1:
                    jogar()
