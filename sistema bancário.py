from time import sleep
print('-' * 50)
print('SISTEMA BANCÁRIO'.center(50))
print('-' * 50)
menu = '''[1] DEPOSITAR
[2] SACAR
[3] EXTRATO
[4] SAIR

-> '''

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
while True:
    opcao = input(menu)
    print('-' * 50)
    if opcao == '1':
        valor = float(input('Informe o valor do depósito: R$'))
        if valor > 0:
            saldo += valor
            extrato += f'Depósito: R$ {valor:.2f}\n'
            print('Depósito realizado com sucesso!')
        else:
            print('\033[0;31mOPERAÇÃO FALHOU! O valor informado é inválido!\033[m')

    elif opcao == '2':
        valor = float(input('Informe o valor do saque: R$'))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES
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

    elif opcao == '3':
        print('EXTRATO'.center(50))
        print('-' * 50)
        print('Não foram realizadas movimentações.' if not extrato else extrato)
        print(f'\nSaldo: R$ {saldo:.2f}')
        print('-' * 50)

    elif opcao == '4':
        print('Encerrando...')
        sleep(1)
        print('Volte Sempre!')
        break

    else:
        print('\033[0;31mOPERAÇÃO INVÁLIDA! Por favor selecione novamente uma operação válida!\033[m')