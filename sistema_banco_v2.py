def menu_banco():
    menu ='''\n
    ========== MENU ===========
    ---> [1] DEPÓSITO      <---
    ---> [2] SAQUE         <---
    ---> [3] EXTRATO       <---
    ---> [0] SAIR          <---
    ===========================
--> '''
    return input(menu)


def depositar(saldo, valor, extrato, contagem_depositos, /):

    if valor > 0:
        saldo += valor
        print('\n==================================')
        print('| Depósito realizado com sucesso |')
        print('==================================')
        extrato += f'--> Deposito {contagem_depositos}: R$ {valor:.2f}\n'
        print(f'\nSaldo: ---> R$ {saldo:.2f} <---\n')
    else:
        print('Valor inválido !')
    
    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, contagem_saques):
            
    if valor > saldo:
        print('\nErro na operação de saque')
    
    elif valor > limite:
        print('\nErro na operação de saque. Valor excede o limite')
    
    elif contagem_saques > 3:
        print('\nLimite de saques diários atingidos')
    
    elif valor > 0:
        saldo -= valor
        extrato += f"--> Saque {contagem_saques}: R$ {valor:.2f}\n"
    else:
        print('Erro na operação')

    return saldo, extrato


def exibir_extrato(saldo, /, *, extrato):
    print('\n============ EXTRATO ==============')

    if saldo > 0:
        print(extrato)
        print(f'\n--> Saldo Atual: R$ {saldo:.2f}')
        
    else:
        print('Não foram realizadas movimentações!')
    print('===================================\n')

    return extrato


def sair_do_sistema():
    print('\n= = = = = = = = = = = = = = = = = = = ')
    print('| Obrigado por usar o nosso sistema |')
    print('|           Até a próxima!          |')
    print('= = = = = = = = = = = = = = = = = = = \n')


def main():

    extrato = ''
    saldo = 0
    SAQUE_LIMITE = 500
    contagem_depositos = 1
    contagem_saques = 1

    while True:
        opcao = menu_banco()
        
        if opcao == '1': #  SAQUE
            valor = float(input('\nValor a depositar: R$ '))
            saldo, extrato = depositar(saldo, valor, extrato, contagem_depositos)
            contagem_depositos += 1
        
        elif opcao == '2': # SAQUE
            
            if saldo == 0:
                print('\n===========================')
                print('|  Voçê não possui saldo  |')
                print('===========================')
                print(f'\nSaldo: ---> R$ {saldo:.2f} <---\n')
            
            elif saldo > 0:
                print(f'Saldo disponível: R$ {saldo:.2f}')
                valor = float(input('Digite o valor que você deseja sacar: R$ '))
                saldo, extrato = sacar(
                    saldo=saldo,
                    valor=valor,
                    extrato=extrato,
                    limite=SAQUE_LIMITE,
                    contagem_saques=contagem_saques,
                )
                contagem_saques += 1
                print('\n=============================')
                print('|Saque realizado com sucesso|')
                print('=============================')
                print(f'\nSaldo Atual: ---> R$ {saldo:.2f} <---\n')
        
        elif opcao == '3': # EXTRATO
            exibir_extrato(saldo, extrato=extrato)
        
        elif opcao == '4': # SAIR DO SISTEMA
            sair_do_sistema()
            break
        else:
            print('\n Operação inválida!')
            print ('Digite novamente a operação desejada.\n')
    

main()