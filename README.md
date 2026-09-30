Sistema de controle de gastos pessoais no terminal, feito em Python utilizando o VS code.
As funções criadas (funcoes.py) foram para facilitar e diminuir o programa principal (main.py)
Funções: 
def leiaInt():
  Serve para ler e validar apenas números inteiros, usada para validar as opções do menu;
def menu(lista):
  Serve para criar a lista com opçõs que o menu oferece para o controle de gastos;
def salvar_dados(transacoes):
  Serve para criar uma lista contendo um dicionário com todas as transações registradas pelo usuário;
def carregar_dados():
  Serve para trazer essa lista com as transações guardadas e mostrar ao usuário;
Hoje 30/09/2026 fiz a parte 3 que mostrar o saldo.
def calacular_saldo(transacoes)
  Serve para que se o 'tipo' for 'ENTRADA' ele soma o 'valor' ao saldo e se for 'tipo' 'SAIDA' ele subtraia o'valor' do saldo

Programa em desenvolvimento: Meu próximo passo agora é criar a função que ira mostrar o saldo por categoria.
