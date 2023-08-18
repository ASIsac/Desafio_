def menu():
    menu = '''\n
    [1] Sacar
    [2] Extrato
    [0] Sair
--> '''
    return input(menu)

def sacar(*, saldo, valor, extrato, limite, contagem_saques):
            
    if valor > saldo:
        print('\nErro na operação de saque')
    
    elif valor > limite:
        print('\nErro na operação de saque. Valor excede o limite')
    
    elif contagem_saques > 3:
        print('\nLimite de saques diários atingidos')
    
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque {contagem_saques}: R$ {valor:.2f}\n"
    else:
        print('Erro na operação')

    return saldo, extrato


def exibir_extrato(saldo, /, *, extrato):
    print('\n============ EXTRATO ==============')

    if saldo > 0:
        print(extrato)
        print(f'\nSaldo Atual: R$ {saldo:.2f}')
        
    else:
        print('Não foram realizadas movimentações!')
    print('===================================\n')

    return extrato

def main():
    saldo = 50
    extrato = ''
    contagem_saques = 1
    SAQUE_LIMITE = 500

    while True:
        opcao = menu()
            
        if opcao == '1': # SAQUE
            
            if saldo == 0:
                print('\n===========================')
                print('|  Voçê não possui saldo  |')
                print('===========================')
            
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

        
        elif opcao == '2':
            exibir_extrato(saldo, extrato = extrato)
main()

    

