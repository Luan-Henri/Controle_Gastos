import funcoes
from time import sleep
from datetime import datetime

transacoes=funcoes.carregar_dados()

#mostrar menu:
while True:
    funcoes.cabecalho('MENU')
    resposta=funcoes.menu(['Registrar uma Transação', 'Listar todas as Transações', 'Mostrar Saldo',
                   'Ver total por categoria','Remover uma Transação', 'Editar Uma Transação', 
                   'Filtrar transações por mês', 'Sair'])
#resposta 1 - Registrar um transação:    
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
#Resposta 2 - Mostrar Transações:        
    elif resposta == 2:
        if transacoes:
            funcoes.mostrar_transacoes(transacoes)
        else:
            print('<Nenhuma transação Registrada Ainda>')
#Resposta 3 - Calcular Saldo:
    elif resposta == 3:
        saldo=funcoes.calcular_saldo(transacoes)
        print(f'Saldo: R${saldo:.2f}')
#Resposta 4 - Total por categoria:
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
#Resposta 5 - Excluir uma transação: 
    elif resposta == 5:
        if transacoes:
            num = funcoes.escolher_transacao(transacoes, 'remover')
            removido = transacoes.pop(num - 1)
            funcoes.salvar_dados(transacoes)
            print('Transação removida com sucesso')
        else:
            print('<Nenhuma transação Registrada Ainda>')
#Resposta 6 - Editar uma transação:
    elif resposta == 6:
        if transacoes:
            num = funcoes.escolher_transacao(transacoes, 'editar')
            funcoes.editar_transacao(transacoes[num - 1])
            funcoes.salvar_dados(transacoes)
            print('Transação atualizada com sucesso')
        else:
            print('<Nenhuma transação Registrada Ainda>')
#Resposta 7 - Filtrar transações por mês:
    elif resposta == 7:
        if transacoes:
            while True:
                mes = funcoes.leiaInt('Mês [1 a 12]: ')
                if 1 <= mes <= 12:
                    break
                print('Mês inválido! Digite novamente...')
            while True:
                ano = funcoes.leiaInt('Ano [AAAA]: ')
                if 2000 <= ano <= 2100:
                    break
                print('Ano inválido! Digite novamente...')
            do_mes = funcoes.filtrar_por_mes(transacoes, mes, ano)
            if do_mes:
                funcoes.mostrar_transacoes(do_mes)
            else:
                print('<Não possui transações com as datas informadas!>')
        else:
             print('<Nenhuma transação Registrada Ainda>')      
#Resposta 8 - Fim do Programa:        
    elif resposta == 8:
        print('\033[31mFIM DO PROGRAMA\033[m')
        break
    else:
        print('\033[31mOpção inválida\033[m')
    sleep(2)

    

    