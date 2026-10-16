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

        transacao['data']=funcoes.leia_data()

        transacoes.append(transacao)
        funcoes.salvar_dados(transacoes)
        
    elif resposta == 2:
        if transacoes:
            funcoes.mostrar_transacoes(transacoes)
        else:
            print('<Nenhuma transação Registrada Ainda>')

    elif resposta == 3:
        saldo=funcoes.calcular_saldo(transacoes)
        print(f'Saldo: R${saldo:.2f}')

    elif resposta == 4:
        if transacoes:
            print('-'*35)
            print(f"{'CATEGORIA':<15} {'TOTAL R$':>10} ")
            print('-'*35)
            totais=funcoes.total_por_categoria(transacoes)
            for categoria, total in totais.items():
                print(f'{categoria:<15} {total:>10.2f}')
            print('-'*35)
        else:
            print('<Nenhuma transação Registrada Ainda>')
    elif resposta == 5:
        print('\033[31mFIM DO PROGRAMA\033[m')
        break
    else:
        print('\033[31mOpção inválida\033[m')
    sleep(2)

    