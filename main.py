import funcoes
from time import sleep
from datetime import datetime

transacoes=funcoes.carregar_dados()

#mostrar menu:
while True:
    funcoes.cabecalho('MENU')
    resposta=funcoes.menu(['Registrar uma Transação', 'Listar todas as Transações', 'Mostrar Saldo',
                   'Ver total por categoria','Remover uma Transação', 'Editar Uma Transação', 'Sair'])
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
            funcoes.mostrar_transacoes(transacoes)
        else:
            print('<Nenhuma transação Registrada Ainda>')
        while True:
            num=funcoes.leiaInt('Número da transação a remover: ')
            if 1 <= num <= len(transacoes):
                break
            print('Número inválido! Digite novamente...')
        removido=transacoes.pop(num-1)
        funcoes.salvar_dados(transacoes)
        print('Transação removida com sucesso')
#Resposta 6 - Editar Uma Transação:
    elif resposta == 6:
        if transacoes:
            funcoes.mostrar_transacoes(transacoes)
    
            while True:
                num=funcoes.leiaInt('Número da transação a editar: ')
                if 1 <= num <= len(transacoes):
                    break
                print('Número inválido! Digite novamente...')
            escolhido=transacoes[num-1]
            print('ENTER para manter valor atual!')
            #Nova Categoria
            nova_categoria=input(f"Nova categoria [{escolhido['categoria']}] para: ").strip().lower()
            if nova_categoria:
                escolhido['categoria'] = nova_categoria
            print('Sucesso! Categoria atualizada para:', escolhido['categoria'])
            #Novo Valor
            while True:
                novo_valor=input(f"Novo valor [{escolhido['valor']:.2f}] para: ").strip().replace(',','.')
                if not novo_valor:
                    break
                try:
                    novo_valor = float(novo_valor)
                except ValueError:
                    print('Digite um valor válido.')
                    continue
                if novo_valor <= 0:
                    print('O valor deve ser maior que zero!')
                    continue
                escolhido['valor'] = novo_valor
                break
            print(f"Sucesso! Valor atualizado para: {escolhido['valor']:.2f}")
            #Nova data
            data_atual = datetime.strptime(escolhido['data'], '%Y-%m-%d').strftime('%d/%m/%Y')
            while True:
                nova_data=input(f"Nova data [{data_atual}] para [DD/MM/AAAA]: ").strip()
                if not nova_data:
                    print('Data Mantida')
                    break
                try:
                    data_convertida = datetime.strptime(nova_data, '%d/%m/%Y')
                except ValueError:
                    print('Data inválida! Digite novamente.')
                    continue
                data_guardar = data_convertida.date().isoformat()
                escolhido['data'] = data_guardar
                print(f"Sucesso! Data atualizada para: {data_convertida.strftime('%d/%m/%Y')}")
                break 
            funcoes.salvar_dados(transacoes)
        else:
            print('<Nenhuma transação Registrada Ainda>')
#Resposta 7 - Fim do Programa:        
    elif resposta == 7:
        print('\033[31mFIM DO PROGRAMA\033[m')
        break
    else:
        print('\033[31mOpção inválida\033[m')
    sleep(2)

    