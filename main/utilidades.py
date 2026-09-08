# main/utilidades
def linha(tamanho=30, simbolo='='):
    return simbolo * tamanho

def cabecalho(titulo, simb='='):
    print(linha(simbolo=simb))
    print(titulo.center(30))
    print(linha(simbolo=simb))

def leia_menu(msg, lista):
    while True:
        try:
            opcao = int(input(msg))
        except (ValueError, TypeError):
            print('Por favor digite um número inteiro válido. (Escolha uma opção do menu)')
            continue
        except KeyboardInterrupt:
            print('SAINDO...')
            return 0
        else:
            if  0 <= opcao <= len(lista) - 1:
                return opcao
            else:
                print('Por favor escolha um número correspondente a uma opção do menu!')
                continue

 

def menu(titulo, msg, lista, simb='='):
    cabecalho(titulo, simb)
    contador = 0
    for item in lista:
        print(f'    {contador} - {item}')
        contador += 1
    print()
    escolha = leia_menu(msg, lista)
    return escolha
