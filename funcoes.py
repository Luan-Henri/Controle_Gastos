import json
from datetime import datetime, date
from time import sleep

def linha():
    print('='*35)

def cabecalho(txt):
    linha()
    print(txt.center(35))
    linha()

def leiaInt(txt):
    while True:
        try:
            entrada_1 = int(input(txt))
        except (ValueError, TypeError):
            print("\033[33mErro: Opção inválida, digite novamente.\033[m")
        else:
            return entrada_1

def menu(lista):
    c=1
    for item in lista:
        print(f'{c} - {item}')
        c+=1
    linha()
    opc=leiaInt('Sua Opção: ')
    linha()
    return opc

def salvar_dados(transacoes):
    with open("entradas.json", "w", encoding="utf-8") as arquivo:
        json.dump(transacoes, arquivo, indent=4, ensure_ascii=False)

def carregar_dados():
    try:
        with open("entradas.json", "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)

    except (FileNotFoundError, json.JSONDecodeError):
        return []

def calcular_saldo(transacoes):
    saldo=0
    for transacao in transacoes:
        if transacao['tipo'] == 'ENTRADA':
            saldo+=transacao['valor']
        
        elif transacao['tipo'] == 'SAIDA':
            saldo-=transacao['valor']
    return saldo
    
def mostrar_transacoes(transacoes):
    print('-'*55)
    print(f"{'Nº':<4}{'TIPO':<8}{'VALOR R$':^16}{'CATEGORIA':<16}{'DATA':<12}")
    print('-'*55)
    for numero, transacao in enumerate(transacoes, start=1):
        tipo = transacao['tipo']
        valor = transacao['valor']
        categoria = transacao['categoria'][:15]
        data = transacao['data'][:12]
        data_guardada=datetime.strptime(data,'%Y-%m-%d')
        data_formatada=data_guardada.strftime('%d/%m/%Y')
        print(f"{numero:<4}{tipo:<8}{valor:^16.2f}{categoria:<16}{data_formatada:<12}")
    print('-'*55)

def total_por_categoria(transacoes):
    totais={}
    for transacao in transacoes:
        if transacao['tipo'] == 'ENTRADA':
            valor=transacao['valor']
        elif transacao['tipo'] == 'SAIDA':
            valor=-transacao['valor']
        totais[transacao['categoria']]=totais.get(transacao['categoria'], 0) + valor
    return totais
    
def leia_data():
    while True:
        texto=input('DATA [DD/MM/AAAA], ENTER para data atual: ').strip()

        if not texto:
            data_final=date.today().isoformat()
            return data_final

        try:
            data = datetime.strptime(texto, '%d/%m/%Y')
            data_final=data.date().isoformat()
            return data_final
        
        except ValueError:
            print('DATA INVÁLIDA. Digite novamente!')

def escolher_transacao(transacoes, acao):
    mostrar_transacoes(transacoes)
    while True:
        num=leiaInt(f'Número da transação a {acao}: ')
        if 1 <= num <= len(transacoes):
            return num
        print('Número inválido! Digite novamente...')
            
def editar_transacao(transacao):
    print('Enter para manter o valor atual!')
    #Nova Categoria
    nova_categoria=input(f"Categoria [{transacao['categoria']}] para: ").strip().lower()
    if not nova_categoria:
        print('Categoria atual mantida!')
    if nova_categoria:
        transacao['categoria'] = nova_categoria
        print(f"Sucesso! Categoria atualizada para: [{transacao['categoria']}]")
    sleep(1)
    #Novo Valor
    while True:
        novo_valor=input(f"Valor [{transacao['valor']:.2f}] para: ").strip().replace(',','.')
        if not novo_valor:
            print('Valor atual mantido!')
            break
        try:
            novo_valor = float(novo_valor)
        except ValueError:
            print('Digite um valor válido.')
            continue
        if novo_valor <= 0:
            print('O valor deve ser maior que zero!')
            continue
        transacao['valor'] = novo_valor
        print(f"Sucesso! Valor atualizado para: [{transacao['valor']:.2f}]")
        break
    sleep(1)
    #Nova data
    data_atual = datetime.strptime(transacao['data'], '%Y-%m-%d').strftime('%d/%m/%Y')
    while True:
        nova_data=input(f"Data [{data_atual}] para [DD/MM/AAAA]: ").strip()
        if not nova_data:
            print('Data atual mantida!')
            break
        try:
            data_convertida = datetime.strptime(nova_data, '%d/%m/%Y')
        except ValueError:
            print('Data inválida! Digite novamente.')
            continue
        data_guardar = data_convertida.date().isoformat()
        transacao['data'] = data_guardar
        print(f"Sucesso! Data atualizada para: [{data_convertida.strftime('%d/%m/%Y')}]")
        break
    sleep(1)
    #Novo tipo
    while True:
        novo_tipo=input(f"Novo tipo [{transacao['tipo']}] para [ENTRADA/SAIDA]: ").strip().upper()
        if not novo_tipo:
            print('Tipo atual mantido!')
            break
        elif novo_tipo in ('ENTRADA', 'SAIDA'):
            transacao['tipo'] = novo_tipo
            print(f"Sucesso! Tipo atualizado para: [{novo_tipo}]")
            break
        else:
            print('Tipo inválido! Digite novamente')
    
def filtrar_por_mes(transacoes, mes, ano):
    filtradas = []
    for transacao in transacoes:
        data = datetime.strptime(transacao['data'], '%Y-%m-%d')
        if data.month == mes and data.year == ano:
            filtradas.append(transacao)
    return filtradas

                   


    