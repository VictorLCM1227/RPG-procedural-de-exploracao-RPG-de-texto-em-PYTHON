# main/conta

import json


def carregar_dados():
    try:
        with open('dados.json', 'r', encoding='utf-8') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []


def salvar_dados(dados):
    with open('dados.json', 'w', encoding='utf-8') as arquivo:
        json.dump(dados, arquivo, ensure_ascii=False, indent=4)


def criar_conta():
    dados = carregar_dados()

    nome_usuario = input('Nome de usuário: ').strip()

    # Verifica se o usuário já existe
    for conta in dados:
        if conta['nome_usuario'] == nome_usuario:
            print('Esse nome de usuário já está cadastrado!')
            return

    senha = input('Senha: ') #depois eu faço uma pseudo cibersegurança

    nova_conta = {
        'nome_usuario': nome_usuario,
        'senha': senha
    }

    dados.append(nova_conta)

    salvar_dados(dados)

    print('Conta criada com sucesso!')


def login():
    dados = carregar_dados()

    nome_usuario = input('Nome de usuário: ').strip()
    senha = input('Senha: ')

    for conta in dados:
        if conta['nome_usuario'] == nome_usuario:
            if conta['senha'] == senha:
                print()
                print(f'Login realizado com sucesso! Bem-vindo, {nome_usuario}!')
                return conta

            print('Senha incorreta!')
            return None

    print('Usuário não encontrado!')
    return None

