import json

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
        return '<sem transações no momento>'

def calcular_saldo(transacoes):
    saldo=0
    for transacao in transacoes:
        if transacao['tipo'] == 'ENTRADA':
            saldo+=transacao['valor']
        
        elif transacao['tipo'] == 'SAIDA':
            saldo-=transacao['valor']
    return saldo
    


    


    