from time import sleep


def menu():
    print('-' * 50)
    print("SISTEMA BANCÁRIO".center(50))
    print('-' * 50)
    print("""
[1] DEPOSITAR
[2] SACAR
[3] EXTRATO
[4] NOVO USUÁRIO
[5] NOVA CONTA
[6] LISTAR CONTAS
[7] SAIR""")


def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    contas = list()
    usuarios = list()

    LIMITE_SAQUES = 0
    AGENCIA = "0001"

    while True:
        opcao = menu()
        opcao = input('Escolha uma opção válida: ')
        print('-' * 50)

        if opcao == '1':
            valor = float(input('Informe o valor do depósito: R$'))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == '2':
            valor = float(input('Informe o valor do saque: R$'))
            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == '3':
            extrato_bancario(saldo, extrato=extrato)

        elif opcao == '4':
            novo_usuario(usuarios)

        elif opcao == '5':
            numero_conta = len(contas) + 1
            conta = nova_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)

        elif opcao == '6':
            listar_contas(contas)

        elif opcao == '7':
            print('Encerrando...')
            sleep(1)
            print('Volte Sempre!')
            break

        else:
            print('\033[0;31mOPERAÇÃO INVÁLIDA! Por favor selecione novamente uma operação válida!\033[m')


def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f'Depósito: R$ {valor:.2f}\n'
        print('Depósito realizado com sucesso!')
    else:
        print('\033[0;31mOPERAÇÃO FALHOU! O valor informado é inválido!\033[m')
    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print('\033[0;31mOPERAÇÃO FALHOU! Saldo insuficiente!\033[m')
    elif excedeu_limite:
        print('\033[0;31mOPERAÇÃO FALHOU! O valor do saque excede o limite!\033[m')
    elif excedeu_saques:
        print('\033[0;31mOPERAÇÃO FALHOU! Número máximo de saques excedido!\033[m')
    elif valor > 0:
        saldo -= valor
        extrato += f'Saque: R$ {valor:.2f}\n'
        numero_saques += 1
    else:
        print('\033[0;31mOPERAÇÃO FALHO! O valor informado é inválido!\033[m')
    return saldo, extrato


def extrato_bancario(saldo, /, *, extrato):
    print('EXTRATO'.center(50))
    print('-' * 50)
    print('Não foram realizadas movimentações.' if not extrato else extrato)
    print(f'\nSaldo: R$ {saldo:.2f}')
    print('-' * 50)


def novo_usuario(usuarios):
    cpf = input('CPF do usuário (somente números: ')
    usuario = usuarios_cadastrados(cpf, usuarios)

    if usuario:
        print('\033[0;31mERRO! Já existe usuário com este CPF!\033[m')
        return
    nome = str(input('Nome completo: '))
    data_nascimento = input('Data de nascimento (dd-mm-aaaa): ')
    endereco = input('Endereço (logadouro, nro - bairro - cidade/sigla estado): ')

    usuarios.append({'nome:': nome, 'data_nascimento': data_nascimento, 'cpf': cpf, 'endereco': endereco})

    print('\033[32mUsuário criado com sucesso!\033[m')


def usuarios_cadastrados(cpf, usuarios):
    usuarios_encontrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return usuarios_encontrados[0] if usuarios_encontrados else None


def nova_conta(agencia, numero_conta, usuarios):
    cpf = input('CPF do usuário (somente números): ')
    usuario = usuarios_cadastrados(cpf, usuarios)

    if usuario:
        print('\033[32mConta criada com sucesso!\033[m')
        return {'agencia': agencia, 'numero_conta': numero_conta, 'usuario': usuario}

    print('\033[0;31mERRO! Usuário não encontrado, fluxo de criação de conta encerrado!\033[m')


def listar_contas(contas):
    for conta in contas:
        linha = f'''\
        Agência:\t{conta['agencia']}
        C/C:\t\t{conta['numero_conta']}
        Titular:\t{conta['usuario']['nome']}
'''
    print('-' * 100)


main()
