def cor(cor: str):
    cor_mapped = {
        "AMARELO": "\33[33m",
        "VERMELHO" : "\33[31m",
        "AZUL" : "\33[34m",
        "VERDE" : '\33[32m',
        "LILAS" : "\33[35m",
        "FINAL" : '\33[0m'
    }
    return cor_mapped.get(cor.upper())
    
def menu():
    print("-" * 50)
    print('{:^57}'.format(f"{cor('amarelo')}MENU PRINCIPAL{cor('FINAL')}"))
    print("-" * 50)
    print(f"""{cor("amarelo")}1{cor("final")} - {cor('azul')}Ver pessoas cadastradas{cor("final")} 
{cor("amarelo")}2{cor("final")} - {cor('azul')}Cadastrar novo usuário{cor("final")}
{cor("amarelo")}3{cor("final")} - {cor('azul')}Sair do sistema{cor("final")}""")
    print("-" * 50)

def opcao1(lista):
        print('{:-^50}'.format(' USUÁRIOS CADASTRADOS '))
        for i, user in enumerate(lista):
            print('| {} - Usuário =\33[33m {} \033[m '.format(i+1, user['Nome']))
        print('-' * 57)
    
def opcao2(lista):
    print('-' * 50)
    print("{:^57}".format(f"{cor('amarelo')}CADASTRO DE USUÁRIO{cor('FINAL')}"))
    while True:
        print('-' * 50)
        dados_usuario = dict()
        dados_usuario['Nome'] = str(input('{}Nome:{}'.format(cor('azul'), cor('FINAL'))))
        dados_usuario['Idade'] = int(input('{}Idade:{}'.format(cor('azul'), cor('FINAL'))))
        dados_usuario['Telefone'] = int(input('{}Telefone:{}'.format(cor('azul'), cor('FINAL'))))
        dados_usuario['Email'] = str(input('{}Email:{}'.format(cor('azul'), cor('FINAL'))))
        dados_usuario['Senha'] = str(input('{}Senha:{}'.format(cor('azul'), cor('FINAL'))))
        lista.append(dados_usuario)
        pergunta = str(input('Quer continuar? [S/N]: '))
    
        if pergunta in 'Ss':
            continue
        else:
            break
def opcao3():
    from time import sleep
    print("-" * 50)
    print("{:^65}".format(f"{cor('vermelho')}SAINDO DO SISTEMA...{cor('FINAL')}"))
    print("-" * 50)
    sleep(2.5)

