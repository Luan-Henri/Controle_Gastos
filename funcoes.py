import json
from datetime import datetime, date

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
    print('-'*50)
    print(f"{'TIPO':<8}{'VALOR R$':^16}{'CATEGORIA':<16}{'DATA':<12}")
    print('-'*50)
    for transacao in transacoes:
        tipo = transacao['tipo']
        valor = transacao['valor']
        categoria = transacao['categoria'][:15]
        data = transacao['data'][:12]
        data_guardada=datetime.strptime(data,'%Y-%m-%d')
        data_formatada=data_guardada.strftime('%d/%m/%Y')
        print(f"{tipo:<8}{valor:^16.2f}{categoria:<16}{data_formatada:<12}")
    print('-'*50)

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


            
         


    