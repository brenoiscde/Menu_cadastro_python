from funcoes import *

lista_de_usuarios = list()
dados_usuario = dict()

while True:
    menu()
    try:
        opcao = int(input(f"{cor('verde')}Digite sua opção: {cor('FINAL')}"))
    except(ValueError, TypeError):
        print(f"{cor('vermelho')}ERRO! Por favor digite um número inteiro.{cor('FINAL')}")
        continue
    if opcao == 1:
        if not lista_de_usuarios:
            print('-' * 50)
            print('{}Não há cadastro ainda{}'.format(cor('vermelho'), cor('FINAL')))
            continue
        else:
            opcao1(lista_de_usuarios)
            pergunta = str(input('Quer ver o cadastro de alguém? '))
            if pergunta in 'Ss':
                posicao = int(input('Quem?'))
                select_user = dict(lista_de_usuarios[posicao - 1])
                print('-' * 50)
                print('CADASTRO {:^45}'.format(select_user['Nome']))
                print('-' * 50)
                for k, v in select_user.items():
                    print('{}{:<20}{}{}'.format(cor('azul'),k,cor('FINAL'),v))
                voltar = str(input('Voltar menu[V]:'))
                if voltar in 'Vv':
                    continue
            else:
                continue    
    elif opcao == 2:
        opcao2(lista_de_usuarios)
        continue
    elif opcao == 3:
        opcao3()

    
    if opcao not in (1,2,3):
        print(f"{cor('vermelho')}ERRO! Número inválido{cor('FINAL')}")
        continue
    else:
        break
