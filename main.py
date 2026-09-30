import funcoes
from time import sleep

transacoes=funcoes.carregar_dados()


while True:
    funcoes.cabecalho('MENU')
    resposta=funcoes.menu(['Registrar uma Transação', 'Listar todas as Transações', 'Mostrar Saldo',
                   'Ver total por categoria','Sair'])
    if resposta == 1:
        transacao=dict()

        tipo=''
        while tipo not in ('ENTRADA', 'SAIDA'):
            tipo=transacao['tipo']=input('Tipo de transação - [ENTRADA/SAIDA]: ').strip().upper()
        
        while True:
            try:   
                transacao['valor']=float(input('Valor: R$').replace(',','.'))
                if transacao['valor'] <= 0:
                    print('Valores negativos não são aceitos!')
                else:
                    break
            except ValueError:
                print('Digite um valor real válido')

        transacao['categoria']=input('Categoria: ').strip().lower()
        transacoes.append(transacao)
        funcoes.salvar_dados(transacoes)
        
    elif resposta == 2:
        for transacao in transacoes:
            print(transacao,end='')
        print()

    elif resposta == 3:
        saldo=funcoes.calcular_saldo(transacoes)
        print(f'Saldo: R${saldo:.2f}')

    elif resposta == 4:
        print('ok 4')
    elif resposta == 5:
        print('\033[31mFIM DO PROGRAMA\033[m')
        break
    else:
        print('\033[31mOpção inválida\033[m')
    sleep(2)

    